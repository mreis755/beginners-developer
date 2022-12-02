#!/usr/bin/python3

primeiro = None
segundo = None

def somar(a, b):
    global primeiro, segundo
    print(a)
    print(b)
    print(a + b)

primeiro = 10
segundo = 5
somar(primeiro, segundo)
