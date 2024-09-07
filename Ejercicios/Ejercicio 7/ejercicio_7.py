#!/usr/bin/python3

pares50 = [i for i in range(50) if i%2==0]
impares50 = [i for i in range(50) if i%2!=0]
cuad10 = [i**2 for i in range(10)]

print(list(map(lambda i: i+1, cuad10)))
