#Israel Villanueva Garcia

print((lambda x, y, z: x * y * z)(2, 2, 2)) # multiplica tres numeros

mi_lista = []

print((lambda x: len(x) == 0 )(mi_lista)) #valida si una lista es vacia.

mi_lista2 = [1,2]

print((lambda x, n: len(x) >= n)(mi_lista2, 3)) #valida si una lista tiene al menos n elemnetos

print((lambda x: x * x)(5)) #cuadrado de un numero

c1 = {1, 2, 3, 4, 5, 6}
c2 = {2, 4, 6, 8, 10}

print((lambda x, y: x & y)(c1, c2)) #interseccion de dos conjuntos