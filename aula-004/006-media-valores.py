#!/usr/bin/python3

lista = []
soma = 0
media = 0

for i in range(0, 5):
    lista.append(int(input("Digite um valor: ")))

for i in lista:
    soma += i

media = soma / len(lista)

print("A média dos valores é", media)
