import  random
import tools
pool = []
flag = False
flag2 = False
count = 0

def initialPool(sub,chatId,cant):
    global  count
    global flag
    count = cant
    sub.send_message(chatId=chatId, message=f"Se creo un grupo para {cant} de jugadores")
    flag = True


def agreePool(user,sub,chatId,flag = False):
    global pool

    if flag is False:
        if len(pool) < count and flag2 is not True:
            if tools.searchArrayJson(pool,user.userId,'userId') is not True:
                pool.append({'userId': user.userId
                             ,'nickname':user.nickname,
                             'puntos':0})
                sub.send_message(chatId=chatId, message=f"El usuario {user.nickname} se agrego al juego")
    else:
        pool.append({'userId': user.userId
                        , 'nickname': user.nickname,
                     'puntos': 0})
        pool += tools.generatePool(sub,chatId,user.userId)


def removePool(user,sub,chatId):
    if flag2 is not True:
        nick = ""
        for userp in pool:
            if userp['userId'] == user['uid']:
                nick = userp['nickname']
                pool.remove(userp)
                break

        sub.send_message(chatId=chatId, message=f"El usuario {nick} se saco del juego")

def closePool(sub,chatId):
    if flag2 is not True:
        users =""
        for user in pool:
            users += f"[B]{user['nickname']}\n"

        sub.send_message(chatId=chatId, message=f"Los Jugadores Son \n{users}")


def deletePool(sub,chatId):
    pool.clear()
    sub.send_message(chatId=chatId, message="Se elimino el grupo")
    flag = False

turn = 0
def nextTurn(sub,chatId,flag = False):
    global turn
    if flag is False:
        if turn == len(pool) -1:
            sub.send_message(chatId=chatId, message=f"El Turno es para:\n[CB]{pool[turn]['nickname']}")
            turn = 0
            return turn
        else:
            sub.send_message(chatId=chatId,message=f"El Turno es para:\n[CB]{pool[turn]['nickname']}")
            turn += 1
            return turn-1
    else:
        sub.send_message(chatId=chatId, message=f"El Turno es para:\n[CB]{pool[turn]['nickname']}")
        return turn


def leaveGroup(sub,chatId,turn):

    sub.send_message(chatId=chatId, message=f"No adivino y se expulsa del grupo a {pool[turn]['nickname']}")
    pool.pop(turn)
    return pool.nextTurn(sub, chatId,True)



def randomTurn():
    random.shuffle(pool)
