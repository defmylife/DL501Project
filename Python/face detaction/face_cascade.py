import cv2
# Reference :   https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
#               https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
#               https://towardsdatascience.com/whats-the-difference-between-haar-feature-classifiers-and-convolutional-neural-networks-ce6828343aeb


# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture('test_fibo1.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # print(len(img))
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if key is pressed
    # 27: escape
    # 32: space bar
    k = cv2.waitKey(30) & 0xff
    if k==32:
        break
# Release the VideoCapture object
cap.release()