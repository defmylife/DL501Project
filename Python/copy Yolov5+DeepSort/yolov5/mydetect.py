import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2 
import time

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp6/weights/last.pt', force_reload=True).autoshape()
print(model)

dt = [0.0, 0.0]
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('test_fibo1.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    dt[0] = time.time()
    results = model(frame)
    dt[1] = time.time()
    
    cv2.imshow('YOLO Detection', np.squeeze(results.render()))

    print(f"processing : YOLO(period={dt[1]-dt[0]:.3f}s / fps={1/(dt[1]-dt[0]):.1f})")
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()