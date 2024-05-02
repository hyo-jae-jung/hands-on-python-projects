"""
파이썬 버전 문제인지 다른 plot은 출력하는데 dispersion_plot은 안됨
정답 코드도 안됨
시각화는 matplotlib로 직접 만들어야 할 듯
"""

import nltk
# from nltk.text import Text
# from nltk.draw.dispersion import dispersion_plot

def text_to_string(filename):
    with open(filename, encoding='utf-8', errors='ignore') as infile:
        return infile.read()


# # 텍스트 데이터 생성
# text_data = text_to_string("hound.txt")

# # 텍스트 데이터를 토큰화하여 리스트로 변환
# tokens = nltk.word_tokenize(text_data)
# tokens = ([token.lower() for token in tokens if token.isalpha()])

# print(nltk.pos_tag(tokens))

# # Text 클래스로 변환
# text = Text(tokens)
# # text.plot(10)
# # dispersion_plot(text,["Holmes","Watson","Mortimer","Henry","Barrymore","Stapleton","Selden","hound"])
# # text.concordance("Holmes")


"""Use NLP (nltk) to make dispersion plot."""
import matplotlib.pyplot as plt
from nltk.draw.dispersion import dispersion_plot
    
# def text_to_string(filename):
#     """Read a text file and return a string."""
#     with open(filename) as infile:
#         return infile.read()

corpus = text_to_string('hound.txt')
tokens = nltk.word_tokenize(corpus)
tokens = nltk.Text(tokens)  # NLTK wrapper for automatic text analysis.
words = ['Holmes', 'Watson', 'Mortimer', 'Henry', 'Barrymore', 'Stapleton', 'Selden', 'hound']
ax = dispersion_plot(tokens, words)
# Correct current bug in NLTK dispersion_plot that reverses label order by mistake:
ax.set_yticks(list(range(len(words))), reversed(words), color="C0")
