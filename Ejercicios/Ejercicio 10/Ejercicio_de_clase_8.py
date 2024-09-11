#!/usr/bin/python3

import hashlib
import re
import os

class PasswordInvalido(Exception):
    pass

class Usuario:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hasheo(password)

    def hasheo(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def cambiar_password(self, new_password):
        if not self.validar_password(new_password):
            raise PasswordInvalido("La contraseña debe tener al menos 5 caracteres y contener tanto letras como números.")
        self.password = self.hasheo(new_password)
        return "Contraseña actualizada con éxito."

    def verificar_password(self, password):
        return self.hasheo(password) == self.password

    @staticmethod
    def validar_password(password):
        if len(password) < 5:
            return False
        if not re.search(r'[a-zA-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True

def leer_usuarios():
    usuarios = {}
    if os.path.exists('Usuarios.txt'):
        with open('Usuarios.txt', 'r') as file:
            for line in file:
                try:
                    name, email, hashed_password = line.strip().split(',')
                    usuarios[email] = (name, hashed_password)
                except ValueError:
                    print("Formato incorrecto en el archivo de usuarios.")
    return usuarios

def guardar_usuario(usuario):
    with open('Usuarios.txt', 'a') as file:
        file.write(f'{usuario.name},{usuario.email},{usuario.password}\n')

def iniciar_sesion():
    intentos = 0
    usuarios = leer_usuarios()

    while True:
        opcion = input('¿Qué deseas hacer?\n> Iniciar sesión [1]\n> Registrarse [2] \n> Terminar [3]\nIngresa el # de opción [1/2/3]: ')

        if opcion == '1':
            email = input('¿Cuál es tu correo?: ')
            password = input('¿Cuál es tu contraseña?: ')
            password = hashlib.sha256(password.encode()).hexdigest()

            if email in usuarios:
                name, hashed_password = usuarios[email]
                usuario = Usuario(name, email, hashed_password)
                if usuario.verificar_password(password):
                    print(f'¡Bienvenido de nuevo, {usuario.name}!')
                    break
                else:
                    intentos += 1
                    print(f'Contraseña incorrecta. Intento {intentos} de 5.')
                    if intentos >= 5:
                        print("Has fallado demasiados intentos. El programa terminará.")
                        break
            else:
                print("El correo electrónico no está registrado.")

        elif opcion == '2':
            name = input('Ingresa tu nombre: ')
            email = input('Ingresa tu correo: ')
            password = input('Ingresa una contraseña: ')

            try:
                if Usuario.validar_password(password):
                    usuario = Usuario(name, email, password)
                    guardar_usuario(usuario)
                    print("Usuario registrado con éxito.")
                else:
                    print("La contraseña no cumple con los requisitos.")
            except PasswordInvalido as e:
                print(e)

        elif opcion == '3':
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

if __name__ == "__main__":
    print('------------¡Bienvenido!------------')
    iniciar_sesion()
()

