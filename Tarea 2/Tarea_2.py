#!/usr/bin/python3

import time

def generar_numero_aleatorio(minimo, maximo):
    tiempo_actual = int((time.time() * 1000) % 1000)
    return minimo + (tiempo_actual % (maximo - minimo + 1))

def adivina_el_numero():
    minimo = 1
    maximo = 100

    numero_aleatorio = generar_numero_aleatorio(minimo, maximo)
    
    print(f"¡Adivina el número entre {minimo} y {maximo}!")

    while True:
        intento = input("Ingresa tu adivinanza (o 'salir' para terminar): ")
        
        if intento.lower() == 'salir':
            print("¡Juego terminado! El número era", numero_aleatorio)
            break
        
        try:
            intento = int(intento)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if intento < minimo or intento > maximo:
            print(f"Por favor, ingresa un número entre {minimo} y {maximo}.")
        elif intento < numero_aleatorio:
            print("El número es mayor. Intenta nuevamente.")
        elif intento > numero_aleatorio:
            print("El número es menor. Intenta nuevamente.")
        else:
            print("¡Felicidades! ¡Has adivinado el número!")
            break

adivina_el_numero()

