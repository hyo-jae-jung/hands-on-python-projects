# 챕터 개요
스타일로메트리 사용으로 잃어버린 세계를 쓴 작가 찾기  


# 환경  

Python 3.10.12  

## packages
nltk                      3.8.1  
  ┣ nltk.download('punkt') / Punkt Tokenizer Models  
  ┣ nltk.download('stopwords') / Stopwords Corpus(불용어 코퍼스)  
  ┗ nltk.download('averaged_perceptron_tagger')  


# 참조

## Chi-square

### 카이제곱 통계량 특징
각 데이터가 독립적이며 범주형 데이터(도수)로 수집  

$$\chi^2 = \sum_{i}\frac{(O_i - E_i)^2}{E_i}$$  
O : 관찰값, E : 기대값  

### 독립성 검정  
  ***하나의 모집단의 두 개 표본 설명변수 비율이 같으면 독립이다.***  
### 동질성 검정  
  ***두 개의 모집단의 표본 각각의 설명변수 비율이 같다면 동질하다.***  

### 계산  
  카이제곱 통계량 계산  
  자유도 계산(df = (r-1)(c-1))  
  카이제곱 분포표에서 자유도와 p값 에 맞는 값과 계산한 값 비교  
  판단은 가설 설정과 통계량 비교로 판단  


## Jaccard similarity coefficient
intersection over union / 교집합 나누기 합집합. 해당 값의 크기로 유사도 판단

## sentiment analysis
[https://www.bbc.com/culture/article/20180525-every-story-in-the-world-has-one-of-these-six-basic-plots]
