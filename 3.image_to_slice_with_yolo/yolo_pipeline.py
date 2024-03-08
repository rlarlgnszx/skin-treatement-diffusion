from ultralytics import YOLO
import os
print(os.path.curdir)
# Load a model
# model = YOLO("./snak/runs/detect/train7/args.yaml")  # build a new model from scratch

model = YOLO('/home/kiru/snak/runs/detect/train7/weights/best.pt')

# - Between-eyebrows
# - Chin
# - Forehead
# - Left-cheek
# - Left-eye
# - Mouth
# - Nose
# - Right-cheek
# - Right-eye

results = model.predict('./snak/2.jpg',save=True)
import matplotlib.pyplot as plt
plots = results[0].plot()
boxes = results[0].boxes
for box in boxes :
    print(box.xyxy.cpu().detach())