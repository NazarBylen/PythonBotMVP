import telebot
from telebot import types

bot = telebot.TeleBot('5154827184:AAHEAaB2nCy0mqJY-FfxzSe1K4c4F3QDIJc')


@bot.message_handler(commands=['start'])
def start(message):
    markup2 = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id,
                     f'<b>hello, {message.from_user.first_name}, type /help to see a command list</b>\u2728',
                     parse_mode='html', reply_markup=markup2)


@bot.message_handler(commands=['credits'])
def credits(message):
    bot.send_message(message.chat.id, f'<b><u>credits</u>\u2705 : \n'
                                      f'Ігор Патько\n'
                                      f'Стас Денисенко\n'
                                      f'Орест Боршовський\n'
                                      f'Назар Билень\n'
                                      f'Максим Мороченець\n'
                                      f'Ігор Бира</b>', parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     f'<b>commands : \n/universities (main bot function)\n/credits (project authors)\n/topUniversities(top 5 universities in your city)</b>',
                     parse_mode='html')


@bot.message_handler(commands=['topUniversities'])
def topUniversities(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn0 = types.KeyboardButton('Lviv')
    btn01 = types.KeyboardButton('Kyiv')
    btn02 = types.KeyboardButton('Ivano-Frankivsk')
    btn03 = types.KeyboardButton('Kharkiv')
    btn04 = types.KeyboardButton('Dnipro')
    btn05 = types.KeyboardButton('Lutsk')
    btn00 = types.KeyboardButton('go back')
    markup.add(btn0, btn01, btn02, btn03, btn04, btn05, btn00)
    bot.send_message(message.chat.id, f'<b>here, you can choose city</b>', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['universities'])
def universities(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('LNU')
    btn2 = types.KeyboardButton('LPNU')
    btn3 = types.KeyboardButton('LTEU')
    btn31 = types.KeyboardButton('UBS')
    btn3999 = types.KeyboardButton('go back')
    markup.add(btn1, btn2, btn3, btn31, btn3999)
    bot.send_message(message.chat.id, f'<b>here, you can choose</b>', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message = message.text.strip().lower()
    if get_message == 'lpnu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('MathLpnu')
        btn2 = types.KeyboardButton('Ukrainian languageLpnu')
        btn3 = types.KeyboardButton('Foreign languagesLpnu')
        btn4 = types.KeyboardButton('PhysicsLpnu')
        btn5 = types.KeyboardButton('HistoryLpnu')
        btn6 = types.KeyboardButton('LiteratureLpnu')
        btn7 = types.KeyboardButton('back')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, f'<b>choose one, you want to study</b>', parse_mode='html',
                         reply_markup=markup)

    elif get_message == 'lnu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn8 = types.KeyboardButton('MathLnu')
        btn9 = types.KeyboardButton('Ukrainian languageLnu')
        btn10 = types.KeyboardButton('Foreign languagesLnu')
        btn11 = types.KeyboardButton('PhysicsLnu')
        btn12 = types.KeyboardButton('HistoryLnu')
        btn13 = types.KeyboardButton('LiteratureLnu')
        btn14 = types.KeyboardButton('back')

        markup.add(btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        bot.send_message(message.chat.id, f'<b>choose one, you want to study</b>', parse_mode='html',
                         reply_markup=markup)

    elif get_message == 'lteu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn15 = types.KeyboardButton('MathLteu')
        btn16 = types.KeyboardButton('Foreign languagesLteu')
        btn17 = types.KeyboardButton('back')

        markup.add(btn15, btn16, btn17)
        bot.send_message(message.chat.id, f'<b>choose one, you want to study</b>', parse_mode='html',
                         reply_markup=markup)

    elif get_message == 'ubs':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn18 = types.KeyboardButton('MathUbs')
        btn19 = types.KeyboardButton('HistoryUbs')
        btn20 = types.KeyboardButton('back')

        markup.add(btn18, btn19, btn20)
        bot.send_message(message.chat.id, f'<b>choose one, you want to study</b>', parse_mode='html',
                         reply_markup=markup)

    elif get_message == 'mathlnu':
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/cydersecurity/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/informatics/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/applied-mathematics/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/informatics-education/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/system-analisys/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/business-economics/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/business-economics/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/marketing/</b>',
                         parse_mode='html')

    elif get_message == 'ukrainian languagelnu':
        bot.send_message(message.chat.id,
                         '<b>https://philology.lnu.edu.ua/academics/bachelor/curriculum-ukrajinska-mova-ta-literatura</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://philology.lnu.edu.ua/department/ukrajinskoji-movy</b>',
                         parse_mode='html')

    elif get_message == 'foreign languageslnu':
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/english-translation/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/german-language/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/english-language/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/translation/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/classic-philology/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/spanish-language/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/french-language/</b>',
                         parse_mode='html')

    elif get_message == 'physicslnu':
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/computer-technologies/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/physics-education/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/quantum-computing/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/computer-physics/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>https://admission.lnu.edu.ua/specialization/physics-and-astrophysics/</b>',
                         parse_mode='html')

    elif get_message == 'historylnu':
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/history-and-archaeology/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/history-education/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/sociology/</b>',
                         parse_mode='html')

    elif get_message == 'literaturelnu':
        bot.send_message(message.chat.id,
                         '<b>https://admission.lnu.edu.ua/specialization/ukrainian-language-education/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/folklore-studies/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://admission.lnu.edu.ua/specialization/ukrainian-language/</b>',
                         parse_mode='html')

    elif get_message == 'mathlpnu':
        bot.send_message(message.chat.id,
                         '<b>http://edu.lp.edu.ua/napryamy/803050401-ekonomika-pidpryiemstva-za-vydamy-ekonomichnoi-diialnosti</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://edu.lp.edu.ua/napryamy/805010302-inzheneriia-prohramnoho-zabezpechennia</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://edu.lp.edu.ua/napryamy/803050301-mizhnarodna-ekonomika</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://edu.lp.edu.ua/napryamy/818010024-prykladna-ekonomika</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://edu.lp.edu.ua/napryamy/818010024-prykladna-ekonomika</b>',
                         parse_mode='html')

    elif get_message == 'ukrainian languagelpnu':
        bot.send_message(message.chat.id,
                         '<b>https://old.lpnu.ua/education/majors/ICSIT/6.035.10.10/8/2019/ua/part</b>',
                         parse_mode='html')

    elif get_message == 'foreign languageslpnu':
        bot.send_message(message.chat.id, '<b>https://lpnu.ua/im</b>', parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>https://old.lpnu.ua/education/majors/ICSIT/6.035.10.10/8/2019/ua/part</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://old.lpnu.ua/education/majors/IHSS/6.291.01/8/2017/ua/part</b>',
                         parse_mode='html')

    elif get_message == 'physicslpnu':
        bot.send_message(message.chat.id,
                         '<b>http://edu.lp.edu.ua/napryamy/805080102-fizychna-ta-biomedychna-elektronika</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://edu.lp.edu.ua/napryamy/8090701-radiotekhnika</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://edu.lp.edu.ua/napryamy/805020201-avtomatyzovane-upravlinnia-tekhnolohichnymy-protsesamy</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://edu.lp.edu.ua/napryamy/805010104-systemy-shtuchnoho-intelektu</b>',
                         parse_mode='html')

    elif get_message == 'historylpnu':
        bot.send_message(message.chat.id, '<b>https://old.lpnu.ua/education/majors/IHSS/6.291.01/8/2017/ua/part</b>',
                         parse_mode='html')

    elif get_message == 'literaturelpnu':
        bot.send_message(message.chat.id,
                         '<b>https://old.lpnu.ua/education/majors/ICSIT/6.035.10.10/8/2019/ua/part</b>',
                         parse_mode='html')

    elif get_message == 'mathlteu':
        bot.send_message(message.chat.id, '<b>http://www.lute.lviv.ua/admissions/gss/sp/051/</b>', parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/075/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/122/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/072/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/071/</b>',
                         parse_mode='html')

    elif get_message == 'mathubs':
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/ekonomika/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/oblik-i-opodatkuvannya/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/finansy/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/kiberbezpeka/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/menedzhment/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/menedzhment/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/inzheneriya/</b>',
                         parse_mode='html')

    elif get_message == 'historyubs':
        bot.send_message(message.chat.id,
                         '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/sotsialne-zabezpechennya/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>https://ubs.edu.ua/abituriyentu/spetsyalnosti/pravo/</b>',
                         parse_mode='html')

    elif get_message == 'foreign languageslteu':
        bot.send_message(message.chat.id, '<b>http://www.lute.lviv.ua/admissions/gss/specialnosti/292/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/122/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         '<b>http://www.lute.lviv.ua/admissions/galuzi-napryamy-spec/specialnosti/061/</b>',
                         parse_mode='html')
        bot.send_message(message.chat.id, '<b>http://www.lute.lviv.ua/admissions/gss/specialnosti/242/</b>',
                         parse_mode='html')

    elif get_message == 'lviv':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://lnu.edu.ua/en/">Львівський національний університет імені Івана Франка</a>\n'
                         '\u27052.<a href="https://lpnu.ua/">Національний університет "Львівська політехніка</a>"\n'
                         '\u27053.<a href="https://new.meduniv.lviv.ua/">Львівський національний медичний університет імені Данила Галицького</a>\n'
                         '\u27054.<a href="https://ucu.edu.ua/ua/">Український католицький університет</a>\n'
                         '\u27055.<a href="https://ubs.edu.ua/">Університет банківської справи</a></b>',
                         parse_mode='html')

    elif get_message == 'kyiv':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://www.univ.kiev.ua/">Київський національний університет імені Тараса Шевченка</a>\n'
                         '\u27052.<a href="https://kpi.ua/">КПІ імені Ігоря Сікорського</a>"\n'
                         '\u27053.<a href="https://knute.edu.ua/">Київський національний торговельно-економічний університет</a>\n'
                         '\u27054.<a href="https://nau.edu.ua/">Національний авіаційний університет</a>\n'
                         '\u27055.<a href="https://kneu.edu.ua/">Київський національний економічний університет імені Вадима Гетьмана</a></b>',
                         parse_mode='html')

    elif get_message == 'ivano-frankivsk':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://pnu.edu.ua/en/">Прикарпатський національний університет імені Василя Стефаника</a>\n'
                         '\u27052.<a href="https://www.ifnmu.edu.ua/uk/">Івано-Франківський національний медичний університет</a>"\n'
                         '\u27053.<a href="https://nung.edu.ua/">Івано-Франківський національний технічний університет нафти і газу</a>\n'
                         '\u27054.<a href="http://www.ifaiz.edu.ua/">Івано-Франківська академія Івана Золотоустого</a>\n'
                         '\u27055.<a href="https://ukd.edu.ua/">Університет Короля Данила</a></b>', parse_mode='html')

    elif get_message == 'kharkiv':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://www.univer.kharkov.ua/en">Харківський національний університет імені В.Н. Каразіна</a>\n'
                         '\u27052.<a href="https://nure.ua/">Харківський національний університет радіоелектроніки</a>"\n'
                         '\u27053.<a href="https://knmu.edu.ua/">Харківський національний медичний університет</a>\n'
                         '\u27054.<a href="https://www.kpi.kharkov.ua/ukr/ntu-hpi/">Національний технічний університет "Харківський політехнічний інститут"</a>\n'
                         '\u27055.<a href="https://nuph.edu.ua/">Національний фармацевтичний університет</a></b>',
                         parse_mode='html')

    elif get_message == 'dnipro':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://www.dnu.dp.ua/">Дніпровський національний університет імені Олеся Гончара</a>\n'
                         '\u27052.<a href="https://dmu.edu.ua/ua/">Дніпровський державний медичний університет</a>"\n'
                         '\u27053.<a href="https://www.nmu.org.ua/ua/">Національний технічний університет "Дніпровська політехніка"</a>\n'
                         '\u27054.<a href="https://udhtu.edu.ua/">Український державний хіміко-технологічний університет"</a>\n'
                         '\u27055.<a href="https://pgasa.dp.ua/">Придніпровська державна академія будівництва та архітектури</a></b>',
                         parse_mode='html')

    elif get_message == 'lutsk':
        bot.send_message(message.chat.id,
                         '<b>\u27051.<a href="https://vnu.edu.ua/uk">Волинський національний університет імені Лесі Українки</a>\n'
                         '\u27052.<a href="https://lntu.edu.ua/uk">луцький національний технічний університет</a>"\n'
                         '\u27053.<a href="http://www.vpba.edu.ua/">Волинська Православна Богословська Академія"</a>\n'
                         '\u27054.<a href="https://artip.com.ua/">Академія рекреаційних технологій і права"</a>\n'
                         '\u27055.<a href="https://op.ua/vnz/shidno-vropeyskiy-nacionalniy-universitet-imeni-lesi-ukrayinki">Східноєвропейський національний університет ім. Л. Українки</a></b>',
                         parse_mode='html')

    elif get_message == 'back':
        universities(message)

    elif get_message == 'go back':
        start(message)

    else:
        bot.send_message(message.chat.id, '<b>error</b>', parse_mode='html')


bot.polling(none_stop=True, timeout=123)