# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def course_selection(request):
    return render(request, 'myapp/course_selection.html')

# MAX курс
def max_course(request):
    context = {
        'page_title': 'Курс MAX',
        'course_text': 'MAX — это универсальный маркетплейс от «Альфа-Банка», который объединяет в одном приложении покупки товаров из тысяч интернет-магазинов, выгодные кешбэк-предложения от популярных брендов, возможность оформления рассрочки и кредитов, а также управление финансами — всё это с максимальным возвратом средств за покупки и персональными условиями для каждого пользователя, что делает его многофункциональной платформой для умного шопинга и финансового контроля.',
        'course_image': 'myapp/images/max_main.png',
        'next_page': 'max_course_2',
    }
    return render(request, 'myapp/course_template.html', context)

def max_course_2(request):
    context = {
        'page_title': 'MAX - Урок 2',
        'images': [
            {'path': 'myapp/images/maxtut1.png'},
            {'path': 'myapp/images/maxtut2.png'},
        ],
        'course_text': 'Прежде чем начать общение в MAX, нужно добавить человека. Для этого нужно в меню снизу перейти во вкладку "контакты", а дальше нажать на плюсик. Ну а дальше у нас появляется два варианта: найти по номеру или добавить контантю Сейчас во всем разберемся! ',
        'back_page': 'max_course',
        'next_page': 'max_course_3',
    }
    return render(request, 'myapp/course_with_images.html', context)

def max_course_3(request):
    context = {
        'page_title': 'MAX - Урок 3',
        'images': [
            {'path': 'myapp/images/maxtut4.png'},
        ],
        'course_text': '"Найти по номеру" используется в тех случаях, когда вам нужно всего один раз написаить человеку и вы не планируете с ним дальнейшее общение',
        'back_page': 'max_course_2',
        'next_page': 'max_course_4',
    }
    return render(request, 'myapp/course_with_images.html', context)

def max_course_4(request):
    context = {
        'page_title': 'MAX - Урок 4',
        'images': [
            {'path': 'myapp/images/maxtut5.png'},
        ],
        'course_text': 'А вот "добавить контакт" нужен чтоб сохранить номерв списке конактов, чтоб после юыло легче его найти. Вы также можете записать информацию об контакте, чтобы вам было легче его определить',
        'back_page': 'max_course_3',
        'next_page': 'max_course_5',
    }
    return render(request, 'myapp/course_with_images.html', context)

# MAX курс - 5-я страница (3 картинки)
def max_course_5(request):
    return render(request, 'myapp/max_course_5.html')

# MAX курс - 6-я страница (1 картинка)
def max_course_6(request):
    context = {
        'page_title': 'MAX - Урок 6',
        'images': [
            {'path': 'myapp/images/maxtut9.png'},
        ],
        'course_text': 'теперь, когда мы добавили контакта, самое время начать беседу! Сначала нужно перейти во вкладку "чаты" и выбрать своего собеседника',
        'back_page': 'max_course_5',
        'next_page': 'max_course_7',
    }
    return render(request, 'myapp/course_with_images.html', context)

# MAX курс - 7-я страница (1 картинка)
def max_course_7(request):
    context = {
        'page_title': 'MAX - Урок 7',
        'images': [
            {'path': 'myapp/images/maxtut10.png'},
            {'path': 'myapp/images/maxtut11.png'},
            {'path': 'myapp/images/maxtut12.png'},
        ],
        'course_text': 'Так как MAX -  месенджер, то в нем полно различных функций. от обычных сообщений, до звоноков и видео звонков! Так же вы можете отправлять аудио и видео сообщения(для этого нужно зажать значок микрофона и камеры соответсвенно) . Вам не обязательно набирать сообщения каждый раз, ведь  MAX предлогает вам стикеры!Стикеры это картина с текстом, способная передать ваши эмоции и чувства. В прмложении стикеров много: от милых котиков до наших отважных и мужественных солдат!  А нажав на значок скрепки вы сможете отправить фотографии, видео, файлы или даже деньги! Но это уже совсем другая история...',
        'back_page': 'max_course_6',
        'next_page': 'max_course_8',
    }
    return render(request, 'myapp/course_with_images.html', context)

# MAX курс - 8-я страница (4 картинки)
def max_course_8(request):
    context = {
        'page_title': 'MAX - Урок 8',
        'images': [
            {'path': 'myapp/images/maxtut13.png'},
            {'path': 'myapp/images/maxtut14.png'},
            {'path': 'myapp/images/maxtut15.png'},
            {'path': 'myapp/images/maxtut16.png'},
        ],
        'course_text': 'Также в  MAX есть каналы, где вы сможете найти новостные каналы, развлекательные и т.п. . Чтобы найти их, во все той же вкладке  “чаты” нужо нажать на лупу. Вы можете либо ввести в поиск название нужного вам канала, либо нажать на “каналы” и найти  в списке канал, на интересующую вас тему! А когда найдете такой не забудте подписаться, чтобы не пропустить все новое и интересное!!',
        'back_page': 'max_course_7',
        'next_page': 'max_course_9',
    }
    return render(request, 'myapp/course_with_images.html', context)

# MAX курс - 9-я страница (финальная с поздравлением)
def max_course_9(request):
    return render(request, 'myapp/max_course_final.html')


# БАНК курс (оставляем как есть)
def bank_course(request):
    return render(request, 'myapp/bank_course.html')

def bank_course_2(request):
    return render(request, 'myapp/bank_course_2.html')

def bank_course_3(request):
    return render(request, 'myapp/bank_course_3.html')

def bank_course_4(request):
    return render(request, 'myapp/bank_course_4.html')

def bank_course_5(request):
    return render(request, 'myapp/bank_course_5.html')

def bank_course_6(request):
    return render(request, 'myapp/bank_course_6.html')

def bank_course_7(request):
    return render(request, 'myapp/bank_course_7.html')

def bank_course_8(request):
    return render(request, 'myapp/bank_course_8.html')

def bank_course_9(request):
    return render(request, 'myapp/bank_course_9.html')

def bank_course_10(request):
    return render(request, 'myapp/bank_course_10.html')

# ART курс
def apt_course(request):
    context = {
        'page_title': 'Курс ART',
        'course_text': '«Еаптека» — это крупный онлайн-сервис-агрегатор, объединяющий товары сотен аптек-партнеров в едином каталоге, что позволяет пользователям быстро находить и бронировать необходимые лекарства, витамины и медицинские изделия, сравнивать цены в реальном времени для максимальной экономии, а также заказывать доставку на дом или самостоятельно забирать заказ из ближайшей удобной аптеки, значительно упрощая и ускоряя процесс покупки товаров для здоровья.',
        'course_image': 'myapp/images/art_main.png',
        'next_page': 'apt_course_2',
    }
    return render(request, 'myapp/course_template.html', context)

def apt_course_2(request):
    context = {
        'page_title': 'ART - Урок 2',
        'images': [
            {'path': 'myapp/images/arttut1.png'},
            {'path': 'myapp/images/arttut2.png'},
            {'path': 'myapp/images/arttut3.png'},
            {'path': 'myapp/images/arttut4.png'},
        ],
        'course_text': 'В ПРИЛОЖЕНИИ ЕСТЬ ОЧЕНЬ УДОБНЫЙ ПОИСК ТОВАРОВ:ВЫ МОЖЕТЕ НАЙТИ НУЖНОЕ ЛЕКАРСТВО НЕ ТОЛЬКО ПО НАЗВАНИЮ, НО И ПО СИМПТОМАМ, ОТ КОТОРЫХ СОЗДАНО ЛЕКАРСТВО!А ЕСЛИ ВЫ ИЩЕТЕ ЛЕКАРСТВО ПО СИМПТОМАМ, ТО В ПРИЛОЖЕНИИ ЕСТЬ ФИЛЬТРАЦИЯ:МОЖНО ОТСОРТИРОВАТЬ ТОВАРЫ, ОСТАВИВ ТОЛЬКО ТЕ ЧТО ПОДХОДЯТ! В ПРИЛОЖЕНИИ ПРЕДЛОЖЕННО МНОГО РАЗНЫХ СВОЙСТВ, ПО КОТОРЫМ БУДЕТ ПРОХОДИТЬ ФИЛЬТРАЦИЯ',
        'back_page': 'apt_course',
        'next_page': 'apt_course_3',
    }
    return render(request, 'myapp/course_with_images.html', context)

def apt_course_3(request):
    context = {
        'page_title': 'ART - Урок 3',
        'images': [
            {'path': 'myapp/images/arttut5.png'},
            {'path': 'myapp/images/arttut6.png'},
        ],
        'course_text': 'КАКТОЛЬКО ВЫ НАЙДЕТЕ ТО, ЧТО ИСКАЛИ, НАЖМИТЕ НА ТОВАР. ВЫ ПЕРЕШЛИ В КАРТОЧКУ ТОВАРА И ТЕПЕРЬ МОЖЕТЕ ПОСМОТРЕТЬ БОЛЕЕ ПОДРОБНУЮ ИНФОРМАЦИЮ О НЕМ И ДАЖЕ ОТЗЫВЫ ОТ ДРУГИХ ПОКУПАТЕЛЕЙ. А ЕСЛИ НАЖАТЬ НА СЕРДЕЧКО ОКОЛО "ДОБАВИТЬ В КОРЗИНУ" ТО ВЫ СМОЖЕТЕТЕ ДОБАВИТЬ ЛЕКАРСТВО В ИЗБРАННОЕ. ДОБАВИВ ЧТО-ТО В ИЗБРАННОЕ ВАМ НЕ НУЖНО БУДЕТ ИСКАТЬ ПРЕДМЕТ ЗАНОВО. БУДЕТ ДОСТАТОЧНО ПЕРЕЙТИ ВО ВКЛАДКУ "ИЗБРАННОЕ" В НИЖНЕМ МЕНЮ. КОГДА ДОБАВИТЕ ВСЕ ТОВАРЫ В КОРЗИНУ ВАМ НУЖНО БУДЕТ ПЕРЕЙТИ ВО ВКЛАДКУ"КОРЗИНА" ВО ВСЕ ТОМ ЖЕ НИЖНЕМ МЕНЮ',
        'back_page': 'apt_course_2',
        'next_page': 'apt_course_4',
    }
    return render(request, 'myapp/course_with_images.html', context)

def apt_course_4(request):
    context = {
        'page_title': 'ART - Урок 4',
        'images': [
            {'path': 'myapp/images/arttut7.png'},
            {'path': 'myapp/images/arttut8.png'},
        ],
        'course_text': 'МОЖНО ЗАРАНИЕ СОБРАТЬ ВСЕ ПОКУПКИ И ПРОСТО СРАЗУ ЗАБРАТЬ ИХ В УКАЗАННОЙ АПТЕКЕ, А МОЖНО ВЫБРАТЬ ДОСТАВКУ НА ДОМ. НО ЕСЛИ ЛЕКАРСТО СОДЕРЖИТ СПИРТ ИЛИ ПОКУПАЕТСЯ ТОЛЬКО ПРИ НАЛИЧИИ РЕЦЕПТА, ПРИДЕТЬСЯ ЗАБРАТЬ В АПТЕКЕ',
        'back_page': 'apt_course_3',
        'next_page': 'apt_course_5',
    }
    return render(request, 'myapp/course_with_images.html', context)

def apt_course_5(request):
    context = {
        'page_title': 'ART - Урок 5',
        'images': [
            {'path': 'myapp/images/arttut10.png'},
            {'path': 'myapp/images/arttut11.png'},
            {'path': 'myapp/images/arttut12.png'},
        ],
        'course_text': 'ПРИ ЗАКАЗЕ МОЖНО ВЫБРАТЬ МНОЖЕСТВО НЬАНСОВ ДОСТАВКИ, НАПИСАТЬ КОМЕНТАРИЙ К ЗАКАЗУ И УКАЗТЬ АДРЕС ДОСТАВКИ . ЕСЛИ ВЫ ПРОХОШЛИ КУРС ПО СБЕРБАНКУ, ТО ЗНАЕТЕ ЧТО ЗАКАЗ МОЖНО БУДЕТ ОПЛАТИТЬ БАЛЛАМИ',
        'back_page': 'apt_course_4',
        'next_page': 'apt_course_6',
    }
    return render(request, 'myapp/course_with_images.html', context)

# ART курс - 6-я страница (заглушка)
def apt_course_6(request):
    return render(request, 'myapp/apt_course_6.html')

# PAT курс
def pat_course(request):
    context = {
        'page_title': 'Курс PAT',
        'course_text': '«Пятерочка» — это удобное мобильное приложение от известной продуктовой сети, которое позволяет пользователям экономить время и деньги: составлять списки покупок, заранее просматривать акции и цены в ближайшем магазине, копить и моментально активировать бонусы по карте «Выручайка», а также оплачивать покупки смартфоном через QR-код на кассе. Дополнительный плюс — регулярные персональные предложения и возможность участия в интересных конкурсах прямо из приложения.',
        'course_image': 'myapp/images/pat_main.png',
        'next_page': 'pat_course_2',
    }
    return render(request, 'myapp/course_template.html', context)

def pat_course_2(request):
    context = {
        'page_title': 'PAT - Урок 2',
        'images': [
            {'path': 'myapp/images/pattut1.png'},
            {'path': 'myapp/images/pattut2.png'},
            {'path': 'myapp/images/pattut3.png'},
            {'path': 'myapp/images/pattut4.png'},
            {'path': 'myapp/images/pattut5.png'},
        ],
        'course_text': 'В приложении пятерочки все устроено прям как в магазине! ведь все товары разбиты по разделам: завтраки, обеды, горячие напитки, фрукты, выпечка и много много много другого! Прежде всего вам нужно перейти во вкладку "каталог", которая находится в нижнем меню. Не смотря на удобное разделение по разделам, в приложении все еще можно найи товар по названию. А теперь давайте попробуем заказать газировку, найдя раздел с ней',
        'back_page': 'pat_course',
        'next_page': 'pat_course_3',
    }
    return render(request, 'myapp/course_with_images.html', context)

def pat_course_3(request):
    context = {
        'page_title': 'PAT - Урок 3',
        'images': [
            {'path': 'myapp/images/pattut6.png'},
            {'path': 'myapp/images/pattut7.png'},
            {'path': 'myapp/images/pattut8.png'},
        ],
        'course_text': 'Найдя нужый вам товар, вам нужно будет нажать на кнопку "В корзину". Корзина здесь т же самое, как и в магазине. Вы также можете добавить товар в избранное, нажав на сердечко в правом верхнем углу иконки товара. КАК ТОЛЬКО ВЫ ВЫБЕРИТЕ ВСЕ НУЖНЫЕ ТОВАРЫ И ДОБАВИТЕ ИХ В КОРЗИНУ ВАМ СЛЕДУЕТ НАЖАТЬ НА КРАСНУЮ КНОПКУ С КОРЗИНКОЙ, ЧТОБЫ ПЕРЕЙТИ К ФИНАЛЬНОЙ ПРОВЕРКЕ ЗАКАЗА И ОПЛАТЫ',
        'back_page': 'pat_course_2',
        'next_page': 'pat_course_4',
    }
    return render(request, 'myapp/course_with_images.html', context)

def pat_course_4(request):
    context = {
        'page_title': 'PAT - Урок 4',
        'images': [
            {'path': 'myapp/images/pattut9.png'},
            {'path': 'myapp/images/pattut10.png'},
            {'path': 'myapp/images/pattut11.png'},
        ],
        'course_text': 'КОГДА ВЫ ВЫБРАЛИ ВСЕ НУЖНЫЕ ВАМ ПРОДУКТЫ ВАМ ОСТАЕТСЯ ЛИШЬ ОПЛАТИТЬ И ПРОВЕРИТЬ ЗАКАЗ. ВЫ МОЖЕТЕ ИЗМЕНИТЬ КОЛИЧЕСТВО НУЖНОГО КОЛИЧЕСТВА ПРОДУКТА НААЖАВ НА ПЛЮСИК, А МОЖЕТЕ И ВОВСЕ УБРАТЬ ЕГО ИЗ СПИСКА, НАЖАВ НА КОПКУ С МУСОРКОЙ. СВЕРХУ, НАЖАВА НА СТРЕЛКУ, ОКОЛО АДРЕСА, ВЫ СМОЖЕТЕ УКАЗАТЬ АДРЕСС ДОСТАВКИ. МОЖНО ОТМЕТИТЬ МЕСТО НА КАРТЕ, А МОЖНО НАПИСАТЬ ТОЧНЫЙ АДРЕС',
        'back_page': 'pat_course_3',
        'next_page': 'pat_course_5',
    }
    return render(request, 'myapp/course_with_images.html', context)

def pat_course_5(request):
    context = {
        'page_title': 'PAT - Урок 5',
        'images': [
            {'path': 'myapp/images/pattut12.png'},
            {'path': 'myapp/images/pattut13.png'},
            {'path': 'myapp/images/pattut14.png'},
        ],
        'course_text': 'НО ЗАКАЗАТЬ 1 ГАЗИРОВКУ БЫЛО БЫ НЕ ПРАВИЛЬНО, ВЕДЬ ВМЕСТО 1 ГАЗИРОВКИ, КУРЬЕР МОГ БЫ ОТВЕЗТИ ВСЕ НЕОХОДИМЫЕ ПРОДУКТЫ ТЕМ, КОМУ РЕАЛЬНО ТРУДНО САМОМУ СХОДИТЬ В МАГАЗИН И ДОНЕСТИ ВСЕ ПОКУПКИ ДО ДОМА . ПОЭТОМУ В ПРИЛОЖЕНИИ УКАЗАННО, ЧТО ЗАКАЗ ДОСТАВЯТ, ТОЛЬКО ЕСЛИ ЕГО ЦЕНА БОЛЬШЕ ЛИБО РАВНА 500Р ',
        'back_page': 'pat_course_4',
        'next_page': 'pat_course_6',
    }
    return render(request, 'myapp/course_with_images.html', context)

def pat_course_6(request):
    context = {
        'page_title': 'PAT - Урок 6',
        'images': [
            {'path': 'myapp/images/pattut15.png'},
            {'path': 'myapp/images/pattut16.png'},
        ],
        'course_text': 'ТАКЖЕ ЕСТЬ ВОЗМОЖНОСТЬ ЗАМЕНИТЬ ЗАКАЗ, ЕСЛИ ЕГО НЕТУ В МАГАЗИНЕ И ДОБАВИТЬ ПОЖЕЛАНИЕ К ЗАКАЗУ. ОБЫЧНО В ЗАКАЗЕ ПИШУТ В КАКОМ ПОДЬЕЗДЕ, В КАКУЮ КВАРТРУ , НА КАКОЙ ЭТАЖ НАДО ДОСТАВИТЬ ЗАКАЗ. НО МОЖНО УКАЗАТЬ НЕКОТОРЫЕ ОСОБЕННОСТИ, ПО КОТОРЫМ НУЖНО ВЫБРАТЬ ПРОДУКТ. КАК ПРИМЕР ВЫ МОЖЕТЕ ПОПРОСИТЬ КИНДЕР СЮРПРИЗ С ОПРДЕЛЕННОЙ КОЛЕКЦИЕЙ ДЛЯ ВАШЕГО ВНУЧКА',
        'back_page': 'pat_course_5',
        'next_page': 'pat_course_final',
    }
    return render(request, 'myapp/course_with_images.html', context)

# PAT курс - финальная страница с поздравлением
def pat_course_final(request):
    return render(request, 'myapp/pat_course_final.html')