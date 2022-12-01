from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from APPbegin_voice.Tools_voice_ACTING import voice_ACTING
from APPbegin_voice.models import audio_book
import json
import datetime


def pr(request):
    return HttpResponse('<br><br><br><center><h1>Приветствую тебя, посетитель) Тут Рашид упражняется)))!</h1></center>')



def ready(request, DijArg):
    userNum = DijArg.split('_')[3] + DijArg.split('_')[1]
    try:
        #Извлечение из БД по номеру записи, сформерованному по данным из url
        BEFORE = audio_book.objects.filter(num=userNum)[0]
        aud_STORE = str(BEFORE).split('---')
        return render(request, 'APPbegin_voice/ready.html', {'aud': aud_STORE[0], 
                                                            'aud_amo': aud_STORE[1]}) 
    except:
        #Раз в сутки происходит очистка mp3 и записей в БД, если юзер перейдет по старой ссылке, то попадет на данную стр:  
        return HttpResponse('<br><br><br><h1><center>❗Ошибка на сервере или ваша ссылка устарела</center></h1>')

#В случае ошибки во время конвертации текста в голос срабатывает эта view:
def errTooMuchChars(request):
    return HttpResponse('<br><br><br><h1>❗Ошибка на сервере или вы ввели слишком длинный текст</h1><br><br><h3>Попробуйте сделать текст короче!</h3>')

def index(request):
    #Если реквест из формы для ввода текста (фронт), то срабатывает код под ифом, строчкой ниже
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if json.loads(request.body)['userInp']:
            message_d = json.loads(request.body)['userInp']
            cur_aud = voice_ACTING(message_d) #Запуск конвертера (текст в голос)
            if cur_aud[0] == 'ok': #Далее формирования json ответа на фронт, с дальнейшем формированием там url для редиректа
                ThreeForURL = cur_aud[2]
                duoForURL = cur_aud[3]
                return JsonResponse({'mark':'ok', 'Three':ThreeForURL, 'duo':duoForURL})
            else:
                return JsonResponse({'mark':'no'})
    return render(request, 'APPbegin_voice/index.html')
    

#Раньше данный проект был на url, что ниже, затем переехал на текущий, но часть
#посетителей могут приходить по старому адресу. Можно было сделать из серии отклика с кодом >300, но
#было принято решение об именно такой реализации
def TESTING(request):
    return render(request, 'APPbegin_voice/TESTING.html')


