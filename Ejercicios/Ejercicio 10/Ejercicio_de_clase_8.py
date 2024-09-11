#!/usr/bin/python3

import hashlib

class Usuario:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = self.hasheo(password)

  def hasheo(self, password):
    #self.password = hash(hs_password)
    #print(f'{self.password}')
    #return(f'{self.password}')
    return hashlib.sha256(password.encode()).hexdigest()

  def pswrd_check(self):
    ans = input(f'Tu contraseña actual es: {self.password}. ¿Desea cambiarla [y/n]?')
    
    if ans.lower() == 'y':
        new_password = input("Ingresa tu nueva contraseña (min 5 caract.): ")
        while(len(self.password) < 5):
            new_password = input("Tu nueva contraseña es demasiado corta (min 5 caract.): ")
        self.password = self.hasheo(new_password)
        return(f'Tu contraseña ha sido actualizada y ahora es: {self.password}')
    else:
        return(f'Tu contraseña actual sigue siendo: {self.password}')

def main():
    print(f'------------¡Bienvenido!------------\n\n')
    opcion = input(f'¿Qué deseas hacer?\n> Iniciar sesión [0]\n> Registrarse [1] \nIngresa el # de opción [0/1]: ')

    if opcion == '0':
        name = input('\n¿Cuál es tu nombre?: ')
        email = input('¿Cuál es tu correo?: ')
        password = input('¿Cuál es tu contraseña?: ')
        
        usuario = Usuario(name, email, password)
        usuario.pswrd_check(password)

    elif opcion == '1':
        #print(Usuario('Esteban', 'correo@gmail.com', '12345'))
        name = input(f'\nIngresa tu nombre: ')
        email = input(f'Ingresa tu correo: ')
        password = input(f'Ingresa una contraseña: ') 

        usuario = Usuario(name, email, password)
        usuario.pswrd_check()

        with open('Usuarios.txt', 'a') as file:
            file.write(f'{usuario.name},{usuario.email},{usuario.password}\n')

    if 'usuario' in locals():
        print(f"Tu contraseña actual es: {usuario.password}")
        

if __name__ == "__main__":
    main()
