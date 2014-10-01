label lb_location_road_main:
    $ place = 'road'
    show place
    show expression get_place_bg(place) as bg
    nvl clear
    $ nochance = game.poverty.value*10      
    $ choices = [("lb_enc_tornament", 10),
                ("lb_enc_fortification", 10),
                ("lb_enc_inn", 10),
                ("lb_enc_peasant_cart", 10),
                ("lb_enc_carriage", 10000),   
                ("lb_enc_qesting_knight", 10000),
                ("lb_enc_trader", 10),
                ("lb_enc_caravan", 10),
                ("lb_enc_lcaravan", 10),
                ("lb_enc_outpost", 10),
                ("lb_enc_noting", nochance),]
    $ enc = core.Game.weighted_random(choices)
    $ renpy.call(enc)
        
    return
    
    
label lb_enc_tornament:
    'Шум вдалеке...'
    show expression 'img/bg/special/tornament.png' as bg
    '...это рыцарский турнир. Победитель готов возложить золотой венец на "королеву любви и красоты".'
    nvl clear
    menu:
        'Вызвать победителя на бой':
            $ game.dragon.drain_energy()
            $ game.foe = core.Enemy('champion', gameRef=game, base_character=NVLCharacter)
            call lb_fight
            'Увидев что их чемпион повержен, гости турнира в панике разбегаются бросая вещи и вопя от ужаса. [dragon.name] не обращает на них внимания, он забирает свой приз - "королеву любви и красоты" и её золотой венец.'
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex      
        'Не ввязываться' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            'Осторожность не повредит. Если этот рыцарь действительно лучше в округе, он может быть опасен. А девицу и кусок золота можно найти где-нибудь ещё...'
    return
    
label lb_enc_inn:
    show expression 'img/bg/special/tabern.png' as bg    
    'Придорожный трактир.'
    nvl clear
    python:
        doit = False
        if 'fire_breath' in game.dragon.modifiers(): 
            doit = True
    menu:
        'Дыхнуть огнём' if doit:
            $ game.dragon.drain_energy()
            "Трактир сгорает вместе с забаррикадировавшимися внутри людьми."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
        'Наколдовать синее пламя' if game.dragon.magic() > 0:
            $ game.dragon.drain_energy()
            "Трактир сгорает синим пламенем вместе с забаррикадировавшимися внутри людьми."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
        'Потребовать бочку эля':
            show expression 'img/bg/special/fear.png' as bg  
            $ game.dragon.drain_energy()
            "[dragon.name] получает от испуганного хозяина трактира целую бочку лучшего эля. После такой выпивки так и тянет на приключения и хорошую закуску!"
            python:
                if bloodlust < 5: dragon.bloodiness += 1
                if dragon.lust < 3: draon.lust += 1
                if dragon.hunger < 3: draon.hunger += 1
        'Пройти мимо' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enc_peasant_cart:
    'Телега с сеном.'
    menu:
        'Убить крестьянина' if dragon.bloodiness >= 5:
            $ game.dragon.drain_energy()
            'Дав волю своему гневу, [dragon.name] переворачивает повозку, убивает лошадь и разрывает крестьянина на куски. У жалкого смертного нет ничего ценного! Да как он посмел встретить дракона если с него и взять нечего?!'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Сожрать лошадь' if game.dragon.hunger > 0: 
            $ game.dragon.drain_energy()
            'Пока [dragon.name] пожирает жилистую крестьянскую лошадку, хозяин повозки в ужасе убегает прочь. Ничего, пусть поведает жалким смертным о вашем величии.'
            $ if game.dragon.bloodiness > 0: game.dragon.bloodiness = 0
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Пропустить' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_carriage:
    'Карета благородной дамы с несколькими тяжело-вооруженными конными арбалетчиками в качестве охраны.'
    nvl clear
    menu:
        'Перевернуть карету':
            $ game.foe = core.Enemy('mounted_guard', gameRef=game, base_character=NVLCharacter)
            call lb_fight
            'Внутри благородная дева.'
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex      
        
        'Пропустить' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
    return
    
label lb_enc_qesting_knight:
    'Странствующий рыцарь.'
    menu:
        'Вызвать на бой':
            $ game.dragon.drain_energy()
            $ game.foe = core.Enemy('champion', gameRef=game, base_character=NVLCharacter)
            call lb_fight
            $ game.dragon.reputation.points += 5
            'Рыцарь повержен. [game.dragon.reputation.gain_description]'
            '[dragon.name] находит на трупе кое-что ценное:'
            python:
                count = random.randint(1,5)
                alignment = 'knight'
                min_cost = 10
                max_cost = 100
                t_list = knight_list
                obtained = "Это предмет принадлежал когда-то беззвестному странствующему рыцарю."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
        'Пропустить' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()   
            
    return
    
label lb_enc_trader:
    'Фургон странствующего торговца.'
    menu:
        'Вымогать деньги':
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Coin('taller', 10)
                game.lair.treasury.recieve_treasures([gold_trs])
            'Торговец с облегчением отдаёт дракону десять серебрянных таллеров, чтобы тот его не трогал и пропустил фургон.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Убить и ограбить' if dragon.bloodiness >= 5:
            python:
                game.dragon.drain_energy()
                gold_trs = [treasures.Coin('farting', 100), treasures.Coin('taller', 10)]
                game.lair.treasury.recieve_treasures([gold_trs])
            'Дав волю своему гневу, [dragon.name] переворачивает фургон, убивает лошадь и разрывает торговца на куски. Его товары особого интереса не представляют, зато в кошельке находятся кое какие деньги:'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Пропустить' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enc_caravan:
    'Торговый караван под охраной взвода наемных конных арбалетчиков.'
    menu:
        'Вымогать деньги':
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Coin('dublon', 10)
                game.lair.treasury.recieve_treasures([gold_trs])
            'Караванщик с ворчанием отдаёт дракону десять золотых дублонов, чтобы тот не трогал повозки и пропустил из дальше.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Разграбить корован' if dragon.bloodiness >= 5:
            $ game.dragon.drain_energy()
            $ game.foe = core.Enemy('champion', gameRef=game, base_character=NVLCharacter)
            call lb_fight
            python:
                gold_trs = [treasures.Coin('taller', 100), treasures.Coin('farting', 10)]
                game.lair.treasury.recieve_treasures([gold_trs])
            'Дав волю своему гневу, [dragon.name] переворачивает фургон, убивает лошадь и разрывает караванщика на куски. Его товары особого интереса не представляют, зато в кошельке находятся кое какие деньги:'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Пропустить' if dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
   
label lb_enc_lcaravan:
    'Большой караван. Плейсхолдер.'
    return
    
label lb_enc_outpost:
    'Застава на дороге. Плейсхолдер.'
    return
    
label lb_enc_fortification:
    'Найден замок. Плейсходлдер'
    return