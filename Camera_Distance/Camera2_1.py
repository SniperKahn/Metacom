import cv2
import numpy as np

# Define the size of the reference object in real-world units (e.g., meters)
REFERENCE_OBJECT_WIDTH = 0.15  # 15 centimeters

# Load the pre-trained face detection model (e.g., Haar cascades)
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Capture video from the camera (you can also use an image)
cap = cv2.VideoCapture(0)

# Camera intrinsic parameters (focal length, principal point)
# You need to obtain these values through camera calibration
focal_length = 1000.0
principal_point = (640, 480)

while True:
    ret, frame = cap.read()
    
    # Convert the frame to grayscale (required for Haar cascades)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        # Calculate the width of the detected face in pixels
        face_width_pixels = w

        distance = (REFERENCE_OBJECT_WIDTH * focal_length) / face_width_pixels
        
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the distance on the frame
        cv2.putText(frame, f"Distance: {distance:.2f} meters", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()