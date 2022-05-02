#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from interfaces.msg import Detect
import numpy as np
import torch
import cv2


capture_index = 0
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# load model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5m6')
model.conf = 0.5

# ------ run model fn
def dectrun():
    # Convert images to numpy arrays
    cap = cv2.VideoCapture(capture_index)
    ret, frame = cap.read()

    results = model(frame)
    labels, cord = results.xyxyn[0][:,-1],results.xyxyn[0][:,:-1] #get label and bounding coordinates
    return labels,cord, frame


#------- ROS2 node
class FineDetect(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Detect, 'topic', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.capture_index = 0

    def get_video_capture(self):
        return cv2.VideoCapture(self.capture_index)

    def timer_callback(self):
        labels, cord, frame = dectrun()
        n = len(labels)
        x_shape,y_shape = frame.shape[1],frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.3:
                msg = Detect()
                msg.x1, msg.y1, msg.x2, msg.y2 = float(row[0]*x_shape), float(row[1]*y_shape), float(row[2]*x_shape), float(row[3]*y_shape)
                msg.confidence = float(row[4])
                # msg.data = 'Hello World: %d' % self.i
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: "%s"' % msg.confidence)
        # self.i += 1


#-------- Run node
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = FineDetect()
    rclpy.spin(minimal_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()