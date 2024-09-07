#!/usr/bin/python3
# HACKERS_FIGHT_CLUB

import numpy as np
from random import choice

calificacion_alumno = {}
calificaciones = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
becarios = [
    "Angel Sánchez",
    "Esteban Arellanes",
    "Danna Márquez",
    "Fernando Romero",
    "Alberto Medel",
    "Luis Lira",
    "Obed Torres",
    "Oscar Caballero",
    "Oscar Ríos",
    "Stephany Marín",
    "Jonathan Valencia",
    "Valeria Ramírez",
    "Israel Villanueva",
    "Juan Legorreta",
]


def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)


def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print("%s tiene %s\n" % (alumno, calificacion_alumno[alumno]))


def status_alumni():
    def build_on_comp(comp):
        tup = ()
        for a in becarios:
            if comp(calificacion_alumno[a]):
                tup = tup + (a,)

        return tup

    return build_on_comp(lambda x: x >= 7), build_on_comp(lambda x: x < 7)


def promedio():
    return sum([c for c in calificacion_alumno.values()]) / len(calificacion_alumno)


def to_set():
    return set(calificacion_alumno.values())


asigna_calificaciones()
imprime_calificaciones()

a, r = status_alumni()
print(f"Aprobados: {a}")
print(f"Reprobados: {r}")

print(f"Promedio clificaciones: {promedio()}")

print(f"Set de calificaciones: {to_set()}")
