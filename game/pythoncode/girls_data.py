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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'earring', 'necklace',
            'pendant', 'ring', 'broch', 'armbrace', 'legbrace', 'brooch', 'farthing'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'brooch', 'taller'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'brooch', 'taller', 'dublon'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'brooch', 'taller', 'dublon'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'brooch'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
            'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
            'brooch', 'farthing', 'taller', 'dublon'],
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            'casket', 'statue', 'mirror', 'comb', 'phallus', 'band', 'diadem', 'tiara', 'earring',
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
            u"Ой, а мне текст не написали (((", #translator: idk."Oh, and I never wrote my poem"?
        ),
        'prelude': (  # Описание прелюдий
            u"With silent movement %(dragon_name)s crept close to the woman and knocked her to the "
            u"ground, and then began to tear her clothes with his teeth like a frenzied dog. %(girl_name)s "
            u"desperately struggled and screamed, but it did no good, her clothes were tattered "
            u"into scattered scraps, leaving her bare naked and defenseless before the "
            u"lustful lizard.",
        ),
        'sex': (  # Описание секса с девушкой
            u"Desperate to save her innocence, %(girl_title)s covered herself with her hands, but %(dragon_type)s "
            u"manuevered around her. With his gaping toothy maw, he grabbed the girl\'s head "
            u"in his jaws so that her whole face was inside, losing access to the air. She opened "
            u"her mouth to try to breathe, but instead the lizard forced his long forked tongue "
            u"into her throat. The girl used all her efforts trying to tear away the stinking mouth, "
            u" forgetting to think of her innocence. Scraping her nails on the hard dragon scales "
            u"and kicking her feet, %(girl_name)s suddenly felt something big and firm between her legs. "
            u"The reptillian member, covered with slime, easily broke through the thin film  "
            u"protecting the entrance to her tight young vagina, ruthlessly stretching everything in its path. "
            u"Almost losing consciousnes from the pain and lack of air, "
            u"%(girl_name)s suddenly felt her rapist\'s jaw open again, "
            u"allowing her to breathe. %(dragon_name)s wanted to take pleasure in her screaming and crying.",
        ),
        'impregnate': (  # Оплодотворение
            u"Squeezed in the pitiless embrance of a lizard, %(girl_title) felt the dragon moving faster. "
            u"The pain became almost unbearable, but the girl\'s screams "
            u"were drowned out by her rapist'\s roar of pleasure. "
            u"The convulsing %(dragon_type)s poured liters of thick, sticky seed "
            u"into her womb, causing her belly to swell. When "
            u"%(dragon_name)s finally pulled away from his victim a waterfall of seed poured out,"
            u"but more than enough remained to ensure insemination. "
        ),
        'new': (  # Описание новой девушки
            u"%(girl_name)s - %(girl_title)s.",
        ),
        'free': (  # Описание процесса выпускания на свободу
            u"She may go now, with your offspring in her belly. Maybe she will survive...",
        ),
        'free_prison': (  # Описание процесса выпускания на свободу из тюрьмы
            u"There is no need to keep her locked up and guarded anymore...let her go where she wishes.",
        ),
        'steal': (  # Описание процесса воровства девушки
            u"%(dragon_name)s carries the captive into his lair...",
        ),
        'jail': (  # Описание процесса заточения в темницу
            u"...and I put it under lock and key.",
        ),
        'jailed': (  # Описание процесса возврата в темницу
            u"%(dragon_name)s returns the girl to the dungeon.",
        ),
        'eat': (  # Описание процесса поедания девушки. Как же ему не стыдно, червяку подколодному.
            u"Are you going to eat me?",
        ),
        'rob': (  # Описание процесса ограбления девушки.
            u"%(dragon_name)s robs the girl and gets: \n %(rob_list)s.",
        ),
        'traps': (  # Описание процесса побега и гибели в ловушке.
            u"%(girl_name)s escapes from the prison, but is killed in a trap.",
        ),
        'escape': (  # Описание успешного побега
            u"%(girl_name)s escapes",
        ),
        'spawn_common': (  # Описание родов
            u"%(girl_name)s lays eggs from which new %(spawn_name)s will hatch, under the supervision of the servants.",
        ),
        'spawn_elite': (  # Описание родов
            u"%(girl_name)s painfully lays a huge egg with a thick scaly shell. \n %(spawn_name)s.",
        ),
        'anguish': (  # Описание смерти от тоски
            u"%(girl_name)s dies in anguish.",
        ),
        'hunger_death': (  # Описание смерти от голода
            u"%(girl_name)s starves to death.",
        ),
        'kill': (  # Описание смерти от селян
            u"Someone discovers that %(girl_name)s was impregnated by a dragon. The angry mob kills her ruthlessly...",
        ),
        'free_spawn': (  # Описание родов на свободе
            u"%(girl_name)s secretly lays eggs from which bloodthirsty monsters will hatch...Now they will go free into the wild, terrorizing the countryside, and perhaps devouring their own mother.",
        ),
        'prison': (  # Проведываем девушку в тюрьме
            u"%(girl_name)s is imprisoned.",
        ),
    },
    'peasant': {  # используется для крестьянок
        'new': (  # описание крестьянки
            u"The rural girl is named %(girl_name)s.",
        ),
        'shout': (  # Реакция девушки, прямой речью 
               #translator: some of these lines I had to make a vague guess at and others I commented out.
            #u"Ой, божечки!..", 
               u"Oh, mama..", 
            u"Where are you poking that vile dripping tongue?!",
            u"Oh,oh,oh, just don\'t eat me, please...", 
            u"Ah...no, no, not there...oh...",
            u"Dragon, darling, please, I\'ll do everything with you, just don\'t eat me!",
            u"What are you doing with that cock, you perverted lizard? Aaaaaaaah....",
            u"Ah, what are you doing?! hurts...no, please...this is huge...uuuy it hurts!!!",
            u"You ugly bastard, let me go...",
            u"Then it\'s true what they say about dragons and girls? Oh, just don\'t roar and bite...",
            #u"Что, люба я тебе змей? Ишь елдаком махает как пастух погонялом!",
            u"Oh Blessed Virgin, what a disgrace...",
            u"(softly cries and covers her face)",
            u"(shakes and puffs furiously through clenched teeth)",
            u"Don\'t, dragon, mama would kill me if she learned that you defiled me. Maybe I can just stroke you there?",
        ),
        'eat': (  # Описание процесса поедания девушки.
            #u"Ой, божечки!..", 
            u"Mama!...", 
            u"Noooooo!...",
            u"Ааааааааh!....",
            u"Don\'t growl, it\'s so scary...",
            u"ah, no, no no...",
            u"Oh shi~",
            u"Don\'t eat me... please, I\'ll do anything, just don\'t eat me!",
            u"He-elp!Someooone!",
            u"You want to eat me, ugly? I hope you choke!",
            u"I\'m just livestock...",
            u"What are you looking at? Oh, you\'re hungry...",
            u"No. Shoo. Ah, do not bite me!",
            u"Get out brute! Why are you licking your lips?",
            u"(muffled groans)",
            u"(softly cries and covers her face)",
            u"(shakes and puffs furiously through clenched teeth)",
        ),
        
    },
    'citizen': {  # используется для горожанок
        'new': (  # описание крестьянки
            u"%(girl_name)s, the daughter of a rich man.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Oh God!", 
            u"Cursed reptile!", 
            u"Don\'t you dare! My father will put you a skewer for that, scum!",
            u"I\'m begging you, Mr. Dragon, you don\'t have to do this, let me go...", 
            u"Ah. No, no, no...not there...oh...",
            u"Just don\'t eat me, I\'ll do anything, I beg you. I know what you want...",
            #u"Ой нет, убеерите эту... это... от меня. Стыд то какой!",
            u"Ah, what are you doing?! It hurts...no, I beg you, it'\s too big... uuuy it hurts!!!",
            u"What are you doing, you spawn of an anteater? Let go...ah, wait!",
            u"I have heard what dragons do with girls...please don\'t growl...don\'t tear it, I\'ll take it off, I\'ll take it off...", 
            #u"Ох, Господи, я такого срама даже у коня в деревне не видала! Жуть то какая...",
            u"Oh Blessed Virgin, save me, protect me...",
            u"(quietly cries and hides her face in her hands)",
            u"(furiously struggles and breathes hard through clenched teeth)",
            u"Why are you tearing off my dress? No, I can\'t, I have a groom, don\'t...!",
        ),
        'eat': (  # Описание процесса поедания девушки.
            u"(praying) Our Father in heaven, hallowed be thy name, thy will be done...", 
            u"(praying) Though I walk through the valley of the shadow of death, I will fear no evil, for thou art with me...", 
            u"Nooooooo!...",
            u"Аааааааа!....",
            u"(coughs from the stench from the dragon\'s mouth)",
            u"Well damn you... ah, no, no, no...",
            u"Oh shi~",
            u"Don\'t eat me... I beg you, I\'ll do anything, just don\'t eat me!",
            u"He-elp! Save me! Somebody! aaah...",
            u"You want to eat me, ugly? I hope you choke!",
            u"No, please...I can buy you a whole herd of pigs...why me??",
            u"I don\'t like this greedy look...",
            u"No! Shoo! Bad dragon! Sit! I told you to sit!!!",
            #u"Пошел вон скотина! А ну ка брысь-кому говорят. Облизывается он, ишь ты!",
            u"(muffled groans)",
            u"(softly cries and covers her face)",
            u"(furiously struggles and breathes hard through clenched teeth)",
        ),
        
    },
    'princess': {  # используется для благородных дам
        'new': (  # описание 
            u"%(girl_name)s, lady of noble blood",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Оh, God!...", 
            u"Do not touch me, demonic fiend!", 
            u"Don\'t you dare! My dather will put you a skewer, pig!",
            u"Some say dragons are noble animals. Maybe you\'ll be so kind as to desist with your paws and tongue?", 
            u"Ah, no, no, not there...oh",
            u"Just not the teeth, I beg you. I\'ll do it, I know what you want...",
            #u"Ой нет, убеерите эту... это... от меня. Стыд то какой!",
            u"Ah, what are you doing!? It hurts, I beg you, it\'s too big, uuuy!!!",
            u"What are you doing, you vermin? Let go...ah, wait!",
               u"I have heard what dragons do with girls...please don\'t growl...don\'t tear it, I\'ll take it off, I\'ll take it off...", 
            #u"Ох, Господи, я такого срама даже у коня в деревне не видала! Жуть то какая...",
            u"Oh Blessed Virgin, save me, protect me...",
            u"(quietly cries and hides her face in her hands)",
            u"(furiously struggles and breathes hard through clenched teeth)",
            u"Why are you tearing off my dress? No, I can\'t, I have a groom, we haven\'t consummated... don\'t...!",
        ),
        'eat': (  # Описание процесса поедания девушки.
            u"(praying) Our Father in heaven, hallowed be thy name, thy will be done...", 
            u"(praying) Though I walk through the valley of the shadow of death, I will fear no evil, for thou art with me...", 
            u"Nooooooo!...",
            u"Аааааааа!....",
            u"(coughs from the stench from the dragon\'s mouth)",
            u"Well damn you... ah, no, no, no...",
            u"Oh shi~",
            u"Don\'t eat me... I beg you, I\'ll do anything, just don\'t eat me!",
            u"He-elp! Save me! Somebody! aaah...",
            u"You want to eat me, ugly? I hope you choke!",
            u"No, please...I can buy you a whole herd of pigs...why me??",
            u"I don\'t like this greedy look...",
            u"No! Shoo! Bad dragon! Sit! I told you to sit!!!",
            #u"Пошел вон скотина! А ну ка брысь-кому говорят. Облизывается он, ишь ты!",
            u"(muffled groans)",
            u"(softly cries and covers her face)",
            u"(furiously struggles and breathes hard through clenched teeth)",
        ),
    },
    'elf': {  # используется для лесных дев
        'new': (  # описание девы
            u"%(girl_name)s, beautiful virgin of the forest elves, the children of the goddess Danu.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Оh, Danu!...", 
            u"Do not touch me, demonic filth!", 
            u"Don\'t you dare! the spirits of the wood will protect my honor!",
            u"Deliver me from this...such a union is an abomination to nature!", 
            u"What have I done to deserve this humililation?!",
            u"You can take my body, but you will never own my soul!",
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Nooooooo!...",
            u"Аааааааа!....",
            u"If you want me to beg for mercy - forget it!",
            u"(coughs from the stench from the dragon\'s mouth)",
        ),
    },        
    'mermaid': {  # используется для русалок
        'new': (  # описание русалки
            u"%(girl_name)s, exotic mermaid",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Оh, Dagon!..", 
            u"Do not touch me, you land lizard!", 
            u"Don\'t you dare! Spirits of the water will protect my honor!",
            u"What is this between your legs? A tentacle???", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Noooooo!...",
            u"Аааааааh!....",
        ),
    },        
    'siren': {  # используется для сирен
        'new': (  # описание
            u"%(girl_name)s, exotic sea giantess.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Оh, Dagon!..", 
            u"Do not touch me, you land lizard!", 
            u"Don\'t you dare! Spirits of the water will protect my honor!",
            u"What is this crap between your legs? A tentacle???", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Noooooo!...",
            u"Аааааааа!....",
        ),
    },        
    'ogre': {  # людоедка
        'new': (  # описание
            u"%(girl_name)s, dimwitted ogre.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"You won\'t fuck me! I\'ll fuck you! ARRRGHh! DEATH BY SNU-SNU!", #yes, it really says that xD 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"The lizard is going to bite me? I bite him back! WHO WILL BITE OFF MORE!?.",
        ),
    },      
    'ice': {  # ледяная великанша
        'new': (  # описание
            u"%(girl_name)s, cold and haughty ice giantess.",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"You want my embrace, snake? Your scales will cover with frost, and your balls will shrink with the cold in my loins. I dare you...", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Аhhhhh!..I\'ll freeze your pathetic guts!..",
        ),
    },      
    'fire': {  # огненная великанша
        'new': (  # описание
            u"%(girl_name)s, temperamental and fiesty fire giantess",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Ha! Let\'s see how you handle me, lover. Do you think you will last two rounds?", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"You think you\'re going to eat me? Not without a fight!!!",
        ),
    },      
    'titan': {  # людоедка
        'new': (  # описание
            u"%(girl_name)s, perfect and majestic Titaness",
        ),
        'shout': (  # Реакция девушки, прямой речью
            u"Clear your dirty mind! You\'re unworthy of my love, worm!", 
        ),
        'eat': (  # Описание процесса поедания девушки
            u"Oh gods, why did you leave me in the hour of my death? Am I not your beloved daughter?",
        ),
    },   
}