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

def euclidean_distance(p1, p2): # (x1, y1), (x2, y2)
    return m.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def create_transformation(top_right_bottom_left): # [(xt, yt), (xr, yr), (xb, yb), (xl, yl)]
    print("> Creating transformation")
    TOP = top_right_bottom_left[0]
    RIGHT = top_right_bottom_left[1]
    BOTTOM = top_right_bottom_left[2]
    LEFT = top_right_bottom_left[3]

    SLOPE = euclidean_distance(TOP, BOTTOM) / euclidean_distance(RIGHT, LEFT)
    print(f"\tslope : {SLOPE*90:.1f}deg.")
    centerline = int(abs((RIGHT[1]+LEFT[1])/2)) # positive value
    Y_OFFSET = ((1/SLOPE)-1)* centerline

    ROTATE = m.atan(abs(TOP[1]-LEFT[1])*((1/SLOPE)) / abs(TOP[0]-LEFT[0])) *180 /m.pi
    print(f"\trotate : {ROTATE:.1f}deg.")
    ROTATE_offset = -8.23

    PERSPEC_X = 0.00034

    PERSPEC_Y = 0.0005
    PERSPEC_Y2 = 0.088

    SCALE = 0.6
    
    return (SLOPE, Y_OFFSET, ROTATE+ROTATE_offset, PERSPEC_X, PERSPEC_Y, PERSPEC_Y2, SCALE)

def transform(xy, MAT, Dx=180, Dy=20, HEIGHT=1000, THETA=29, GAMMA=0, DX=0, DY=1700, print_MAT=False):
    # Version 2
    SLOPE, Y_OFFSET, ROTATE, PERSPEC_X, PERSPEC_Y, PERSPEC_Y2, SCALE = MAT
    
    xy1 = (xy[0], (1/SLOPE)*xy[1] - Y_OFFSET)

    xyz1 = np.matrix([[xy1[0]],
                     [xy1[1]],
                     [0]])
    xyz2 = np.dot(Rotz(deg2rad(ROTATE)), xyz1)
    xy2 = (xyz2.tolist()[0][0], xyz2.tolist()[1][0])

    xy3 = (xy2[0], (1- (400-xy2[0])*PERSPEC_X)*xy2[1])

    xy4 = ((1- (xy3[1])*PERSPEC_Y)*xy3[0] - PERSPEC_Y2*xy3[1], xy3[1])

    XY = (int(SCALE*xy4[0])+Dx, int(SCALE*xy4[1])+Dy)

    # Version 1
    """
    xyz = np.matrix([
        [xy[0]], 
        [xy[1]],
        [(HEIGHT/m.sin(deg2rad(THETA)))-(xy[1]/m.tan(deg2rad(THETA)))]
        ])
    # print('xyz:', xyz)
    # print('xyz shape:', xyz.shape)

    XYZ = np.dot(Rotx(deg2rad(270-THETA)), xyz)
    # XYZ = np.dot(Rotz(deg2rad(GAMMA)), np.dot(Rotx(deg2rad(270-THETA)), xyz))
    # print('XYZ:', XYZ)
    # print('XYZ shape:', XYZ.shape)
    if print_MAT: print("Rotx:", Rotx(deg2rad(270-THETA)))

    output = XYZ.transpose().tolist()[0]
    output[0] = output[0]+DX
    output[1] = output[1]+DY
    """
    return XY

def REF_XYZ(REF, MAT):
    REF2 = []
    for i, ref in enumerate(REF):
        REF2.append([])
        for xy in ref:
            # Transformation (Perspective transform -> Camera-to-Global frame transform)
            XY = transform(xy, MAT)
            
            REF2[i].append((int(XY[0]), int(XY[1])))
    print("> Loaded the reference line to GLOBAL")
    print("\tREF:", REF); print("\tREF2:", REF2)
    return REF2

def recorded(records, id, path, LPfilter):
    # first record
    if len(records)==0:
        records.append([id, [path]])
        return records, [path], path
    # append record
    for record in records:
        if record[0]==id:
            # apply low-pass filter
            if LPfilter:
                path = (
                    int(LPfilter*path[0] + (1-LPfilter)*record[1][0][0]), 
                    int(LPfilter*path[1] + (1-LPfilter)*record[1][0][1]))

            record[1].insert(0, path)
            return records, record[1], path
    # add new record
    records.append([id, [path]])
    return records, [path], path

def plot1(image, xywh, id, REF, size=5, thickness=2):

    center = (int(xywh[0]) + int(xywh[2])/2, int(xywh[1]) + int(xywh[3])/2)

    # Transformation
    xy = transform(center, MAT)

    # represents the top left corner of rectangle
    start_point = (int(center[0]-size), int(center[1]-size))
    # represents the bottom right corner of rectangle
    end_point = (int(center[0]+size), int(center[1]+size))

    # Blue color in BGR
    # color = (255, 0, 0)
    color = (255, 255, 255)
    
    # Using cv2.rectangle() method
    for ref in REF:
        pts = np.array(ref)
        pts = pts.reshape((-1, 1, 2))
        image = cv2.polylines(image, [pts], True, color, 1)

    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Using cv2.putText() method
    # image = cv2.putText(
    #     image, 'ID'+id, (end_point[0]+5, end_point[1]), cv2.FONT_HERSHEY_SIMPLEX, .4, color, thickness-1, cv2.LINE_AA)
    image = cv2.putText(
        image, f"{xy[0]:.1f},{xy[1]:.1f}",
        (end_point[0]+5, end_point[1]+15), cv2.FONT_HERSHEY_SIMPLEX, .4, color, thickness-1, cv2.LINE_AA)

    return image

def plot2(image, xywh, id, REF, MAT, records, LPfilter=0.1, size=5, thickness=2, show_rec=50):

    center = (int(xywh[0]) + int(xywh[2])/2, int(xywh[1]) + int(xywh[3])/2)

    # Transformation (Perspective transform -> Camera-to-Global frame transform)
    XY = transform(center, MAT)

    # Recording the path
    records, paths, XY = recorded(records, id, XY, LPfilter)
    paths = paths[0:show_rec+1] if len(paths)>show_rec else paths

    # represents the top left corner of rectangle
    start_point = (int(XY[0]-size), int(XY[1]-size))
    # represents the bottom right corner of rectangle
    end_point = (int(XY[0]+size), int(XY[1]+size))

    # Blue color in BGR
    # color = (255, 0, 0)
    color = (255, 255, 255)

    # Using cv2.polylines() method
    # Reference
    # for ref in REF:
    #     pts = np.array(ref)
    #     pts = pts.reshape((-1, 1, 2))
    #     image = cv2.polylines(image, [pts], True, (255,255,255), 1)
    # Paths
    path = np.array(paths)
    path = path.reshape((-1, 1, 2))
    image = cv2.polylines(image, [path], False, (67,67,67), 1)

    # Using cv2.rectangle() method
    image = cv2.rectangle(image, start_point, end_point, (67,67,67), thickness)

    # Using cv2.putText() method
    image = cv2.putText(
        image, 'ID'+id, (end_point[0]+5, end_point[1]), cv2.FONT_HERSHEY_SIMPLEX, .4, color, thickness-1, cv2.LINE_AA)
    image = cv2.putText(
        image, f"{XY[0]},{XY[1]}",
        (end_point[0]+5, end_point[1]+15), cv2.FONT_HERSHEY_SIMPLEX, .4, (67,67,67), thickness-1, cv2.LINE_AA)
    
    return image, records

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
    print("> Saved the video to", file_path)


if __name__ == '__main__':
    print("\nRunning in main"); print("-"*20)

    PATH = 'runs/monitor/'
    FILE = 'test_trafficb480_trackcars'
    BG = 'background3.png'

    _AUTO_CLOSE = True
    _SAVE_VDO = True
    _DEBUG = False
    _SHOW_RECORD = False

    with open(PATH+FILE+".txt", "r") as f:
        data = f.readlines()
        # data[i][0] = frame index
        # data[i][1] = object index
        # data[i][2] = x-coordinate
        # data[i][3] = y-coordinate
        # data[i][4] = object width
        # data[i][5] = object height
        # data[i][6] 
        # data[i][7] 
        # data[i][8] 
        # data[i][9] 
    cap = cv2.VideoCapture(PATH+FILE+'.mp4')
    bg = cv2.imread(PATH+BG)

    REF = ((
            (390, 108), (600, 208), (295, 375), (111, 233)),
        (
            (390, 80), (675, 205), (280, 430), (40, 230)
        ))
    MAT = create_transformation(REF[0])
    REF2 = REF_XYZ(REF, MAT)

    frames = []; frame_idx = 0; monitors = []; records = []; dt = time.time()
    print("> Start the process")
    while cap.isOpened():
        ret, frame = cap.read()
        monitor = bg.copy()
        if ret == True:
            frame_idx+=1
            # print(len(frame), len(frame[0])) # frame size

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
                    # Plotting monitor
                    monitor, records = plot2(
                        monitor, 
                        xywh=info[2:6],
                        id=info[1],
                        REF=REF2,
                        MAT=MAT,
                        records=records
                        )

            # cv2.imshow('YOLO DeepSort tracking', frame)
            cv2.imshow('YOLO DeepSort monitoring', monitor)
            frames.append(frame)
            monitors.append(monitor)

        if (cv2.waitKey(10) & 0xFF == ord('q')) or (_AUTO_CLOSE and frame_idx==int(data[-1].split()[0])): 
            print("> Finish the process")
            break
        # (For 1-loop only debugging)
        if _DEBUG:
            if frame_idx==3: break
    
    # Show all recorded path
    if _SHOW_RECORD:
        print("> Recorded paths")
        for record in records:
            print(f"\tID{record[0]}: {record[1] if len(record[1])<=5 else record[1][0:6]}{'' if len(record[1])<=5 else ' . . .'}")

    # Save monitering result to VDO
    if _SAVE_VDO:
        write_video(PATH+FILE+'_plot.mp4', frames)
        # write_video(PATH+FILE+'_monitor.mp4', monitors)

    print("-"*20)
    print("total frame:", frame_idx)
    print(f"total process time: {time.time()-dt:.3f}s")
    cap.release()
    cv2.destroyAllWindows()