import cv2

# Define the actual width of the object in meters
actual_object_width = .1347   # Adjust this value based on your object's size

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use contour detection to find objects in the frame
    _, thresh = cv2.threshold(gray, 110, 205, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the object's width in pixels
        x, y, w, h = cv2.boundingRect(contour)

        # Calculate the object's distance based on its size and the actual size
        object_width_pixels = w
        object_distance = (actual_object_width * frame.shape[1]) / (2 * object_width_pixels)  # Assuming 0.3048 meters per foot

        # Draw the bounding box and distance information
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Distance: {object_distance:.2f} feet", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Distance Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
