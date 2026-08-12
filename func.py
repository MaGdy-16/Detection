from ultralytics import YOLO

model = YOLO("best.pt")

def bows(img_path):
    result = model.predict(source= img_path,save=True)
    return result