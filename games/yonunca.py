from pymongo import MongoClient
import tools
from initial import  pool,puntuacion


db =MongoClient()
db = db['amino_mongo_test']
qdb = db.yonunca
repeat = []



def initialYonunca(sub,chatId,points = 10):
    global pool
    for user in pool.pool:
        user['puntos'] = points

    sub.send_message(chatId=chatId,message= f"[BC] Empezo el juego de yo nunca\n[C]Cada jugador iniciara con {points} puntos")


def responseQuest(userId):
    for usr in pool.pool:
        if usr["userId"] == userId:
            puntuacion.changePuntuation(-1,userId)
            break


def showPoints(sub,chatId):
    pointsUsers = []
    for usr in pool.pool:
        pointsUsers.append(usr["puntos"])
    listUser= tools.forStringPropeties(pool.pool,typeLetter="[C]",points=pointsUsers,atribute="nickname")
    sub.send_message(chatId=chatId,message= f"[CB]Puntuacion:\n{listUser}")

def showQuest(sub,chatId):
    global repeat
    quests = qdb.find()
    question = tools.randomSelection(quests,qdb.count_documents({}) - 1)
    if tools.searchArray(repeat,question['pregunta']) is not True:
        repeat.append(question['pregunta'])
        sub.send_message(chatId=chatId,message=f"Yo nunca nunca:\n[BC]{question['pregunta']}")
    else:
        showQuest(sub,chatId)


def closeYonunca(sub,chatId):
    repeat.clear()
    pool.pool.clear()
    sub.send_message(chatId=chatId,message="Termino el Yo nunca")



