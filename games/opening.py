import tools
import youtube


def initialOp(openings,sub,chatId):
    global gameTemp
    global rangeG
    rangeG = [*range(1, 4)]
    op = tools.randomSelection(openings.find(), openings.count_documents({}) - 1)
    youtube.performanceY(op['url'])
    gameTemp['respuesta'] = op['respuesta']
    with open(f"videos/cut{rangeG[0]}.mp3", 'rb') as file:
        sub.send_message(chatId=chatId, file=file, fileType='audio')
        file.close()
    file.close()
    rangeG.pop(0)
    gameY = True

def solver(users,data,chatId,sub):
    score = users.find_one({'uid': data.message.author.userId})['scoreG']
    sub.send_message(chatId=chatId,
                     message=f"[C]Punto para\n[BC]{data.message.author.nickname}\n Puntos acumulados :{score + 1}")
    gameY = False

    users.update_one({'uid': data.message.author.userId}, {'$set': {'scoreG': score + 1}})

def nextT(rangeG,sub,chatId):
    if len(rangeG) != 0:
        with open(f"videos/cut{rangeG[0]}.mp3", 'rb') as file:
            sub.send_message(chatId=chatId, file=file, fileType='audio')
            file.close()
        file.close()
        rangeG.pop(0)