#!/usr/bin/python3

dicc = {}
tmp = dicc

num50 = [i for i in range(50)]
binarios = [bin(i) for i in range(50)]
hexa = [hex(i) for i in range(50)]

binarios1 = []
hexa1 = []

for i in range(50):
    if binarios[i].count('1') % 2 != 0:
        binarios1.append(binarios[i])
        hexa1.append(hexa[i])

dicc = {tuple(binarios1):hexa1}

print(f'{dicc}')

