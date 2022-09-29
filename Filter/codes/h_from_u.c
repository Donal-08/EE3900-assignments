#include<stdio.h>
#include<stdlib.h>

int main(){
    int n[14];
    double x[6] = {1.0,2.0,3.0,4.0,2.0,1.0} ;
    double fn[14], hn1[14], hn2[14];
    double h[14];
    double y[21];
    
    for (int i=0; i < 14; i++){
        n[i] = i;
        fn[i] = pow((-1/2), n[i]);
    }


    for (int i = 0; i < 16; i++){
        if (i < 1){
            hn1[i] = fn[i];
            hn2[i] = 0;
        }
        else if (i > 1 && i < 14){   
        hn1[i] = fn[i];
        hn2[i] = fn[i-2];
        }

        else{
            hn1[i] = 0;
            hn2[i] = fn[i-2];
        }
        h[i] = hn1[i] + hn2[i];         
    }

for(int i=0;i<21;i++){
    y[i] = 0;
}

for (int k=0;k<21;k++){
	for(int n=0;n<6;n++){
		if ((k-n >= 0) && (k-n < 16))
			y[k]+=x[n]*h[k-n];
    }
}


    

    
    int k = 12;
    double h[12];
    FILE *fp = fopen("hu.txt","w");

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
    