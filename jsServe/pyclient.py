import torch
import numpy as np
import cv2
from time import time
import requests

from models.common import Detections


class Detect:

    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device:" , self.device)
    
    def get_video_capture(self):
        return cv2.VideoCapture(self.capture_index)

    def load_model(self,model_name):
        if model_name: #if we insert model name
            model = torch.hub.load('ultralytics/yolov5','custom', path=model_name,force_reload=True)
        else: #else we will use pretrained model
            model = torch.hub.load('ultralytics/yolov5','yolov5',pretrained=True)
        return model
    
    def score_frame (self,frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:,-1],results.xyxyn[0][:,:-1] #get label and bounding coordinates
        return labels,cord

    def class_to_label(self,x):
        return self.classes[int(x)] # the label from the model is an integer you need to match it with the defined classes
    
    def plot_boxes (self,results,frame):
        labels, cord = results
        n = len(labels)
        x_shape,y_shape = frame.shape[1],frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.3:
                x1,y1,x2,y2 = int(row[0]*x_shape),int(row[1]*y_shape),int(row[2]*x_shape), int(row[3]*y_shape)
                
                bounding = [x1,y1,x2,y2]
                print(str(bounding))
                data = {'result': bounding, 'class':self.class_to_label(labels[i])}
                # print (bounding)
                # The POST request to our node server
                res = requests.post('http://127.0.0.1:3000/result', json=data)

                # # Convert response data to json
                returned_data = res.json()

                # print(returned_data)
                # result = returned_data['result']
                bgr = (0,255,0)
                cv2.rectangle(frame, (x1,y1), (x2,y2),bgr,2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1,y1),cv2.FONT_HERSHEY_SIMPLEX,0.9,bgr)

        return frame

    def __call__(self):
        cap = self.get_video_capture()
        assert cap.isOpened()

        while 1:
            ret, frame = cap.read()
            assert ret
            frame = cv2.resize(frame,(416,416))

            start_time = time()
            results = self.score_frame(frame)
            frame = self.plot_boxes(results,frame)

            end_time = time()
            fps = 1/np.round(end_time-start_time,2)
            data = {'fps':fps}
            # print (bounding)
            # The POST request to our node server
            res = requests.post('http://127.0.0.1:3000/fps', json=data)

            # # Convert response data to json
            returned_data = res.json()

            cv2.putText(frame,f'FPs: {int(fps)}',(20,70),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
            cv2.imshow('YOLOv5 Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()

detector = Detect(capture_index=0,model_name='yolov5s.pt')
detector()
