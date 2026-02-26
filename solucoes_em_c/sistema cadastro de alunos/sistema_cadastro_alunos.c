#include <stdio.h>
#include <stdlib.h>
#define APROVACAO 6

typedef struct{
    char nome[50];
    int matricula;
    double nota1, nota2, media;
} registro_aluno;

void cadastrar(registro_aluno aluno[], int *qtd){
    if(*qtd >= 100){
        printf("LIMITE MÁXIMO DE ALUNOS ATINGIDO!\n");
        return;
    }
    printf("Nome: ");
    scanf(" %49[^\n]", aluno[*qtd].nome);
    
    printf("ID da Matrícula (até 4 dígitos): ");
    scanf("%d", &aluno[*qtd].matricula);
    
    printf("Nota 1: ");
    scanf("%lf", &aluno[*qtd].nota1);

    printf("Nota 2: ");
    scanf("%lf", &aluno[*qtd].nota2);

    for(int i=0; i<*qtd; i++){
        if(aluno[*qtd].matricula == aluno[i].matricula){
            printf("MATRÍCULA JÁ CADASTRADA! VERIFIQUE OS DADOS E TENTE NOVAMENTE.\n");
            return;
        }
    }
    
    if(aluno[*qtd].nota1 > 10 || aluno[*qtd].nota1 < 0 || aluno[*qtd].nota2 > 10 || aluno[*qtd].nota2 < 0 || aluno[*qtd].matricula > 9999){
        printf("ERRO NO CADASTRO DO ALUNO! VERIFIQUE OS DADOS E TENTE NOVAMENTE.\n");
        return;
    }
    
    aluno[*qtd].media = (aluno[*qtd].nota1 + aluno[*qtd].nota2)/2;
    printf("\nCADASTRO EFETUADO COM SUCESSO!\n");
    (*qtd)++;
}

void listar(registro_aluno aluno[], int *qtd){
    if(*qtd == 0){
        printf("NENHUM ALUNO CADASTRADO!\n");
        return;
    }
    int i;
    for(i=0;i<*qtd;i++){
        printf("Nome: %s\n", aluno[i].nome);
        printf("Matrícula: %d\n", aluno[i].matricula);
        printf("Média: %.1lf\n", aluno[i].media);
        printf("----------------------\n");
    }
}

void buscar(registro_aluno aluno[], int *qtd){
    if(*qtd == 0){
        printf("NENHUM ALUNO CADASTRADO!\n");
        return;
    }
    int busca_matricula, controle = 0, i;
    printf("Digite o número da matrícula: ");
    scanf("%d", &busca_matricula);
    for(i=0;i<*qtd;i++){
        if(busca_matricula == aluno[i].matricula){
            printf("DADOS DO ALUNO:\n");
            printf("Nome: %s\n", aluno[i].nome);
            printf("Média: %.1lf\n", aluno[i].media);
            controle = 1;
        }
    }
    if(controle == 0){
        printf("ALUNO NÃO ENCONTRADO!\n");
    }
}

void mediageral(registro_aluno aluno[], int *qtd){
    if(*qtd == 0){
        printf("NENHUM ALUNO CADASTRADO!\n");
        return;
    }
    double medgeral=0;
    int i;
    for(i=0;i<*qtd;i++){
        medgeral += aluno[i].media; 
    }
    medgeral = medgeral/(*qtd);
    printf("Média geral da turma: %.1lf\n", medgeral);
}

void maiormedia (registro_aluno aluno[], int *qtd){
    if(*qtd == 0){
        printf("NENHUM ALUNO CADASTRADO!\n");
        return;
    }
    double maiormed = 0;
    int numaluno, i;
    for(i=0;i<*qtd;i++){
        if(aluno[i].media > maiormed){
            maiormed = aluno[i].media;
            numaluno = i;
        }
    }
    printf("DADOS DO ALUNO COM A MAIOR MÉDIA:\n");
    printf("Nome: %s\n", aluno[numaluno].nome);
    printf("Matrícula: %d\n", aluno[numaluno].matricula);
    printf("Média: %.1lf\n", aluno[numaluno].media);
}

void percentaprovacao(registro_aluno aluno[], int *qtd){
    if(*qtd == 0){
        printf("NENHUM ALUNO CADASTRADO!\n");
        return;
    }
    double percent;
    int aprovados = 0, i;
    for(i=0;i<*qtd;i++){
        if(aluno[i].media >= APROVACAO){
            aprovados++;
        }
    }
    percent = (aprovados*100.0)/(*qtd);
    printf("PERCENTUAL DE ALUNOS APROVADOS NA TURMA: %.1lf%%\n", percent);
}


int main(){
    registro_aluno aluno[100];
    int tecla, qtd=0;
    do{
        printf("----------------------------- SISTEMA DE CADASTRO DE ALUNO -----------------------------\n");
        printf("1 - Cadastrar aluno\n2 - Listar alunos\n3 - Buscar aluno por matrícula\n4 - Mostrar média da turma\n5 - Mostrar aluno com maior média\n6 - Mostrar percentual de aprovação\n0 - Sair\n\n");
        scanf("%d", &tecla);
        switch(tecla){
            case 1: cadastrar(aluno, &qtd); break;
            case 2: listar(aluno, &qtd); break;
            case 3: buscar(aluno, &qtd); break;
            case 4: mediageral(aluno, &qtd); break;
            case 5: maiormedia(aluno, &qtd); break;
            case 6: percentaprovacao(aluno, &qtd); break;
            case 0: printf("ENCERRANDO SISTEMA...\n"); break;
            default: printf("OPÇÃO INVÁLIDA!\n");
        }
    } while(tecla != 0);
    return 0;
}