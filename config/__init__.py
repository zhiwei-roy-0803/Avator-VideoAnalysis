# Configure
fp = open("config/coco.names", "r")
coco_class = fp.read().split("\n")[:-1]
# RPC server host
RPC_SERVICE_HOST = "162.105.85."