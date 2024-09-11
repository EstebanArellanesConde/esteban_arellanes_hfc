#!/usr/bin/python3


class Usuario:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def hasheo(self, hs_password):
    self.password = hash(hs_password)
    #print(f'{self.password}')
    return(f'{self.password}')

  def pswrd_check(self, password):
    ans = input(f'Tu contraseña actual es: {hash(str(self.password))}. ¿Desea cambiarla [y/n]?')
    
    if ans == 'y':
        while(len(self.password)<5):
            self.password = input("Ingresa tu nueva contraseña (min 5 caract.): ")
        return(f'Tu contraseña actual es: {hash(str(self.password))}')
    else:
        return(f'Tu contraseña actual es: {hash(str(self.password))}')

def main():
    print(f'------------¡Bienvenido!------------\n\n')
    opcion = input(f'¿Qué deseas hacer?\n> Iniciar sesión [0]\n> Registrarse [1] \nIngresa el # de opción [0/1]: ')

    if opcion == 0 or '0':
        name = input('\n¿Cuál es tu nombre?: ')
        email = input('¿Cuál es tu correo?: ')
        password = input('¿Cuál es tu contraseña?: ')
        
        #if name 

    elif opcion == 1 or '1':
        #print(Usuario('Esteban', 'correo@gmail.com', '12345'))
        name = input(f'\nIngresa tu nombre: ')
        email = input(f'Ingresa tu correo: ')
        password = input(f'Ingresa una contraseña: ') 
        hs_passwrd = str(hash(password))
        print(f'Tu contraseña actual es: {hs_passwrd}')
        
        usuario = Usuario(name, email, password)
        usuario.pswrd_check(password)
        print(f"Tu contraseña actual es: {hash(str(self.password))}")
        

if __name__ == "__main__":
    main()
