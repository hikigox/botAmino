from pymongo import MongoClient
from initial import pool
import tools
db = MongoClient()
db = db['amino_mongo_test']
db = db.verdadoreto
dbf = db.find()


def verdad(sub,chatId):

    verdadQ= tools.randomSelection(dbf,db.count_documents({}) - 1)
    sub.send_message(chatId=chatId,message= f"Verdad:\n[B]{verdadQ['verdad']}")


def retro(sub,chatId):

    retoQ= tools.randomSelection(dbf,db.count_documents({}) - 1)
    sub.send_message(chatId=chatId,message= f"Reto:\n[B]{retoQ['reto']}")




