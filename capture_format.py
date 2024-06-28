import os
import cv2

# Create the "Images" directory if it doesn't exis
if not os.path.exists("Images"):
    os.makedirs("Images")

# Open a video capture device (webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a frame from the webcam
ret, frame = cap.read()

# Check if the frame was captured
if not ret:
    print("Error: Could not capture frame.")
    cap.release()
    exit()


resized_frame = cv2.resize(frame, (216, 216))

# Generate a unique filename for the resized image
image_number = len(os.listdir("Images")) + 1
resized_image_filename = f"Images/{image_number}.jpeg"

cv2.imwrite(resized_image_filename, resized_frame)

cap.release()

print("Image captured and resized successfully.")
print("Resized image saved as:", resized_image_filename)
