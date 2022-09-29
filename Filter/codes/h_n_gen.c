#include<stdio.h>
#include<stdlib.h>

int main(){
    int k = 12;
    double h[12];
    FILE *fp = fopen("h.txt","w");

    h[0] = 1;
    h[1] = -0.5*h[0];
    h[2] = -0.5*h[1] + 1;

    fprintf(fp,"%lf\n",h[0]);
    fprintf(fp,"%lf\n",h[1]);
    fprintf(fp,"%lf\n",h[2]);

    for(int i=3; i < k; i++){
        h[i] = -0.5*h[i-1];
        fprintf(fp,"%lf\n",h[i]);

    }
}
    