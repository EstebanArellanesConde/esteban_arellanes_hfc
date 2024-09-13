#!/usr/bin/python3
import re

file = open('57FD6325.VBN','rb')
binario = file.read()
print(type(binario))
#print(binario)
#byte = file

#xor_data = bytes(byte ^ xor_value for byte in binario)

file.close()
cadena = ''

for i in range(255):
    xor_value = i  
    xor_data = bytes(byte ^ xor_value for byte in binario)
    cadena = b'This program' in xor_data

    if cadena:
        with open('Archivo_tmp', 'wb') as tmp:
            tmp.write(xor_data)
        
for i in range(cadena):
    xor_value = i 
    xor_data = bytes(byte ^ xor_value for byte in binario)    

    with open('Archivo_tmp', 'rb') as tmp1:
        cadena = re.search('4d 5a', tmp1)
        file = open('NOHEAD','wb')
        file.write(cadena)
        file.close()

print(type(xor_data))
print(cadena)

#file.close()

