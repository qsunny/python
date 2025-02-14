import insightface
import cv2
import numpy as np


"""
人脸识别
pip install insightface
pip install -U insightface
pip install dlib

https://github.com/deepinsight/insightface

unzip it under ~/.insightface/models/ first before you call the program
https://github.com/deepinsight/insightface/tree/master/python-package


在 Windows 上，检查 PATH 是否包含 OpenCV 的安装路径（如 C:\ProgramData\Anaconda3\envs\python3.9\Lib\site-packages\cv2）
"""


if __name__ == "__main__":

    # detection = insightface.app.FaceAnalysis(providers=['CPUExecutionProvider'])
    # antelopev2 buffalo_m
    detection = insightface.app.FaceAnalysis(name='buffalo_m', providers=['CPUExecutionProvider'])
    detection.prepare(ctx_id=-1, det_size=(640, 480))

    cap = cv2.VideoCapture('C:/Users/Administrator/Videos/dance.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        faces = detection.get(frame)
        for face in faces:
            box = face.bbox.astype(np.int32)
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)
            cv2.imshow('frame', frame)
            cv2.waitKey(30)

