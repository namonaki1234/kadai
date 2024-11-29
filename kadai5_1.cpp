#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 3// 3x3の行列を扱う
int main() {
	int i, j, k;
	double a[N][N] = { {2, -4, 6}, {-1, 3, -4}, {1, 1, -
	2} };// 行列A
	double l[N][N], u[N][N];
	// LとUの初期化
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (i == j) {
				l[i][j] = 1.0;// 対角成分は1
			}
			else {
				l[i][j] = 0.0;// それ以外は0
			}
			u[i][j] = 0.0;// U行列は全て0で初期化
		}
	}
	// ガウスの消去法でLU分解
	for (k = 0; k < N; k++) {
		// U行列の計算
		for (j = k; j < N; j++) {
			u[k][j] = a[k][j];
		}
		// L行列の計算
		for (i = k + 1; i < N; i++) {
			l[i][k] = a[i][k]/ u[k][k];
			for (j = k; j < N; j++) {
				a[i][j] = a[i][j]- l[i][k]* u[k][j];
			}
		}
	}
	// L行列の表示
	printf("下三角行列L:\n");
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			printf("%10.6f ", l[i][j]);
		}
		printf("\n");
	}
	// U行列の表示
	printf("上三角行列U:\n");
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			printf("%10.6f ", u[i][j]);
		}
		printf("\n");
	}
	return 0;
}