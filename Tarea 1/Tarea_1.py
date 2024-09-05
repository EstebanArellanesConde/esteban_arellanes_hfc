#!/usr/bin/python3

import random
import string

def password(num_minus, num_mayus, num_digitos, num_especiales):
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    digitos = string.digits
    especiales = string.punctuation
    
    if (num_minus < 0 or num_mayus < 0 or num_digitos < 0 or num_especiales < 0):
        raise ValueError("ERROR: ¡La cantidad de caracteres no puede ser negativa!")
    
    psswrd_minus = [random.choice(minusculas) for _ in range(num_minus)]
    psswrd_mayus = [random.choice(mayusculas) for _ in range(num_mayus)]
    psswrd_digitos = [random.choice(digitos) for _ in range(num_digitos)]
    psswrd_especiales = [random.choice(especiales) for _ in range(num_especiales)]
    
    password_list = (psswrd_minus + psswrd_mayus + psswrd_digitos + psswrd_especiales)
    
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

num_minus = int(input("Ingrese el número de letras minúsculas: "))
num_mayus = int(input("Ingrese el número de letras mayúsculas: "))
num_digitos = int(input("Ingrese el número de dígitos: "))
num_especiales = int(input("Ingrese el número de caracteres especiales: "))

password = password(num_minus, num_mayus, num_digitos, num_especiales)
print(f"\nLa contraseña generada es: {password}")

