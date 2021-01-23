import tools
import time

def randomQuest(quest,sub,chatId,users):
    flag = False
    selectQ = []
    time.sleep(300)
    while True:
        if flag is False:
            selectQ = tools.randomSelection(quest.find(), quest.count_documents({}) - 1)
            selectQ['flag'] = True
            print(selectQ)
            try:
                sub.send_message(chatId=chatId, message=str(selectQ['quest']),messageType=100)
            except : pass
            flag = True

        else:
            msg = sub.get_chat_messages(chatId=chatId, size=5)
            for msgC, author, authorId, messageId, typeId in zip(msg.content, msg.author.nickname, msg.author.userId,
                                                                 msg.messageId, msg.type):
                if tools.searchArray(selectQ['solucion'].lower(), msgC) and selectQ['flag'] and users.find_one({'uid':authorId}) is not None :
                    score = users.find_one({'uid': authorId})['scoreG']
                    sub.send_message(chatId=chatId,
                                     message=f"[C]Punto para\n[BC]{author}\n Puntos acomulados :{score+1}")
                    selectQ['flag'] = False
                    users.update_one({'uid': authorId}, {'$set': {'scoreG': score + 1}})
                    time.sleep(1500)
                    flag = False
