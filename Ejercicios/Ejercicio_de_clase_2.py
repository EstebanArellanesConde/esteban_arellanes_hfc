#!/usr/bin/python3

palindromo = list(input())
print(f'',palindromo)


if len(palindromo) != 0:
    for i in range(len(palindromo)):
        if palindromo[i] == palindromo[len(palindromo)-i-1]:
            print(f'La palabra es un palindromo')
        else:
            print(f'La palabra no es un palindromo')


     
