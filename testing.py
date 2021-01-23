# import pymongo
# from pymongo import MongoClient
# from queue import Queue
# import pafy
# from moviepy.editor import *
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# import shutil
# import amino
# def instaciaMongo():
#     client = MongoClient()
#     db = client['amino_mongo_test']
#     users = db.users
# Cantidad de datos en la coleccion
# print(db.users.count_documents({}))
# # con db.user.find()[n] -> podemos acceder en forma de arreglo a la coleccion
# valor =db.users.find_one({"uid" : "bd7c7073-4f91-450c-acad-aaea22a87e43"})
#
# print(valor)
# valor['_id'] = 'cambiado'
# valor['flag'] = 'true'
# print(valor['_id'])
# print(valor)
# print(db.users.find_one({'uid': '123'}))
import random

# print(h)
# # print(h1["hola"])
# email = 'tasinim655@ahhtee.com'
# password = '123890'
# #CHAT COMUNIDAD TEST
# chatId = '7a984e59-004a-4fe5-8f82-206c95fff3cb'
#
# comId = '76917488'
# mongo = MongoClient()  # Mongo url, example: go to > mongodb.com > create collection > then ONLY get mongodb+srv://DETAILS/
# db = mongo['amino_mongo_test']
# db = db.testing
# client = amino.Client()
# client.login(email=email, password=password)
# sub = amino.SubClient(comId=comId, profile=client.profile)
# import json
# # db.insert({'usr':"hola"})
# user1 = sub.profile.json
# user1 = amino.objects.UserProfile(user1).UserProfile
#
#
# print(user1.userId)


# print(type(1) == int)
# for u in array:
#     if u['id'] == 1:
#         u['na'] = "Cambio"
#

# print(array)


# import amino
# email = 'tasinim655@ahhtee.com'
# password = '123890'
# # COMUNIDAD ANIME
# comId = '67'
#
#
# client = amino.Client()
# client.login(email=email, password=password)
#
# sub = amino.SubClient(comId=comId,profile=client.profile)
# for i in sub.get_chat_threads():
#     print(i)
# import unicodedata
#
# def strip_accents(s):
#     """
#     Sanitarize the given unicode string and remove all special/localized
#     characters from it.
#
#     Category "Mn" stands for Nonspacing_Mark
#     """
#     try:
#         return ''.join(
#             c for c in unicodedata.normalize('NFD', s)
#             if unicodedata.category(c) != 'Mn'
#         )
#     except:
#         return s
#
# print(strip_accents("Cañon"))


# h = {"id":1 ,"na":"hola"}
# h1 = {"id":2 ,"na":"hola2"}
# h2 = {"id":3 ,"na":"hola3"}
# h3 = {"id":4 ,"na":"hola4"}
#
# # array = [h,h1,h2,h3]
#
# # Muestra si "id" es atributo de h (diccionario)
# print("id" in h)



# convertir lowerCase un arreglo

# h = ["HOLA","COMO","ESTAS"]
# h = [world.lower() for world in h]
#
# print("yola".capitalize())

# mirar si pasa luego de un if a lo que sigue
# h = []
# def n2():
#
#     h.append(1)
#     if len(h) == 2:
#         print("ya hay 2!")
#
# n2()
# n2()

# mirar si podemos generar un arreglo apartir de otro
# h = {"id":1 ,"na":"hola"}
# h1 = {"id":2 ,"na":"hola2"}
# h2 = {"id":3 ,"na":"hola3"}
# h3 = {"id":4 ,"na":"hola4"}
# 
# array = [h,h1,h2,h3]
# 
# 
# array2 = [usr['na'] for usr in array]
# 
# print(array2)

# Prueba split con maxleght
# h = "habia una ves una vaca"
#
# h2 = h.split(" ", 1)
#
# print(h2)


# Importar Imagen de Url
# import sys
# import requests
# from PIL import Image
# 
# response = requests.get("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F151657441266-0-1%2Fs-l1000.jpg&f=1&nofb=1")
# image = open("games/hands.PNG",'wb')
# image.write(response.content)
# image.close()
# 
# img = Image.open("games/hands.PNG")
# img.show()


# Organizar arreglo
# h = {"id":1 ,"na":"hola1"}
# h1 = {"id":2 ,"na":"hola7"}
# h2 = {"id":3 ,"na":"hola8"}
# h3 = {"id":4 ,"na":"hola1"}
#
# array = [h,h1,h2,h3]
# print(array)
#
# arrayN = sorted(array,key= lambda k : k['na'])
# print(arrayN)

# lambda fuction

# example = lambda x: x+1
#
#
#
# print(example(2))
 
# Sacar y mostrar un valor del arreglo

# arr = [1,2,3,4,5,7,8]
# leter = arr.pop()
# print(leter)
# print(arr)

# Crear un string de un solo caracter multiples veces
#
# arr = ["hola","mundo"]
# arr2 = ["_"*len(word) for word in arr]

# imprimir o guardar un arreglo como string
# print(" ".join(arr2))

# Contar cuantas veces se repite algo en un arreglo
# from collections import Counter
#
# h = "hola"
# h1 = Counter(h)['x']
# print(h1)


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




# Copiar un arreglo

# referencia (si cambiamos una cosa del uno tambien del otro)
# arr = ["a","b","c","d"]
# print(arr)
# sin referencia

# arr2 = arr.copy()
#
# arr2[1] = "cambio"
#
# print(arr2)
# print(arr)


# Jugando con arreglos
# randomWord = "hola como"
# randomWord2 = "hola como".split(" ")
#
# chart = "o"
# randomWordE = randomWord.split(" ")
# print(randomWordE)
# randomWordE = ["_"*(len(word)) for word in randomWordE]
# """
#            DEPRECATE (CAMBIADO PORQUE TIENE MUCHO TIMEOUT
#            En este ejemplo lo que buscamos es cambiar un elemento de un arreglo,
#            pero para esto tenemos que acceder a la posicion del elemento en el arreglo
#            no podemos solo cambiarlo con la referencia en el for porque no nos hace el cambio.
#            aparte aqui como estamos trabajando con un string y queremos cambiar un char pasa lo mismo que con el arreglo
#            entonces para poder cambiarlo lo que hacemos es cambiar el string a list y luego acceder a la posicion que queremos cambiar.
#            Ya teniendo esto lo que hacemos es lo mismo que con el arreglo accedemos a la posicion y luego la cambiamos.
#
#            Como lo volvimos una list ahora para pasarlo a str otra ves lo que hacemos es usar el .join()
#
#
#            METHOD TO FAST:
#            Este metodo es casi parecido al anterior sino que usamos el slice para este lo que hacemos es coger directamente el string sin tener que pasarlo
#            por list sino que sencillamente cortamos el string en la parte donde tenemos que cambiar el char y colocamos el nuevo char
#            y luego lo pasamos a la lista directamente
#
#            randowWordS = randowWordS[:i]+ chart+ randowWordS[i+1:] -> modificar la palabra dentro del arreglo para que guarde los cambios mientras sigue iterando
#            randomWordE[j]= randowWordS[:i]+ chart+ randowWordS[i+1:]
#
#            """
# for j,randowWordS in enumerate(randomWord2,start=0):
#     for i,char in enumerate(randowWordS,start=0):
#         if char == chart:
#             wordT = list(randomWordE[j])
#             wordT[i] = chart
#             randomWordE[j] = wordT
#
#
# print("  ".join([" ".join(word4) for word4 in randomWordE]))
#
#
# text = 'abcdefg'

# Coge el string y elimina los primeros caracteres segun le digamos
# text = text[2:]
# print(text)
# text = 'abcdefg'

# inicial el string desde el inicio hasta la cantidad de caractes que digamos
# text = text[:2]
# print(text)
#
# txt = "Hola Ramon"
# txt = txt[:1]+"O"+ txt[2:]
# txt2 = "_ _ _ _"
# txt2 = txt2[:0]+"H"+txt2[1:]
# print(txt2)
#


# cambiar las posiciones del arreglo

# arr = [1,6,7,9]
# random.shuffle(arr)
#
# print(arr)


# random = "".join([str(random.randint(0, 9)) for i in range(4)])
# random = [1,2,3,4]
# random2 = ["1","2","3","4"]
# random2 ="".join(random2)


# print(random)


# jugando con un api
# import requests
# 
# # Crear objeto api
# num = str(random.randint(0,1000000000))
# print(num)
# 
# response = requests.get(f'https://source.unsplash.com/collection/{num}')
# # print(response.content)
# # Importar Imagen de Url
# import sys
# import requests
# from PIL import Image
# #
# # response = requests.get("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F151657441266-0-1%2Fs-l1000.jpg&f=1&nofb=1")
# image = open("games/hands.PNG",'wb')
# image.write(response.content)
# image.close()


# pegando arrays

arr = [1,2,3]
arr2 = [2,3,4]
arr = arr+arr2

print(arr)

