# instruction ={
#     'face_filler_with_temples':"Fills in hollow temples, balancing facial contours.",
#     'botox_with_perioral_line':"Diminishes fine lines around the mouth.",
#     "face_filler_with_cheek":"Adds volume to cheeks for a lifted, fuller look.",
#     'face_vascular_laser':"Reduces redness and visibility of vascular lesions on the skin's surface.",
#     'face_genesis_laser':"Smoothens skin texture, reduces pore size, and softens mild wrinkles.",
#     'face_filler_with_nasolabial_folds':"Softens deep lines from the nose to the mouth.",
#     'botox_with_bunny_line':"Reduces wrinkles on the nose and eyes",
#      'botox_with_jaw':"Slims and contours the jawline for a more refined appearance.",
#      "radiofrequency":"Tightens skin, improves contour, and reduces fine lines for a rejuvenated appearance."
#      ,'face_filler_with_marionette_lines':" Reduces the appearance of lines from mouth corners to the chin.",
#      'face_fractional_laser':"Improves skin texture, diminishes fine lines, wrinkles, and acne scars.",
#      'botox_with_forehead':"Reduces horizontal forehead lines for a smoother forehead.",
#      'botox_with_dimpled_chin':" Smoothens the orange peel-like texture of the chin.",
#      'face_filler_with_tear_troughs':"Reduces under-eye hollows for a refreshed look.",
#      "botox_with_glabellar":"Softens frown lines between the eyebrows.",
#      'face_thread_lifting':"Provides an immediate lifting effect, reducing sagging and enhancing the youthfulness of the face.",
#      'face_filler_with_chin':"Enhances the chin profile for a stronger appearance.",
#      'face_laser_toning':"Enhances skin tone uniformity and reduces pigmentation issues like melasma and sun spots.",
#      'botox_with_crow_feet':" Smoothens wrinkles around the eyes.",
#      'face_filler_with_lips':"Adds volume for fuller, more defined lips.",
#      'face_filler_with_nose':"Corrects minor bumps or irregularities for a smoother nose contour.",
#      'radiofrequency_microneedling':"Enhances skin texture, tightens skin, and reduces the appearance of scars and large pores.",
#      'high_intensity_focused_ultrasound':"Lifts and tightens skin, especially around the jawline and cheeks for a more youthful look."
#     }

import requests

# 이미지 파일 경로
image_path = '../data/face_filler_with_nose/before/image_0.jpg' # 이미지 설정해주세요

# prompt 데이터
prompt = 'face_laser_toning'

# POST 요청 보내기
url = 'http://127.0.0.1:5000/predict'  # 실제 서버 주소로 변경해주세요

# 이미지 파일 열기
with open(image_path, 'rb') as file:
    image_data = file.read()

# POST 요청의 body 데이터 설정
data = {
    'prompt': prompt,
    # 'type':prompt
}

# 이미지 파일과 함께 POST 요청 보내기
files = {
    'image': (image_path, image_data, 'image/jpeg')
}

# POST 요청 보내기
response = requests.post(url, data=data, files=files)

# 응답 결과 확인
if response.status_code == 200:
    prediction = response.json()
    print('예측 결과:', prediction['result'])
    # print('result Image', prediction['image_data'])
    
else:
    print('예측 요청에 실패하였습니다. 상태 코드:', response.status_code)
