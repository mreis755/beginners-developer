#!/usr/bin/python3

def imc(a, b):
    resultado = a / (b * b)
    if resultado <= 18.5:
        classificacao = "Classificação IMC: Baixo peso"

    elif resultado <= 24.9:
        classificacao = "Classificação IMC: Peso ideal"
    
    elif resultado <= 29.9:
        classificacao = "Classificação IMC: Sobrepeso"
    
    elif resultado <= 34.9:
        classificacao = "Classificação IMC: Obesidade 1°"
    
    elif resultado <= 39.9:
        classificacao = "Classificação IMC: Obesidade 2°"
    
    elif resultado >= 40:
        classificacao = "Classificação IMC: Obesidade grave"

    return classificacao

peso = 98
altura = 1.85

print(imc(peso, altura))
