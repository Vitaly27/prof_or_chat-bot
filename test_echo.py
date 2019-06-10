import telebot

from telebot import types

name = ''
otvet = ''
p=0
t=0
c=0
z=0
h=0
odin='1'
dva='2'
otv=''

bot = telebot.TeleBot("835209382:AAFeY1RmWlpq0l35z2W0ywgYnre1-GSX9AA")

@bot.message_handler(content_types=['text'])
def send_name(message):
    bot.send_message(message.from_user.id, "Привет, как тебя зовут?")
    bot.register_next_step_handler(message, send_welcome)
y="да"
n="нет"

def send_welcome(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, "Приятно познакомиться, " + name +"! \n Хочешь пройти тест на профессиональную ориентацию?")
    bot.register_next_step_handler(message, send_otvet)

def send_povtor(message):
    global name;
    

def send_otvet (message):
    global otvet;
    otvet = message.text;
    if otvet.lower()==n:
      keyboard = types.InlineKeyboardMarkup()
      url_button = types.InlineKeyboardButton(text="Официальный сайт ЮРГПУ  (НПИ)", url="http://npi-tu.ru")
      keyboard.add(url_button)
      bot.send_message(message.from_user.id,  "Тогда можешь ознакомиться с сайтом нашего ЮРГПУ (НПИ)!  ", reply_markup=keyboard)
    elif otvet.lower() !=y:
        bot.send_message(message.from_user.id,  "Ответь, пожалуйста <<Да>> или <<Нет>>!")
        bot.send_message(message.from_user.id, name + ", хочешь пройти тестирование?")
        bot.register_next_step_handler(message, send_otvet)
    else:
        bot.send_message(message.from_user.id,  "Тогда начнем! \n Тебе предстоит ответить на 20 вопросов. Отвечать надо однозначно 1 или 2. \n В итоге ты получишь несколько ссылок на наиболее подходящие для тебя профессии! \n Выбирай то, что действительно ближе тебе! \n\n\n Первый вопрос: \n Что ты выберешь?\n 1. Ухаживать за животными \n 2. Обслуживать какие-нибудь приборы, следить за ними, регулировать их")
        bot.register_next_step_handler(message, send_2v)



def send_2v (message):
    global otv, p, t;
    otv = message.text;
    if otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "1. Помогать больным людям, лечить их \n 2. Составлять таблицы, чертить схемы, разрабатывать компьютерные программы")
           bot.register_next_step_handler(message, send_3v)

    elif otv.lower()== dva:
           t+=1
           bot.send_message(message.from_user.id,  "1. Помогать больным людям, лечить их \n 2. Составлять таблицы, чертить схемы, разрабатывать компьютерные программы")
           bot.register_next_step_handler(message, send_3v)

    else: 
            bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
            bot.send_message(message.from_user.id,  "1. Ухаживать за животными \n 2. Обслуживать какие-нибудь приборы, следить за ними, регулировать их")
            bot.register_next_step_handler(message, send_2v)
    
def send_3v (message):
    global otv, c, z;
    otv = message.text;
    if otv.lower()== odin:
           c+=1
           bot.send_message(message.from_user.id,  "1. Рассматривать книжные иллюстрации, художественные открытки, конверты грампластинок \n 2. Следить за состоянием и развитием растений")
           bot.register_next_step_handler(message, send_4v)
    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "1. Рассматривать книжные иллюстрации, художественные открытки, конверты грампластинок \n 2. Следить за состоянием и развитием растений")
           bot.register_next_step_handler(message, send_4v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Помогать больным людям, лечить их \n 2. Составлять таблицы, чертить схемы, разрабатывать компьютерные программы")
           bot.register_next_step_handler(message, send_3v)
    

def send_4v (message):
    global otv, p, h;
    otv = message.text;
    if otv.lower()== odin:
           h+=1
           bot.send_message(message.from_user.id,  "1. Обрабатывать материалы (дерево, ткань, пластмассу, металл и т.п.) \n 2. Доводить товары до потребителя (рекламировать, продавать).")
           bot.register_next_step_handler(message, send_5v)
    elif otv.lower()== dva:
           p+=1
           bot.send_message(message.from_user.id,  "1. Обрабатывать материалы (дерево, ткань, пластмассу, металл и т.п.) \n 2. Доводить товары до потребителя (рекламировать, продавать).")
           bot.register_next_step_handler(message, send_5v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Рассматривать книжные иллюстрации, художественные открытки, конверты грампластинок \n 2. Следить за состоянием и развитием растений")
          bot.register_next_step_handler(message, send_4v) 
    
    
def send_5v (message):
    global otv, c, t;
    otv = message.text;
    if otv.lower()== odin:
           t+=1
           bot.send_message(message.from_user.id,  "1. Обсуждать научно-популярные книги, статьи \n 2. Обсуждать художественные книги (или пьесы, концерты)")
           bot.register_next_step_handler(message, send_6v)
    elif otv.lower()== dva:
           c+=1
           bot.send_message(message.from_user.id,  "1. Обсуждать научно-популярные книги, статьи \n 2. Обсуждать художественные книги (или пьесы, концерты)")
           bot.register_next_step_handler(message, send_6v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Обрабатывать материалы (дерево, ткань, пластмассу, металл и т.п.) \n 2. Доводить товары до потребителя (рекламировать, продавать).")
           bot.register_next_step_handler(message, send_5v)
          

 
def send_6v (message):
    global otv, z, h;
    otv = message.text;
    if otv.lower()== odin:
           z+=1
           bot.send_message(message.from_user.id,  "1. Выращивать молодняк (животных какой-либо породы) \n 2. Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).")
           bot.register_next_step_handler(message, send_7v)
    elif otv.lower()== dva:
           h+=1
           bot.send_message(message.from_user.id,  "1. Выращивать молодняк (животных какой-либо породы) \n 2. Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).")
           bot.register_next_step_handler(message, send_7v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Обсуждать научно-популярные книги, статьи \n 2. Обсуждать художественные книги (или пьесы, концерты)")
           bot.register_next_step_handler(message, send_6v)

 
def send_7v (message):
    global otv, p, c;
    otv = message.text;
    if otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "1. Копировать рисунки, изображения (или настраивать музыкальные инструменты). \n 2. Управлять каким-либо грузовым (подъемным или транспортным) средством: подъемным краном, трактором, тепловозом и др.)")
           bot.register_next_step_handler(message, send_8v)
    elif otv.lower()== dva:
           c+=1
           bot.send_message(message.from_user.id,  "1. Копировать рисунки, изображения (или настраивать музыкальные инструменты). \n 2. Управлять каким-либо грузовым (подъемным или транспортным) средством: подъемным краном, трактором, тепловозом и др.)")
           bot.register_next_step_handler(message, send_8v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Выращивать молодняк (животных какой-либо породы) \n 2. Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).")
           bot.register_next_step_handler(message, send_7v)



def send_8v (message):
    global otv, h, t;
    otv = message.text;
    if otv.lower()== odin:
           h+=1
           bot.send_message(message.from_user.id,  "1. Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.) \n 2. Художественно оформлять выставки, витрины (или участвовать в подготовке пьес, концертов)")
           bot.register_next_step_handler(message, send_9v)
    elif otv.lower()== dva:
           t+=1
           bot.send_message(message.from_user.id,  "1. Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.) \n 2. Художественно оформлять выставки, витрины (или участвовать в подготовке пьес, концертов)")
           bot.register_next_step_handler(message, send_9v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Копировать рисунки, изображения (или настраивать музыкальные инструменты). \n 2. Управлять каким-либо грузовым (подъемным или транспортным) средством: подъемным краном, трактором, тепловозом и др.)")
           bot.register_next_step_handler(message, send_8v)



def send_9v (message):
    global otv, c, h;
    otv = message.text;
    if otv.lower()== odin:
           c+=1
           bot.send_message(message.from_user.id,  "1. Ремонтировать вещи, изделия (одежду, технику), жилище \n 2. Искать и исправлять ошибки в текстах, таблицах, рисунках")
           bot.register_next_step_handler(message, send_10v)
    elif otv.lower()== dva:
           h+=1
           bot.send_message(message.from_user.id,  "1. Ремонтировать вещи, изделия (одежду, технику), жилище \n 2. Искать и исправлять ошибки в текстах, таблицах, рисунках")
           bot.register_next_step_handler(message, send_10v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.) \n 2. Художественно оформлять выставки, витрины (или участвовать в подготовке пьес, концертов).")
           bot.register_next_step_handler(message, send_9v)


def send_10v (message):
    global otv, t, z;
    otv = message.text;
    if otv.lower()== odin:
           t+=1
           bot.send_message(message.from_user.id,  "1. Лечить животных \n 2. Выполнять вычисления, расчеты.")
           bot.register_next_step_handler(message, send_11v)
    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "1. Лечить животных \n 2. Выполнять вычисления, расчеты.")
           bot.register_next_step_handler(message, send_11v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Ремонтировать вещи, изделия (одежду, технику), жилище \n 2. Искать и исправлять ошибки в текстах, таблицах, рисунках.")
           bot.register_next_step_handler(message, send_10v)
    


def send_11v (message):
    global otv, p, z;
    otv = message.text;
    if otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "1. Выводить новые сорта растений \n 2. Конструировать, проектировать новые виды промышленных изделии (машины или одежду, дома, продукты питания и т.п.)")
           bot.register_next_step_handler(message, send_12v)
    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "1. Выводить новые сорта растений \n 2. Конструировать, проектировать новые виды промышленных изделии (машины или одежду, дома, продукты питания и т.п.)")
           bot.register_next_step_handler(message, send_12v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Лечить животных \n 2. Выполнять вычисления, расчеты.")
           bot.register_next_step_handler(message, send_11v)
    



def send_12v (message):
    global otv, p, t;
    otv = message.text;
    if otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "1. Разбирать споры, ссоры между людьми, убеждать, разъяснять поощрять, наказывать. \n 2. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).")
           bot.register_next_step_handler(message, send_13v)
    elif otv.lower()== dva:
           t+=1
           bot.send_message(message.from_user.id,  "1. Разбирать споры, ссоры между людьми, убеждать, разъяснять поощрять, наказывать. \n 2. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).")
           bot.register_next_step_handler(message, send_13v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Выводить новые сорта растений \n 2. Конструировать, проектировать новые виды промышленных изделии (машины или одежду, дома, продукты питания и т.п.)")
           bot.register_next_step_handler(message, send_12v)
    


def send_13v (message):
    global otv, c, z;
    otv = message.text;
    if otv.lower()== odin:
           c+=1
           bot.send_message(message.from_user.id,  "1. Наблюдать, изучать работу кружков художественной самодеятельности \n 2. Наблюдать, изучать жизнь микробов.")
           bot.register_next_step_handler(message, send_14v)
    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "1. Наблюдать, изучать работу кружков художественной самодеятельности \n 2. Наблюдать, изучать жизнь микробов.")
           bot.register_next_step_handler(message, send_14v)
    else: 
           bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
           bot.send_message(message.from_user.id,  "1. Разбирать споры, ссоры между людьми, убеждать, разъяснять поощрять, наказывать. \n 2. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).")
           bot.register_next_step_handler(message, send_13v)



def send_14v (message):
    global otv, h, p;
    otv = message.text;
    if otv.lower()== odin:
           h+=1
           bot.send_message(message.from_user.id,  "1. Обсуждать, налаживать медицинские приборы, аппараты \n 2. Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.")
           bot.register_next_step_handler(message, send_15v)
    elif otv.lower()== dva:
           p+=1
           bot.send_message(message.from_user.id,  "1. Обсуждать, налаживать медицинские приборы, аппараты \n 2. Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.")
           bot.register_next_step_handler(message, send_15v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Наблюдать, изучать работу кружков художественной самодеятельности \n 2. Наблюдать, изучать жизнь микробов.")
          bot.register_next_step_handler(message, send_14v)
    



def send_15v (message):
    global otv, t, c;
    otv = message.text;
    if otv.lower()== odin:
           t+=1
           bot.send_message(message.from_user.id,  "1. Составлять точные описания - отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др. \n 2. Художественно описывать, изображать события (наблюдаемые или представляемые)")
           bot.register_next_step_handler(message, send_16v)
    elif otv.lower()== dva:
           c+=1
           bot.send_message(message.from_user.id,  "1. Составлять точные описания - отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др. \n 2. Художественно описывать, изображать события (наблюдаемые или представляемые)")
           bot.register_next_step_handler(message, send_16v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Обсуждать, налаживать медицинские приборы, аппараты \n 2. Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.")
          bot.register_next_step_handler(message, send_15v)
    



def send_16v (message):
    global otv, z, h;
    otv = message.text;
    if otv.lower()== odin:
           z+=1
           bot.send_message(message.from_user.id,  "1. Делать лабораторные анализы в больнице \n 2. Принимать, осматривать больных, беседовать с ними, назначать лечение.")
           bot.register_next_step_handler(message, send_17v)
    elif otv.lower()== dva:
           h+=1
           bot.send_message(message.from_user.id,  "1. Делать лабораторные анализы в больнице \n 2. Принимать, осматривать больных, беседовать с ними, назначать лечение.")
           bot.register_next_step_handler(message, send_17v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Составлять точные описания - отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др. \n 2. Художественно описывать, изображать события (наблюдаемые или представляемые)")
          bot.register_next_step_handler(message, send_16v)



def send_17v (message):
    global otv, p, c;
    otv = message.text;
    if otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "1. Красить или расписывать стены помещений, поверхность изделий. \n 2. Осуществлять монтаж зданий или сборку машин, приборов.")
           bot.register_next_step_handler(message, send_18v)
    elif otv.lower()== dva:
           c+=1
           bot.send_message(message.from_user.id,  "1. Красить или расписывать стены помещений, поверхность изделий. \n 2. Осуществлять монтаж зданий или сборку машин, приборов.")
           bot.register_next_step_handler(message, send_18v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Делать лабораторные анализы в больнице \n 2. Принимать, осматривать больных, беседовать с ними, назначать лечение.")
          bot.register_next_step_handler(message, send_17v)



def send_18v (message):
    global otv, h, t;
    otv = message.text;
    if otv.lower()== odin:
           h+=1
           bot.send_message(message.from_user.id,  "1. Организовывать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п. \n 2. Играть на сцене, принимать участие в концертах")
           bot.register_next_step_handler(message, send_19v)
    elif otv.lower()== dva:
           t+=1
           bot.send_message(message.from_user.id,  "1. Организовывать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п. \n 2. Играть на сцене, принимать участие в концертах")
           bot.register_next_step_handler(message, send_19v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Красить или расписывать стены помещений, поверхность изделий. \n 2. Осуществлять монтаж зданий или сборку машин, приборов.")
          bot.register_next_step_handler(message, send_18v)



def send_19v (message):
    global otv, c, h;
    otv = message.text;
    if otv.lower()== odin:
           c+=1
           bot.send_message(message.from_user.id,  "1. Изготовлять по чертежам детали, изделия (машины, одежду) строить здания \n 2. Заниматься черчением, копированием чертежей, карт")
           bot.register_next_step_handler(message, send_20v)
    elif otv.lower()== dva:
           h+=1
           bot.send_message(message.from_user.id,  "1. Изготовлять по чертежам детали, изделия (машины, одежду) строить здания \n 2. Заниматься черчением, копированием чертежей, карт")
           bot.register_next_step_handler(message, send_20v)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Организовывать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п. \n 2. Играть на сцене, принимать участие в концертах")
          bot.register_next_step_handler(message, send_19v)



def send_20v (message):
    global otv, t, z;
    otv = message.text;
    if otv.lower()== odin:
           t+=1
           bot.send_message(message.from_user.id,  "1. Вести борьбу с болезнями растений, с вредителями леса, сада. \n 2. Работать на компьютере")
           bot.register_next_step_handler(message, send_result)
    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "1. Вести борьбу с болезнями растений, с вредителями леса, сада. \n 2. Работать на компьютере")
           bot.register_next_step_handler(message, send_result)
    else: 
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Изготовлять по чертежам детали, изделия (машины, одежду) строить здания \n 2. Заниматься черчением, копированием чертежей, карт")
          bot.register_next_step_handler(message, send_20v)
    




def send_result (message):
    global otv, h, p, c, z, t;
    otv = message.text;
    if otv!= odin and otv != dva:
          bot.send_message(message.from_user.id,  "Необходимо отвечать <<1>> или <<2>> (цифрами)!")
          bot.send_message(message.from_user.id,  "1. Вести борьбу с болезнями растений, с вредителями леса, сада. \n 2. Работать на компьютере")
          bot.register_next_step_handler(message, send_result)
    elif otv.lower()== odin:
           p+=1
           bot.send_message(message.from_user.id,  "А вот и результаты: \n Человек природа: "+str(p)+"\n Человек техника: "+str(t)+"\n Человек человек: "+str(c)+"\n Человек знаковая система: "+str(z)+"\n Человек художественный образ: "+str(h))
           if h>=p and h>=t and h>=c and h>=z:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Строительный Факультет ЮРГПУ (НПИ)", url="http://sf.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif p>=t and p>=c and p>=z and p>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Факультет геологии, горного и нефтегазового дела  ЮРГПУ (НПИ)", url="http://fggngd.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif t>=p and t>=c and t>=z and t>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button_1 = types.InlineKeyboardButton(text="Факультет информационных технологий и управления ЮРГПУ (НПИ)", url="http://fitu.npi-tu.ru")
                keyboard.add(url_button_1)
                url_button_2 = types.InlineKeyboardButton(text="Механический факультет ЮРГПУ (НПИ)", url="http://mf.npi-tu.ru")
                keyboard.add(url_button_2)
                url_button_3 = types.InlineKeyboardButton(text="Энергетический факультет ЮРГПУ (НПИ)", url="http://enf.npi-tu.ru")
                keyboard.add(url_button_3)
                url_button_4 = types.InlineKeyboardButton(text="Факультет транспорта и логистики ЮРГПУ (НПИ)", url="http://ftil.npi-tu.ru")
                keyboard.add(url_button_4)
                bot.send_message(message.from_user.id,  "Попробуйте найти подходящую специальность: ", reply_markup=keyboard)
           elif c>=p and c>=t and c>=z and c>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Факультет инноватики и организации производства ЮРГПУ (НПИ)", url="http://fiop.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif z>=p and z>=t and z>=c and z>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Институт фундаментального инженерного образования ЮРГПУ (НПИ)", url="http://ifio.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           p=0
           t=0
           c=0
           z=0
           h=0 
    

    elif otv.lower()== dva:
           z+=1
           bot.send_message(message.from_user.id,  "А вот и результаты: \n Человек природа: "+str(p)+"\n Человек техника: "+str(t)+"\n Человек человек: "+str(c)+"\n Человек знаковая система: "+str(z)+"\n Человек художественный образ: "+str(h))
           if h>=p and h>=t and h>=c and h>=z:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Строительный Факультет ЮРГПУ (НПИ)", url="http://sf.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif p>=t and p>=c and p>=z and p>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Факультет геологии, горного и нефтегазового дела  ЮРГПУ (НПИ)", url="http://fggngd.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif t>=p and t>=c and t>=z and t>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button_1 = types.InlineKeyboardButton(text="Факультет информационных технологий и управления ЮРГПУ (НПИ)", url="http://fitu.npi-tu.ru")
                keyboard.add(url_button_1)
                url_button_2 = types.InlineKeyboardButton(text="Механический факультет ЮРГПУ (НПИ)", url="http://mf.npi-tu.ru")
                keyboard.add(url_button_2)
                url_button_3 = types.InlineKeyboardButton(text="Энергетический факультет ЮРГПУ (НПИ)", url="http://enf.npi-tu.ru")
                keyboard.add(url_button_3)
                url_button_4 = types.InlineKeyboardButton(text="Факультет транспорта и логистики ЮРГПУ (НПИ)", url="http://ftil.npi-tu.ru")
                keyboard.add(url_button_4)
                bot.send_message(message.from_user.id,  "Попробуйте найти подходящую специальность: ", reply_markup=keyboard)
           elif c>=p and c>=t and c>=z and c>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Факультет инноватики и организации производства ЮРГПУ (НПИ)", url="http://fiop.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           elif z>=p and z>=t and z>=c and z>=h:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Институт фундаментального инженерного образования ЮРГПУ (НПИ)", url="http://ifio.npi-tu.ru")
                keyboard.add(url_button)
                bot.send_message(message.from_user.id,  "Обратите внимание на специальности: ", reply_markup=keyboard)
           p=0
           t=0
           c=0
           z=0
           h=0 
    


bot.polling ( none_stop=True )
