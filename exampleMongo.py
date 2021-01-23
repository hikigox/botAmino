import amino
from pymongo import MongoClient
from amino import objects
import tools
import threading
from initial import welcome, register, pool,puntuacion
import youtube
from games import tuttyFruty, questions, yonunca,verdadoreto,respuestaTiempo,sinopsis,imagenAdivina,ahorcado,cortocircuito,adivinaColor


email = 'tasinim655@ahhtee.com'
password = '123890'
#CHAT COMUNIDAD TEST
chatId = '7a984e59-004a-4fe5-8f82-206c95fff3cb'
#CHAT COMUNIDAD DEL TAC
#chatIdT = '69249f93-b33f-4940-9452-9a84c58751c3'
# CHAT EN AMINO MIO
#chatId = '6818bae8-7abb-4c25-8a84-54ab25bfa5db'
#COMUNIDAD TEST
comId = '76917488'
# COMUNIDAD ANIME
#comId = '67'
mongo = MongoClient()  # Mongo url, example: go to > mongodb.com > create collection > then ONLY get mongodb+srv://DETAILS/
db = mongo['amino_mongo_test']
users = db.users
quest = db.questRandom
openings = db.openings
client = amino.Client(socketDebugging=True)
client.login(email=email, password=password)
print("Bot logged in")
sub = amino.SubClient(comId=comId, profile=client.profile)
print("Bot logged onto the community, id:", comId, "\nBot Name:", sub.profile.nickname)
oldMessages = []
selectQ = []
t2 = threading.Thread(name="QuestionRandom", target=questions.randomQuest, args=(quest, sub, chatId, users))
t1 = threading.Thread(name="Welcome",daemon= True, target=welcome.welcomeMessage, args=(sub, chatId, oldMessages))
gameY = False
gameTemp = {}
game = ""
rangeG = []
t2.start()
t1.start()


@client.callbacks.event("on_text_message")
def on_text_message(data: objects.Event):
    global gameY
    global rangeG
    global game
    if str(data.message.content).startswith("."):
        print(data.message.content)
        if str(data.message.content).startswith(".1"):
            try:
                sub.send_message(chatId=chatId,message="example",messageType=100)
            except: pass

        if str(data.message.content).startswith(".unirme"):
            register.register(users, sub, chatId, data)

        if users.find_one({'uid': data.message.author.userId}) is not None:
        # Comandos para crear grupo
            if str(data.message.content).startswith(".+") and pool.flag is True:
                pool.agreePool(data.message.author, sub, chatId)

            if str(data.message.content).startswith(".jG") and pool.flag is True:
                pool.closePool(sub, chatId)

            if str(data.message.content).startswith(".cG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                count = str(data.message.content).split(" ")
                if len(count) == 1:
                    pool.initialPool(sub, chatId, 6)
                else:
                    pool.initialPool(sub, chatId, int(count[1]))

            if str(data.message.content).startswith(".gG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                pool.agreePool(data.message.author,sub,chatId,True)

            if str(data.message.content).startswith(".rG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                pool.removePool(data.message.extensions['mentionedArray'][0], sub, chatId)

            if str(data.message.content).startswith(".fG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                pool.deletePool(sub, chatId)
            if str(data.message.content).startswith(".nG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                pool.nextTurn(sub, chatId)

            if str(data.message.content).startswith(".Gr") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                pool.randomTurn()
            # if str(data.message.content).startswith(".rG") and users.find_one({'uid': data.message.author.userId})[
            #     'host'] is True and gameY is False:
            #     puntuacion.getGame(sub,chatId)

            if str(data.message.content).startswith(".pG") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True and gameY is False:
                puntuacion.getPoints(sub,chatId)

        # Comandos de adivina el color
        if str(data.message.content).startswith(".caI") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is False:
            adivinaColor.initialColors(sub,chatId)
            game = "color"

        if str(data.message.content).startswith(".caN") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True is True and game == "color":
            adivinaColor.nextImage(sub,chatId)

        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True and game == "color":
            color = data.message.content.split(" ")[1].lower()
            adivinaColor.response(sub,chatId,data.message.author.userId,data.message.extensions['mentionedArray'][0]['uid'],color)

        # Comandos de Corto Circuito
        if str(data.message.content).startswith(".cI") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is False:
            game = "corto"
            if len(pool.pool) > 1:
                cortocircuito.initialC(sub,chatId)
        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True and game == "corto":
            message = str(data.message.content).split(" ",maxsplit=2)
            if len(message[1]) == 4:
                cortocircuito.resonseT(sub,chatId,data.message.author.userId,message[1])

                
            

        # Comandos Ahorcado
        if str(data.message.content).startswith(".aI") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is False:
            game ="ahorcado"
            if len(pool.pool) > 1:
                if len(str(data.message.content).split(" ")) > 1:
                    ahorcado.initialA(sub,chatId,str(data.message.content).split(" ")[1])
                else:
                    ahorcado.initialA(sub, chatId)

        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True and game == "ahorcado":
            message = str(data.message.content).split(" ",maxsplit=2)
            if len(message) > 1:
                ahorcado.responseA(sub,chatId,message[1].lower(),data.message.author.userId)





        # Comandos para di el mismo numero
        if str(data.message.content).startswith(".Mi") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:

            if len(pool.pool) > 1:
                respuestaTiempo.createPair(sub,chatId)
                
        if str(data.message.content).startswith(".Mc") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and len(respuestaTiempo.groupPair) == 2:
            respuestaTiempo.challenge(sub,chatId)
            
        if str(data.message.content).startswith(".Ms") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and len(respuestaTiempo.groupPair) == 2:
                respuestaTiempo.startGame(sub,chatId)
            
        if str(data.message.content).startswith(".Mr") and len(respuestaTiempo.groupPair) == 2:

            respuestaTiempo.response(sub,data.message.chatId,data.message.content)

        if str(data.message.content).startswith(".Ms") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and len(respuestaTiempo.groupPair) == 2:
            respuestaTiempo.startGame(sub, chatId)

            # Comandos de verdad o reto

        if str(data.message.content).startswith(".Nr") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True:
                verdadoreto.retro(sub,chatId)
        if str(data.message.content).startswith(".Nv") and users.find_one({'uid': data.message.author.userId})[
           'host'] is True:
            verdadoreto.verdad(sub,chatId)



        #Comandos de juego yo nunca
        if str(data.message.content).startswith(".y-") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True:
            yonunca.responseQuest(data.message.author.userId)
            
            
        if str(data.message.content).startswith(".yI") and users.find_one({'uid': data.message.author.userId})['host'] is True:
            points = data.message.content.split(" ")
            if len(points) > 1:
                yonunca.initialYonunca(sub,chatId,points[1])
            else:
                yonunca.initialYonunca(sub, chatId)
        if str(data.message.content).startswith(".yS") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:
            yonunca.showQuest(sub,chatId)

        if str(data.message.content).startswith(".yP") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:
            yonunca.showPoints(sub,chatId)
        if str(data.message.content).startswith(".yC") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:
            yonunca.closeYonunca(sub,chatId)


        #Comandos de juego tutti frutti
        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,'userId') is True and tuttyFruty.flag is True and game == "tutty":
            messageS = str(data.message.content).split("\n",1)
            if len(messageS) == 2:
                tuttyFruty.saveResponse(data.message.author.userId,message=messageS[1])

        if str(data.message.content).startswith(".tt") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is False:
            game ="tutty"
            count = 4 if (len(str(data.message.content).split(" ")) < 2) else str(data.message.content).split(" ")[1]
            tuttyFruty.initialGame(sub,chatId,count)
        if str(data.message.content).startswith(".ttL") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is True:
            tuttyFruty.randomLetter(sub,chatId)
        if str(data.message.content).startswith(".ttC") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is True:
            game = ""
            tuttyFruty.closeGame(sub,chatId)
        if str(data.message.content).startswith(".ttT") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is True:
            tuttyFruty.calificate(sub,chatId=chatId)
        if str(data.message.content).startswith(".ttA") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and tuttyFruty.flag is True:
            dataM = str(data.message.content).split(" ")
            if len(dataM) > 2:
                tuttyFruty.addAgreePoints(data.message.extensions['mentionedArray'][0]['uid'],dataM[1],sub,chatId)

            #Comandos adivina la sinopsis
        if str(data.message.content).startswith(".iS") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:
            if len(pool.pool) >= 1:
                game = "sinopsis"
                sinopsis.randomSig(sub,chatId)
        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True and game == "sinopsis":
            sinopsis.responseS(sub,chatId,data.message)

        if str(data.message.content).startswith(".sF") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True:
            game = ""
            sinopsis.finalS(sub,chatId)
        # Comandos Adivina el personaje
        if str(data.message.content).startswith(".pS") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True:
            if len(pool.pool) >= 1:
                game = "personaje"
                imagenAdivina.imageRandom(sub,chatId)
        if str(data.message.content).startswith(".R") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True and game == "personaje":
            imagenAdivina.responseImage(sub,chatId,data.message)

        if str(data.message.content).startswith(".pF") and tools.searchArrayJson(pool.pool,data.message.author.userId,"userId") is True:
            game = ""
            imagenAdivina.closeImage(sub,chatId)

        #            Comandos para empezar adivina el opening
        if str(data.message.content).startswith(".op") and users.find_one({'uid': data.message.author.userId})[
            'host'] is True and gameY is False:
            game = "opening"
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

        if gameY:

            if str(data.message.content).startswith(".opf") and users.find_one({'uid': data.message.author.userId})[
                'host'] is True:
                sub.send_message(chatId=chatId, message="Se cancelo el Evento")
                gameY = False
                game = ""

            if str(data.message.content).startswith('.R') and game == "opening":
                response = str(data.message.content).split(" ",1)
                if len(response) > 1:
                    if tools.searchArray(gameTemp['respuesta'], response[1]):
                        score = users.find_one({'uid': data.message.author.userId})['scoreG']
                        sub.send_message(chatId=chatId,message=f"[C]Punto para\n[BC]{data.message.author.nickname}\n Puntos acumulados :{score + 1}")
                        gameY = False

                        users.update_one({'uid': data.message.author.userId}, {'$set': {'scoreG': score + 1}})

            if str(data.message.content).startswith(".opN") and users.find_one({'uid': data.message.author.userId})[
                'host'] is not False:
                if len(rangeG) != 0:
                    with open(f"videos/cut{rangeG[0]}.mp3", 'rb') as file:
                        sub.send_message(chatId=chatId, file=file, fileType='audio')
                        file.close()
                        file.close()
                        rangeG.pop(0)




