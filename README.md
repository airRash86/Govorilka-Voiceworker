# 🖹→🔊 Озвучка текста с применением мощностей Джанго.
### 👉 Работающий проект можно найти по адресу:  https://rashprojs.ru/voiceworker/

✅Посредством этого мини проекта можно поберечь глазки и, вогнав текст в обработчик,
получить на выходе вместо текст - звук. Полученный результат к вашим услугам: доступен для скачачивания
в виде мп3 файла или же для прослушивания в самом браузере (скорость воспроизведения варьируется).
Автоматическая очистка накопленных на удаленном сервере мп3 файлов, а также записей
в БД производится раз в сутки. Этот функционал реализован через Телеграм бот (см. репо https://github.com/airRash86/BOT_checker_debuger)


✅ 1. О том, что проект желательно держать в отдельном вирт. окружении я тут писать не буду 
и сам процесс по запуску этого самого venv тоже описывать не стану: он стандартный 
в сети достаточно много материалов по этому поводу.

✅ 2. Если вы не находите в папке приложения такие файлы, как admin.py, apps.py итд - это
означает, что в процессе написания своего проекта, я их не трогал, соответственно, они остались
неизменными (их наполнение - дефолтное, джанговское). 

✅ 3. Папка media, которая фигурирует, как директория для сохранения мп3 файлов 
(см файл APPbegin_voice/Tools_voice_ACTING.py) - это Джанговский концепт для 
сохранения медиа файлов. Стандартный ход.
Из нее-то (папки media) и берутся файлы для воспроизведения для конечного пользователя. 
Эту папку я сюда не добавил, т.к. все равно сейчас она будет пуста.  

✅ 4. Стандартуню папку admin, что включает статические файлы (css, js, img итд) и располагается
в папке static, в корне проекта, я сюда выкладывать не стал, также, как и файл фавикон. 

✅ 4.5 Кроме этого, картинки (которые отрисовываются при загрузке index.HTML (главная стр. проекта rashprojs.ru/voiceworker)
и ready.HTML (стр. с результатом работы скрипта rashprojs.ru/ready/<slug>)), которые также
расположены в папке static (gal.png и mega.jpg: <мегафон> и <зеленая галочка> (см. картинки на сайте)) я сюда 
выкладывать не стал аналогично.

✅ 5. Проект по размеру скромный и в папке templates (в шаблонах приложения) всего три
этих самых HTML шаблона.

✅ 6. Также еще раз позвольте обратить ваше внимание, что многое из стандартного наполнения
Джанго проекта я  сюда выкладывать не стал, т.к., по моему скромному мнению, в этом 
нет необходимости:   "рыба" проекта заключается в файлах, которые тут, а остльное
сформируется по стандартной джанговоской схеме, когда вы введете в командной строке: 
django-admin.py startproject <proj_name>

✅ 7. Структуру Базы Данных отражена в скрине ниже (см. п.10).  Также с ней можно легко ознакомится,
проверив файл  APPbegin_voice/models.py (модель). Не забудьте произвести миграции.

✅ 8. Ну а файл manage.py в корне я выложил просто для того, чтобы он служил в кач-ве 
"навигатора":  если кто-то из пользователей посетит данный репо и будет переходить по папкам, то видя
manage.py, он будет понимать: "Ага, вот он корень, от него и отсчет")

✅ 9. Еще немного об очистке. Я знаю, что удаление старых файлов из папки media (та, что наполняется этими самыми мп3 файлами) 
можно проводить посредствоми Джанго сигналов. Я узнал об этой технологии (сигналы)
уже после того, как начал реализацию задачи по упомянутой очистке через Телеграм бота (ежесуточно он 
проверяет наличие скопившихся файлов и, в соответствии с логикой, удаляет их).  
Данная затея реализованна именно через ТГ, т.к.  уведомления в этом популярной мессенджере удобны, 
привычны и отреагировать на них и даже что-то подправить в режиме диалога с ботом (реализовано и это)
мне, как админу, разрабу и руководителю в одном лице, значительно проще и быстрее. 
Еще раз, ссылка на этого бота-"дворника" тут https://github.com/airRash86/BOT_checker_debuger

📸  10. Скриншот структуры БД: 
![Структура таблицы в БД](https://user-images.githubusercontent.com/107410620/205463903-fd703ece-4440-4e04-9f61-bbb71067ccba.png)

ℹ Деплой производился с применением технологии nginx и gunicorn, SSL сертификат бесплатный и получен через сервис LET`S ENCRYPT 
 (конфигурационные файлы по разделу deploy выкладывать не стал: если они понадобятся - LET ME KNOW👋)))







 
