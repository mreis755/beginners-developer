#!/usr/bin/python3

a = None

# Primeira maneira de apresentar números ímpares de 0 a 10

for a in range(0, 10):
    if a % 2 != 0:
        print(a)

print("")

# Segunda maneira de apresentar números ímpares de 0 a 10

for a in range(1, 10, 2):
    print(a)
