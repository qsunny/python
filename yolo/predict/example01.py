from ultralytics import YOLO

if __name__ == "__main__":

    model = YOLO("D:\\workspace-py\\python\\yolo\\quickstart\\runs\\detect\\train\\weights\\last.pt")
    # Run inference on an image
    results = model("D:\\workspace-py\\python\\yolo\\quickstart\\bus.jpg")  # results list

    # results = model(
    #     ["https://ultralytics.com/images/bus.jpg", "https://ultralytics.com/images/zidane.jpg"]
    # )  # list of 2 Results objects

    # Run inference on 'bus.jpg' with arguments
    model.predict("D:\\workspace-py\\python\\yolo\\quickstart\\bus.jpg", save=True, imgsz=320, conf=0.5)

    # View results
    for r in results:
        print(r.keypoints)  # print the Keypoints object containing the detected keypoints
        print(r.probs)  # print the Probs object containing the detected class probabilities
        print(r.boxes)  # print the Boxes object containing the detection bounding boxes