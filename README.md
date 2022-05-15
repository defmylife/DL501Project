
# **YOLOv5 DeepSort Tracking Vehicle Network for Traffic Control**

### Introduction
🚀This repository introduces real-time tracking vehicle network for the traffic control system using [YOLOv5](https://github.com/ultralytics/yolov5) [DeepSORT](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet). The network is composed of two subsystems: edge-device tracking system and edge server. Edge-device tracking system used YOLOv5 DeepSORT, a lightweight machine learning model, as the major computing algorithm. After the edge-device tracking activates, it will send the detection result to the server to perform further analysis. For simulating network operation, we use a Node.js HTTP Module webserver as the communication protocol, and path generation as the main task of edge server.

### Overview of source files
- `app.js`: Webserver host.
- `track.py`: Running (edge-device) vehicle detection and tracking system, sending data to the server.
- `monitor_realtime.py`: Running (edge-server) perspective transformation and visualization.

### Installation
Require [Node.js](https://nodejs.org/) and [Python](https://www.python.org/) to run.

For Node.js environments:
```sh
npm install express
```

For Python environments:
```sh
pip install -r requirements.txt
```


