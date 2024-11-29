#include <stdio.h>
#include <math.h>

#define N 6     // データ数
#define M 4     // 次数
#define EPS 0.0001  // 許容誤差

double a[M + 1][M + 2];  // 行列の拡大版（M+1行, M+2列）

int jordan(void);  // カウス・ジョルダン法

int main(int argc, char* argv[]) {
    double X[N] = {0.0, 1.0, 2.0, 3.0, 3.1, 5.0};  // Xのデータ
    double Y[N] = {0.0, 1.1, 2.5, 4.0, 4.1, 5.0};  // Yのデータ
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
                a[i][j] += pow(X[k], (double)(i + j));
            }
        }
    }
    
    // 正規方程式の右辺を作成
    for (j = 0; j <= M; j++) {
        for (k = 0; k < N; k++) {
            a[j][M + 1] += Y[k] * pow(X[k], double(j));
        }
    }
    
    // カウス・ジョルダン法で解を求める
    if (jordan() == 1) return 1;
    
    // 結果を表示
    for (i = 0; i <= M; i++) {
        printf("A%2d = %7.3f\n", i, a[i][M + 1]);
    }
    
    return 0;
}

int jordan(void) {
    double pivot, delta;
    int i, j, k;
    
    for (i = 0; i <= M; i++) {
        pivot = a[i][i];
        if (fabs(pivot) < EPS) {
            printf("ピボットが許容誤差以下\n");
            return 1;
        }
        for (j = i; j <= M + 1; j++) {
            a[i][j] /= pivot;
        }
        for (k = 0; k <= M; k++) {
            delta = a[k][i];
            
            for (j = i; j <= M + 1; j++) {
                if (k != i) {
                a[k][j] -= delta * a[i][j];
                }
            }
        }
    }
    
    return 0;
}
