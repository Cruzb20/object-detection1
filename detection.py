import cv2
import numpy as np

# Load the YOLOv3 model and class names
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Function to perform object detection
def detect_objects(image):
    height, width = image.shape[:2]

    # Prepare the frame for detection
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Get the output layer names
    layer_names = net.getUnconnectedOutLayersNames()

    # Forward pass through the network
    outs = net.forward(layer_names)

    class_ids = []
    confidences = []
    boxes = []

    # Process the output
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maximum suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes and labels on the image
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)  # BGR color for the bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return image

# Check if you're processing an image or a video
input_path = 'happier.mp4'  # Change this to the path of your image or video

if input_path.endswith('.mp4') or input_path.endswith('.avi'):
    cap = cv2.VideoCapture(input_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_objects(frame)
        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press the 'Esc' key to exit
            break
    cap.release()
else:
    image = cv2.imread(input_path)
    result_image = detect_objects(image)
    cv2.imshow("Object Detection", result_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

