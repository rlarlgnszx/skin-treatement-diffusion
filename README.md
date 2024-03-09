# skin-treatement-diffusion

## 피부시술 AI 생성 프로젝트 
### 피부시술시에 내 모습은 어떨까?
![6955343](https://github.com/rlarlgnszx/skin-treatement-diffusion/assets/40743105/2788900e-9aa4-4ec4-a937-b3a2d3d51f95)

## STACK
- **python3.10**
    - **opencv :**
        - 이미지 편집 및 가공등의 전처리 수행
    - **matplotlib :**
        - 다양한 이미지 시각화 기능으로써 활용
    - **wandb :**
        - 훈련모델의 loss와 output값 시각화 및 저장
    - **transformer :**
        - transfer learning을 위한 모델 weight load
    - **dlib :**
        - 데이터 전처리시 face recognition을 위한 모델 load로써 활용
    - **ultralytics :  yolo**
        - 데이터 전처리시 image slice를 위해 face region dection에 활용
    - **torch+cuda 11.8 , RTX 3090**
        - 모델 훈련
    - **streamlit :**
        - demo 모델 배포 및 사용자 적을 경우의 서버로써 활용
    - **flask :**
        - 모델훈련결과를 받기위해 backend 팀과의 모델 endpoint의 방식을 HTTP로 사용하기 위해 활용
     

- **MediaPipe : Face Landmark**
    - 이미지의 Mask를 생성해 내기위해  opencv와 결합해 이미지 landmark로부터 mask추출
 

- **huggingface**
    - 다양한 pretrained 모델 search와 모델 storage와 개발한 모델을 API로써 활용하기 위해 사용
 

- AI model
    - **Swin Transformer**
        - Noisy data에서 적절한 feaure를 가진 image를 추출하기 위한 binary classifcation 모델로써 활용
    - **Yolo v8**
        - 1차적 분류를 통한 data를 Face Region Detection을 통해 모델 개발에 필요한 데이터셋으로 변경해주기 위해 활용
    - **Stable Diffusion InstructPix2Pix**
        - 처음 선택한 모델로써 피부타입의 변화를 생성하기 위한 모델로써 사용
            - 아래 모델로 변경
    - **Stable Diffusion Inpainting**
        - Mediapipe를 통해 생성한 mask로부터 masking된 부분의 부분생성을 위한 모델로써 활용
     
  
## OverView
![image](https://github.com/rlarlgnszx/skin-treatement-diffusion/assets/40743105/c905d114-8acc-4690-b187-a40ad48630df)
### 
## Demo 1. NO Inpainting

## File Structure
```
┖ 1.Data Downloader : Image Downloader
┖ 2.Data2right_image : Can't Use Image Classification 
┖ 3.image_to_slice_with_yolo : Image to Split with AI Algorithm
┖ 4.Making_dataset : Image to Dataset
┖ 5.skin_treatment_model : AI Model Training
┖ 6.Face Landmark : For AI Dataset( Use it after 3 )
┖ Wrinkle Detector : AI for Wrinkle Detection (Adding)
```

<hr>
<!-- <h4 align="center">A minimal Markdown Editor desktop app built on top of <a href="http://electron.atom.io" target="_blank">Electron</a>.</h4> -->

## Key Features

* 사용된 모델 : [Huggingface InpaintingDiffusion]
	* Model Reference
	* [Huggingface](https://huggingface.co/runwayml/stable-diffusion-inpainting)
* 이미지 분할을 위한 Yolov8
  - Noisy data의 사용화
<hr>

## How To Use
<hr>

### 1.Clone this repository

```
# Clone this repository
$ git clone  https://github.com/rlarlgnszx/skin-treatment-diffusion.git
```

### 2.Run for your data search

```
$ python 1.Data Downloader/bing_search.py
```

### 3. Select Using data to put True,other to put False => SemiSupervised 
![image](https://github.com/rlarlgnszx/skin-treatement-diffusion/assets/40743105/f97a7bd7-e9e6-431b-91c7-515d7d3fd325)

```
$ jupyternotebook
# open data2right.ipynb and train
```


### 4. If image has more than two face, use
![image](https://github.com/rlarlgnszx/skin-treatement-diffusion/assets/40743105/30b09510-443e-4b25-9aa0-043f08372378)
```
$ jupyternotebook
# finetuning_yolo8.ipynb
# split_with_yolov8.ipynb
```
- 방법 1. opencv의 선검출을 통한 이미지 붙여진 선 검출을 통해 자르는 모델
    - 분류 효과가 좋지 않았고 선검출을 잘 못하는 경우가 많아 확실하게 잘리지 않음
        - **실패**
- 방법 2. dlib의 face recognitino을 통한 얼굴 검출을 통한 얼굴 분리
    - 얼굴 전체가 나타나지 않는 경우가 많아 확실하게 잘리지 않음
        - **실패**
- 방법 3. yolo  v8을 통한 얼굴부위 별 검출을 통해 얼굴 부위펼 평균값을 통해 각 얼굴부위의 중앙값을 판별하고 중앙값들의 차이를 통해 가로선과 세로선으로 구분해 반으로 slice
![image](https://github.com/rlarlgnszx/skin-treatement-diffusion/assets/40743105/73087de5-a2cb-4177-a0f2-1bd92f1f7da0)
### 4. If image has more than two face, use
```
$ jupyternotebook
# finetuning_yolo8.ipynb
# split_with_yolov8.ipynb
```


### 3.Upload folder
![image](https://user-images.githubusercontent.com/40743105/190638113-737d8ed6-4e88-4721-81e4-38ce90b36c33.png)


### End. Go to News site And Wait Untill it summary News And detect the Fake News!


백엔드, 크롬익스텐션 부분 = 김기훈
AI 모델 , 크롤링 = 안제준 

