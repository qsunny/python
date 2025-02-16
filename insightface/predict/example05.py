
import cv2
import numpy as np
import insightface
from numpy.linalg import norm
from scipy.spatial.distance import euclidean

"""
从视频中获取每一帧图片 人脸识别
计算特征向量之间的欧氏距离
"""

if __name__ == "__main__":

    detector = insightface.app.FaceAnalysis(allowed_modules=['detection', 'recognition'], providers=['CPUExecutionProvider'])
    # ctx_id=0 means using the first GPU or CPU for inference
    detector.prepare(ctx_id=-1, det_size=(640, 640))
    # 加载人脸数据库的数据
    musk_img = cv2.imread('img/aaron.jpg')
    musk_face = detector.get(musk_img)
    musk_embedding = musk_face[0].normed_embedding

    cap = cv2.VideoCapture('C:/Users/Administrator/Videos/aaron2.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        faces = detector.get(frame)
        for face in faces:
            bbox = face.bbox.astype(np.int32)
            embedding = face.normed_embedding
            # 人脸相似度比较
            # sim = np.dot(embedding, musk_embedding) / (norm(musk_embedding) * norm(embedding))
            # score = (sim * 100).astype(np.int32)

            # 计算特征向量之间的欧氏距离
            score = euclidean(embedding, musk_embedding)

            # print('sim:', sim)
            print('score:', score)
            if score < 1.192:
                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(frame, f'match score:{score}', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1
                            , color=(0, 255, 0), thickness=2)
                cv2.rectangle(frame, (bbox[0], bbox[3]), (bbox[2], bbox[3]), (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)
                cv2.putText(frame, f'unknown ', (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1
                            , color=(255, 0, 0), thickness=2)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)



