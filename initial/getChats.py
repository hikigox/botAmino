import amino
from amino import objects
email = 'tasinim655@ahhtee.com'
password = '123890'
chatId = '7a984e59-004a-4fe5-8f82-206c95fff3cb'
comId = '67'

client = amino.Client()
client.login(email=email, password=password)
subClient = amino.SubClient(comId=comId,profile=client.profile)
chats = subClient.get_chat_threads()

for id,title in zip(chats.chatId,chats.title):
    print(id,",",title)
