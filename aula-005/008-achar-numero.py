#!/usr/bin/python

from os import system, name
import math

num_escolhido = None
chute = None
num_qtd = None

x = None
numero = None

# Função que limpa a tela de acordo com o sistema operacional
def clear():

    # Limpando a tela no Windows
    if name == 'nt':
        system('cls')

    # Limpando a tela no Linux e Mac
    else:
        system('clear')

def acharNumero(numero):
    global num_escolhido, chute, num_qtd, x

    num_qtd = round(num_qtd / 2)
    chute = num_qtd

    while chute != numero:

        num_qtd = round(num_qtd / 2)
        print(str("\nChute: ") + str(chute))

        if chute < numero:
            print("Chute é menor que o número escolhido.")
            chute += num_qtd

        else:
            print("Chute é maior que o número escolhido.")
            chute -= num_qtd

    return chute

num_qtd = 100
num_escolhido = 28

clear()

print(str("\nO número escolhido foi: ") + str(acharNumero(num_escolhido)))
