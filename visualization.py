import matplotlib.pyplot as plt
from bayes_challenge2 import main

# 두 개의 리스트 생성 (예시)
data1 = []
data2 = []

# for _ in range(10):
#     data1.append(main('123'))
#     data2.append(main('456'))

print(data1,data2)

# 히스토그램 그리기
plt.hist(data1, color='blue', alpha=0.5, label='Data 123')
plt.hist(data2, color='red', alpha=0.5, label='Data 456')

# 축 레이블과 범례 추가
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 그래프 보이기
plt.show()
