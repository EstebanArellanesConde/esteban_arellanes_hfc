#Escribir una funcion lambda que multiplique 3 numeros 
tres = (lambda x, y ,z : x* y* z)
vacia = (lambda a : len(a)==0 )
n_elem = lambda b , c : len(b) >= c
raiz = lambda d : d ** (1/2)
inter = lambda e , f: e.intersection(f)

print(tres(1,2,3))
print(vacia([1,2]))
print(n_elem([1,2,3,4],3))
print(raiz(9))
print(inter({1,2,3,4},{2,4,6}))