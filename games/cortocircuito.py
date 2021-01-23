import random
from initial import pool
turn = 0
randomN = ""
def cortos (numero,respuesta):
    pivot = 0
    for i,digit in enumerate(numero,start=0):
        if digit == respuesta[i]:
            pivot += 1
            numero = numero[:i]+'o'+numero[i+1:]

    return cables(numero,respuesta,pivot)


def cables (numero,respuesta,pivotO):
    pivot = 0
    for i,digit in enumerate(numero,start=0):
        try:
            look = respuesta.index(digit)
            if look != i:
                pivot += 1
                numero= numero[:i]+'a'+numero[i+1:]
        except :pass
    return [pivotO,pivot]

def initialC(sub,chatId):
    global randomN,turn
    randomN = "".join([str(random.randint(0, 9)) for i in range(4)])
    turn = pool.nextTurn(sub, chatId)


def resonseT(sub,chatId,userId,message):
    global turn
    if pool.pool[turn]['userId'] == userId:
        if len(message) == 4:
            resolve = cortos(message,randomN)
            if resolve[0] == 4:
                sub.send_message(chatId=chatId,message=f"[C]El jugador\n[CB]{pool.pool[turn]['nickname']}\nHizo Corto Circuito!!")
                clearGame()
            else:
                sub.send_message(chatId=chatId,message=f"[C]Cortos\n[CB]{resolve[0]}\n[C]Cables\n[CB]{resolve[1]}")
                turn = pool.nextTurn(sub,chatId)


def clearGame():
    global turn,randomN
    turn = 0
    randomN= ""