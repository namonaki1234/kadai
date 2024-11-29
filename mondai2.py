import numpy as np
import matplotlib.pyplot as plt

# 目的関数
def f(x, y):
    return 0.2 * x**4 + 2 * x**2 + 3 * x * y + 6 * y**2

# 勾配
def grad_f(x, y):
    return np.array([0.8 * x**3 + 4 * x + 3 * y, 3 * x + 12 * y])

# 最急降下法
def steepest_descent(x0, y0, L, tol=1e-6):
    x, y = x0, y0
    alpha = 0.0684 #1 / L
    iterations = []
    norms = []
    
    while True:
        g = grad_f(x, y)
        norm_g = np.linalg.norm(g)
        iterations.append(len(iterations))
        norms.append(norm_g)
        
        if norm_g < tol:
            break
        
        x -= alpha * g[0]
        y -= alpha * g[1]
    
    return iterations, norms

# Nesterovの加速勾配法(改)
def nesterov_accelerated_gradient(x0, y0, L, tol=1e-6):
    x, y = x0, y0
    A_k = 0  # 初期値
    beta_k =1  # 初期値
    k = 0
    w_k, z_k = x, y  # w_k, z_kを初期点として設定
    iterations = []
    norms = []
    
    while True:
        # 勾配の計算
        u_k = (A_k / (A_k + beta_k)) * x + (1 - (A_k / (A_k + beta_k))) * w_k
        v_k = (A_k / (A_k + beta_k)) * y + (1 - (A_k / (A_k + beta_k))) * z_k
        
        g = grad_f(u_k, v_k)
        norm_g = np.linalg.norm(g)
        iterations.append(len(iterations))
        norms.append(norm_g)
        
        if norm_g < tol:
            break
        
        # 更新式
        x_new = u_k - (1 / L) * g[0]
        y_new = v_k - (1 / L) * g[1]
        
        # β_kの計算
        beta_k = (1 + (4 * A_k) ** 0.5) / 2
        
        # (w_k, z_k)の更新
        w_k, z_k = w_k - (beta_k / L) * g[0], z_k - (beta_k / L) * g[1]
        
        # A_(k+1)の更新
        A_k += beta_k
        
        # 次の反復のための準備
        x, y = x_new, y_new
        k += 1
    
    return iterations, norms

#再スタート付きNAG(改)
def restart_nag(x0, y0, L, tol=1e-6):
    x, y = x0, y0
    A_k = 0  # 初期値
    beta_k = 1 # 初期値
    k = 0
    w_k, z_k = x, y  # w_k, z_kを初期点として設定
    iterations = []
    norms = []
    
    while True:
        # τ_kの計算
        beta_k = (1 + (4 * A_k) ** 0.5) / 2
        tau_k = A_k / (A_k + beta_k)

        # (u_k, v_k)の計算
        u_k = tau_k * x + (1 - tau_k) * w_k
        v_k = tau_k * y + (1 - tau_k) * z_k
        
        # 勾配の計算
        g = grad_f(u_k, v_k)
        norm_g = np.linalg.norm(g)
        iterations.append(len(iterations))
        norms.append(norm_g)
        
        if norm_g < tol:
            break
        
        # 更新式
        x_new = u_k - (1 / L) * g[0]
        y_new = v_k - (1 / L) * g[1]
        
        # (w_k, z_k)の更新
        w_new = w_k - (beta_k / L) * g[0]
        z_new = z_k - (beta_k / L) * g[1]
        
        # A_(k+1)の更新
        A_k_next = A_k + beta_k
        
        # fの値を比較してA_kを更新
        if f(x_new, y_new) > f(x, y):
            A_k_next = 0
            w_new, z_new = x_new, y_new
        
        # A_kの更新
        A_k = A_k_next
        
        # 次の反復のための準備
        x, y = x_new, y_new
        w_k, z_k = w_new, z_new
        k += 1
    
    return iterations, norms


# 初期点の設定
x0, y0 = 2, -3
L = 14.61
tol = 1e-6

# 各アルゴリズムの実行
iterations_sd, norms_sd = steepest_descent(x0, y0, L, tol)
iterations_nag, norms_nag = nesterov_accelerated_gradient(x0, y0, L, tol)
iterations_restart_nag, norms_restart_nag = restart_nag(x0, y0, L, tol)

# プロット
plt.figure(figsize=(12, 6))
plt.semilogy(iterations_sd, norms_sd, label='steepest descent', marker='o')
plt.semilogy(iterations_nag, norms_nag, label='Nesterov Accelerated Gradient', marker='s')
plt.semilogy(iterations_restart_nag, norms_restart_nag, label='Restarted NAG', marker='^')
plt.xlabel('number of iterations', fontsize=14)
plt.ylabel('||∇f||', fontsize=14)
plt.title('semi-log plot of the gradient norm', fontsize=16)
plt.legend(loc='upper right', fontsize=12)
plt.grid()
plt.show()
