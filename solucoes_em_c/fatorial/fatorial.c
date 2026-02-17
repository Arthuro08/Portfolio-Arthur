#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int x,n,fat;
    while(scanf("%d", &n) && n!=-1){
        fat=1;
        for(x=2;x<=n ;x++){
            fat=fat*x;
        }
        printf("%d\n", fat);
    }
    
	return 0;
}