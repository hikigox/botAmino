from pymongo import MongoClient
from initial import pool,puntuacion
import time
from collections import Counter
import tools
db = MongoClient()
db = db['amino_mongo_test']
db = db.ahorcado
randomWord = []
randomWordE = []
tempPool = []
turn = 0
HANGMANPICS = ['''
  +--------+
  |        |
           |
           |
           |
           |
============''', '''
  +--------+
  |        |
  O        |
           |
           |
           |
============''', '''
  +--------+
  |        |
  O        |
 /         |
           |
           |
============''', '''
  +--------+
  |        |
  O        |
 /|        |
           |
           |
============''', '''
  +--------+
  |        |
  O        |
 /|\       |
           |
           |
============''', '''
  +--------+
  |        |
  O        |
 /|\       |
 /         |
           |
============''', '''
  +--------+
  |        |
  O        |
 /|\       |
 / \       |
           |
============''']
tried = 0
groupL = ""
def initialA(sub,chatId,type = "random"):
    global randomWord,randomWordE,groupL,tried,turn
    clearAll()

    if type == "random":
        type = tools.randomSelection(db.find(),db.count_documents({}) - 1)['tema']

    dbTheme = db.find_one({"tema": type})['palabras'].split(",")
    randomWord.append(tools.randomSelection(dbTheme, len(dbTheme) - 1)) 
    randomWord.append(randomWord[0].split(" "))
    randomWordE = ["_"*len(word) for word in randomWord[1]]
    sub.send_message(chatId=chatId,message = f"El tema seleccionado es \n[CB]{type.capitalize()}\n[C]{HANGMANPICS[0]}\n[C]{printWordE()}")
    time.sleep(3)
    pool.pool = tools.randomSelection(pool.pool, len(pool.pool) - 1, len(pool.pool))
    pool.randomTurn()
    turn = pool.nextTurn(sub,chatId)
    


# def initialTurn(sub,chatId):
#     global pool,tempPool,turn
#     if len(pool.pool) > 0:
#         if len(tempPool) < 1:
#             tempPool = pool.pool.copy()
#
#         turn = tempPool.pop(0)
#         sub.send_message(chatId=chatId,message= f"Turno de {turn['nickname']}")

def responseA(sub,chatId,message,userId):
    global randomWordE,tried,groupL,turn
    if pool.pool[pool.turn-1]['userId'] == userId:
        if len(message) == 1:
            count = Counter(randomWord[0])[message]
            if count == 0  or tools.searchArray(groupL,message):
                tried +=1
                if len(HANGMANPICS) == (tried+1):
                    sub.send_message(chatId=chatId, message=f"[C]FIN DEL JUEGO\n{HANGMANPICS[tried]}\n[C]{printWordE()}")
                    clearAll()

                else:
                    sub.send_message(chatId=chatId,message=f"{HANGMANPICS[tried]}\n[C]{printWordE()}")
                    turn = pool.nextTurn(sub, chatId)
            else :
                for i,word in enumerate(randomWord[1],start=0):
                    for j,char in enumerate(word, start=0):
                        if char == message:
                            wordC = list(randomWordE[i])
                            wordC[j] = message
                            randomWordE[i] = wordC
                groupL += message
                sub.send_message(chatId=chatId,message=f"[C]{HANGMANPICS[tried]}\n[C]{printWordE()}")
                turn = pool.nextTurn(sub, chatId)
        else:
            if tools.searchArray(randomWord[0],message) is True:
                sub.send_message(chatId= chatId,message = f"Has adivinado {pool.pool[turn]['nickname']}")

                sub.send_message(chatId=chatId,message=f"[C]{HANGMANPICS[tried]}\n[C]{randomWord[0]}")
                puntuacion.changePuntuation(10,userId)
                clearAll()
            else:
                turn = pool.leaveGroup(sub,chatId,turn)




def clearAll():
    global randomWord, randomWordE, groupL, tried
    randomWord.clear()
    randomWordE.clear()
    groupL = ""
    tried = 0
    groupL = ""


def printWordE():
    return "    ".join([" ".join(word4) for word4 in randomWordE])
