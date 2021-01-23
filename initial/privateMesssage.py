admin = 'bd7c7073-4f91-450c-acad-aaea22a87e43'


def privateAdm (sub):
    sub.start_chat(userId=admin, message="Creando chat Privado")


def privateMessage(sub,userId,message):
    sub.start_chat(userId=userId,message=message)

def leavePrivateChat(sub,userId):
    for chat in sub.get_chat_threads().chatId:
        search = sub.get_chat_thread(chatId=chat).membersSummary.json
        if len(search) == 2 and (search[0]['uid'] == userId or search[1]['uid'] == userId):
            sub.leave_chat(chatId=chat)
            break

def getChatId(sub,userId):
    for chat in sub.get_chat_threads().chatId:
        search = sub.get_chat_thread(chatId=chat).membersSummary.json
        if len(search) == 2 and (search[0]['uid'] == userId or search[1]['uid'] == userId):
            return chat