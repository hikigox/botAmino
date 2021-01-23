from pymongo import MongoClient
from initial import pool,privateMesssage,puntuacion
import tools
import requests
import random
db = MongoClient()
db = db['amino_mongo_test']
db = db.colores


def initialColors(sub,chatId):
    global pool
    if len(pool.pool) > 1 :
        
        colors = db.find()
        colors = tools.randomSelection(colors,db.count_documents({}) - 1,len(pool.pool))
        for i,user in enumerate(pool.pool,start=0):
            colorS= colors.pop(0)
            privateMesssage.privateMessage(sub,user['userId'],colorS['color'])
            pool.pool[i]['color'] = colorS['color']
            pool.pool[i]['intento'] = 0

        sub.send_message(chatId=chatId,message= "[B]Se han enviado los colores al privado !!!")


def nextImage(sub,chatId):
    num = str(random.randint(0, 1000000000))
    print(num)

    response = requests.get(f'https://source.unsplash.com/collection/{num}')
    image = open("games/hands.PNG", 'wb')
    image.write(response.content)
    image.close()
    with open("games/hands.PNG",'rb') as file:
        sub.send_message(chatId=chatId, file=file, fileType='image')
        file.close()



def response(sub,chatId,userId,userIdR,message):
    if tools.searchArrayJson(pool.pool,userId,"userId") is True:
        if tools.searchArrayJson(pool.pool, userIdR, "userId") is True:
            i = tools.searchArrayJsonIndex(pool.pool,userIdR,"userId")
            if pool.pool[i]['color'] == tools.strip_accents(message):
                j = tools.searchArrayJsonIndex(pool.pool, userId, "userId")

                sub.send_message(chatId=chatId,message=f"[CB]El Jugador \n{pool.pool[j]['nickname']}\n[CB]Adivino el Color de {pool.pool[i]['nickname']}")
                puntuacion.changePuntuation(5,userId)
                pool.pool.pop(i)
            else:
                j = tools.searchArrayJsonIndex(pool.pool, userId, "userId")
                player = pool.pool[j]
                letra = player['color'][player['intento']]
                pool.pool[j]['intento'] +=1

                sub.send_message(chatId=chatId,
                                 message=f"[CB]El Jugador \n{pool.pool[j]['nickname']}\n[CB]Tiene en su color la letra {letra}")
                puntuacion.changePuntuation(-10, userId)


             
            




