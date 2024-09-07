#!/bin/bash

import numpy as np
import pandas as pd
import math

mult3 = lambda x, y, z: x*y*z
lista_vacia = lambda lista: (len(lista) == 0) ? print(f'La lista está vacía') : print(f'La lista no está vacía')
lista_n_el = lambda lista, n: (len(lista) == n) ? print(f'La lista tiene n elementos') : print(f'La lista está vacía')
sqr_root = lambda x: math.sqrt(x)
set_in = lambda conj1, conj2: conj1 in conj2

print(mult3(3,4,5))
print(lista_vacia(lista = ['a','b','c','d']))
print()
print(lista_vacia(lista = ['a','b','c','d']))
print(sqr_root(9))
print(set_in([2,3,4,5,6],[1,2,3,4,5,6]))
