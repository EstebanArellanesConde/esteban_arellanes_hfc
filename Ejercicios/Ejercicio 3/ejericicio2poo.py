#!/usr/bin/python
#HACKERS_FIGHT_CLUB
from poo1 import Alumno
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

asigna_calificaciones()

def lista_alum():
    alumnos_list=[]
    for alumno in calificacion_alumno:
        alum = Alumno(alumno,calificacion_alumno[alumno])
        alumnos_list.append(str(alum))
    print(alumnos_list)

lista_alum()