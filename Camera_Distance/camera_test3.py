import cv2
from yolov4.tf import YOLOv4 

YOLO = YOLOv4()

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Read and display frames from the camera
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame from the camera")
        break

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    YOLO(frame)
    YOLO.make_model()
    YOLO.load_weights("yolov4-tiny.weights", weights_type="yolo")
    YOLO.summary(summary_type="yolo")
    YOLO.summary()
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()