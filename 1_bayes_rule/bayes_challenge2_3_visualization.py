import matplotlib.pyplot as plt
import time
from bayes_challenge2_monte_carlo import main
from bayes_challenge3 import main as main3

# 두 개의 리스트 생성 (예시)
data1 = []
data2 = []
data3 = []

start = time.time()
cnt = 1000
for _ in range(cnt):
    data1.append(main('123'))
    data2.append(main('456'))
    data3.append(main3())

print(sum(data1)/cnt,sum(data2)/cnt,sum(data3)/cnt)
print(time.time() - start)

# 히스토그램 그리기
plt.hist(data1, color='blue', alpha=0.5, label='Data 1')
plt.hist(data2, color='red', alpha=0.5, label='Data 2')
plt.hist(data3, color='green', alpha=0.5, label='Data 3')

# 축 레이블과 범례 추가
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 그래프 보이기
plt.show()