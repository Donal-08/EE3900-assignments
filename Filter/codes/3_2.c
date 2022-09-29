#include<stdio.h>
#include<stdlib.h>

int main(){
    double x[6] = {1.0,2.0,3.0,4.0,2.0,1.0} ;
    
    FILE *fpx = fopen("x.txt","w");
    for(int i=0; i < 6; i++){
        fprintf(fpx,"%lf\n",x[i]);

    }
    int k = 20;
    double y[20];
    FILE *fp = fopen("y.txt","w");

    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];
    
    fprintf(fp,"%lf\n",y[0]);
    fprintf(fp,"%lf\n",y[1]);

    for(int n = 2; n < k; n++){
	if (n < 6)
		y[n] = -0.5*y[n-1]+x[n]+x[n-2];

	else if ((n > 5) && (n < 8))
		y[n] = -0.5*y[n-1]+x[n-2];

	else
		y[n] = -0.5*y[n-1];

    fprintf(fp,"%lf\n",y[n]);
    }

    

}