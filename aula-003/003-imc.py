#!/usr/bin/python3

peso = None
altura = None
imc = None

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em m): "))

imc = peso / (altura * altura)

print("Seu IMC é", imc)

if imc < 18.5:
    print("Baixo peso")

if imc > 18.5 and imc < 24.9:
    print("Peso ideal")
    
if imc > 25 and imc < 29.9:
    print("Sobrepeso")

if imc > 30 and imc < 34.9:
    print("Obesidade 1°")

if imc > 35 and imc < 39.9:
    print("Obesidade 2°")

if imc >= 40:
    print("Obesidade grave")
