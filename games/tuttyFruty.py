from builtins import str
from collections import Counter
from pymongo import MongoClient
import tools
import time
from initial import pool, puntuacion

db = MongoClient()
db = db['amino_mongo_test']
worlds = db.tutty
flag = False
worldP = []
worldS = []
repeatW = []
letter = ""
letters = []
idG = ""
timeG = 0
turn = 0
import string

asscii = list(string.ascii_lowercase)


def initialGame(sub, chatID, colums,timeS = 0):
    global flag
    global timeG
    if flag is False:

        worldP = tools.randomSelection(worlds.find(), worlds.count_documents({}) - 1, colums)

        for i in worldP:
            worldS.append(i['tema'])

        sub.send_message(chatId=chatID,
                         message=f"Se va a empezar el juego de Tutty Frutty:\n[C]Los temas son: \n{tools.forString(worldS, '[B]')}")
        flag = True
        timeG = timeS
        letters = tools.randomSelection(asscii, len(asscii) - 1, len(asscii))


def randomLetter(sub, chatId,):
    if flag is True:
        global letter
        letter = letters.pop(0)

        if len(letter) > 0:
            sub.send_message(chatId=chatId,
                         message=f"Todas las palabras tienen que empezar con la letra :\n[BC]{str(letter).upper()}")

        if timeG > 0:
            time.sleep(timeG)
            calificate(sub,chatId)


def closeGame(sub, chatId):
    global flag
    global worldP, worldS, listPlayers, letter, idG
    if flag is True:
        worldP = []
        worldS = []
        listPlayers = []
        flag = False
        letter = ""
        idG = ""
        pool.pool.clear()
        letters.clear()

        sub.send_message(chatId=chatId, message="Se a finalizado el juego")


def calificate(sub, chatId):
    points = []
    global idG
    global pool
    pool.pool = sorted(pool.pool,key= lambda x: x['turno'])
    for usr in pool.pool:
        if "temas" in usr:
            temas = str(usr['temas']).split("\n")
            if len(temas) > 1:
                for i, tema in enumerate(worldS, start=0):
                    if tools.searchArray(worlds.find_one({'tema': tema})[letter], str(temas[i]).lower()) is True:
                        if tools.searchArray(repeatW, temas[i].lower()) is True:
                            repeatA = Counter(repeatW)
                            if repeatA[temas[i].lower()] > 5:
                                points.append(0)
                            else:

                                points.append(5 - repeatA[temas[i].lower()])
                                puntuacion.changePuntuation(5 - repeatA[temas[i].lower()], usr['userId'])
                                repeatW.append(tools.strip_accents(temas[i].lower()))


                        else:
                            points.append(5)
                            puntuacion.changePuntuation(5, usr['userId'])
                            repeatW.append(tools.strip_accents(temas[i].lower()))

                    else:
                        points.append(0)

                response = f'Jugador: {usr["nickname"]}\n{tools.forString(worldS, points=points)}\n[CB]Puntuacion Total:{usr["puntos"]}'
                sub.send_message(chatId=chatId, message=response)
                if idG == "":
                    idG = puntuacion.saveGame("tuttyFruti")
                else:
                    puntuacion.updateGame(idG)
                turn = 0
                points.clear()


def addAgreePoints(userId, tema, sub, chatId):
    for usr in pool.pool:
        if usr['userId'] == userId:
            if tools.searchArray(worldS, tema) is True:
                i = tools.searchArray(worldS, tema, position=True)
                worldU = str(usr['temas']).split("\n")[i]
                worlds.update_one({'tema': tema}, {'$set': {
                    letter.lower(): worlds.find_one({'tema': tema.lower()})[(letter).lower()] + "," + worldU.lower()}})
                puntuacion.changePuntuation(5, userId)
                sub.send_message(chatId=chatId,
                                 message=f"se le han sumado 5 puntos a:\n[CB]{usr['nickname']}\n[CB]Total Puntos: {usr['puntos']}")
                break


def saveResponse(userId, message):
    global turn
    for user in pool.pool:
        if user['userId'] == userId:
            turn += 1
            user['temas'] = message
            user['turno'] = turn
            break
