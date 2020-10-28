import os
# Configure
with open(os.path.join(os.pardir, "models", "yolo3", "coco.names"), "r") as fp:
    coco_class = fp.read().split("\n")[:-1]
# RPC server host
# RPC_SERVICE_HOST = "162.105.85.250"
RPC_SERVICE_HOST = "localhost"
# RPC server port
RPC_SERVICE_PORT = str(50051)
# GPU Configuration
device_allocation = {
    "yolo3": "cpu"
}
# Some hyper-parameters for Yolo3 detector
yolo_hyperparameters = {
    "conf_thres": 0.8,
    "nms_thres": 0.4,
    "img_size": 416
}
