import streamlit as st
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
from PIL import Image
import torch
import time
# Streamlit 앱의 타이틀 설정
st.title("Stable Diffusion 이미지 변환 데모")

# Hugging Face 모델 파이프라인 초기화
try:
    model_id = "C:/Users/kihoon/Desktop/AI/skin_care/diffusion_model/skinTreat"

    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None) # GPU 있을때
    # pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, safety_checker=None)
    # pipe.to("cpu")
    pipe.to('cuda') # GPU 있을때
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    
    print('MODEL LOADING :OK')
except Exception as e:
    print(e)
    print("MODEL LOAD : FAILE")

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
# 사용자 입력 받기
st.title("피부 치료 선택")

# 사용자에게 선택을 위한 드롭다운 메뉴 표시
selected_treatment = st.selectbox("치료 방법을 선택하세요:", list(instruction.keys()))

# 선택된 치료 방법에 대한 설명을 표시
st.write("선택한 치료 방법에 대한 설명:")
st.write(instruction[selected_treatment])

prompt =  f"Transform the image to show a subtle and natural improvement as if face style have chante to enhanced {selected_treatment} while preserving the original facial structure "
# print(promp)
# 이미지 입력 받기
uploaded_file = st.file_uploader("변환할 이미지 업로드", type=["jpg", "jpeg", "png"])

# 제출 버튼 추가
if st.button('변환'):
    if uploaded_file is not None and prompt:
        # PIL로 이미지 로드
        image = Image.open(uploaded_file).convert("RGB")
        progress_bar = st.progress(0)
        status_text = st.empty()
        # 모델을 사용하여 이미지 변환
        # time.sleep(2)
        with torch.no_grad():
            outputs = pipe(prompt, image=image, num_inference_steps=30, image_guidance_scale=0.2,guidance_scale=5.0,num_images_per_prompt=4)['images']
            for i in range(30):  # num_inference_steps에 해당하는 반복 횟수
                progress_bar.progress((i + 1) / 30)  # 프로그레스 바 업데이트
                status_text.text(f"변환 중... {int((i + 1) / 30 * 100)}%")
                time.sleep(0.1)  # 이 부분은 실제 모델 실행 시간에 맞게 조정해야 함
        print(outputs)
        st.image(image, caption="원본 이미지", use_column_width=True)
        # 변환된 이미지를 화면에 표시
        st.image(outputs[:2], width=300, caption=["변환된 이미지 1", "변환된 이미지 2"])  # 예시로 3개의 이미지가 있다고 가정
        st.image(outputs[2:], width=300, caption=["변환된 이미지 3", "변환된 이미지 4"])
# Streamlit 앱 실행 방법
# 터미널에 "streamlit run your_script_name.py" 명령어 입력
