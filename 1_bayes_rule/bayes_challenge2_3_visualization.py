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

print("123전략",sum(data1)/cnt,"회\n","456전략",sum(data2)/cnt,"회\n","PoD전략",sum(data3)/cnt,"회")
print(f"시뮬레이션 횟수: {cnt}")
print("파일 실행 시간(초)",time.time() - start)

# 히스토그램 그리기
plt.hist(data1, color='blue', alpha=0.5, label='한 개 영역 집중 탐색')
plt.hist(data2, color='red', alpha=0.5, label='두 개 영역 분산 탐색')
plt.hist(data3, color='green', alpha=0.5, label='가장 큰 PoD 탐색')

# 축 레이블과 범례 추가
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 그래프 보이기
plt.show()
