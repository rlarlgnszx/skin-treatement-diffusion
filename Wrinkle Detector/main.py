import cv2
from model.Detectron import model
import torch
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode

img = cv2.imread('./face.webp')
predictor = model()

outputs = predictor(img)

visualizer = Visualizer(
    img[:, :, ::-1],
    # metadata=metadata,
    scale=1.6,
    instance_mode=ColorMode.SEGMENTATION
)
out = visualizer.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imshow(out.get_image()[:, :, ::-1])
