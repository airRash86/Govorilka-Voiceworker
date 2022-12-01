from gtts import gTTS
import datetime
from .models import audio_book
from random import randint


def voice_ACTING(TheDoc): #TheDoc - текст от юзера с фронта
    msk = datetime.datetime.now().strftime("%d_%m_%y_[%H-%M-%S]_%A")  #%A - название дня недели
    resul = None
    ThreeForURL = None
    duoForURL = None
    try:
        tts = gTTS( text = TheDoc, lang = 'ru' )
        tts.save( F'media//{msk}_Filename.mp3' ) #Save in dir mp3 (внимание к настройкам Джанго: медиа)
        s_N_P = str(F'{msk}_Filename.mp3') #Name new line in DB
        ThreeForURL = randint(100, 999) #Заготовка для идентификации по номеру в БД (по части url)
        duoForURL = randint(10, 99) #Вторая часть заготовки для идентификации по номеру в БД (по части url)  
        saving_PATH_new_POST(s_N_P, ThreeForURL, duoForURL, len(TheDoc))
        resul = s_N_P
        arg_1 = 'ok' #Маркер для фронта (отклик 200)
    except:
        arg_1 = 'loose' #Маркер для фронта (отклик 500)
    return arg_1, resul, ThreeForURL, duoForURL

#Фиксация в БД   
def saving_PATH_new_POST(s_N_P, ThreeForURL, duoForURL, lenTEXT):
    pass_sum = str(ThreeForURL) + str(duoForURL)
    aaa = audio_book(num=pass_sum, book=s_N_P, amoChars=lenTEXT)
    aaa.save()
