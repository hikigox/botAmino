from initial import pool,privateMesssage
import tools
from pymongo import MongoClient
groupPair = []
db = MongoClient()
db = db['amino_mongo_test']
db = db.challeges
chatIdP = ""
flagP = []
def createPair(sub,chatId):
    if len(pool.pool)> 1:
        global groupPair
        global chatIdP
        chatIdP = chatId
        groupPair = tools.randomSelection(pool.pool,len(pool.pool)-1,2)

        pairS= tools.forString([usr['nickname'] for usr in groupPair],typeLetter="[CB]")
        sub.send_message(chatId=chatId,message=f"[C]La Pareja es:\n{pairS}")

def challenge(sub,chatId):
    challengeDB  = tools.randomSelection(db.find(), db.count_documents({}) - 1)
    sub.send_message(chatId=chatId,message=f"[BC]RETO:\n[C]{challengeDB['reto']}")

from amino import SubClient
def startGame(sub,chatId):

    for user in groupPair:
        privateMesssage.privateMessage(sub,user['userId'],"Escribe un numero entre 1 o 2 (ejemplo .Mr 1)")
        user["chatId"] = privateMesssage.getChatId(sub,user['userId'])
    sub.send_message(chatId =chatId, message= "Revisen sus prv (La paraja de este turno)!!!")

def response(sub,chatId,message):
    global flagP

    if tools.searchArrayJson(groupPair,chatId,"chatId"):
        response = message.split(" ")
        if len(response) == 2 :
            if response[1] == "1":
                flagP.append(True)
            else:
                flagP.append(False)
    if len(flagP) == 2:
        groupPair.clear()
        if flagP[0] == flagP[1]:
            sub.send_message(chatId=chatIdP,message= "[B]La pareja escribio el mismo numero!!!")


        else:
            sub.send_message(chatId=chatIdP,message= "[B]La pareja escribio diferente numero!!!")

        flagP.clear()













