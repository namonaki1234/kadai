import numpy as np

# 目的関数
def f(x):
    return (1/4) * x**4 + (2/3) * x**3 - (9/2) * x**2 + 10 * x

# 一階導関数
def df(x):
    return x**3 + 2 * x**2 - 9 * x + 10

# 二階導関数
def d2f(x):
    return 3 * x**2 + 4 * x - 9

# ニュートン法の実装
def newton_method(x0, tol=1e-6, max_iter=100):
    k = 0
    x_k = x0
    
    while k < max_iter:
        f_prime = df(x_k)
        f_double_prime = d2f(x_k)
        
        # 終了条件
        if abs(f_prime) < tol:
            print(f"収束しました: x = {x_k}, f(x) = {f(x_k)}, 反復回数 = {k}")
            return x_k
        
        # 更新式
        x_k = x_k - f_prime / f_double_prime
        k += 1
    
    print("最大反復回数に達しました。")
    return None

# 初期点の設定
x0 = 0.5  # 初期点 x_0 = 0.5
result = newton_method(x0)
