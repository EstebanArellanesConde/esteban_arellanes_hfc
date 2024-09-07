#!/usr/bin/python3
#HACKERS_FIGHT_CLUB

import statistics
from random import choice


calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
    'Angel Sánchez',
    'Esteban Arellanes',
    'Danna Márquez',
    'Fernando Romero',
    'Alberto Medel',
    'Luis Lira',
    'Obed Torres',
    'Oscar Caballero',
    'Oscar Ríos',
    'Stephany Marín',
    'Jonathan Valencia',
    'Valeria Ramírez',
    'Israel Villanueva',
    'Juan Legorreta']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno[alumno]:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))

def aprob_reprob():
    for alumno in range(calificacion_alumno[alumno]):
        if int(calificacion_alumno.keys()) > 5:
            print('Alumno Aprobado')
        else: 
            print('Alumno Reprobado')


#asigna_calificaciones()
#imprime_calificaciones()

print(calificacion_alumno)
