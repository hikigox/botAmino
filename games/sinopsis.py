from pymongo import MongoClient
import tools
from initial import puntuacion,pool
db = MongoClient()
db = db['amino_mongo_test']
db = db.sinopsis
answer = ""
repeat = []
def randomSig(sub,chatId):
    global answer
    dbA = db.find()
    quest = tools.randomSelection(dbA,db.count_documents({}) - 1)
    answer = quest["respuesta"]
    try:
        sub.send_message(chatId=chatId,message= f"Sinopsis:\n{quest['sinopsis']}",messageType=115)
    except: pass



def responseS(sub,chatId,message):
    global answer
    if tools.searchArray(answer,message.content) is True:
        sub.send_message(chatId=chatId,message=f"El Participante:\n[CB]{message.author.nickname}\nAdivino la sinopsis, gana 5 puntos")
        puntuacion.changePuntuation(5,message.author.userId)
        answer = ""

def finalS(sub,chatId):

    pool.pool.clear()
    sub.send_message(chatId=chatId,message ="Se termino el juego de las sinopsis")

