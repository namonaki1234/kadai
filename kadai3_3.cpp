#include <stdio.h>
#include <math.h>

#define N 8     // データ数
#define M 3     // 次数（今回は三次多項式）
#define EPS 0.0001  // 許容誤差

double a[M + 1][M + 2];  // 拡大係数行列（M+1行, M+2列）

int jordan(void);  // ガウス・ジョルダン法

int main(int argc, char* argv[]) {
    // 与えられたX, Yデータ
    double X[N] = {-4.0, -2.0, -1.0, 0.0, 1.0, 3.0, 4.0, 6.0};
    double Y[N] = {-35.1, 15.1, 8.9, 8.9, 0.1, 0.1, 21.1, 135.0};
    int i, j, k;
    
    // 行列を初期化
    for (i = 0; i <= M; i++) {
        for (j = 0; j <= M + 1; j++) {
            a[i][j] = 0.0;
        }
    }
    
    // 正規方程式の係数行列を作成
    for (i = 0; i <= M; i++) {
        for (j = 0; j <= M; j++) {
            for (k = 0; k < N; k++) {
                a[i][j] += pow(X[k], (double)(i + j));  // ΣX^i * X^j
            }
        }
    }
    
    // 正規方程式の右辺を作成
    for (j = 0; j <= M; j++) {
        for (k = 0; k < N; k++) {
            a[j][M + 1] += Y[k] * pow(X[k], (double)j);  // ΣY * X^j
        }
    }
    
    // ガウス・ジョルダン法で解を求める
    if (jordan() == 1) return 1;
    
    // 結果を表示（多項式の係数）
    for (i = 0; i <= M; i++) {
        printf("A%d = %7.3f\n", i, a[i][M + 1]);
    }
    
    return 0;
}

// ガウス・ジョルダン法
int jordan(void) {
    double pivot, delta;
    int i, j, k;
    
    for (i = 0; i <= M; i++) {
        pivot = a[i][i];
        if (fabs(pivot) < EPS) {
            printf("ピボットが許容誤差以下です\n");
            return 1;
        }
        for (j = i; j <= M + 1; j++) {
            a[i][j] /= pivot;  // ピボット行を正規化
        }
        for (k = 0; k <= M; k++) {
            if (k != i) {
                delta = a[k][i];
                for (j = i; j <= M + 1; j++) {
                    a[k][j] -= delta * a[i][j];  // 他の行を操作してピボット列を0に
                }
            }
        }
    }
    
    return 0;
}
