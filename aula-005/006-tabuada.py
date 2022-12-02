#!/usr/bin/python3

def tabuada(x):
        for i in range(1, 11):
        print(x, "X", i, "=", x * i)

numero = int(input("Digite um número: "))

print("\nApresentando a tabuada do número digitado:")
tabuada(numero)
