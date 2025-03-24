
#trae funciones que vienen en el lenguaje python pero que estan fuera de mi file
import string
import random

print("Comenzar")

#creo una lista de caracteres posibles para mi password
chars = ["a","b","c"]
#con python y sus librerias
#chars = string.ascii_letters + string.digits + string.punctuation
password = ""
length = 10

for _ in range(length):
    password = password + random.choice(chars)

print("contrseña generada: " + password)    
