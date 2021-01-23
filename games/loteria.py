from pymongo import MongoClient
from datetime import datetime
import random
from initial import privateMesssage
bd = MongoClient()
loteria = bd.loteria
week = 604800


def initialLoteria():
    date = loteria.find_one()
    if date['flag'] is not True:
        dateN = datetime.now()
        loteria.update_one({'$set': {'fechaInicio': dateN , 'fechaFinal': datetime.fromtimestamp(dateN.timestamp() + week),"flag": True}})





def inscribirLoteria(usr,num,sub,chatId):
    if num <= 100:
        for persona in loteria.find_one()['pool']:
            if persona['num'] == num:
                sub.send_message(chatId,"El numero ingresado ya fue escogido")
            else:
                loteria.update_one({"$push": {
                    'pool': {
                        'id': usr.userId,
                        'nick': usr.nick,
                        'num': num
                    }

                }})


def ganadorNumber(sub,chatId):
    date = loteria.find_one()
    dateN = datetime.now()
    if(( datetime.fromtimestamp(dateN) - datetime.fromtimestamp(date['fechaFin'])) <= 0):
        numeroWin = random.randint(0,100)
        for user in loteria['pool']:
            if user['num'] == numeroWin:
                sub.send_message(chatId,f"El ganador fue\n[CB]{user['nick']}\n[C]Con el numero :[B]{numeroWin}")
                privateMesssage.privateAdm(sub)










