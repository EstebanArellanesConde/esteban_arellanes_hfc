#!/usr/bin/python3

import requests

pag = 'https://jsonplaceholder.typicode.com/posts/1'
pag_post = 'https://jsonplaceholder.typicode.com/posts/'
auth_data = {'titulo': 'titulo', 'cuerpo': 'cuerpo'}
usuario = {'userID': 1, 'id': 1, 'title':'POST REQUEST'}
r_usuario = {'email': "correo@gmail.com", 'password': "12345"}

peticion = requests.get(pag, params=auth_data)
print(peticion)

pJSON = peticion.json()
print(pJSON)

respuesta = requests.post(pag_post, json=auth_data)
rJSON = respuesta.json()
print(rJSON)


respuesta2 = requests.post(pag_post, json=usuario)
rJSON2 = respuesta2.json()
print(respuesta2)

new_user = requests.post('https://reqres.in/api/register', json=r_usuario)
nu = new_user.json()
print(nu)
