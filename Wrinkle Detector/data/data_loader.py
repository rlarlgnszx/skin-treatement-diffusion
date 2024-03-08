from roboflow import Roboflow
from dotenv import load_dotenv
import os 

def roboflow_dataloder():
    load_dotenv()
    rf = Roboflow(os.environ.get('API'))
    project = rf.workspace("teknofest23").project("wrinkle-segmentation-5iaty")
    dataset = project.version(1).download("coco-segmentation")
    os.environ['DATASET']
    return dataset
