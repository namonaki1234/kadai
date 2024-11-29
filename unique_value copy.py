import numpy as np

# 行列の定義
A = np.array([[4, 2, 1],
              [2, 1, 2],
              [1, 2, 8]])

# 与えられた固有値と固有ベクトル
lambda1 = 4.2361
v1 = np.array([0.8715, 0.2977, -0.3897])

lambda2 = -0.2361
v2 = np.array([-0.3868, 0.9058, -0.1730])

lambda3 = 9.0000
v3 = np.array([0.3015, 0.3015, 0.9045])

# 検算
result1 = A @ v1
expected1 = lambda1 * v1

result2 = A @ v2
expected2 = lambda2 * v2

result3 = A @ v3
expected3 = lambda3 * v3

print("A v1:", result1)
print("lambda1 v1:", expected1)

print("A v2:", result2)
print("lambda2 v2:", expected2)

print("A v3:", result3)
print("lambda3 v3:", expected3)
