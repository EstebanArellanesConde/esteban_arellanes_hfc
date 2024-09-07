#Crea una función lambda que multiplique 3 números
print((lambda x, y, z: x * y * z)(10, 2, 4))

#Validar si una lista está vacía
print((lambda x: True if len(x) == 0 else False ) ([]))

#Validar si una lista tiene al menos 'n elementos'
print((lambda x, y: True if len(x) >= y else False ) ([],1))

#Calcular la raíz cuadrada de un número
print((lambda x: x**1/2)(10))

#Obtener la intersección de dos conjuntos
print((lambda x, y: x.intersection(y))({1,2,3},{2}))