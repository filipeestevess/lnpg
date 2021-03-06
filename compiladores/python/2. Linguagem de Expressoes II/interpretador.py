import sys
import re
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from simbolos import tabela, adicionar, ler, remover
from ast import *

#code = 'A = 10; B = A + 2; imprimir(A); imprimir(B);'
code = 'A = [1, 3, 5]; imprimir(A); tamanho(A); remover(A, 1); imprimir(A); tamanho(A);'
tokens = analise_lexica(code, tokens_da_linguagem)

print('\n\n\n')

print(tokens)

print('\n\n\n')

programa = analise_sintatica(tokens)
print (programa)

print('\n\n\n')

for construcao in programa:
    if construcao[1] == 'AtrSimples':
        inicio = int(construcao[0].split('-')[0])
        atrSimples = AtrSimples(tokens[inicio][0], tokens[inicio + 2][0])
        atrSimples.interpretar()
    if construcao[1] == 'Atr':
        inicio = int(construcao[0].split('-')[0])
        atr = Atr(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 3][0]
        )
        atr.interpretar()
    if construcao[1] == 'Lista':
        inicio = int(construcao[0].split('-')[0])
        idlista = tokens[inicio][0]
        #elementos = []
        elemento1 = tokens[inicio + 3][0]
        elemento2 = tokens[inicio + 5][0]            

        lista = Lista(idlista, elemento1, elemento2)
        lista.interpretar()
    if construcao[1] == 'Listade3':
        contador = 0
        inicio = int(construcao[0].split('-')[0])
        idlista = tokens[inicio][0]
        #elementos = []
        elemento1 = tokens[inicio + 3][0]
        elemento2 = tokens[inicio + 5][0]
        elemento3 = tokens[inicio + 7][0]   

        lista = Listade3(idlista, elemento1, elemento2, elemento3)
        lista.interpretar()
    if construcao[1] == 'Remover':
        inicio = int(construcao[0].split('-')[0])
        remover = Remover(tokens[inicio + 2][0], tokens[inicio + 4][0])
        remover.interpretar()
    if construcao[1] == 'Tamanho':
        inicio = int(construcao[0].split('-')[0])
        lista = TamanhoLista(tokens[inicio + 2][0])
        lista.interpretar()
    if construcao[1] == 'Imprimir':
        inicio = int(construcao[0].split('-')[0])
        imprimir = Imprimir(
            tokens[inicio + 2][0]
        )
        imprimir.interpretar()

