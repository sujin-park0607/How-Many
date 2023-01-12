# How Many
유동인구 자동 측정 시스템으로 실시간으로 받아오는 이미지 데이터로 영상처리를 진행한 후 실시간 스트리밍 영상을 웹 페이지에 보여주고 통계 그래프를 제공하는 Web Application이다.

## Technical Stack
|분야|기술|설명|
|---|---|---|
|BackEnd|<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">|Django Rest Framwork 사용|
|FrontEnd|<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white">|.|
|Python|<img src="https://img.shields.io/badge/YOLOv4-00FFFF?style=for-the-badge&logo=Yolo&logoColor=white">|YOLOv4사용|
|HardWare|<img src="https://img.shields.io/badge/Raspberry Pi-A22846?style=for-the-badge&logo=RaspberryPi&logoColor=white">| Raspberry pi4 사용|

## Architecture
1. RaspberryPi에 연결되어있는 웹캠으로 이미지를 입력받아 스트리밍 서버를 통해 모니터링페이지, Python 모듈에 전달
2. Python OpenCV를 통해 이미지를 영상처리 후 Django서버에 전송하고 유동인구 측정값을 DB에 저장
3. 스트리밍 서버에서 이미지, 데이터베이스에서 유동인구 측정값을 가져와 실시간 스트리밍페이지와 통계페이지를 사용자에게 제공

![image](https://user-images.githubusercontent.com/75667075/212143282-72426328-5e7f-4025-bef5-60e096864c87.png)

## EndPoint
|URL|Http|설명|
|---|---|---|
|/login|GET|로그인, user데이터를 모두 반환|
|/signup|POST|로그인, user데이터를 모두 반환|
|/year, /month, /day, /time, /now|GET|메인 그래프인 년 ,월 ,일 ,시 ,실시간 데이터를 반환|
|/subyear, /submonth, /subday, /subtime, /subnow|GET|서브그래프로 년별, 월별, 일별, 시간별을 비교하여 
각각 숫자로, 퍼센트로 구분하여 표시|
|/result_getStream|POST|영상처리된 이미지 파일을 받는 url|

## 실행방법
```
git clone https://github.com/sujin-park0607/HM.git
pip install -r requirements.txt

npm install
(경로 진입 후)npm start

```

## Demo Video
https://www.youtube.com/watch?v=Dzk2jMXjMtc&ab_channel=%EB%B0%95%EC%88%98%EC%A7%84



