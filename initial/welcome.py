import tools
import typesId as TYPEID

def welcomeMessage(sub,chatId,oldMessages):

    global selectQ
    while True:

        msg = sub.get_chat_messages(chatId=chatId, size=5)
        for msgC, author, authorId, messageId, typeId in zip(msg.content, msg.author.nickname, msg.author.userId,
                                                             msg.messageId, msg.type):
            if not messageId in oldMessages:

                if typeId == TYPEID.Message.GET_IN.value:
                    sub.send_message(chatId=chatId,
                                     message=f"[C]┏━━━━━━༻✧༺━━━━━━┓\n[C]Bienvenid@ al Chat\n[CB]{author}\n[C]Lee la descripcion y \n[C]enterate de lo que tenemos \n[C]para ti\n[C]┗━━━━━━༻✧༺━━━━━━┛")
                oldMessages.append(messageId)

