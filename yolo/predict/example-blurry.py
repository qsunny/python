
import cv2
import numpy as np
from ultralytics import YOLO


if __name__ == "__main__":
    model = YOLO("D:\\workspace-py\\python\\yolo\\quickstart\\yolo11n.pt")
    print(model.names)

    cap = cv2.VideoCapture("C:/Users/Administrator/Videos/dance.mp4")
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            break

        results = model.predict(im0)
        for box in results[0].boxes.xyxy.cpu().tolist():
            obj = im0[int(box[1]): int(box[3]), int(box[0]): int(box[2])]
            im0[int(box[1]):int(box[3]), int(box[0]):int(box[2])] = cv2.blur(obj, (5, 50))
        cv2.imshow("Y0L011 Blurring", im0)
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()