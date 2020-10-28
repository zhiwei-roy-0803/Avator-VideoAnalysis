from models.utils.utils import load_classes

fp = open("config/coco.names", "r")
coco_class = fp.read().split("\n")[:-1]