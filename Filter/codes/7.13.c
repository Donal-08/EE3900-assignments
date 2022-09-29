

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "header.h"

int main() {
    
// Writing to this file the real part of output data 'X' so as to use it to plot
    FILE *fp = fopen("fft.dat", "w");
    
    int N = 8; 
	double complex x[8] = {1, 2, 3, 4, 2, 1, 0, 0};
	double complex *X = FFT(x, N);
    
	for (int i = 0; i < 8; i++) {
		printf("%lf %lf\n", creal(X[i]), cimag(X[i]));
		fprintf(fp, "%lf\n", creal(X[i]));
	}
	fclose(fp);
	return 0;
}