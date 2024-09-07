print((lambda x, y, z: x*y*z)(2, 3, 5)), 
print((lambda x: x==[])(x=[1, 2, 3]))
print((lambda x, n: len(x)>=n)([1, 2, 3], 4))
print((lambda x: x**(0.5))(64))
print((lambda x, y: x.intersection(y)) ({1, 2, 3},{3, 4, 5}))