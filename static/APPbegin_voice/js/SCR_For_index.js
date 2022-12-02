"use strict"
var btn = document.getElementById('btn');
    document.forms.ourForm.onsubmit = function(e){
    e.preventDefault();
    
    var userInp = document.forms.ourForm.ourForm__inp.value;
    if(userInp.length > 0) {
        if(userInp.length > 2500){
            document.getElementById("AlarmLenTEXT").innerHTML = '⚠️Длина введенного вами текста составляет: '+ (userInp.length) + ' симв.  <br>\
            Если загрузка превысит 30 сек., то перезагрузите страницу <br> \ и попробуйте вводить текст частями:\
            <br>так, чтобы его длина была не больше ~2500 символов!'
            }
        btn.disabled = true;
        document.getElementById("headLoading").innerHTML = 'Загрузка...'
        document.getElementById("secondLoading").innerHTML = 'это может занять несколько секунд'
        makeReq(userInp)
        }
    else{alert("⚠️Поле ввода не должно быть пустым!");}
    }

    async function  makeReq(userInp){
        const CSRF = document.querySelector('[name=csrfmiddlewaretoken]').value   //CSRF токен для POST запроса на Джанго
        let headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': CSRF}

        let user_FOR_aj = {
            userInp: userInp};
            
        let response = await fetch('/voiceworker/', {
            method: 'post',
            headers: headers,
            body: JSON.stringify(user_FOR_aj)
        });
        let ans_serv = await response.json();
        if(ans_serv['mark'] == 'ok'){
            let link_slug = 'https://rashprojs.ru/ready/12asw305_' + ans_serv['duo'] +'_399_' + ans_serv['Three'] + '_6913-69w/' 
            passLinkAudioReq(link_slug);
            }
        else{let link_slug = 'https://rashprojs.ru/error/'
            passLinkAudioReq(link_slug);
            }
    }

    async function passLinkAudioReq(link_slug){
        btn.disabled = false;
        document.getElementById("headLoading").innerHTML = ''
        document.getElementById("secondLoading").innerHTML = ''
        document.getElementById("AlarmLenTEXT").innerHTML = ''
        window.location.href = link_slug}


  