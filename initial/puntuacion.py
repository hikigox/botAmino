from pymongo import MongoClient
from initial import pool
import tools
db = MongoClient()

db = db['amino_mongo_test']
db = db.games

def changePuntuation(points, userId):
    for usr in pool.pool:
        if usr['userId'] == userId:
            usr['puntos'] = usr['puntos'] + points
            break


def saveGame(game):

    if len(pool.pool) > 1:
        return db.insert({"players":pool.pool,"game": game})


def updateGame(id):
    if len(pool.pool) > 1:
        db.update_one({"_id":id},{'$set':{"players":pool.pool}})


def getGame(sub, chatId):
    global pool
    pooldb= db.find_one()
    pool.pool= pooldb['players']
    sub.send_message(chatId=chatId,message=f"Se ah restaurado la partida de {pooldb['game']}")


def getPoints(sub,chatId):
    nicks = [usr['nickname'] for usr in pool.pool]
    points = [usr['puntos'] for usr in pool.pool]
    sub.send_message(chatId=chatId,message=f"[CB]Tabla de puntaje:\n{tools.forString(nicks,points=points)}")





