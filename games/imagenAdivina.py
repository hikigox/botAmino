from pymongo import MongoClient
import requests
import tools

from initial import puntuacion,pool
db = MongoClient()
db = db['amino_mongo_test']
db = db.personajes
response =""
def imageRandom(sub,chatId):
    global response
    url = tools.randomSelection(db.find(),db.count_documents({}) - 1)
    response = url['respuesta']
    sub.send_message(chatId=chatId,message="[CB]Quien es este personaje ?")
    request = requests.get(url['url'])
    img = open("personaje.png",'wb')
    img.write(request.content)
    img.close()

    with open("personaje.png",'rb') as file:
        sub.send_message(chatId=chatId, file=file, fileType='image')


def responseImage(sub,chatId,message):
    global response
    if tools.searchArray(response,message.content) is True:
        sub.send_message(chatId= chatId,message=f"[CB]Correcto !\n[C]El jugador {message.author.nickname} gana 5 puntos")
        response = ""
        puntuacion.changePuntuation(5,message.author.userId)


def closeImage(sub,chatId):
    global response
    pool.pool.clear()
    response = ""
    sub.send_message(chatId=chatId, message="Se termino el juego de adivina el personaje")

