# coding=utf-8
# имена девушек генерируются из списков имен (тип девушки_first) и фамилий (тип девушки_last). Если списка фамилий
# нет - генерируется только из списка имен.
girls_names = {
    'peasant_first': [
        u'Jhoann', u'Herda', u'Babetta', u'Susie', u'Alba', u'Amely', u'Anneth', u'Jorgette', u'Betty',
        u'Beatsy', u'Blanka', u'Bjanka', u'Daisy', u'Ginny', u'Judie', u'Dorothu', u'Zoe', u'Iren', u'Ivete',
        u'Kolette', u'Krissie', u'Kitty', u'Kait', u'Lilli', u'Lydie', u'Lulu'
    ],
    'citizen_first': [
        u'Adelia', u'Aurora', u'Alberthine', u'Angela', u'Aurelia', u'Beatrice', u'Bernadett',
        u'Brgitte', u'Veronique', u'Violett', u'Virginia', u'Gabriella', u'Janneth', u'Julian', u'Dominika',
        u'Jackline', u'Josefine', u'Juliette', u'Kamilla', u'Karoline', u'Catelin', u'Iren', u'Melissa', u'Marjori',
        u'Natalie', u'Peneloppe', u'Rosalie', u'Roset', u'Seleste', u'Simone', u'Stephanie', u'Susanne',
        u'Teresa', u'Flora', u'Emmanuele', u'Adalinde', u'Alberthine', u'Amelinde', u'Griselda',
        u'Victoria', u'Irma', u'Caroline', u'Kristiana', u'Caterine', u'Lione', u'Lorely', u'Margarett', u'Franciska',
        u'Henelore', u'Hilda', u'Eleonor', u'Abbigail', u'Antonya', u'Dolores', u'Dorothy',
        u'Jenevieve', u'Josefine', u'Iness', u'Carmelitta', u'Consuella', u'Lethiscia', u'Marcella', u'Priscilla',
        u'Ramone', u'Sofia', u'Ephimia', u'Ephania', u'Lydia', u'Beatrix',
    ],
    'princess_first': [
        u'Annabele', u'Adelia', u'Eveline', u'Icedora', u'Alberthine', u'Anastasia', u'Anthuanette',
        u'Beathrice', u'Valentine', u'Victoria', u'Gabriella', u'Ginnevere', u'Dominika', u'Juliann',
        u'Juliet', u'Justine', u'Josefine', u'Ivonne', u'Isabella', u'Camilla', u'Clarice',
        u'Clementine', u'Cristine', u'Lucrecia', u'Margo', u'Mathelde', u'Millisenth', u'Marianna', u'Olympia',
        u'Peneloppe', u'Rosalinde', u'Rosamunde', u'Celestine', u'Ceraphine', u'Susan', u'Spehanie', u'Teresa',
        u'Flavia', u'Felicia', u'Henriet', u'Gertrude', u'Charlotte', u'Emmanuelle', u'Alberthine', u'Amelinde',
        u'Brunhild', u'Vilhelmina', u'Raphaella', u'Amaranta', u'Delphinia', u'Dorothea',
        u'Mercedes', u'Ophelia',
    ],
    'princess_last': [
        u"d'Musie", u'von Baugraff', u"d'Albere", u"d'Blua", u"d'Virgie", u"d'Guisse", u"d'Brienn",
        u"d'Colinie", u"d'La-Tour", u"d'Luisinyan", u"d'Fua", u"d'Bruisac", u"d'Crua", u"d'Linyom",
        u"d'Qylote", u"d'Sen-Prie", u'von Buttenberg', u'von Bennigs', u'von Valbits', u'von Vittelsbauch',
        u'von Gogenshaufen', u'von Zalts', u'von Ludenshtaff', u'von Mirbach', u'von Rozen', u'von Zeringer',
        u'von Grunnberg', u'von Shturnberg', u'von Shellengaupf', u'Strotzzi', u'Sforza', u'Albizi',
        u'Barbarigo', u'Pazzi', u'Brancattio', u'da Verana', u'Viscontti', u'Grimaldi', u'da Polenta', u'della Tori',
        u'da Camino', u'Montrefelto', u'Manfreddi', u'Farnezze', u'Fregozo', u'da Mendoza', u'la Sarda',
    ],
    'elf_first': [
        u'Breunvehn', u'Fanaveihn', u'Arveihn', u'Luthien', u'Fealinde', u'Esthelindel', u'Astherra', u'Theolinvenn',
        u'Quivinienn', u'Marvainn', u'Inthialvenn', u'Anarven', u'Amaniel', u'Anariel', u'Lariel', u'Lotharinge',
        u'Isilindil', u'Selfariani', u'Yoringel', u'Orosinvell', u'Gilestell', u'Valakirre'
    ],
    'ogre_first': [
        u'Xunn', u'Yorva', u'Dirga', u'Velga', u'Siga', u'Yalghull', u'Dorba', u'Girga', u'Daviri', u'Shalgha',
        u'Orva', u'Dezra', u'Argha', u'Bighra', u'Vargha', u'Enza', u'Zartha', u'Ikla', u'Cordha', u'Loghaza',
        u'Mirbu', u'Nira',
    ],
    'mermaid_first': [
        u'Ariel', u'Blazhena', u'Budimila', u'Vedana', u'Velina', u'Ventseslava', u'Vereya', u'Велезара',
        u'Веселина', u'Витана', u'Влада', u'Весемлиа', u'Годица', u'Горлина', u'Далина', u'Ждана',
        u'Деяна', u'Дивина', u'Доляна', u'Есена', u'Жилена', u'Завида', u'Зоряна', u'Златина', u'Ивица',
        u'Калёна', u'Красоя', u'Купава', u'Лада', u'Леля', u'Малиша', u'Млава', u'Милана', u'Младлена',
        u'Мирана', u'Невена', u'Обрица', u'Пава', u'Пригода', u'Рада', u'Ракита', u'Ружана',
        u'Силимина', u'Серебрина', u'Славена', u'Станимира', u'Стояна', u'Томила', u'Умила', u'Ундина',
        u'Цветана', u'Чаруна', u'Янина', u'Яромила', u'Ясмания'
    ],
    'siren_first': [
        u'Ариэль', u'Блажена', u'Будимила', u'Ведана', u'Велина', u'Венцеслава', u'Верея', u'Велезара',
        u'Веселина', u'Витана', u'Влада', u'Весемлиа', u'Годица', u'Горлина', u'Далина', u'Ждана', u'Деяна',
        u'Дивина', u'Доляна', u'Есена', u'Жилена', u'Завида', u'Зоряна', u'Златина', u'Ивица', u'Калёна',
        u'Красоя', u'Купава', u'Лада', u'Леля', u'Малиша', u'Млава', u'Милана', u'Младлена', u'Мирана',
        u'Невена', u'Обрица', u'Пава', u'Пригода', u'Рада', u'Ракита', u'Ружана', u'Силимина', u'Серебрина',
        u'Славена', u'Станимира', u'Стояна', u'Томила', u'Умила', u'Ундина', u'Цветана', u'Чаруна',
        u'Янина', u'Яромила', u'Ясмания'
    ],
    'ice_first': [
        u'Астрид', u'Бригита', u'Боргильда', u'Вигдис', u'Вилла', u'Гурдун', u'Гунхильд', u'Дорта', u'Ингрид',
        u'Ингеборга', u'Йорнун', u'Матильда', u'Рангильда', u'Руна', u'Сигурд', u'Сванхильда', u'Сигюнд',
        u'Ульрика', u'Фрида', u'Хлодвен', u'Хильда', u'Эрика'
    ],
    'fire_first': [
        u'Азиль', u'Азиза', u'Базайна', u'Багира', u'Будур', u'Бушра', u'Гюльчатай', u'Гуля', u'Гульнара',
        u'Гулистан', u'Фируза', u'Фатима', u'Ясмин', u'Айгюль', u'Зульфия', u'Ламия', u'Лейла', u'Марьям',
        u'Самира', u'Хурма',
        u'Чинара', u'Эльмира'
    ],
    'titan_first': [
        u'Агата', u'Адонисия', u'Алексино', u'Амброзия', u'Антигона', u'Ариадна', u'Артемисия', u'Афродита',
        u'Гликерия', u'Дельфиния', u'Деметра', u'Зиновия', u'Калисто', u'Калипсо', u'Кора', u'Ксения',
        u'Медея', u'Мельпомена', u'Мнемозина', u'Немезида', u'Олимпия', u'Пандора', u'Персефона',
        u'Таисия', u'Персея', u'Персея', u'Психея', u'Сапфо', u'Талия', u'Терпсихора', u'Фаломена',
        u'Гаромония', u'Хрисеида', u'Эфимия', u'Юнона'
    ]
}

# Информация о всех типах девушек
girls_info = {
    'peasant': {
        'magic_rating': 0,  # магический рейтинг
        'regular_spawn': 'poisonous_asp',  # идентификатор обычного отродья
        'advanced_spawn': 'basilisk',  # идентификатор продвинутого отродья
        'giantess': False,  # является ли великаншей
        'avatar': 'peasant',  # аватарка
        'description': u'peasant girl',  # описание для вывода в текст
        't_count_min': 0,  # количество сокровищ минимальное
        't_count_max': 2,  # количество сокровищ максимальное
        't_price_min': 1,  # минимальная цена предмета
        't_price_max': 25,  # максимальная цена предмета
        't_alignment': 'human',  # тип украшений
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'earring', 'necklace',
            'pendant', 'ring', 'broch', 'armbrace', 'legbrace', 'fibula', 'farting'],
        # список возможных предметов в сокровищах
    },
    'citizen': {
        'magic_rating': 0,
        'regular_spawn': 'winged_asp',
        'advanced_spawn': 'kobold',
        'giantess': False,
        'avatar': 'citizen',
        'description': u'citizen',
        't_count_min': 0,
        't_count_max': 4,
        't_price_min': 25,
        't_price_max': 100,
        't_alignment': 'human',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'fibula', 'taller'],
    },
    'thief': {
        'magic_rating': 0,
        'regular_spawn': 'winged_asp',
        'advanced_spawn': 'kobold',
        'giantess': False,
        'avatar': 'thief',
        'description': u'воровка',
        't_count_min': 2,
        't_count_max': 5,
        't_price_min': 25,
        't_price_max': 250,
        't_alignment': 'human',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'fibula', 'taller', 'dublon'],
    },
    'knight': {
        'magic_rating': 1,
        'regular_spawn': 'krokk',
        'advanced_spawn': 'lizardman',
        'giantess': False,
        'avatar': 'knight',
        'description': u'warrior',
        't_count_min': 2,
        't_count_max': 5,
        't_price_min': 25,
        't_price_max': 250,
        't_alignment': 'knight',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'fibula', 'taller', 'dublon'],
    },
    'princess': {
        'magic_rating': 0,
        'regular_spawn': 'krokk',
        'advanced_spawn': 'lizardman',
        'giantess': False,
        'avatar': 'princess',
        'description': u'noble maiden',
        't_count_min': 2,
        't_count_max': 5,
        't_price_min': 100,
        't_price_max': 1000,
        't_alignment': 'knight',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'fibula'],
    },
    'elf': {
        'magic_rating': 1,
        'regular_spawn': 'gargoyle',
        'advanced_spawn': 'dragonborn',
        'giantess': False,
        'avatar': 'elf',
        'description': u'elven maiden',
        't_count_min': 1,
        't_count_max': 4,
        't_price_min': 250,
        't_price_max': 2000,
        't_alignment': 'elf',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain'],
    },
    'mermaid': {
        'magic_rating': 1,
        'regular_spawn': 'octopus',
        'advanced_spawn': 'sea_bastard',
        'giantess': False,
        'avatar': 'mermaid',
        'description': u'mermaid',
        't_count_min': 0,
        't_count_max': 4,
        't_price_min': 10,
        't_price_max': 200,
        't_alignment': 'merman',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain'],
    },
    'ogre': {
        'magic_rating': 2,
        'regular_spawn': 'strigg',
        'advanced_spawn': 'minotaur',
        'giantess': True,
        'avatar': 'ogre',
        'description': u'ogress',
        't_count_min': 0,
        't_count_max': 3,
        't_price_min': 250,
        't_price_max': 1500,
        't_alignment': 'knight',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'fibula', 'farting', 'taller', 'dublon'],
    },
    'siren': {
        'magic_rating': 2,
        'regular_spawn': 'murloc',
        'advanced_spawn': 'naga',
        'giantess': True,
        'avatar': 'mermaid',
        'description': u'siren',
        't_count_min': 1,
        't_count_max': 4,
        't_price_min': 250,
        't_price_max': 2000,
        't_alignment': 'merman',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'taller', 'dublon'],
    },
    'ice': {
        'magic_rating': 2,
        'regular_spawn': 'ice_worm',
        'advanced_spawn': 'yettie',
        'giantess': True,
        'avatar': 'ice',
        'description': u'frost giantess',
        't_count_min': 1,
        't_count_max': 5,
        't_price_min': 250,
        't_price_max': 2500,
        't_alignment': 'human',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'taller', 'dublon'],
    },
    'fire': {
        'magic_rating': 2,
        'regular_spawn': 'hell_hound',
        'advanced_spawn': 'barlog',
        'giantess': True,
        'avatar': 'fire',
        'description': u'fire giantess',
        't_count_min': 1,
        't_count_max': 5,
        't_price_min': 250,
        't_price_max': 2500,
        't_alignment': 'dwarf',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'taller', 'dublon'],
    },
    'titan': {
        'magic_rating': 2,
        'regular_spawn': 'chimera',
        'advanced_spawn': 'troll',
        'giantess': True,
        'avatar': 'titan',
        'description': u'titanid',
        't_count_min': 3,
        't_count_max': 6,
        't_price_min': 500,
        't_price_max': 5000,
        't_alignment': 'elf',
        't_list': [
            'casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'taller', 'dublon'],
    },
}

# Информация о всех типах отродий
spawn_info = {
    'goblin': {
        'power': 1,  # сила
        'modifier': [],  # возможные роли
        'name': u'goblin',  # название
        'born': u'error', # Описание при рождении
    },
    'poisonous_asp': {
        'power': 1,  # сила
        'modifier': ['poisonous'],  # возможные роли
        'name': u'Venomous snake',  # название
        'born': u'Hatched from an egg, this long, soft-bellied poisoned snake is not much different from a bog viper, except that it is larger and more aggressive. But instead of hiding in remote places, these venomous creatures are forever looking for someone to bite, whether men or livestock. Their toxin has no antidote, and the deaths they cause are extremely slow and painful.', # Описание при рождении
    },
    'winged_asp': {
        'power': 2,
        'modifier': ['poisonous'],
        'name': u'Winged snake',
        'born': u'These large poisonous snakes, unlike normal reptiles, are endowed by their dragon\'s blood with wings. It\'s one thing to accidentally step on a viper, and quite another thing to have it drop down on your neck from the sky. The poison of asps leads to a long and painful death, and oh, how they love to bite!', # Описание при рождении
    },
    'krokk': {
        'power': 1,
        'modifier': ['servant'],
        'name': u'Krokk',
        'born': u'Born of a noble lady, these creatures are superior monsters which surpass the progeny of any commoner. However, desite their physical strength and some intelligence, Krokki are not the most suitable guards. They are indolent, always sleeping in the sun or swimming in the mud. However, they can be forced to do housework.', #translator: can't translate very last word. "Впрочем их можно заставить выполнять работу по дому или на строителсьстве." 
    },
    'basilisk': {
        'power': 3,
        'modifier': ['poisonous'],
        'name': u'Basilisk',
        'born': u'These hideous fledglings have a cock\'s comb and snake tails. Although brainless, they are still much more dangerous than a usual poison asp. The basilisk, also known as cocatrice, can poison a person with a mere glance, and can fly short distances.', # Описание при рождении
    },
    'kobold': {
        'power': 2,
        'modifier': ['servant'],
        'name': u'Kobold',
        'born': u'This small, gnarled Kobold is all that a common woman was able to give birth to, even from the seed of a mighty dragon. Nevertheless, these draconic humanoids possess sufficent intelligence to do manual labor. In battle, they are about equal to a goblin, but cower at danger, so it would be foolish to task them with the protection of a lair.', # Описание при рождении
    },
    'lizardman': {
        'power': 3,
        'modifier': ['warrior'],
        'name': u'Lizardman',
        'born': u'THe combination of powerful dragon seed and pure noble blood has produced the best that a mortal woman can spawn. An adult lizardman is much bigger and stronger than the average man, covered with scales, and insensitive to pain. Reptillians are quick, observan and smart enough to become skilled warriors. They also like to hatch plans for secret domination of the world, but they will get in line behind their grandmother - Mistress.', # Описание при рождении
    },
    'dragonborn': {
        'power': 3,
        'modifier': ['elite'],
        'name': u'Dragonborn',
        'born': u'The dragonborn descendant of a Aein Sidhe combines the fury and power of dragon magic with ancient blood of the children of the goddess Danu. His size and strength of mind is beyond the capacity of mortal men, elves, and dwarves. Dragonborn can compete with power of giants and can make excellent treasure guards or elite soldiers in the army of darkness.', # Описание при рождении
    },
    'gargoyle': {
        'power': 4,
        'modifier': ['warrior'],
        'name': u'Gargulie',
        'born': u'The dragon seed did not have the power to fully open up the possibilities of the blood of the children of Danu. Even so, such ugly gargoyles will be useful in the army of darkness or as guards of the lair. Their ability to fly makes them superior to to the usual reptillians, not even considering goblins and men.', # Описание при рождении
    },
    'sea_bastard': {
        'power': 3,
        'modifier': ['poisonous', 'marine'],
        'name': u'Sea Bastard',
        'born': u'Combined with mighty dragon seed, the blood of the sea people gave birth to a terrible parody of a mermaid - a sea bastard. These vicious and ugly creatures are able to live only in salt water, which is all that prevents them from joining the army of darkness that gathers at the hand of the Mistress. But besides, they are too gluttonous, and easily distracted from guard duty to score a school of fish. But still, you can force them to serve in the sea lair.', # Описание при рождении
    },
    'octopus': {
        'power': 5,
        'modifier': ['poisonous', 'marine'],
        'name': u'Venopus',
        'born': u'Similar to a huge purple octopus, these brainless aquatic creatures differ only the the shortness of their temper and the quantity of poison in their suckers. Divers are not in luck.', # Описание при рождении
    },
    'hell_hound': {
        'power': 4,
        'modifier': ['poisonous'],
        'name': u'Hellhound',
        'born': u'The dragon seed suffered badly from the heated uterus of the fiery giantess. From the eggs were born mutated, multi-headed creatures resembling a cross between a dog, lizard, and a gas torch. They are too wild and stupid for army service, but unleashed they will bring terror to the settled lands.', # Описание при рождении
    },
    'minotaur': {
        'power': 5,
        'modifier': ['elite'],
        'name': u'Minotaur',
        'born': u'The insidious seed of the dragon was perfect to unlock the potential for savagery and rage in the blood of the ogress. Horned, hairy, prone to fits of rage, the Minotaur can dispatch a detatchment of heavily armored infantry and rape every woman in a village in a single night. Still, it is smart enough to obey a higher power, so that it makes a good treasury guardian or elite fighter.', # Описание при рождении
    },
    'murloc': {
        'power': 3,
        'modifier': ['warrior', 'marine'],
        'name': u'Murloc',
        'born': u'Weirdly distorted parody of frogs and fish, Murlocs would make good soldiers in the army of darkness if they could live away from water. But all they can do is protect the underwater lair, or terrorize the mermaids', # Описание при рождении
    },
    'naga': {
        'power': 6,
        'modifier': ['elite', 'marine'],
        'name': u'Naga',
        'born': u'The insidiousness of the dragon allowed it to generate from the siren a huge and powerful creature called the Naga. The Naga combines the qualities of man and the sea serpent, but additionally has giant size and incredible strength and vitality. It could become an elite fighter in the army of darkness, if it didn\'t dry out on land. But it will make an excellent guard for the treasury.', # Описание при рождении
    },
    'ice_worm': {
        'power': 7,
        'modifier': ['poisonous'],
        'name': u'Ice Worm',
        'born': u'The seed, too weak for the ice giantess, made degenerate offspring. This worm is hideous, with a cold ice shell and terrifying jaws. Men it will kill without hesitation, but it is too brainless for military service.', # Описание при рождении
    },
    'yettie': {
        'power': 6,
        'modifier': ['elite'],
        'name': u'Yeti',
        'born': u'The union of dragon and ice giantess produced a shaggy, horned giant, more like a monkey than a sapient being. But though he is wild, he is very smart. The Yeti can be an excellent elite soldier in the army of darkness.', # Описание при рождении
    },
    'troll': {
        'power': 8,
        'modifier': ['elite'],
        'name': u'Troll',
        'born': u'Troll - the most powerful of the dragonspawn that can be born without the intervention of the Mistress. Bigger and stronger than titanium, virtually invincible, and smart enough to serve in the army of darkness. It is also fat, green, and loves to be fed.', # Описание при рождении
    },
    'strigg': {
        'power': 6,
        'modifier': ['poisonous'],
        'name': u'Striga',
        'born': u'The birth was a failure. The seed of the dragon was too thin for the ogress, and brainless winged freaks were born. Striga are naturally agressive and even poisonous, but are too dumb to serve in the army.', # Описание при рождении
    },
    'barlog': {
        'power': 6,
        'modifier': ['elite'],
        'name': u'Balrog',
        'born': u'The dragon seed had the ability to merge seamlessly with the firey essence of the giantess. The result was a huge Balrog, not only enormously strong, but with the power to control fire. An elite warrior for the army of darkness.', # Описание при рождении
    },
    'chimera': {
        'power': 10,
        'modifier': ['poisonous'],
        'name': u'Chimera',
        'born': u'Titan blood merged badly with the magical essence of the dragon, creating an ugly predatory chimera. While this many-headed, aggressive and poisonous creature could smash even a giant in direct combat, it does not have even rudimentary intelligence. It is not destined to serve in the army of darkness.', # Описание при рождении
    },
}

girl_events = {
    'escape': 'lb_event_girl_escape',  # событие "побег из заключения"
    'spawn': 'lb_event_girl_spawn',  # событие "рождение отродий"
    'free_spawn': 'lb_event_girl_free_spawn',  # событие "рождение отродий на воле"
    'hunger_death': 'lb_event_girl_hunger_death',  # событие "смерть девушки от голода"
    'kill': 'lb_event_girl_kill',  # событие "беременную девушку убивают на свободе"
}

girls_texts = {
    # Подстановки:
    # %(dragon_name)s = Краткое имя текущего дракона
    # %(dragon_name_full)s = Имя дракона с эпитетом
    # %(dragon_type)s = Тип анатомии дракона (змей, линдвурм и т.п.)
    # %(girl_name)s = имя текущей женщины (однако, игра слов :) )
    # %(girl_title)s = тип женщины (крестьянка, горожанка, леди, русалка, эльфийска дева и т.п.)
    # %(spawn_name)s - тип отродий для описаний рождения (начинается с заглавной буквы)
    # %(rob_list)s - список украденного
    'girl': {  # используется, если нет подходящего текста или отсутствует нужный тип девушки
        'shout': (  # Реакция девушки, прямой речью
            u"Ой, а мне текст не написали (((",
        ),
        'prelude': (  # Описание прелюдий
            u"Одним неуловимым движением %(dragon_name)s подобрался вплотную к женщине и сбил её с "
            u"ног, а затем начал рвать зубами её одежду словно остервенелый пёс. %(girl_name)s "
            u"отчаянно отбивалась и кричала, но толку от этого было не много, изодранная одежда "
            u"разлетелась клочками оставляя её полностью обнаженной и беззащитной перед охваченным "
            u"похотью ящером.",
        ),
        'sex': (  # Описание секса с девушкой
            u"Отчаянно пытаясь спасти свою невинность, %(girl_title)s закрылась руками но %(dragon_type)s "
            u"предпринял обходной манёвр. Широко разинув свою зубастую пасть он обхватил голову девушки "
            u"челюстями, так что всё её лицо оказалось внутри, лишаясь доступа к воздуху. Девушка широко "
            u"открыла рот пытаясь вдохнуть хоть немного кислорода, но вместо этого в её глотку проник "
            u"длинный раздвоенный язык ящера. Теперь все когда все силы девушки были направлены на то "
            u"чтобы оторвать смрадную пасть от своего лица она и думать забыла о невинности. Скребя "
            u"ногтями по твёрдой чешуе дракона и дрыгая ногами %(girl_name)s внезапно почувствовала как "
            u"снизу в неё проникает что-то большое и твёрдое. Покрытый слизью рептилоидный член с "
            u"лёгкостью прорвал тонкую плёнку защищавшую вход в тугое молодое влагалище, безжалостно "
            u"растягивая и продавливая всё на своём пути. Почти теряя сознание от боли и недостатка "
            u"воздуха, %(girl_name)s внезапно почувствовала что челюсти насильника размыкаются, вновь "
            u"позволяя ей вдохнуть. %(dragon_name)s хотел насладиться её воплями и плачем.",
        ),
        'impregnate': (  # Оплодотворение
            u"Сдавленная в безжалостных объятьях ящера, %(girl_title)s почувствовала как он "
            u"ускоряет темп своих движений. Боль стала практически невыносимой но крик девушки "
            u"потерялся, перекрытый рёвом наслаждения насильника. Конвульсивно содрагаясь всем "
            u"телом %(dragon_type)s вливал в истерзанное лоно девушки целые литры липкого и "
            u"густого семени, заставляя её маленький животик раздуться изнутри. Когда "
            u"%(dragon_name)s наконец отстранился от своей жертвы из неё вытек целый водопад "
            u"семени, но тем не менее количества оставшегося внутри было более чем достаточно "
            u"чтобы гарантировать надёжное оплодотворение. Дело было сделано надёжно.",
        ),
        'new': (  # Описание новой девушки
            u"%(girl_name)s - %(girl_title)s.",
        ),
        'free': (  # Описание процесса выпускания на свободу
            u"She may go now, whith your offspring in her belly. If she will survive...",
        ),
        'free_prison': (  # Описание процесса выпускания на свободу из тюрьмы
            u"Незачем держать её взаперти, охранять ещё... пусть катится на все четыре стороны.",
        ),
        'steal': (  # Описание процесса воровства девушки
            u"%(dragon_name)s относит пленницу в своё логово...",
        ),
        'jail': (  # Описание процесса заточения в темницу
            u"...и сажает её под замок.",
        ),
        'jailed': (  # Описание процесса возврата в темницу
            u"%(dragon_name)s возвращает девушку в темницу.",
        ),
        'eat': (  # Описание процесса поедания девушки. Как же ему не стыдно, червяку подколодному.
            u"Ты меня съешь?",
        ),
        'rob': (  # Описание процесса ограбления девушки.
            u"%(dragon_name)s грабит девушку и получает: \n %(rob_list)s.",
        ),
        'traps': (  # Описание процесса побега и гибели в ловушке.
            u"%(girl_name)s убегает из темницы и гибнет в ловушках.",
        ),
        'escape': (  # Описание успешного побега
            u"%(girl_name)s спасается бегством",
        ),
        'spawn_common': (  # Описание родов
            u"%(girl_name)s откладывает яйца из которых под наблюдением слуг вылупятся новые отродья. \n %(spawn_name)s.",
        ),
        'spawn_elite': (  # Описание родов
            u"%(girl_name)s в мучениях откладывает огромное яйцо с толстой чешуйчатой скорлупой. \n %(spawn_name)s.",
        ),
        'anguish': (  # Описание смерти от тоски
            u"%(girl_name)s умирает в тоске.",
        ),
        'hunger_death': (  # Описание смерти от голода
            u"%(girl_name)s умирает от голода.",
        ),
        'kill': (  # Описание смерти от селян
            u"Someone, discovers that %(girl_name)s is impregnated by a dragon. The angry mob kills her ruthlesly...",
        ),
        'free_spawn': (  # Описание родов на свободе
            u"%(girl_name)s в тайне от людей откладывает яйца из которых вылупляются кровожадные монстры... Теперь они будут резвиться на воле, терроризируя округу и возможно сожрут собственную мать.",
        ),
        'prison': (  # Проведываем девушку в тюрьме
            u"%(girl_name)s находится в заключении.",
        ),
    },
    'peasant': {  # используется для крестьянок
        'new': (  # описание крестьянки
            u"Сельская девица по имени %(girl_name)s.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Ой, божечки!..", 
            u"Ай мамочка!..", 
            u"Ты куда языком своим слюнявым тычешь змеюка поганая?!",
            u"Ой-ой-ой, только не ешь меня пожалуйста...", 
            u"Ай. Нет-нет-нет, только не туда... ох...",
            u"Драконьчик, миленький, я всё сделаю тебе, только не кушай меня пожалуйста!",
            u"Ты что собрался делать этим елдаком, бесстыдник?! Да он не влезет же, ящерица смердячая! Ааааааааай...",
            u"Ай, что ты делаешь?! Больно... нет, пожалуйста... такой то здоровенный... уууй больно же!!!",
            u"Ишь что удумал, чудище. Пусти... ай, падла... пусти говорят тебе.",
            u"Неужто правду бабы говорят что драконы девок портат? Ой, не рычи. Понялая я, поняла. Не кусайся только.", 
            u"Что, люба я тебе змей? Ишь елдаком махает как пастух погонялом!",
            u"Ох пресвятая дева, срамота то какая...",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
            u"Ой, ну не надо драконьчик, меня же маменька убьёт если узнает что я от тебя понесла. Может я ручками тебя там поглажу?",
        ),
        'eat': (  # Описание процесса поедания девушки.
            u"Ой, божечки!..", 
            u"Ай мамочка!..", 
            u"Неееееет!...",
            u"Аааааааа!....",
            u"Ой не рычи так, мне страшно...",
            u"Ну и зубищи у тебя... ай нет-нет-нет...",
            u"Oh shi~",
            u"Не жри меня,... пожалуйста, я всё сделаю, только не жри!",
            u"Спаси-ите! Лю-юди!",
            u"Сожрать меня вздумал, уродина?! Чтобы ты подавился!",
            u"Я описилась...",
            u"Ой какой взгляд у тебя голодный...",
            u"Нет. Фу. Брысь. Ай не кусай меня.",
            u"Пошел вон скотина! А ну ка брысь-кому говорят. Облизывается он, ишь ты!",
            u"(сдавленно хрипит)",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
        ),
        
    },
    'citizen': {  # используется для горожанок
        'new': (  # описание крестьянки
            u"%(girl_name)s, дочь богача.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"О, Господи!..", 
            u"Проклятая гадина!", 
            u"Не смей! Мой отец тебя на шашлык за такое пустит, змеюка!",
            u"Прошу вас, господин дракон, не надо. Отпустите меня, умоляю...", 
            u"Ай. Нет-нет-нет, только не туда... ох...",
            u"Только не надо зубов, я всё сделаю. Умоляю. Я же знаю чего вы хотите.",
            u"Ой нет, убеерите эту... это... от меня. Стыд то какой!",
            u"Ай, что вы делаете?! Больно... нет, умоляю... он же огромный... уууй больно же!!!",
            u"Ты что задумал, отродье Ехидны?! Пусти... ай, тварь... пусти говорят тебе.",
            u"Я слышала что драконы делают с девушками... Нет. пожалуйста не надо рычать. Я понимаю. Нет, не рвите я сниму... вот снимаю...", 
            u"Ох, Господи, я такого срама даже у коня в деревне не видала! Жуть то какая...",
            u"Ох пресвятая дева, спаси и сохрани...",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
            u"Зачем вы сдираете с меня платье? Нет, я не могу. У меня же жених... Это свершенно не... ааааАХ!",
        ),
        'eat': (  # Описание процесса поедания девушки.
            u"(молится) Отец наш небесный, да святится имя твоё, да пребудет воля твоя...", 
            u"(молится) Если я пойду и долиною смертной тени, не убоюсь зла, потому что Ты со мной...", 
            u"Неееееет!...",
            u"Аааааааа!....",
            u"(кашляет от исходящего изо рта дракона смрада)",
            u"Ну и зубищи у вас... ай нет-нет-нет...",
            u"Oh shi~",
            u"Не кушайте меня,... умоляю, я всё сделаю, только не ешьте!",
            u"Спаси-ите! Помогите! Кто-ниб... аааа....",
            u"Сожрать меня вздумал, уродина?! Чтобы ты подавился!",
            u"Нет, пожалуйста... я куплю вам целое стадо свиней... зачем меня то??",
            u"Ох этот алчный взгляд...",
            u"Нет. Фу. Брысь. Плохой дракон! Сидеть! Кому сказала сидеть!!!.",
            u"Пошел вон скотина! А ну ка брысь-кому говорят. Облизывается он, ишь ты!",
            u"(сдавленно хрипит)",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
        ),
        
    },
    'princess': {  # используется для благородных дам
        'new': (  # описание 
            u"%(girl_name)s, дама благородных кровей.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"О, Господи!..", 
            u"Не тронь меня бесовское исчадие!", 
            u"Не смей! Мой отец тебя на шашлык за такое пустит, змеюка!",
            u"Некоторые сичтают драконов благородными животными. Может вы будете так добры и перестанете распускать свои лапы и язык?", 
            u"Ай. Нет-нет-нет, только не туда... ох...",
            u"Только не надо зубов, я всё сделаю. Умоляю. Я же знаю чего вы хотите.",
            u"Ой нет, убеерите эту... это... от меня. Стыд то какой!",
            u"Ай, что вы делаете?! Больно... нет, умоляю... он же огромный... уууй больно же!!!",
            u"Ты что задумал, отродье Ехидны?! Пусти... ай, тварь... пусти говорят тебе.",
            u"Я слышала что драконы делают с девушками... Нет. пожалуйста не надо рычать. Я понимаю. Нет, не рвите я сниму... вот снимаю...", 
            u"Ох, Господи, я такого срама даже у коня в деревне не видала! Жуть то какая...",
            u"Ох пресвятая дева, спаси и сохрани...",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
            u"Зачем вы сдираете с меня платье? Нет, я не могу. У меня же жених... Это свершенно не... ааааАХ!",
        ),
        'eat': (  # Описание процесса поедания девушки.
            u"(молится) Pater noster, qui es in caelis, sanctificetur nomen tuum. Adveniat regnum tuum. Fiat voluntas tua,..", 
            u"(молится) Nam etsi ambulavero in medio umbrae mortis, non timebo mala, quoniam tu mecum es. Virga tua, et baculus tuus,..", 
            u"Неееееет!...",
            u"Аааааааа!....",
            u"(кашляет от исходящего изо рта дракона смрада)",
            u"Ну и зубищи у вас... ай нет-нет-нет...",
            u"Oh shi~",
            u"Не кушайте меня,... умоляю, я всё сделаю, только не ешьте!",
            u"Спаси-ите! Помогите! Кто-ниб... аааа....",
            u"Сожрать меня вздумал, уродина?! Чтобы ты подавился!",
            u"Нет, пожалуйста... я куплю вам целое стадо свиней... зачем меня то??",
            u"Ох этот алчный взгляд...",
            u"Нет. Фу. Брысь. Плохой дракон! Сидеть! Кому сказала сидеть?!!.",
            u"Пошел вон скотина! А ну ка брысь-кому говорят. Облизывается он, ишь ты!",
            u"(сдавленно хрипит)",
            u"(тихонько плачет и закрывает лицо руками)",
            u"(яростно отбивается и пыхтит сквозь сжатые зубы)",
        ),
    },
    'elf': {  # используется для лесных дев
        'new': (  # описание девы
            u"%(girl_name)s, прекрасная лесная дева из народа альвов, детей богини Дану.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"О, Дану!..", 
            u"Не тронь меня исчадие скверны!", 
            u"Не смей! Духи леса отомсят за мою поргуанную честь!",
            u"Уебери от меня эту... этот... Такой союз противен природе!", 
            u"Чем я заслужила такое унижение?!",
            u"Ты можешь взять моё тело, но моей душой тебе не завладеть!",
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Неееееет!...",
            u"Аааааааа!....",
            u"Если хочешь чтобы я просила пощады - не надейся!",
            u"(кашляет от исходящего изо рта дракона смрада)",
        ),
    },        
    'mermaid': {  # используется для русалок
        'new': (  # описание русалки
            u"%(girl_name)s, экзотическая морская дева.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"О, Дагон!..", 
            u"Не тронь меня сухопутная ящерица!", 
            u"Не смей! Духи вод отомсят за мою поргуанную честь!",
            u"Что это за хрень у тебя между ног?! Щупальце???", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Неееееет!...",
            u"Аааааааа!....",
        ),
    },        
    'siren': {  # используется для сирен
        'new': (  # описание
            u"%(girl_name)s, экзотическая морская великанша.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"О, Дагон!..", 
            u"Не тронь меня сухопутная ящерица!", 
            u"Не смей! Духи вод отомсят за мою поргуанную честь!",
            u"Что это за хрень у тебя между ног?! Щупальце???", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Неееееет!...",
            u"Аааааааа!....",
        ),
    },        
    'ogre': {  # людоедка
        'new': (  # описание
            u"%(girl_name)s, глупая и диковатая людоедка.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Твоя меня не выебать! Моя сама выебать твоя!!! АРррргх! Смерть через СНУ-СНУ!", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Большая ящерица кусать? Я тоже кусать! КТО БОЛЬШЕ ОТКУСИТ?!.",
        ),
    },      
    'ice': {  # ледяная великанша
        'new': (  # описание
            u"%(girl_name)s, холодная и надменная ледяная великашна.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Хочешь моих обьятий, змей? Твоя чешуя покроется инеем, а стручок скукожится от стужи в моих чреслах. Дерзай...", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Ашшшшь... Я отморожу твои ничтожные кишки!..",
        ),
    },      
    'fire': {  # огненная великанша
        'new': (  # описание
            u"%(girl_name)s, темпераментная и страстная огненная великанша.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Ха! Поглядим какой из тебя любовник, змеюка. Хоть два раунда то выдержишь?", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Решил меня сожрать? Без боя я не дамся!!!",
        ),
    },      
    'titan': {  # людоедка
        'new': (  # описание
            u"%(girl_name)s, совершенная и величественная титанида.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Повелеваю тебе оставить грязные мысли! Ты не достоин моей любви, червь!", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"О Боги, почему вы оставляете меня в смертый час?! Или я не ваша возлюбленная дщерь?",
        ),
    },   
}