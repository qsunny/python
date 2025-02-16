#年龄、性别检测
import numpy as np
import cv2
import insightface

if __name__ == "__main__":
    detection = insightface.app.FaceAnalysis(allowed_modules=['detection', 'genderage'], providers=['CPUExecutionProvider'])
    detection.prepare(ctx_id=-1, det_size=(640, 480))
    img =cv2.imread('img/wang_test.png')
    faces = detection.get(img)
    for face in faces:
        box = face.bbox.astype(np.int32)
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)
        if face.age is not None and face.sex is not None:
            cv2.putText(img, f'{face.sex}-{face.age}', (box[0], box[1]-10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

