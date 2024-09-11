#!/usr/bin/python3

import hashlib

def hasheo(password):
    return hashlib.sha256(password.encode()).hexdigest()

def leer_usuarios(filename):
    usuarios = {}
    with open(filename, 'r') as file:
        for line in file:
            try:
                name, email, hashed_password = line.strip().split(',')
                usuarios[email] = (name, hashed_password)
            except ValueError:
                print("Formato incorrecto en el archivo de usuarios.")
    return usuarios

def escribir_resultados(filename, resultados):
    with open(filename, 'w') as file:
        for email, (name, password) in resultados.items():
            file.write(f'{name},{email},{password}\n')

def ataque_fuerza_bruta(usuarios):
    # Ejemplo de conjunto de contraseñas comunes (Se debe de ampliar esto para un ataque real)
    contrasenas_comunes = ['12345', 'password', '123456', '123456789', 'qwerty', 'abc123', 'password1', '12345678', 'qwerty123']

    resultados = {}
    
    for email, (name, hashed_password) in usuarios.items():
        for password in contrasenas_comunes:
            if hasheo(password) == hashed_password:
                resultados[email] = (name, password)
                break  # Si se encuentra la contraseña, no es necesario seguir probando

    return resultados

def main():
    usuarios = leer_usuarios('Usuarios.txt')
    resultados = ataque_fuerza_bruta(usuarios)
    escribir_resultados('Resultados_Fuerza_Bruta.txt', resultados)
    print(f'Los resultados se han guardado en "Resultados_Fuerza_Bruta.txt".')

if __name__ == "__main__":
    main()

