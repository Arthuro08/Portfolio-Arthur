#include <stdio.h>
#include <stdlib.h>

int main(){
    int x,y,z;
    scanf("%d %d %d", &x, &y, &z);
    if((x>28 && y==2) || (x>31) || (y>12) || (y<1) || (z<0) || (x<1)){
        printf("Invalid\n");
    } else if(x>30 && (y==4 || y==6 || y==9 || y==11)){
        printf("Invalid\n");
    }
    else{
        x = x+1;
        if (x>31 || (x==29 && y==2)) {
            x = 1;
            y = y+1;
        } 
        if (y>12) {
            y = 1;
            z = z+1;
        }
        printf("%d.%d.%d\n", x, y, z);
    }
    
    return 0;
}