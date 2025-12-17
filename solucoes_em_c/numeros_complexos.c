#include <stdio.h>
#include <stdlib.h>

typedef struct{
        int a, b;
    } complexo;

int main()
{
    complexo num[2];
    int i, sA, sB, mA, mB;
    for(int i = 0; i < 2; i++){
        scanf("%d%d", &num[i].a, &num[i].b);
    }
    sA = num[0].a + num[1].a;
    sB = num[0].b + num[1].b;
    mA = num[0].a * num[1].a - num[0].b * num[1].b;
    mB = num[0].a * num[1].b + num[1].a * num[0].b;
    printf("Soma: %d+%di\n", sA, sB);
    printf("Multi: %d+%di\n", mA, mB);
    return 0;
}
