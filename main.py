import numpy as np
import matplotlib.pyplot as plt


x = np.array([0, 1, 2, 3]) # 1x4 벡터
y = np.array([-1, 0.2, 0.9, 3.1])

x1 = np.vstack([x, np.ones(len(x))])

Temp = np.linalg.inv(np.matmul(x1,x1.T))
w = np.matmul(np.matmul(Temp, x1), y)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, w[0]*x + w[1], 'r', label='Fitted line')
plt.legend()
plt.show()