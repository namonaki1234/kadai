import numpy as np
import matplotlib.pyplot as plt

# データ
X = np.array([-4.0, -2.0, -1.0, 0.0, 1.0, 3.0, 4.0, 6.0])
Y = np.array([-35.1, 15.1, 8.9, 8.9, 0.1, 0.1, 21.1, 135.0])

# 3次多項式の係数を求める
coefficients = np.polyfit(X, Y, 3)

# 結果を表示
print("多項式の係数:")
for i, coef in enumerate(coefficients):
    print(f"A{3-i} = {coef:.3f}")

# 近似曲線を生成
X_smooth = np.linspace(X.min(), X.max(), 200)
Y_smooth = np.polyval(coefficients, X_smooth)

# プロットを作成
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='red', label='Original Data')
plt.plot(X_smooth, Y_smooth, color='blue', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('3次多項式による近似')
plt.legend()
plt.grid(True)

# グラフを表示
plt.show()

# 近似の精度を評価
Y_pred = np.polyval(coefficients, X)
mse = np.mean((Y - Y_pred)**2)
print(f"\n平均二乗誤差 (MSE): {mse:.4f}")