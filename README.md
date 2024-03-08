# skin-treatement-diffusion

## 피부시술 AI 생성 프로젝트 
### 피부시술시에 내 모습은 어떨까?
<h1 align="center">
  <br>
  <a><img src="https://user-images.githubusercontent.com/40743105/190645078-09a24278-d0a9-4bcf-ba6f-6ed74d86c8d2.png" alt="Markdownify" width="500" style=```border-radius:70px;```></a>
  <br>
  낚시성 기사 판별을 위한 크롬 확장 프로그램
  <br>
</h1>

## Enviroment
```
jupyter
pytorch==2.0+cu118
CUDA 11.8
huggingface
yolov8
```
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

<p align="center">
  <h2> 기존 사용자 창 </h2>
  <span> 빨강색은 사용자가 마우스를 올려놓아 활성화 할수 있는 상태를 명시적으로 보여주기 위해 설정 </span>
  <img src="https://user-images.githubusercontent.com/40743105/190434799-9951a97c-e61a-45db-9701-4099c37c8d60.png" alt="Markdownify">
</p>

## Key Features

* 사용된 모델 : [Huggingface InpaintindDiffusion]
	* Model Reference
	* [Huggingface]  https://github.com/SKT-AI/KoBART   
* 네이버 특화 News Document Crawling
  - python KoreaNewsCrawler에서 조금더 보완(뉴스이미지명칭,기사주체 등을 빠지게 함)
  - Module Reference 
  	- [Korea News Crawler]  https://github.com/lumyjuwon/KoreaNewsCrawler
<hr>

## How to build
* AWS ec2 (Ubuntu20.04 LTS) 사용해 Chrome 사용자와 REST API 통신
* Server는 Apache2 , Wsgi , Flask 이용해 구축
<hr>


## How To Use
<hr>
### 1.Clone this repository

```
# Clone this repository
$ git clone  https://github.com/rlarlgnszx/Fake_news_Chrome_Extension.git
```

### 2.Go into the chorme extensions

[Chrome_Extension](chrome://extensions)


### 3.Upload folder
![image](https://user-images.githubusercontent.com/40743105/190638113-737d8ed6-4e88-4721-81e4-38ce90b36c33.png)


### End. Go to News site And Wait Untill it summary News And detect the Fake News!


백엔드, 크롬익스텐션 부분 = 김기훈
AI 모델 , 크롤링 = 안제준 

