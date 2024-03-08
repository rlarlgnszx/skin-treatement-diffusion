import torch, detectron2
import os
import cv2
from dotenv import load_dotenv
import os 

from datetime import datetime
from google.colab.patches import cv2_imshow

# DATA SET PREPARATION AND LOADING
from detectron2.data.datasets import register_coco_instances
from detectron2.data import DatasetCatalog, MetadataCatalog

# VISUALIZATION
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode

# CONFIGURATION
from detectron2 import model_zoo
from detectron2.config import get_cfg

# EVALUATION
from detectron2.engine import DefaultPredictor

# TRAINING
from detectron2.engine import DefaultTrainer
# HYPERPARAMETERS
DATA_SET_NAME = 'Wrinkle-Segmentation'
ARCHITECTURE = "mask_rcnn_R_101_FPN_3x"
CONFIG_FILE_PATH = f"COCO-InstanceSegmentation/{ARCHITECTURE}.yaml"
MAX_ITER = 2000
EVAL_PERIOD = 200
BASE_LR = 0.001
NUM_CLASSES = 3

# OUTPUT DIR
OUTPUT_DIR_PATH = os.path.join(
    DATA_SET_NAME,
    ARCHITECTURE,
    datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
)

os.makedirs(OUTPUT_DIR_PATH, exist_ok=True)
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file(CONFIG_FILE_PATH))
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(CONFIG_FILE_PATH)
# cfg.DATASETS.TRAIN = (TRAIN_DATA_SET_NAME,)
cfg.DATASETS.TRAIN = ()
cfg.DATASETS.TEST = ()
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 64
cfg.TEST.EVAL_PERIOD = EVAL_PERIOD
cfg.DATALOADER.NUM_WORKERS = 2
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.INPUT.MASK_FORMAT='bitmask'
cfg.SOLVER.BASE_LR = BASE_LR
cfg.SOLVER.MAX_ITER = MAX_ITER
cfg.MODEL.ROI_HEADS.NUM_CLASSES = NUM_CLASSES
cfg.OUTPUT_DIR = OUTPUT_DIR_PATH

def model():
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
    predictor = DefaultPredictor(cfg)
    return predictor

def loading_dataset():
    DATA_SET_NAME = dataset.name.replace(" ", "-")
    ANNOTATIONS_FILE_NAME = "_annotations.coco.json"
    # TRAIN SET
    TRAIN_DATA_SET_NAME = f"{DATA_SET_NAME}-train"
    TRAIN_DATA_SET_IMAGES_DIR_PATH = os.path.join(dataset.location, "train")
    TRAIN_DATA_SET_ANN_FILE_PATH = os.path.join(dataset.location, "train", ANNOTATIONS_FILE_NAME)

    register_coco_instances(
        name=TRAIN_DATA_SET_NAME,
        metadata={},
        json_file=TRAIN_DATA_SET_ANN_FILE_PATH,
        image_root=TRAIN_DATA_SET_IMAGES_DIR_PATH
    )

    # VALID SET
    VALID_DATA_SET_NAME = f"{DATA_SET_NAME}-valid"
    VALID_DATA_SET_IMAGES_DIR_PATH = os.path.join(dataset.location, "train")
    VALID_DATA_SET_ANN_FILE_PATH = os.path.join(dataset.location, "train", ANNOTATIONS_FILE_NAME)

    register_coco_instances(
        name=VALID_DATA_SET_NAME,
        metadata={},
        json_file=VALID_DATA_SET_ANN_FILE_PATH,
        image_root=VALID_DATA_SET_IMAGES_DIR_PATH
    )
    