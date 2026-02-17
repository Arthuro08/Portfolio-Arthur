#include <stdio.h>
#include <math.h>

double calc(double x1, char operador, double x2){
    switch(operador){
        case '+': return x1 + x2;
        case '-': return x1 - x2;
        case '*': return x1 * x2;
        case '/': return x1 / x2;
        case 'e': return pow(x1, x2);
        case 'r': return sqrt(x1);
        default: return 0;
    }
}

int main(){
    double x1, x2, result;
    char operador;
    printf("Digite a operação desejada:\n1. '+' para adição;\n2. '-' para subtração;\n3. '*' para multiplicação;\n4. '/' para divisão;\n5. 'e' para exponenciação;\n6. 'r' para radiciação.\n");
    printf("________________________________________________________________\nDigite a entrada: ");
    scanf("%lf %c %lf", &x1, &operador, &x2);
    if(operador!='+' && operador!='-' && operador!='*' && operador!='/' && operador!='e' && operador!='r'){
        printf("Operador inválido!\n");
    } else{
        if(operador=='r'){
        result = calc(x1,operador,0);
        } else{
        result = calc(x1,operador,x2);
        }
        printf("Resultado: %.2lf", result);
    }
    
    return 0;
}