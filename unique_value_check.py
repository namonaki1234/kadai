import numpy as np

# 行列の定義
A = np.array([[3.0, 0.0, 0.0, 1.0],
              [0.0, 3.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 0.0],
              [1.0, 0.0, 0.0, 3.0]])

# 固有値と固有ベクトルの計算
eigenvalues, eigenvectors = np.linalg.eig(A)

print("固有値:", eigenvalues)
print("固有ベクトル:\n", eigenvectors)
