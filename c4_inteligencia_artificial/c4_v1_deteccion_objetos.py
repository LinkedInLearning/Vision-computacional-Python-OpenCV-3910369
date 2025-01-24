import cv2
import math

from ultralytics import YOLO


model = YOLO('yolov8n.pt')
class_names = model.names

img = cv2.imread("src/Tabby cat_LIL_191692.jpeg")

model_results = model(img)
for result in model_results:
    boxes = result.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        class_id = int(box.cls[0])
        name = class_names[int(class_id)]
        conf = box.conf[0]

        label = f"{name}: {box.conf[0]:.2f}"
        print(label)

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0 ,255), 5)
        img = cv2.putText(img, label, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 5)

cv2.imshow("Objetos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
