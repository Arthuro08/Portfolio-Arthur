#include <stdio.h>
#include <stdlib.h>

int menor(int *p){
    int k, menor=p[0];
    for(k=0;k<6;k++){
        if(p[k]<menor){
            menor=p[k];
        }
    }
    return(menor);
}

int maior(int *q){
    int j, maior=q[6];
    for(j=0;j<6;j++){
        if(q[j]>maior){
            maior=q[j];
        }
    }
    return(maior);
}

int main() {
    int v[6], i;
    for(i=0;i<6;i++){
        scanf("%d", &v[i]);
    }
    printf("%d\n%d", menor(v), maior(v));
    
    
	return 0;
}