import cv2 
import time
import numpy as np
import math as m

def deg2rad(deg):
    return m.tan(deg/180.0*m.pi)
  
def Rotx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                    [ 0, m.cos(theta),-m.sin(theta)],
                    [ 0, m.sin(theta), m.cos(theta)]])
  
def Roty(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                    [ 0           , 1, 0           ],
                    [-m.sin(theta), 0, m.cos(theta)]])
  
def Rotz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                    [ m.sin(theta), m.cos(theta) , 0 ],
                    [ 0           , 0            , 1 ]])

def write_video(file_path, frames, fps):
    """
    Writes frames to an mp4 video file
    :param file_path: Path to output video, must end with .mp4
    :param frames: List of PIL.Image objects
    :param fps: Desired frame rate
    """

    w, h = frames[0].size
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv.VideoWriter(file_path, fourcc, fps, (w, h))

    for frame in frames:
        writer.write(pil_to_cv(frame))

    writer.release() 

def transform(xy, HEIGHT, THETA, GAMMA):
    xyz = np.matrix([
        [xy[0]], 
        [xy[1]],
        [(HEIGHT-xy[1]) / deg2rad(THETA)]
        ])
    # print('xyz:', xyz)
    # print('xyz shape:', xyz.shape)

    XYZ = np.dot(Rotz(deg2rad(GAMMA)), np.dot(Rotx(deg2rad(90-THETA)), xyz))
    # print('XYZ:', XYZ)
    # print('XYZ shape:', XYZ.shape)

    XY = xy
    return XYZ.transpose().tolist()[0]

def plot1(image, xywh, id, REF, size=5, thickness=2):

    center = (int(xywh[0]) + int(xywh[2])/2, int(xywh[1]) + int(xywh[3])/2)

    # Transformation
    xyz = transform(center, HEIGHT=500, THETA=45, GAMMA=45)

    # represents the top left corner of rectangle
    start_point = (int(center[0]-size), int(center[1]-size))
    # represents the bottom right corner of rectangle
    end_point = (int(center[0]+size), int(center[1]+size))

    # Blue color in BGR
    color = (255, 0, 0)
    
    # Using cv2.rectangle() method
    for ref in REF:
        pts = np.array(ref)
        pts = pts.reshape((-1, 1, 2))
        image = cv2.polylines(image, [pts], True, (255,255,255), 1)

    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Using cv2.putText() method
    image = cv2.putText(
        image, 'ID'+id, (end_point[0]+5, end_point[1]), cv2.FONT_HERSHEY_SIMPLEX, .4, color, thickness-1, cv2.LINE_AA)
    image = cv2.putText(
        image, f"{xyz[0]:.1f},{xyz[1]:.1f},{xyz[2]:.1f}",
        (end_point[0]+5, end_point[1]+15), cv2.FONT_HERSHEY_SIMPLEX, .4, color, thickness-1, cv2.LINE_AA)

    return image

def write_video(file_path, frames, fps=30):
    """
    Writes frames to an mp4 video file
    :param file_path: Path to output video, must end with .mp4
    :param frames: List of PIL.Image objects
    :param fps: Desired frame rate
    """

    w, h = len(frames[0][0]), len(frames[0])
    # writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, (w, h))
    writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    for frame in frames:
        writer.write(frame)

    writer.release() 


if __name__ == '__main__':

    PATH = 'runs/monitor/'
    FILE = 'test_trafficb480_track'
    with open(PATH+FILE+".txt", "r") as f:
        data = f.readlines()
        # data[0] = frame index
        # data[1] = object index
        # data[2] = x-coordinate
        # data[3] = y-coordinate
        # data[4] = object width
        # data[5] = object height
        # data[6] 
        # data[7] 
        # data[8] 
        # data[9] 
    cap = cv2.VideoCapture(PATH+FILE+'.mp4')

    REF = ((
            (390, 108), (600, 208), (295, 375), (111, 233)),
        (
            (390, 80), (675, 210), (280, 430), (40, 230)
        ))
    frames = []; frame_idx = 0; dt = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frame_idx+=1
            # print(len(frame), len(frame[0]))

            for data_i in data:
                info = data_i.split()
                # print(info)
                if int(info[0]) == frame_idx:

                    # Plotting coordinate
                    frame = plot1(
                        frame, 
                        xywh=info[2:6],
                        id=info[1],
                        REF=REF
                        )

            cv2.imshow('YOLO DeepSort tracking', frame)
            frames.append(frame)

        if cv2.waitKey(10) & 0xFF == ord('q'): break
        # if frame_idx==3: break
        
    # Save monitering result to VDO
    write_video(PATH+FILE+'_monitor.mp4', frames)

    print("total frame:", frame_idx)
    print(f"total process time: {time.time()-dt:.3f}s")
    cap.release()
    cv2.destroyAllWindows()