#include <stdio.h>
#include <stdlib.h>
typedef struct{
        char nome[50];
        double motor, susp, turbo;
        double mediap;
    } tipo_carro;

int main()
{
    tipo_carro carro[100];
    int n,i;
    double mediap, mediaa=0, acum_mediaa=0;

    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf(" %50[^\n]", carro[i].nome);
        scanf("%lf%lf%lf", &carro[i].motor, &carro[i].susp, &carro[i].turbo);
        carro[i].mediap = ((carro[i].motor*5)+(carro[i].susp*2)+(carro[i].turbo*3))/10;
        acum_mediaa += carro[i].mediap;
    }
    mediaa= acum_mediaa/n;

    for(i=0;i<n;i++){
        if(carro[i].mediap >= mediaa){
            printf("%s\n", carro[i].nome);
        }
    }
    return 0;
}