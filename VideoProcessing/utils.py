import datetime
import cv2
from config import coco_class
import numpy as np

def get_time():
    time = datetime.datetime.now()
    return time.strftime('%Y-%m-%d %H:%H:%S')

def get_all_video_meta(videos):
    items = []
    meta = {}
    for video in videos:
        meta["filename"] = video.name
        meta["owner"] = video.owner
        if video.processed:
            meta["status"] = "Processed"
        else:
            meta["status"] = "Raw"
        meta["creat_time"] = video.created.strftime('%Y-%m-%d %H:%M:%S')
        items.append(meta.copy())
    return items

def get_frame_with_bbox_yolo3(img, det):
    COLORS = np.random.uniform(255, 125, size=(len(coco_class), 3))
    for frame_idx in det.keys():
        if len(det[frame_idx]) > 0:
            num_obj_this_frame = len(det[frame_idx]['class'])
            for obj_idx in range(num_obj_this_frame):
                class_label = det[frame_idx]['class'][obj_idx]
                class_idx = det[frame_idx]['class_idx'][obj_idx]
                conf_score = det[frame_idx]['conf_score'][obj_idx]
                x1, y1, x2, y2 = det[frame_idx]['coordinate'][obj_idx]
                label = "{}: {:.2f}%".format(class_label, conf_score)
                y = y1 - 15 if y1 - 15 > 15 else y1 + 15
                cv2.rectangle(img, (x1, y1), (x2, y2), color=COLORS[class_idx])
                cv2.putText(img, label, (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[class_idx], 2)
    return img

def get_frame_with_bbox_face(img, det):
    for face_location in det:
        top, right, bottom, left = face_location
        cv2.rectangle(img, (left, top), (right, bottom), color=[64, 255, 125])
    return img