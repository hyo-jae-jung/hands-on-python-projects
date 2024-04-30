import nltk
from nltk.text import Text
from nltk.draw.dispersion import dispersion_plot

def text_to_string(filename):
    with open(filename, encoding='utf-8', errors='ignore') as infile:
        return infile.read()


# 텍스트 데이터 생성
text_data = text_to_string("hound.txt")

# 텍스트 데이터를 토큰화하여 리스트로 변환
tokens = nltk.word_tokenize(text_data)
tokens = ([token.lower() for token in tokens if token.isalpha()])
# Text 클래스로 변환
text = Text(tokens)
# text.plot(10)
text.dispersion_plot(["holmes"])

