
from ultralytics import YOLO


"""
https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode
"""



if __name__ == "__main__":

    model = YOLO("YOLO11n-cls.pt")

    # Run batched inference on a list of images
    results = model(["C:\\Users\\Administrator\\Pictures\\车图\\车身.png"])  # return a list of Results objects
    # Run batched inference on a list of images
    # results = model(["image1.jpg", "image2.jpg"], stream=True)  # return a generator of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        # print(boxes)

        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        print(probs)
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename="result.jpg")  # save to disk