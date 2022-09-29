// Generating the toeplitz matrix corresponding to h(n)



#include <stdio.h>

#define N 20

double delta(int n) {
	if (n == 0) return 1;
	else return 0;
}

double h(int n) {
	if (n == 0) return 1;
	else if (n > 0) return delta(n) + delta(n-2) - 0.5*h(n-1);
	else return 2*(delta(n+1) + delta(n-1) - h(n+1));
}

int main() {
	FILE *fp = fopen("toeplitz.dat", "w");
	for (int i = 0; i < 2*N - 1; i++) {
		for (int j = 0; j < N; j++) {
			if (i >= j && i - j < N) fprintf(fp, "%lf ", h(i-j));
			else fprintf(fp, "0 ");
		}
		fprintf(fp, "\n");
	}
	fclose(fp);
	return 0;
}