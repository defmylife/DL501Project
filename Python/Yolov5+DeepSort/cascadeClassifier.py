import cv2
import time

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

face_cascade = cv2.CascadeClassifier('cars.xml')
# source cars.xml from https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6
vc = cv2.VideoCapture('test_trafficb480_trim1.mp4')

frames = []; t = [0.0, 0.0, 0.0]
while vc.isOpened():
    t[0] = time.time()
    rval, frame = vc.read()
    
    if rval == True:
        # car detection.
        cars = face_cascade.detectMultiScale(frame, 1.1, 2)
        
        ncars = 0
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            ncars = ncars + 1

        # show result
        cv2.imshow("Result",frame)
        frames.append(frame)
        t[1] = time.time()-t[0]
        print(">", t[1], "s")
        t[2] += t[1]

    if cv2.waitKey(10) & 0xFF == ord('q'): break

print("> total:", t[2], "s")
PATH = 'runs/cascade/'
FILE = 'test_trafficb480_track'
write_video(PATH+FILE+'_cascade.mp4', frames)

cv2.waitKey(1);
vc.release()
