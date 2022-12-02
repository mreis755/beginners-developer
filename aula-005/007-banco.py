#!/usr/bin/python3

import os

saldo = 900.0

def saque(a):
    global saldo
    saldo -= a
    print("SALDO: R$", saldo)

def deposito(b):
    global saldo
    saldo += b
    print("SALDO: R$", saldo)

os.system('clear')

while True:

    print("BANCO 4LINUX")
    print("\nQual operação deseja realizar?")

    print("\n[ 1 ] Saque")
    print("[ 2 ] Depósito")
    print("[ 3 ] Sair")

    op = int(input("\nSua escolha: "))

    match op:
        case 1:
            print("SALDO: R$", saldo)
            valor = float(input("Quanto deseja sacar? R$ "))

            while a > saldo:
                print("VALOR ACIMA DO SALDO")
                print("SAQUE BLOQUEADO")

            saque(valor)
            os.system('clear')

        case 2:
            print("SALDO: R$", saldo)
            valor = float(input("Quanto deseja depositar? R$ "))

            deposito(valor)
            os.system('clear')
            
        case 3:
            break
