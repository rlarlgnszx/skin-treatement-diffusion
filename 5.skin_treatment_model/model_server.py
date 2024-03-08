from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler,StableDiffusionPix2PixZeroPipeline
import PIL
import torch
from datasets import Image
import numpy as np


app = Flask(__name__)
print('Model Loading...')
try:
    model_id = 'skin_treat'
    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None) # GPU 있을때
    # pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, safety_checker=None)
    # pipe.to("cpu")
    pipe.to('cuda') # GPU 있을때
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    instruction ={
        'face_filler_with_temples':"Fills in hollow temples, balancing facial contours.",
        'botox_with_perioral_line':"Diminishes fine lines around the mouth.",
        "face_filler_with_cheek":"Adds volume to cheeks for a lifted, fuller look.",
        'face_vascular_laser':"Reduces redness and visibility of vascular lesions on the skin's surface.",
        'face_genesis_laser':"Smoothens skin texture, reduces pore size, and softens mild wrinkles.",
        'face_filler_with_nasolabial_folds':"Softens deep lines from the nose to the mouth.",
        'botox_with_bunny_line':"Reduces wrinkles on the nose and eyes",
        'botox_with_jaw':"Slims and contours the jawline for a more refined appearance.",
        "radiofrequency":"Tightens skin, improves contour, and reduces fine lines for a rejuvenated appearance."
        ,'face_filler_with_marionette_lines':" Reduces the appearance of lines from mouth corners to the chin.",
        'face_fractional_laser':"Improves skin texture, diminishes fine lines, wrinkles, and acne scars.",
        'botox_with_forehead':"Reduces horizontal forehead lines for a smoother forehead.",
        'botox_with_dimpled_chin':" Smoothens the orange peel-like texture of the chin.",
        'face_filler_with_tear_troughs':"Reduces under-eye hollows for a refreshed look.",
        "botox_with_glabellar":"Softens frown lines between the eyebrows.",
        'face_thread_lifting':"Provides an immediate lifting effect, reducing sagging and enhancing the youthfulness of the face.",
        'face_filler_with_chin':"Enhances the chin profile for a stronger appearance.",
        'face_laser_toning':"Enhances skin tone uniformity and reduces pigmentation issues like melasma and sun spots.",
        'botox_with_crow_feet':" Smoothens wrinkles around the eyes.",
        'face_filler_with_lips':"Adds volume for fuller, more defined lips.",
        'face_filler_with_nose':"Corrects minor bumps or irregularities for a smoother nose contour.",
        'radiofrequency_microneedling':"Enhances skin texture, tightens skin, and reduces the appearance of scars and large pores.",
        'high_intensity_focused_ultrasound':"Lifts and tightens skin, especially around the jawline and cheeks for a more youthful look."
        }
    print('MODEL LOADING :OK')
except Exception as e:
    print(e)
    print("MODEL LOAD : FAILE")
# 모델 예측 함수

def diffusion_get(image,type):
    # url = "data/botox_with_bunny_line/before/image_0.jpg"
    # type = 'botox_with_glabellar'
    type = instruction[type]
    prompt = f"turn image to show a subtle and natural improvement as if face style have chante to make {type} while preserving the original facial structure "
    # prompt = type
    # prompt = f' face style change : {type}  , perserving : facial structure '
    # and enhanced skin clarity and even tone"
    # while preserving the original facial structure and features."# prompt = "Reduces wrinkles on the nose when smiling."
    images = pipe(prompt, image=image, num_inference_steps=20, image_guidance_scale=0.2,guidance_scale=5,num_images_per_prompt=7).images
    # images = list(map(np.array,images))
    images.append(image)
    return images


def download_image(url):
        image = PIL.Image.open(url)
        image = PIL.ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        image.resize((300,300))
        return image
    

def predict(prompt, image_data):
    images = diffusion_get(image_data,prompt)
    size= images[0].size
    images = list(images[0].getdata())
    prediction = {
        'prompt': prompt,
        'image_data':images,
        'image_shape':size,
        'result': '예측 결과입니다.'
    }
    return prediction

# POST 요청을 처리하는 라우트
@app.route('/predict', methods=['POST'])

def handle_predict():
    # POST 요청에서 prompt와 이미지 데이터를 받아옵니다.
    prompt = request.form.get('prompt')
    image_file = request.files['image']
    # 이미지 데이터를 PIL Image로 변환합니다.
    image = download_image(image_file)
    
    # 이미지 데이터를 numpy 배열로 변환합니다.
    # image_data = np.array(image)

    # 모델 예측 함수를 호출하여 결과를 받아옵니다.
    prediction = predict(prompt, image)
    # 예측 결과를 JSON 형태로 반환합니다.
    return jsonify(prediction)

if __name__ == '__main__':
    # pipe = model_init(model_id)
    app.run()
