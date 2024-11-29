#include <stdio.h>
#include <math.h>

#define N 3    
#define E 0.001  // 許容誤差

int main(int argc, char* argv[]) {
    // 拡大係数行列
    double a[N][N + 1] = {
        {2.0, 2.0, 6.0, 24.0},
        {3.0, 5.0, 13.0, 52.0},
        {5.0, 8.0, 24.0, 93.0}
    };

    double pivot, del;
    int i, j, k;

    // ガウスジョルダン法
    for (i = 0; i < N; i++) {
        pivot = a[i][i];  // 対角要素をピボットとする
        
        // ピボットが許容誤差以下か確認
        if (fabs(pivot) < E) {
            printf("エラー: ピボット要素が許容誤差レベル以下です。\n");
            return 1;
        }

        // ピボット行の正規化
        for (j = i; j < N+1; j++) {
            a[i][j] /= pivot;
        }

        // ピボット列を0にする
        for (k = 0; k < N; k++) {
            if (k != i) {
                del = a[k][i];
                for (j = i; j < N+1; j++) {
                    a[k][j] -= del * a[i][j];
                }
            }
        }
    }

    // 結果を表示
    for (i = 0; i < N; i++) {
        printf("x%d = %6.2f\n", i + 1, a[i][N]);
    }

    return 0;
}
