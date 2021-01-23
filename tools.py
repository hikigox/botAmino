import random
import unicodedata
def searchArray(arr, data,flag = 0,position = False):
    """
    Funcion que busca en un arreglo una palabra o numero en un arreglo tanto string como array
    arr: array
    data: search Object
    flag : iterador recursivo
    position: para retornar la posicion donde esta el elemento buscado
    """

    if data == "":
        return False
    if flag < 2:

        try:
            if type(data) == int:
                arr.index(data)
            else:
                if type(arr) != str:
                    arr = [world.lower() for world in arr]
                else :
                    arr = arr.lower()
                if position:
                    return arr.index(strip_accents(data.lower()))
                arr.index(strip_accents(data.lower()))
            return True




        except:
            return searchArray(data,arr,flag+1)


    else:
        return False

def searchArrayObject(arr,data,tag):
    flag = False
    for item in arr:
        if getattr(item,tag) == data:
            flag = True
            break
    return flag

def searchArrayJson(arr,data,tag):
    flag = False
    for item in arr:
        if item[tag] == data:
            flag = True
            break
    return flag

def searchArrayJsonIndex(arr,data,tag):
    flag = -1
    for i,item in enumerate(arr,start=0):
        if item[tag] == data:
            flag = i
            break
    return flag


def randomSelection(arr,maxLength,count = 0):
    """
     Funcion que devuelve un numero random o un arreglo nuevo de el anterior pero con posiciones diferentes.

     arr : arreglo,
     maxLnegth : tamaño arreglo
     count = cantidad de items para nuevo arreglo
     """

    randomN = random.randint(0,maxLength)
    if count == 0:
        return arr[randomN]
    else:
        uniqueRandom= []
        i = 0
        while i < count :
            randomN = random.randint(0, maxLength)
            if searchArray(uniqueRandom,randomN) is not True:
                uniqueRandom.append(randomN)
                i +=1
        i = 0
        arr2 = []
        for i in uniqueRandom:
            arr2.append(arr[i])
        return arr2








def forString(arr,typeLetter = "",points = ""):
    """
    funcion que crea un string espaciado con los datos de un arreglo
    arr: arreglo
    typeLetter : tipo de letra (amino [CB]
    points : funcionalidad para agregarle puntos
    """

    list = ""
    if points == "":
        for i in arr:
            list +=f"{typeLetter}{i.capitalize()}\n"
        return list
    else:
        for j,i in enumerate(arr,start=0):
            list += f"{typeLetter}{i.capitalize()} : {points[j]}\n"
        return list

def forStringPropeties(arr,typeLetter = "",points = "",atribute = ""):
    list = ""
    if points == "":
        for i in arr:
            if type(i[atribute]) == int:
                list +=f"{typeLetter}{i[atribute]}\n"
            else:
                list +=f"{typeLetter}{i[atribute].capitalize()}\n"
        return list
    else:
        for j,i in enumerate(arr,start=0):
            list += f"{typeLetter}{i[atribute].capitalize()} : {points[j]}\n"
        return list


def strip_accents(s):
    """
    Sanitarize the given unicode string and remove all special/localized
    characters from it.

    Category "Mn" stands for Nonspacing_Mark
    """
    try:
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )
    except:
        return s
    
    
def generatePool(sub,chatId,userId):
    sub.send_message(chatId=chatId,message="Se genero una lista en la pool")
    return [{'userId': userId
                         ,'nickname':f"bot{i}",
                         'puntos':0} for i in range(5)]
