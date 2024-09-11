import re

# pattern = r'\d+'
# text = "Hay 12 hackers y 7 hackeados."
# result = re.search(pattern, text) # regresa un objeto Match
# if result:
#     print(result.group()) # Group devuelve la parte del texto que coincide con el patrón
#     print("Inicio:", result.start()) 
#     print("Fin:", result.end())  
#     print("Span:", result.span())   


# pattern = r'\d+'  
# text = "10 exploits"
# result = re.match(pattern, text)
# if result:
#     print(result.group())  

# pattern = r'\d+'  
# text = "Hay 2 vulnerabilidades y 1 hacker."
# result = re.findall(pattern, text)
# print(result)

# pattern = r'\d+' 
# text = "Hay 4 scripts y 3 están mal."
# new_text = re.sub(pattern, 'varios', text)
# print(new_text) 


# pattern = r'\s+' 
# text = "Hay varios espacios aquí."
# result = re.split(pattern, text)
# print(result)  


# pattern = r'\d{2,4}'  # Busca dígitos que tengan entre 2 y 4 cifras
# text = "Año 1995, año 2023, año 0."
# result = re.findall(pattern, text)
# print(result)  


# pattern = r'\bsol\b'
# text = "El sol de México"
# result = re.findall(pattern, text)
# print(result)  

# pattern = r'\bsol.*'
# text = "El sol de México"
# result = re.findall(pattern, text)
# print(result) 


# #Modificadores
# pattern = r'hackers'
# text = "Hay Hackers aquí."
# result = re.search(pattern, text, re.I)
# if result:
#     print("Encontrado") 


# pattern = r'\.com | hacker\w*'
# text = "Visita hackersfightclub.com para más información."
# result = re.findall(pattern, text)
# if result:
#     print(result)  # Salida: Encontrado



# pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
# text = "Erick Garcia y Bruno Ortiz son amigos"
# result = re.findall(pattern, text)
# print(result)  

# --------------- Grupos ----------------
# pattern = r'(\d{3})-(\d{2})-(\d{4})'
# text = "Número: 123-45-6789"
# result = re.findall(pattern, text)
# print(result) 

# pattern = r'(?:\d{3}-\d{2})-\d{4}'
# text = "Número: 123-45-6789"
# result = re.findall(pattern, text)
# print(result) 

