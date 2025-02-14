from ultralytics import YOLO

"""
pip install ultralytics

yolov8导出onnx报错ONNX: export failure ❌ 0.8s: DLL load failed while importing onnx_cpp2py_export: 动态链
pip uninstall onnx
pip install onnx==1.16.1

人脸识别
pip install insightface
pip install dlib

视频、图片视觉分割
https://github.com/facebookresearch/segment-anything/tree/main
"""

if __name__ == "__main__":

    # Create a new YOLO model from scratch
    model = YOLO("yolo11n.yaml")

    # Load a pretrained YOLO model (recommended for training)
    model = YOLO("yolo11n.pt")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data="coco8.yaml", epochs=3)

    # Evaluate the model's performance on the validation set
    results = model.val()

    # Perform object detection on an image using the model
    results = model("https://ultralytics.com/images/bus.jpg")

    # Export the model to ONNX format
    success = model.export(format="onnx")