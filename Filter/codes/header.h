#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include<math.h>

double complex *FFT(double complex *signal, int N);


double complex *FFT(double complex *signal, int N){
    /* Execute the end of the recursive even/odd split 
    once we have only one sample */
    if( N == 1) return signal; 

    // Split the samples into even and odd subsums 
    int M = N/2;
    double complex *X_even = malloc(N/2 * sizeof(*X_even));
    double complex *X_odd = malloc(N/2 * sizeof(*X_odd));

    for(int i=0; i < M; i++){
        X_even[i] = signal[2*i];
        X_odd[i] = signal[2*i + 1];
    }

    double complex *F_even = FFT(X_even, M);
    double complex *F_odd = FFT(X_odd, M);

    double complex *X = malloc(N * sizeof(*X));

    for(int k = 0;k!=N/2; k++){
        X[k] = 	F_even[k] + cexp(-2 * I * M_PI * k / N) * F_odd[k];
		X[k + N/2] = F_even[k] - cexp(-2 * I * M_PI * k / N) * F_odd[k];
	}
	return X;
}


double complex *ifft(double complex *X, int N) {
	if (N == 1) {
		return X;
	}
	double complex *F1 = malloc(N/2 * sizeof(*F1));
	double complex *F2 = malloc(N/2 * sizeof(*F2));
	for (int i = 0; i < N/2; i++) {
		F1[i] = X[2*i];
		F2[i] = X[2*i + 1];
	}
	double complex *f1 = FFT(F1, N/2);
	double complex *f2 = FFT(F2, N/2);
	double complex *x = malloc(N * sizeof(*x));
	for (int i = 0; i < N/2; i++) {
		x[i] = 	0.5 * (f1[i] + cexp(2 * I * M_PI * i / N) * f2[i]);
		x[i + N/2] = 0.5 * (f1[i] - cexp(2 * I * M_PI * i / N) * f2[i]);
	}
	return x;
}

double complex *convolution(double complex *x, int nx, double complex *h, int nh) {
	int ny = nx + nh - 1;
	double complex *y = malloc(ny * sizeof(*y));
	for (int n = 0; n < ny; n++) 
		for (int k = 0; k < nx; k++) 
			if (n - k >= 0 && n - k < nh)
				y[n] = x[k] * h[n-k];
	return y;
}
