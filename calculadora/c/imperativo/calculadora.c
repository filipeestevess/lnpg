#include "stdio.h"
#include "menu.h"
#include "funcionalidades.h"

int main(){

    int escolha=0;
    float num1;
    float num2;

    while(escolha != 5){

        imprimeMenu();
        printf("Qual a operacao desejada? ");
        scanf("%d", &escolha);

        if(escolha == 1){
            printf("\n\nDigite o primeiro número: ");
            scanf("%f", &num1);

            printf("Digite o segundo número: ");
            scanf("%f", &num2);
            printf("\n");

            printf("Resultado: %.1f\n", soma(num1, num2));
            printf("-------------------------------------\n\n");
        }

        else if(escolha == 2){
            printf("Digite o primeiro número: ");
            scanf("%f", &num1);
            printf("\n");

            printf("Digite o segundo número: ");
            scanf("%f", &num2);
            printf("\n");

            printf("Resultado: %.1f\n", subtracao(num1, num2));
            printf("-------------------------------------\n\n");
        }

        else if(escolha == 3){
            printf("Digite o primeiro número: ");
            scanf("%f", &num1);
            printf("\n");

            printf("Digite o segundo número: ");
            scanf("%f", &num2);
            printf("\n");

            printf("Resultado: %.1f\n", multiplicacao(num1, num2));
            printf("-------------------------------------\n\n");
        }

        else if(escolha == 4){
            printf("Digite o primeiro número: ");
            scanf("%f", &num1);
            printf("\n");

            printf("Digite o segundo número: ");
            scanf("%f", &num2);
            printf("\n");

            printf("Resultado: %.1f\n", divisao(num1, num2));
            printf("-------------------------------------\n\n");
        }

        else if(escolha < 1 || escolha > 5){
            printf("Digite um numero válido.\n");
            printf("-------------------------------------\n\n");
        }

    }

    return 0;
}