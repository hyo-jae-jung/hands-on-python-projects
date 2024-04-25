# 챕터 개요
실종자 빨리 찾기 게임. 베이즈 규칙을 이용해 다양한 전략 적용


# 환경

Python 3.10.12

## packages
opencv-python          4.9.0.80  
matplotlib             3.5.1  
jupyterlab             4.1.6  
numpy                  1.26.3  


# 파일 구조 및 개요

📦1_bayes_rule  
 ┣ 📂__pycache__  
 ┃ ┣ 📜bayes_challenge2_monte_carlo.cpython-310.pyc  
 ┃ ┗ 📜bayes_challenge3.cpython-310.pyc  
 ┣ 📜28p_bayes_rule.ipynb / 28페이지 베이즈 정리 계산 및 해석  
 ┣ 📜30p.ipynb / 30페이지 베이즈 정리 계산 결과 해석  
 ┣ 📜README.md  
 ┣ 📜bayes.py / 기본 제공 파일. 실행 시 게임 시작  
 ┣ 📜bayes_challenge1.py / 중복 좌표 수색 제한 전략 게임 파일  
 ┣ 📜bayes_challenge2_3_visualization.py / 전략(123,456,PoD)에 따른 시뮬레이션 결과 히스토그램  
 ┣ 📜bayes_challenge2_monte_carlo.py / 방문 전략에 따른 실적 비교. 시행횟수, 방문전략(123,456) 인자를 받아서 실행  
 ┣ 📜bayes_challenge3.py / PoD(probability of detection)전략 게임 파일  
 ┗ 📜cape_python.png / 기본 제공 이미지  


# 참조 이론

## 베이즈 정리
사전확률과 추가정보로 사후확률 구하는 방법

## 몬테 카를로 시뮬레이션
불확실한 사건의 가능한 결과를 추정하는 데 사용되는 수학적 기법

