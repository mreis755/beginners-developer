#!/usr/bin/python3

from os import system, name
from time import sleep

saldo = 900.0

# Função que limpa a tela de acordo com o sistema operacional
def clear():

    # Limpando a tela no Windows
    if name == 'nt':
        _ = system('cls')
    
    # Limpando a tela no Linux e Mac
    else:
        _ = system('clear')

def saque(val_saque):
    global saldo

    while val_saque > saldo:
        print("\nVALOR ACIMA DO SALDO")
        print("SAQUE BLOQUEADO")
        val_saque = float(input("\nQuanto deseja sacar? R$ "))

    while val_saque < 0:
        print("\nVALOR INVÁLIDO")
        print("SAQUE BLOQUEADO")
        val_saque = float(input("\nQuanto deseja sacar? R$ "))

    saldo -= val_saque
    print("SALDO: R$", saldo)

def deposito(val_deposito):
    global saldo

    while val_deposito < 0:
        print("\nVALOR INVÁLIDO")
        print("DEPÓSITO BLOQUEADO")
        val_deposito = float(input("\nQuanto deseja depositar? R$"))

    saldo += val_deposito
    print("SALDO: R$", saldo)


while True:

    clear()
    print("BANCO 4LINUX")

    print("\nSALDO: R$", saldo)
    print("\nQual operação deseja realizar?")

    print("\n[ 1 ] Saque")
    print("[ 2 ] Depósito")
    print("[ 3 ] Sair")

    op = int(input("\nSua escolha: "))

    match op:
        case 1:
            print("\nSALDO: R$", saldo)
            valor = float(input("Quanto deseja sacar? R$ "))

            saque(valor)
            sleep(1)

        case 2:
            print("\nSALDO: R$", saldo)
            valor = float(input("Quanto deseja depositar? R$ "))

            deposito(valor)
            sleep(1)
            
        case 3:
            break

        case _:
            print("ESCOLHA INVÁLIDA")
            sleep(1)
