
def register (users,sub,chatId,data):
    if users.find_one({'uid': data.message.author.userId}) is None:
        users.insert_one({'uid': data.message.author.userId,
                          'nickname': data.message.author.nickname,
                          'scoreG': 0,
                          'scoreR': 0,
                          'host': False}).inserted_id
        sub.send_message(chatId=chatId, message=f"Se a unido correctamente \n[B]{data.message.author.nickname}")