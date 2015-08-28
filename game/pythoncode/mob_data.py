# coding=utf-8
# Одноразовые противники
mob = {
    'aircruiser': {
        'name': u"Flying cruiser",  # название моба применяемое в описании
        'power': {'base': (6, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # особые модификаторы
        'image': 'aircruiser',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A dwarven flying cruiser slowly turns its side to face the enemy. Steam artillery prepares to fire a salvo."],
            [['foe_fear'],  u"The heavily armed battle cruiser rapidly unfurls all sails and flies away. There are opponents that not even the brave dwarves will face..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s furiously smashes decks and bulkheads, breaking the ship in half and flinging dwarven bodies overboard. Dwarves simply cannot match a dragon in a close fight, and soon the burning fragments of the ship rain down on the ground."],
            [['foe_dead', 'dragon_wounded'], u"Volleys of the flying cruiser\'s onboard artillery hit their mark. Cast iron projectiles crush the dragon\'s scales and break bones, but %(dragon_name)s does not stop. The paint of his wounds just enrages him and gives him strength. As the dwarves try to quickly reload their weapon, %(dragon_type)s rushes to the deck and begins to tear into the ship. Seeing their futile situation the artillery crew jumps overboard in a vain attempt to escape. Less than a minute later, the main boiler explodes and the ship is split in two."],
            [['foe_alive', 'dragon_wounded'], u"Accelerating to great speed, %(dragon_type)s tries to break onto the deck of the cruiser, but a well aimed volley of artillery blasts it back. %(dragon_name)s roars with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The airship captain waits for the dragon to close. %(dragon_name)s also waits, in no hurry to take a volley from the steam artillery. Someone must take a chance.",],
            [['foe_alive', 'lost_head'], u"The cruiser\'s onboard artillery fires a broadside. Heavy iron balls crash into the dragon\'s head, smashing his skull with a crunch. Luckily %(dragon_name_full)s is able to survive such damage..."],
            [['foe_dead', 'lost_head'], u"Ignoring the danger, %(dragon_type)s rams the flying cruiser The dwarven artillery fires a salvo at point blank range into one of the dragon\'s heads, but his inertia carries him foward to smash through the hull of the ship. %(dragon_name_full)s is able to survive the loss of his head, but the dwarven ship is ruined."],
            [['dragon_dead'], u"Time after time, %(dragon_name_full) rushes at the steam ship, and time after time, bursts of explosive bombs force it back. Even the scales and bones of a dragon cannot withstand this forever. Beaten and mortally wounded, %(dragon_type)s falls to the ground and breathes his last breath..."]
        ]
    },

    'airfleet': {
        'name': u"Air fleet",  # название моба применяемое в описании
        'power': {'base': (5, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 3)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # особые модификаторы
        'image': 'airfleet',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A fleet of flying ships line up to attack."],
            [['foe_fear'],  u"At first sight of the dragon, the flying ships quickly turn full steam in the other direction."],
            [['foe_dead', 'dragon_undamaged'], u"The flying dwarven ships are too slow and clumsy to withstand the onslaught of the dragon. %(dragon_name_full) destroys them one by one, never once crossing the firing zones of the steam guns."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the battle formation of the flying fleet and begins destroying warships. Their panicked fire does more damage to themselves than the dragon, though a few projectiles hit their target. %(dragon_name_full)s triumphs."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_type_cap)s tries to break into the ranks of the fighting ships, but is thrown back by salvos from multiple ships."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_type_cap)s is cautious, trying not to get into a crossfire from the steam guns. But there is no way to destroy the ships without getting closer.",],
            [['foe_alive', 'lost_head'], u"The airbone cruisers\' artillery fires steady volleys. A heavy iron ball smashes into one of the dragon\'s heads with a crunch and shatters his skull. Luckily %(dragon_name_full)s is able to survive such an injury..."],
            [['foe_dead', 'lost_head'], u"Flying ships cannot withstand the onslaught of a furious dragon, but the dwarves fight to the death. Although %(dragon_type)s wins, one of his heads does not survive its wounds."],
            [['dragon_dead'], u"%(dragon_name_full) bursts into the flagship of the fleet, smashing through bulkheads and killing crewmen. The captain, seeing that his crew cannot be saved, closes the valves on the ship\'s boiler. A massive explosion of supherheated steam takes with it the ship, the crew, and the dragon..."]
        ]
    },

    'airship': {
        'name': u"Airship",  # название моба применяемое в описании
        'power': {'base': (4, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['poison_immunity'],  # особые модификаторы
        'image': 'airship',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A flying dwarven ship slowly turns to face its enemy. A steam catapult prepares to fire."],
            [['foe_fear'],  u"(Rapidly unfurling all sails, the airship turns and flies away. There are opponents not even the brave dwarves will face..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s furiously smashes decks and bulkheads, breaking the ship in half and flinging dwarven bodies overboard. Dwarves simply cannot match a dragon in a close fight, and soon the burning fragments of the ship rain down on the ground."],
            [['foe_dead', 'dragon_wounded'], u"Shots from the airship\'s steam catapult hit their mark. Cast iron projectiles crush the dragon\'s scales and break bones, but %(dragon_name)s does not stop. The paint of his wounds just enrages him and gives him strength. As the dwarves try to quickly reload their weapon, %(dragon_type)s rushes to the deck and begins to tear into the ship. Seeing their futile situation the catapult crew jumps overboard in a vain attempt to escape. Less than a minute later, the main boiler explodes and the ship is split in two."],
            [['foe_alive', 'dragon_wounded'], u"Accelerating to great speed, %(dragon_type)s tries to break onto the deck of the airship, but a well aimed catapult shot knocks it back. %(dragon_name)s roars with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The airship captain waits for the dragon to close. %(dragon_name)s also waits, in no hurry to take a hit from the steam catapult. Someone must take a chance.",],
            [['foe_alive', 'lost_head'], u"The airship\'s onboard catapult fires repeatedly. Heavy iron balls crash into the dragon\'s head, smashing his skull with a crunch. Luckily %(dragon_name_full)s is able to survive such damage..."],
            [['foe_dead', 'lost_head'], u"Ignoring the danger, %(dragon_type)s rams the flying ship The dwarven catapult hurls a ball at point blank range into one of the dragon\'s heads, but his inertia carries him foward to smash through the hull of the ship. %(dragon_name_full)s is able to survive the loss of his head, but the dwarven ship is ruined."],
            [['dragon_dead'], u"Time after time, %(dragon_name_full) rushes at the airship, and time after time, explosive bombs force it back. Even the scales and bones of a dragon cannot withstand this forever. Beaten and mortally wounded, %(dragon_type)s falls to the ground and breathes his last breath..."]
        ]
    },

    'angel': {
        'name': u"Angel",  # название моба применяемое в описании
        'power': {'base': (8, 3)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 3)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sound_immunity'],  # особые модификаторы
        'image': 'angel',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"An angel holds a shining sword. He is determined the punish the dragon in the name of heaven."],
            [['foe_fear'],  u"The angel runs away in fear."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s easily evades a blow from a magic sword and bites the angel\'s throat. His blood tastes like wine..."],
            [['foe_dead', 'dragon_wounded'], u"The battle of the two mighty creatures lasts a long time, but in the end the %(dragon_name)s emerges as the victor, covered in wounds."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_type_cap)s charges the enemy but, receiving a painful blow from a magic sword, is forced to retreat."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but neither fighter gains the advantage. They are an equal match for each other.",],
            [['foe_alive', 'lost_head'], u"With a mighty blow the angel takes off one of the dragon\'s heads. But this is not the end, %(dragon_name_full)s can survive such a wound."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s defeats the angel, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"Covered with wounds, the %(dragon_type)s charges for a final attack, but filled with holy fury the angel does not flinch. Putting all his force into one mighty blow, the winged warrior splits the dragon in half!"]
        ]
    },

    'archer': {
        'name': u"Archer",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (1, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'archer',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A royal archer nocks an arrow."],
            [['foe_fear'],  u"The royal archer runs away in horror. He was not prepared for this fight."],
            [['foe_dead', 'dragon_undamaged'], u"The archer manages to fire three times before %(dragon_name)s reaches him. But the arrows simply glance of the scaly skin of the dragon. At close range, the archer has no defense against the fanged lizard."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s opens his jaws to roar, and an arrow punctures his soft mouth. Unable to bite, %(dragon_type)s angrily beats the archer to death with his tail."],
            [['foe_alive', 'dragon_wounded'], u"The sharpshooting archer manages to hit the lizard right in the eye. The lizard stops, going mad with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The archer\'s arrows glance off the natural armor of the dragon.",],
            [['foe_alive', 'lost_head'], u"A tempered arrow with a fire hardened shaft piereces through one of the dragon\'s mouths and into a brain. Luckily, %(dragon_name_full)s can survive such a wound."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s wins, but one of his heads is withering from its wounds."],
            [['dragon_dead'], u"The archer looses a tempered arrow with a fire hardened shaft, and it piereces through one the dragon\'s mouth and into his brain. %(dragon_name_full) falls dead."]
        ]
    },

    'band': {
        'name': u"Band of thieves",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'xbow',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Bandits are lined up in a semicircle, squeezing their weapons tightly."],
            [['foe_fear'],  u"When the dragon attacks the bandits, they flee in fear in all directions. By blind luck, a few escape."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the crowd of robbers and begins to tear them to peices. The disorganized bandits are unable to put up worthy resistance."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the crowd of robbers and begins to tear them to pieces. A few strokes of the bandits reach their mark, but the wounded %(dragon_type)s emerges victorious."],
            [['foe_alive', 'dragon_wounded'], u"Using effectively cooridnated tactics, the bandits strongly rebuff to the dragon, inflicting injury. A few of the robbers are dead, but the rest are full of determination."],
            [['foe_alive', 'dragon_undamaged'], u"The thieves fight desperatel, and manage to hold back the furious assault of the dragon.",],
            [['foe_alive', 'lost_head'], u"%(dragon_type_cap)s attacks thoughtly, exposing his back to several bandits. One clever thief jumps onto his back, smashing one of his skulls in with an iron capped club."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s is covered with serious wounds, and the victory over the bandits hurt him badly. One of his heads is mortally wounded."],
            [['dragon_dead'], u"The robbers pounce on the dragon all at once, frantically thrashing him with their weapons. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath."]
        ]
    },


    'battleship': {
        'name': u"Battleship",  # название моба применяемое в описании
        'power': {'base': (7, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # особые модификаторы
        'image': 'ship',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"On the deck of a warship, a boatswain whistles frantically. Gunners quickly roll out their cannons."],
            [['foe_fear'],  u"Unfurling its sails, the formidable warship turns into the wind and sails from the dragon at top speed. The captain is not ready to fight with such a monster as %(dragon_name_full)s."],
            [['foe_dead', 'dragon_undamaged'], u"Hiding beneath the waves, %(dragon_name)s swims under the warship, and punches a hole in it at top speed. Now the sinking sailors can be caught one by one."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s dives into the depths, but not quickly enough. The warship has time for one volley, and cannonballs break the drago\'s ribs. The furious %(dragon_type)s rips off a section of the ship\'s hull under the waterline. The ocean quickly rushes in, and the battleship is doomed."],
            [['foe_alive', 'dragon_wounded'], u"Coordinated volleys of cannonfire smash into the dragon and he is forced to retreat, throwing up swirling columns of water."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_name)s dives under the ship and tries to punch a hole below the waterline, but to no avail.",],
            [['foe_alive', 'lost_head'], u"A cast-iron bomb stuffed with black powder detonates directly on the dragon\'s forhead. From such a wound few can recover..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type) climbs onto the deck of the ship and happily starts to make a bloodbath out of the crew. The sailors scattor in panic, and in his enthusiastic pursuit %(dragon_name)s fails to notice the captain climbing on a yardarm. Jumping from above, the captain slices off the dragon\'s head with a blow from his sord. Unfortunately for him, it isn\'t enough for victory. The warship is doomed."],
            [['dragon_dead'], u"%(dragon_name_full) is too weak to withstand anothe volley from the warship. Pummeled by iron projectiles, the dragon sinks beneath the depths, no longer able to cling to life."]
        ]
    },

    'boar': {
        'name': u"Enormous boar",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'boar',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A huge boar bows his head to the ground, exposing his menacing curved tusks."],
            [['foe_fear'],  u"The huge boar shrieks in fear of the monstrous predator and tries to escape it. Not that it can..."],
            [['foe_dead', 'dragon_undamaged'], u"The wild boar charges forward, but the %(dragon_type)s knocks him off his feet with one powerful blow."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s wrestles with the giant boar. The horrible fangs of the forest boar pierce the scales of the dragon, inflicting a bleeding wound, but nevertheless the dragon gains the advantage. Within a minute, everything is still and %(dragon_name_full)s can at last eat in peace..."],
            [['foe_alive', 'dragon_wounded'], u"The two huge bodies collde with a roar and a squel. The impact from the boar is great that the %(dragon_type)s goes flying off to the side."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but no one gains the upper hand.",],
            [['foe_alive', 'lost_head'], u"The wounded dragon makes a clumsy move, and the curved tusk of the boar gores one of his necks. This may end badly..."],
            [['foe_dead', 'lost_head'], u"The wounded dragon makes a clumsy move, and the curved tusk of the boar gores one of his necks. But in the end, the boar is doomed to defeat."],
            [['dragon_dead'], u"%(dragon_name_full)s receives a mortal blow. The last thought in his fading conciousness - how humilitating to die from a pig."] #trans: could not translate last part of last sentence.  "буд-то какой-нибудь пьяный человеческий королёк..."
        ]
    },


    'bear': {
        'name': u"Cave bear",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'bear',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"A cave bear stands on its hind legs and bares its teeth."],
            [['foe_fear'],  u"The huge cave bear runs like a frightened puppy. He is surprisngly fast, considering his clumsy gate, but not fast enough..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s опрокидывает медведя навзичь и впивается зубами в его горло. Косолапый пытается отбиться когтями но безуспешно и вскоре затихает."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n От рёва сошедшихся в схватке чудовищ по горам проносится эхо. Исполосованный когтями медведя %(dragon_type)s выходит из этой битвы победителем, но дорогой ценой."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s пытается атаковать огромного медведя, но получает в ответ болезненный удар тяжелой когтистой лапы. Этот зверь так просто не сдастся..."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Пешерному медведю удаётся разкусить череп дракона. %(dragon_name)s всё ещё жив, но спасти голову вряд ли удастся. Эта битва обходится слишком дорого..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Израненный %(dragon_type)s одолевает медведя с огромным трудом. Под ударами тяжелых когтистых лап, одна из голов змея оказывается настолько измочаленной что её вряд-ли удастся спасти..."],
            [['dragon_dead'], u"(you lose) \n Израненный дракон отчаянно атакует гигантского медведя, но тот оказывается сильнее. %(dragon_name_full)s падает наземь не выдержав веса горного исполина и задыхается в его мохнатых объятьях."]
        ]
    },

    'bull': {
        'name': u"Бык",  # название моба применяемое в описании
        'power': {'base': (2, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (2, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'bull',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Бык выставляет рога и роет копытом землю."],
            [['foe_fear'],  u"(you win [fear]) \n Обезумевший от страха бык бросается наутёк, но %(dragon_type)s быстрее..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Одним могучим ударом %(dragon_name)s сбивает быка на землю и впивается в него клыками."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n В ходе короткой но ожесточенной схватки быку удаётся пробить чешую дракона рогом, но раненый %(dragon_name)s всё же выходит из битвы победителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Бык таранит дракона на полной скорости и отбрасывает его в сторону. %(dragon_name)s серьёзно ранен."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог быка попадает ящеру прямо в глаз разрывая мозг одной из голов."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог быка наносит смертельную рану одной из голов, однако дракон выходит из схватки победителем."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог быка пробивает чешую на груди. %(dragon_name_full)s умирает от страшной раны."]
        ]
    },

    'bull_champion': {
        'name': u"Призовой бык",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'bull',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Бык-чемпион выставляет рога и роет копытом землю."],
            [['foe_fear'],  u"(you win [fear]) \n Обезумевший от страха призовой бык бросается наутёк, но %(dragon_type)s быстрее..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Одним могучим ударом %(dragon_name)s сбивает призового быка на землю и впивается в него клыками."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n В ходе короткой но ожесточенной схватки призовому быку удаётся пробить чешую дракона рогом, но раненый %(dragon_name)s всё же выходит из битвы победителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Бык-чемпион таранит дракона на полной скорости и отбрасывает его в сторону. %(dragon_name)s серьёзно ранен."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог призового быка попадает ящеру прямо в глаз разрывая мозг одной из голов."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог призового быка наносит смертельную рану одной из голов, однако дракон выходит из схватки победителем."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s движется слишком медленно, кривой и острый рог быка-чемпиона пробивает чешую на груди. %(dragon_name_full)s умирает от страшной раны."]
        ]
    },

    'castle_guard': {
        'name': u"Защитники замка",  # название моба применяемое в описании
        'power': {'base': (7, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'town',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Защитники замка занимают места на стенах. Они готовят копья, тяжелые камни и котлы с кипящей смолой."],
            [['foe_fear'],  u"(you win [fear]) \n Разглядев дракона получше защитники замка дрогнули. Они в панике бегут со стен и прячутся кто-куда, а битва выиграна даже не начавшись."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Под градом почти безполезных камней, стрел и копий %(dragon_name_full)s подбирается к воротам и вложив весь свой вес в несколько таранных ударов, высаживает их. Оставшиеся без прикрытия воины на стенах беззащитны перед яростью дракона."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Под градом камней, стрел и копий %(dragon_name_full)s подбирается к воротам и вложив весь свой вес в несколько таранных ударов, высаживает их. Оружие защитников оставилиона теле дракона раны, но теперь когда врата пали его уже ничто не остановит."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Поток копий, камней и стрел обруженный защитниками крепости со стен и башен так силён, что дракону приходится отступить от ворот. Взять эту крепость не так просто..."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s налегает на ворота всем весом, пытаясь выбить их в то вреям как защитники крепости поливают его со стне потокм камней, стрел и копий. Но и то и другое совершенно бесполезно. Копья отскакиваю от прочной чешуи дракона, но и окованные сталью врата не желают поддаваться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Пятеро дюжих защитников сбрасывают со стены толстенный ствол дерева, который придавливает одну из голов дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Пятеро дюжих защитников сбрасывают со стены толстенный ствол дерева, который придавливает одну из голов дракона, однако это им не помогает. Разъярённый %(dragon_type)s вышибает ворота и врывается в замок."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s слишком изранен и устал для такой битвы. Всего один метко сброшенный со стены камень прерывает его штурм. Отважные защитники города торжествуют победу, в то вреям как %(dragon_name_full)s издыхает у так и не поддавшихся напору врат."]
        ]
    },
        
    'catapult': {
        'name': u"Катапульты",  # название моба применяемое в описании
        'power': {'base': (3, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (2, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # особые модификаторы
        'image': 'catapult',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Рассчёт судорожно заряжает катапульту, готовясь открыть огонь на поражение."],
            [['foe_fear'],  u"(you win [fear]) \n Рассчёт катапульты разбегается в страхе, оставляя грозную боевую машину без управления."],
            [['foe_dead', 'dragon_undamaged'], u"flawless victory) \n %(dragon_name_full)s с лёгкостью разрушает катапульту и убивает рассчёт."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n (%(dragon_name)s бросается в лобовую атаку и получает попадание прямой наводкой, однако не останавливается. Рассчёт боевой машины обречён."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Меткий выстрел катапульты отбрасывает дракона назад, но это ещё не конец!"],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Рассчёт катапульты не торопится, они знают что успеют выстрелить лишь раз и боятся промахнуться. %(dragon_name)s маневрирует не давая им шанса прицелиться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Снаряд катапульты попадает дракону точно в голову. Это очень серёзная рана!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Снаряд катапульты попадает дракону точно в голову, однако дракона это не останавливает. Разъярённый от ран %(dragon_type)s уничтожает расчёт метательно машины с особой жестокостью."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s переоценил свои силы. Меткий выстрел из катапульты сносит ему единственную живую голову."]
        ]
    },
    
    'champion': {
        'name': u"Рыцарь-чемпион",  # название моба применяемое в описании
        'power': {'base': (5, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'champion',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Победитель турнира подхватывает новое копье и разворачивает боевого коня для атаки."],
            [['foe_fear'],  u"(you win [fear]) \n Победитель турнира рвётся в бой, но его конь слишком напуган - он встаёт на дыбы и сбрасывает наездника в грязь, оставляя его совершенно беззащитным."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s ловко уворачивается от острого наконечника копья и хлёстким ударом на противоходе вышибает чемпиона из седла."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s и чемпион со страшным грохотом сшибаются грудь на грудь. Рыцарь опрокидывается вместе с конём, но и %(dragon_name)s получает ранение."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Таранный удар копья помноженный на вес и скорость коня со всадником отбрасывает дракона в сторону."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Противники сталкиваются под скрежет металла и ржание боевого коня, но силы примерно равны.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Рыцарь метким ударом сносит голову дракону, однако это ещё не конец."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n Рыцарь метким ударом сносит голову дракону. %(dragon_name_full)s умирает."]
        ]
    },

    'city_guard': {
        'name': u"Городская стража",  # название моба применяемое в описании
        'power': {'base': (6, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'city_guard',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Стражники выстраиваются полукольцом, покрепче сжимая алебарды."],
            [['foe_fear'],  u"(you win [fear]) \n При виде атакующего дракона городские стражнкии в страхе разбегаются кто куда. Некотрым повезло, другим уйти не удалось..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s врывается в построение стражников и начинает рвать их на куски. Дезорганизованные бойцы нес пособны оказать достойного сопротивления."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s врывается в построение стражников и начинает рвать их на куски. Тяжело вооруженные бойцы держатся достойно, но %(dragon_type)s хоть и раненый выходит из битвы пбедителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Применяя грамотную тактику взаимодействия, стражники ухитряются дать дракону серьёзный отпор и даже наносят ему ощутимые раны. Пара бойцов падает мертвыми, но остальные полны решимости."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Стражники сражаются отчаянно и на некоторое время им удаётся сдержать яростный напор дракона.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s атакует без оглядки и пропускает нескольких алебардистов за спину. Эта ошибка стоит ему головы. Одной из..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s жестоко изранен и победа над стражниками даётся ему нелегко. Одна из голов получила смертельную рану."],
            [['dragon_dead'], u"(you lose) \n Стражники набрсываются все разом и отчаянно молотят дракона своими алебардами. Израненный %(dragon_type)s в последнем порыве ярости ухитряется убить нескольких врагов, но их слишком много. %(dragon_name_full)s падает наземь и испускает последний дух."]
        ]
    },

    'city': {
        'name': u"Надвратная башня",  # название моба применяемое в описании
        'power': {'base': (9, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 3)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'city_siege',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Стражи ворот хватают оружие и встают по местам."],
            [['foe_fear'],  u"(you win [fear]) \n Защитники ворот в ужасе бегут от атакующего дракона. Лёгкая победа."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s проламывает ворота и разбрасывает пытающихся дать отпор защитников словно тряпичные куклы."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s бросается на ворота, под градом стрел и камней. Ранений избежать не удаётся, но в итоге ворота разбиты и стражники в ужасе бегут."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s бросается на ворота, под градом стрел и камней. Это плохая идея - ворота слишком прочны, а вот чешуя дракона оказывается пробита сразу в нескольких местах."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s бросается на ворота, под градом стрел и камней. Огонь защитников не причиняет ему особого вреда, но сделанные на совесть ворота и укрепленния тоже не поддаются.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Кто-то выливает на голову дракона целый чан кипящей смолы."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но победа стоила ему головы. Дорогая цена."],
            [['dragon_dead'], u"(you lose) \n Израненый %(dragon_type)s остервенело бьётся в прочные ворота но те не поддаются. Не в силах прдолжать бой %(dragon_name_full)s падает у неодолимых укреплений и истекает кровью."]
        ]
    },
    
    'dog': {
        'name': u"Овчарка",  # название моба применяемое в описании
        'power': {'base': (1, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (1, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'dog',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Цепной пёс рычит и скалит зубы."],
            [['foe_fear'],  u"(you win [fear]) \n Цепной пёс скулит и прячется в страхе."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s разрывает собаку в клочки."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s и цепной пёс сплетаются в глубок клацающих зубов и скребущих когтей. %(dragon_name)s выходит из схватки победителем, но не без ранений."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Злобный пёс ухитряется прижать дракона к земле и вцепиться ему в глотку. Положение становится неприятным."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Дракон и собака кружат друг вокруг друга, скаля клыки и рыча. Никто не решается сделать выпад.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Злобный пёс ухитряется прижать дракона к земле и вцепиться ему в глотку. Ранение очень серьёзное."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает загрызенный деревенской шавкой. Какой позор для всего его рода!"]
        ]
    },

    'domik': {
        'name': u"Деревянный домик",  # название моба применяемое в описании
        'power': {'base': (7, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 4)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['poison_immunity', 'magic_immunity'],  # особые модификаторы
        'image': 'domik',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Ветхая избушка на шарнирных ногах чем то напоминает циплёнка. Огромного, агрессивного циплёнка, вооруженного пушками 50го калибра..."],
            [['foe_fear'],  u"(you win [fear]) \n Аура ужаса которую испускает %(dragon_name_full)s столь велика, что от него отбигает даже деревянный домик."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s наносит по домику удары такой силы, что бревенчатый сруб лопается и трескается, гвозди вылетают словно пули и битая черепица сыпется на землю. Древний ужас лесов столетиями набигающий эльфов..."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s и домик сжимают друг друга в смертельных стальных объятьях. Ребра дракона трещат, но всё же дерево оказывается слабее и домик сминается словно огромный коробок спичек."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Залп из автоматических пушек отбрасывает дракона назад."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s и голем бьют друг друга изо всех сил, но оба столь хорошо защищены что отделываются лишь незначительными царапинамми. Старые пихты трясутся от этой схватки исполинов.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Залп из автоматических пушек отбрасывает дракона назад. Разрывными стреляет, подумал %(dragon_name)s, пораскинув мозгами."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Израненный %(dragon_type)s с треском раскатывает деревянное тело голема по брёвнышку, оставляя в цепких стальных пальцах ног домика одну из своих оторванных голов."],
            [['dragon_dead'], u"(you lose) \n Залп из автоматических пушек разносит дракону череп. Разрывными стреляет, подумал %(dragon_name)s, пораскинув мозгами. Это была его последняя мысль."]
        ]
    },

    'druid': {
        'name': u"Друид",  # название моба применяемое в описании
        'power': {'base': (5, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'druid',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Трава вокруг другида наливается изумрудной зеленью - он собирает к себе силы дикой природы."],
            [['foe_fear'],  u"(you win [fear]) \n Друид оборачивается быстроногим оленем и бросется на утёк. Он не готов к битва с таким противником как %(dragon_name_full)s."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Друид призывает целую тучу пчёл убийц, но это его роковая ошибка - насекмые наспособны пробить чешую дракона своими жалами. %(dragon_type)s разрывает друида в клочки."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Друид окружает себЯ стеной из ядовитых шипов, но %(dragon_type)s проламывается сквозь них и убивает эльфа. По жилам дракона растекается ял... ничего это не смертельно."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Друид призывает себе на помощь множество сверепых лесных зверей. В жестокой схватке с ними %(dragon_name_full)s одерживает нелегкую победу, но друид всё ещё не вредим а вот %(dragon_type)s весь в крови."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Друиду удаётся задержать дракона призвав ядовитые лианы. Но это лишь временная мера, рано или поздно %(dragon_name)s вырвется.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Подчинясь силе друида земля порождает каменные пасти полные острых сталактитов. Одна из них намертво зажимает голову дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Друид встречает атаку дракона ударом сияющего зелёным огнём посоха. Удар настолько силён, что %(dragon_name_full)s теряет одну из своих голов, однако не оставливается и одним мощным ударом убивает ненавистное дитя Дану."],
            [['dragon_dead'], u"(you lose) \n Израненый %(dragon_type)s не может спротивляться заклятьям друида. %(dragon_name)s падает от удара толстой дубовой ветви в затылок и тогда на него набрасываются разъярённые лесные звери."]
        ]
    },

    'dwarf_champion': {
        'name': u"Король цвергов",  # название моба применяемое в описании
        'power': {'base': (7, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'dwarf_champion',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Король цвергов одевает огнеупорную маску и покрепче перехватывает усиленный колдовскими рунами боевой топор."],
            [['foe_fear'],  u"(you win [fear]) \n Едва заметив приближение дракона, король цвергов и вся его свита бегут в рассыпную, в надежде найти укрытие в ремесленных цехах или скрыться потайными ходами."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Король цвергов сражается с отчаянием обречённого, но даже он не в силах выдержать напор дракона. Израненный воитель падает бездыханным."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s сходится с королём цвергов в рукопашной схватке и побеждает, но дорогой ценой - удар зачарованного топора пробивший чешцую, навсегда оствит памятный шрам."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s самонадеянно атакует заковонного в адамант карлика, но вынужден отступить получив блезненный удар руническим потопорм."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой с королём цвергов продолжается некоторое время но никто не может взять верх. Оба соперника очень выносливы и отменно защищены.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Могучим ударом рунического топора король цвергов отсекает одну из голов дракона. Однако  %(dragon_name_full)s способен пережить это."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_name_full)s побеждает короля цвергов, однако дорогой ценой. Ударом рунической секиры отсечена одна из голов."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s собрав последние силы бросается в отчаянную атаку, но король цвергов крепко стоит на ногах и наносит один точный удар. %(dragon_name_full)s падает к его ногам обезглавленный!"]
        ]
    },

    'dwarf_citizen': {
        'name': u"Цверг",  # название моба применяемое в описании
        'power': {'base': (2, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'dwarf_citizen',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Загнанный в угол карлик готовится к отчаянной схватке."],
            [['foe_fear'],  u"(you win [fear]) \n Даже будучи загнанным в угол карлик настолько испуган жутким видом дракона, что не способен защищаться. Легкая добыча."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s с лёгкостью одолевает почти беззащитного цверга."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Даже слабо вооруженный цверг ухитряется нанести дракону ощутимое ранение, прежде чем пасть от его клыков. Вот это сила духа!"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Кажущийся почти беззащитным цверг тем не менее даёт яростный отопр. Раненый %(dragon_type)s вынужден отпрянуть назад."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Юркий цверг ловко маневрирует в узких проходах и прячется за коллонами - достать его оказывается совсем не просто!",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Карлик прячется темном проходе на втором уровне тоннеля и неожданно прыгат прямо на спину дракону. Его тяжёлая стальная кирка пробивает череп змея насквозь! К счастью для дракона такая рана ещё не смертельна."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Цверг прячется темном проходе на втором уровне тоннеля и неожданно прыгат прямо на спину дракону. Его тяжёлая стальная кирка пробивает череп змея насквозь! %(dragon_name)s перекатывается на спину чтобы раздавить мерзкого карлика. "],
            [['dragon_dead'], u"(you lose) \n Цверг прячется темном проходе на втором уровне тоннеля и неожданно прыгат прямо на спину дракону. Его тяжёлая стальная кирка пробивает череп змея насквозь! Эта рана оказывается смертельной..."]
        ]
    },

    'dwarf_guards': {
        'name': u"Стражи тоннелей",  # название моба применяемое в описании
        'power': {'base': (6, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'dwarf_guards',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Закованные в стальные панцири цверги выстраиваются плотной группой, перекрывая тоннель почти несокрушимой стеной щитов."],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s вселяет в серца цвергов ужас одним лишь своим видомю. Стражи тоннелей не готовы принять бой с таким могучим противником."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Используя весь свой немалый вес %(dragon_type)s проламывается сквозь сомкнутые щиты цвергов и ломает их строй. После этого победа даётся ему с лёгкостью."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s решает атаковать стену щитов с разбега. Выставленные вперёд пики пробивают его чешую в нескольких местах, но %(dragon_type)s не сбавляет напора и разбрасывает карликов в стороны, словно бильярдный шар сносящий кегли."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_name)s решает атаковать стену щитов с разбега, но цверги готовы. Уперев древки копий в пол они останавливают напор чудовища и даже наносят несколько метких ударов двуручными топорами."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_name)s не решается атаковать стену щитов в лоб, это может быть слишком опасно. Цверги не двигаются с места и пытаются дракона врага из арбалетов, но безрезультатно.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Лобовая атака на стену щитов оказывается очень дурной идеей. Один из двуручных топорв цвергов стоящих во втором ряду сносит дракону голову! Это пока не смертельно, но очень и очень серьёзно."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Используя весь свой немалый вес %(dragon_type)s проламывается сквозь сомкнутые щиты цвергов и ломает их строй. Даже лишившись своей основной защиты карлики сражаются отчаянно и прежде чем одолеть их %(dragon_name_full)s теряет одну из своих голов."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name)s страдает от ран полученных им в прошлых битвах. Видя это стражи тоннелей идут в атаку и побеждают, задавив дракона числом. Победа стоила им дорого, это победа которую воспоют в легендах!"]
        ]
    },

    'elf_ranger': {
        'name': u"Страж границ",  # название моба применяемое в описании
        'power': {'base': (6, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (2, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'elf_ranger',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Страж границ натягивает свой лук и берёт прицел."],
            [['foe_fear'],  u"(you win [fear]) \n Решив что дракон ему не по зубам, страж границ растворяется в густой листве. Наверняка он предупредит своих..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_type_cap)s с силой бьёт хвостом по стволу дерева и страж границ падает с ветки. В ближнем бою у него уже нет никаких шансов."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s шатает дерево, чтобы скинуть альва с ветки, но в процессе получает стрелу в пасть. Стрелку тоже не везёт, он падает прямо на разъяренного дракона вслед за своей стрелой..."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Страж границ ловко прыгает по деревьям, то и дело скрываясь в листве а затем делая внезапный выстрел и снова скрывась. Влшебные стрелы наносят болезненные раны..."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Страж границ ловко прыгает по деревьям, то и дело скрываясь в листве. Он выжидает удобного момента для единственного точного выстрела. Видимо бережет стрелы.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Израненный %(dragon_type)s таранит ствол дерева всем весом своего тела и страж границ падает прямо ему на голову. Не растерявшись альв вонзает зажатую в руке стрелу прямо в глаз дракона и тут же отпрыгивает в кусты."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Израненный %(dragon_type)s таранит ствол дерева всем весом своего тела и страж границ падает прямо ему на голову. Не растерявшись альв вонзает зажатую в руке стрелу прямо в глаз дракона, но это не спасает его от суровой участи."],
            [['dragon_dead'], u"(you lose) \n Страж границ достаёт зачарованную стрелу с трёлезвиныйм наконечником и зелёным оперением. Дождавшись пока дракон встанет на дыбы, он делает точный выстрел прямо в сердце чудовища. %(dragon_name_full)s испускает дух в жутких корчах."]
        ]
    },

    'elf_witch': {
        'name': u"Лесная чародейка",  # название моба применяемое в описании
        'power': {'base': (6, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'elf_witch',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"%(dragon_type)s крадётся так тихо как только может, но острый эльфийский слух улавливает даже малейшее движение. Во взрыве зелёно-золотого пламени лесная чародейка взмывает к аронам деревев и начинает ткать смертоносные чары."],
            [['foe_fear'],  u"(you win [fear]) \n Аура ужаса и тьмы что принёс собой дракон так сильна, что цветы и листья вянут кругом. Не в силах взглянуть в глаза чудовища, лесная чародейка закрывает лицо руками ожидая своей усасти и не помышляя о сопротивлении."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Чародейка наращивает вокруг себя толстый панцирь из живой древесной коры, скрывающий всё её тело и протягивает к дракону узловатые когти-корневища. Против человека такое бы сработало, но %(dragon_type)s с легкостью разбивает деревянную скорлупу и вытаскивает на свет нежную начинку. Угрозы драконьих зубов достаточно, чтобы чародейка прекратила свои фокусы."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Лесная дева припечатывает дракона ударом сияющего посоха, но %(dragon_name)s в ответ стегает её хвостом. %(dragon_type)s остаётся стоять, а чародейка падает скорчившись от нестерпимой боли и звона в ушах."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Лесная чародейка призывает себе на помощь множество сверепых лесных зверей. В жестокой схватке с ними %(dragon_name_full)s одерживает нелегкую победу, но дева всё ещё невредима, а вот %(dragon_type)s весь в крови."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Прекрасная чародейка кидает в дракона одно заклятье за другим но всё без толку. %(dragon_name)s ходит кругами, размышляя как бы схватить фею не повредив её, ведь ей ещё предстоит рожать его детишек...",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Подчинясь силе феи земля порождает каменные пасти полные острых сталактитов. Одна из них намертво зажимает голову дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Лесная чародейка встречает атаку дракона ударом сияющего зелёным огнём посоха. Удар настолько силён, что %(dragon_name_full)s теряет одну из своих голов, однако не оставливается и прижимает прелестное дитя Дану к земле."],
            [['dragon_dead'], u"(you lose) \n Израненый %(dragon_type)s не может спротивляться заклятьям чародейки. %(dragon_name)s падает от удара толстой дубовой ветви в затылок и тогда на него набрасываются разъярённые лесные звери."]
        ]
    },
    
    'footman': {
        'name': u"Пехотинцы",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'footman',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Пехотинцы выстраиваются полукольцом, покрепче сжимая мечи и копья."],
            [['foe_fear'],  u"(you win [fear]) \n При виде атакующего дракона пехотинцы в страхе разбегаются кто куда. Некотрым повезло, другим уйти не удалось..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s врывается в построение воинов и начинает рвать их на куски. Дезорганизованные бойцы не способны оказать достойного сопротивления."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s врывается в построение пехоты и начинает рвать их на куски. Тяжело вооруженные бойцы держатся достойно, но %(dragon_type)s хоть и раненый выходит из битвы пбедителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Применяя грамотную тактику взаимодействия, пехотинцы ухитряются дать дракону серьёзный отпор и даже наносят ему ощутимые раны. Пара бойцов падает мертвыми, но остальные полны решимости."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Пехотинцы сражаются отчаянно и на некоторое время им удаётся сдержать яростный напор дракона.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s атакует без оглядки и пропускает нескольких бойцов из отряда себе за спину. Эта ошибка стоит ему головы. Одной из..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s жестоко изранен и победа над воинами даётся ему нелегко. Одна из голов получила смертельную рану."],
            [['dragon_dead'], u"(you lose) \n Пехотнцы набрсываются все разом и отчаянно молотят дракона своими мечами и копьями. Израненный %(dragon_type)s в последнем порыве ярости ухитряется убить нескольких врагов, но их слишком много. %(dragon_name_full)s падает наземь и испускает последний дух."]
        ]
    },

    'golem': {
        'name': u"Железный голем",  # название моба применяемое в описании
        'power': {'base': (7, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 4)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['poison_immunity', 'fire_immunity', 'magic_immunity'],  # особые модификаторы
        'image': 'golem',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Приземистый стальной гигант, похожий на ожившие доспехи загораживает собой весь проход."],
            [['foe_fear'],  u"(you win [fear]) \n Аура ужаса которую испускает %(dragon_name_full)s столь велика, что перед ним отступает даже стальной страж."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s наносит голему удары такой силы, что сталь лопается и трескается, заклёпки вылетают словно пули и обломки брони со звоном сыплются на землю. Почти непобедимый страж повержен..."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s и голем сжимают друг друга в смертельных стальных объятьях. Ребра дракона трещат, но всё же сталь оказывается слабее и голем сминается словно огромная консервная банка."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Практически неуязвимый стальной гигант молотит древнего ящера своими стальными кулаками."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s и голем бьют друг друга изо всех сил, но оба столь хорошо защищены что отделываются лишь незначительными царапинамми. Стены тоннеля трясутся от этой схватки исполинов.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Стальной гигант сцепляет руки над головой и словно молот обруживает их на голову дракона разбивая череп в крошку."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Играненный %(dragon_type)s со скрежетом разрывает стальное тело голема на части, оставляя в цепких стальных пальцах стража одну из своих оторванных голов."],
            [['dragon_dead'], u"(you lose) \n Стальной гигант сцепляет руки над головой и словно молот обруживает их на голову дракона разбивая череп в крошку. %(dragon_name_full)s умирает от полученных ран"]
        ]
    },

    'griffin': {
        'name': u"Дикий грифон",  # название моба применяемое в описании
        'power': {'base': (5, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'griffin',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Дикий грифон расправляет свои огромные орлиные крылья и вытягивает острые когти. В его глазах ярость."],
            [['foe_fear'],  u"(you win [fear]) \n С жалобным клёкотом дикий грифон переворачивается прямо в воздухе и пытается скрыться, но %(dragon_type)s настигает его и убивает одним ударом."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s налетает на дикого грифона словно ястреб на куропатку. Перья и кровавые ошёметки летят во все стороны."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Сцепившись в воздухе словно две кошки %(dragon_type)s и дикий грифон падают на землю. Этот удар оказывается для грифона смертельным, но и %(dragon_name)s тоже ушибся при падении."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s хватает дикого грифона за шею, но тот наносит мощный удар задними львиными когтями, чуть не распоров ящеру брюхо. %(dragon_name)s с болезненным воплем отлетает назад."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Дикий грифон закладывает в небе невероятные виражи и кульбиты. Летающие враги борятся за превосходство в высоте не спеша сойтись в рукопашную.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Удар могучих когтей дикого грифона распарывает глотку дракона. Не многие могут пережить такой удар, но %(dragon_name_full)s один из них."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n (difficult victory) \n %(dragon_type_cap)s побеждает в битве с диким грифоном, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n Удар могучих когтей дикого грифона распарывает глотку дракона. Даже %(dragon_name_full)s не может пережить такой удар."]
        ]
    },

    'griffin_rider': {
        'name': u"Всадник на грифоне",  # название моба применяемое в описании
        'power': {'base': (9, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'griffin_rider',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Небесный рыцарь поднимает своего летучего скакуна к облакам, параллельно проверяя свою пику и арбалет."],
            [['foe_fear'],  u"(you win [fear]) \n Небесный рыцарь разворачивает грифона и стелясь вдоль земли улетает прочь."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Стремительно сблизившись с небесным рыцарем, %(dragon_type)s одним точным ударом выбивает всадника из седла. Оставшийся без управления грифон - лёгкая добыча, а рыцарь обречён разбиться при падении с огромной высоты."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Поровнявшись по высоте %(dragon_type)s и всадник на грифоне сшибаются грудь на грудь, словно рыцари на турнире. %(dragon_name)s ранен обломком копья, но всадник вылетает из седла и падает с огромной высоты."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Не сближаясь на опасное расстояние, всадник на грифоне обстреливает дракона из своего арабалета. Один из выстрелов достигает цели."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Небесный рыцарь закладывает в воздухе невероятные виражи и кульбиты. Летающие враги борятся за превосходство в высоте не спеша сойтись в рукопашную.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Не сближаясь на опасное расстояние, всадник на грифоне обстреливает дракона из своего арабалета. Один из выстрелов попадает дракону прямо в глаз!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Поровнявшись по высоте %(dragon_type)s и всадник на грифоне сшибаются грудь на грудь, словно рыцари на турнире. Копьё всадника входит прямо в открытую пасть дракона нанося страшную рану, однако сам небесный рыцарь не удержавшись в седле пдает с огромной высоты."],
            [['dragon_dead'], u"(you lose) \n Израненный и обессилевший %(dragon_type)s пытается приземлиться, но небесный рыцарь нагоняет его в воздухе и пронзает насквозь своим остро отточенным копьём."]
        ]
    },

    'heavy_cavalry': {
        'name': u"Тяжелая кавалерия",  # название моба применяемое в описании
        'power': {'base': (8, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'heavy_cavalry',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Закованные в стальные доспехи кавалеристы разворачиваются цепью и опускают пики параллельно земле."],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s издаёт ужасающий рёв и кони бросаются в рассыпную, сбрасывая и топча собственных всадников."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Один за другим тяжелые всадники атакую дракона, но %(dragon_name)s ловко уклоняется от этих неуклюжих и прямолинейных атак. Щёлкая хвостом словно иполинским кнутом %(dragon_type)s вышибает кавалеристов из седла."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s способен опрокинуть всадника вместе с лошадью одним ударом, но их много, поэтому невредимым из битвы ему выйти не удаётся."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s отвлекается на одного из всадников и не замечает как второй проезжает совсем рядом, на всём скаку всаживая свою гранёную пику в бок ящера."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Всадники ловко маневрируют, избегая клыков дракона и пытаясь достать его своими длинными пиками. Такая тактика вряд ли принесёт им победу, зато сохраняет жизнь.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s сбивает бронированного скакуна с ног и бросается к всаднику чтобы растерзать его, но тот резво вскакивает на ноги и наносит точный удар остро отточенным мечём. Голова дракона падает на землю. Как хорошо что в запасе есть ещё головы..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В жаркой схватке %(dragon_type)s побеждает, но одна из его голов остаётся валяться на поле, отрубленная тяжелым кавалерийским палашом."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s сражается очаянно, но всадников слишком много. Убив много людей и коней, %(dragon_name_full)s в конце концов падает наземь, истекая кровью."]
        ]
    },

    'heavy_infantry': {
        'name': u"Латники",  # название моба применяемое в описании
        'power': {'base': (5, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'heavy_infantry',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Латники выстраиваются полукольцом, покрепче сжимая двуручные мечи."],
            [['foe_fear'],  u"(you win [fear]) \n При виде атакующего дракона латники в страхе разбегаются кто куда. Некотрым повезло, другим уйти не удалось..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s врывается в построение латников и начинает рвать их на куски. Дезорганизованные бойцы не способны оказать достойного сопротивления."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s врывается в построение пехоты и начинает рвать их на куски. Тяжело вооруженные бойцы держатся достойно, но %(dragon_type)s хоть и раненый выходит из битвы пбедителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Применяя грамотную тактику взаимодействия, латники ухитряются дать дракону серьёзный отпор и даже наносят ему ощутимые раны. Пара бойцов падает мертвыми, но остальные полны решимости."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Латники сражаются отчаянно и на некоторое время им удаётся сдержать яростный напор дракона.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s атакует без оглядки и пропускает нескольких вооруженных двуручниками латников себе за спину. Эта ошибка стоит ему головы. Одной из..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s жестоко изранен и победа над латниками даётся ему нелегко. Одна из голов получила отрублена ударом тяжелого двуручного меча."],
            [['dragon_dead'], u"(you lose) \n Латники набрсываются все разом и отчаянно молотят дракона своими двуручными мечами. Израненный %(dragon_type)s в последнем порыве ярости ухитряется убить нескольких врагов, но их слишком много. %(dragon_name_full)s падает наземь и испускает последний дух."]
        ]
    },

    'ifrit': {
        'name': u"Ифрит",  # название моба применяемое в описании
        'power': {'base': (6, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['fire_immunity', 'sfatk_2up'],  # особые модификаторы
        'image': 'ifrit',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Глаза ифрита пылают словно угли. Он крепче сжимает свой огненный молот и покрывается с ног до головы сполохами дымного алого пламени."],
            [['foe_fear'],  u"(you win [fear]) \n Завороженный ифрит стоит некоторое время неподвижно, устрашенный обликом дракона. Затем он исчезает во вспышке дымного поламени словно вылетевший в трубу дым."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Огонь ифрита оказывается бессилен - %(dragon_name_full)s побеждает"],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s сходится с ифритом в рукопашную. Яростное пламя окутывает обоих бойцов и хотя %(dragon_name)s страшно обожжён, он выходит из схватки победителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Огненный молот великана бьёт с такой ошеломительной силой, что %(dragon_type)s отлетает в дальний угол словно шавка."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Сталь и пламя против чешуи и клыков. Битва равная, некоторое время кажется что ни одна сторона не сможет одержать победу в этом сражении.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Мощныйм ударом объятого пламенем молота ифрит разбивает голову дракона, словно спелый арбуз. %(dragon_name_full)s чудом выживает после такого."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s переоценил свои силы. Огненный великан с лёгкостью сокрушает его своим заклаённым в вулканическом огне молотом."]
        ]
    },

    'jotun': {
        'name': u"Йотун",  # название моба применяемое в описании
        'power': {'base': (6, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['siatk_2up', 'ice_immunity'],  # особые модификаторы
        'image': 'jotun',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Синеволосый гигант в рогатом шлеме крепко сжимает покрытый инеем топор."],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s окутывает йотуна аурой страха и тот в панике бежит прочь."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Гигант слишком медлителен. Пока он замахивается своим огромным тпором, %(dragon_type)s стремительно атакует. Несколько смертоносных словно броски змеи ударов решают исход боя."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Огромный топор великана врезается в стену и застревает в трещине. %(dragon_name)s тут же бросается вперёд, стремясь использовать выгодный момент и враги сходятся в рукопашную. Безоружный йотун ухитряется сломать дракону пару костей, но всё же силы не равны и %(dragon_name_full)s побеждает."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Йотун отламывает от потолка огромную сосульку и мечет её словно дротик. Удар глыбы льда не смертельный, но всё же весьма болезненный."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Йотун остервенело размахивает своим инеистым топором, не давая дракону приблизиться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Одним могучим ударом покрытого инеем топора Йотун сносит дракону голову. Но %(dragon_name_full)s способен пережить даже такую рану!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В ходе тяжелейшей схватки %(dragon_name_full)s одолевает великана, но одна из его голов умирает от полученых в бою ран."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s бьётся до последнего, но йотун берёт верх. Одним могучим ударом своего ледяного топора он разрубает дракона пополам!"]
        ]
    },

    'jagger': {
        'name': u"Егерь",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (1, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'jagger',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Егерь накладывает стрелу на тетиву."],
            [['foe_fear'],  u"(you win [fear]) \n Егерь бежит в ужасе. Он не готов к такому бою."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Егерь успевает выстрелить трижды, прежде чем %(dragon_name)s добирается до него. Но стрелы просто отскакивают от чещуйчатой шкуры дракона. А вот у самого стрелка нет никакой защиты от зубов ящера."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s открывает пасть чтобы издать громогласный рык и тут же получаёт стрелу в мягкое нёбо. Лишённый возможности кусаться, %(dragon_type)s в ярости забивает стрелка ударами хвоста."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Меткий лучник ухитряется попасть дракону точно в глаз. Обезумевший от боли ящер мешкает."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Стрела выпущенная лучником отскакивает от прочной чешуи дракона.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Закалённая стрела с чёрным древком влетает в пасть дракону и проходит точно в мозг.  К счастью %(dragon_name_full)s способен пережить даже такую рану."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n Закалённая стрела с чёрным древком влетает в пасть дракону и проходит точно в мозг. %(dragon_name_full)s падает замертво."]
        ]
    },

    'knight': {
        'name': u"Рыцарь",  # название моба применяемое в описании
        'descriptions': [
            [['foe_intro'], u"%(foe_name)s готовится к бою."],
            [['foe_fear'], u"(you win [fear]) \n %(foe_name)s бежит в страхе."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s побеждает"],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(foe_name)s наностит дракону ранение, но %(dragon_name)s побеждает"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(foe_name)s наносит дракону серьёзную рану"],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(foe_name)s метким ударом сносит голову дракону"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран"]
        ],
    },
    
    'king': {
        'name': u"Рыцарь-чемпион",  # название моба применяемое в описании
        'power': {'base': (5, 2)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'king',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"%(dragon_name_full)s прорывается сквозь ряды телохранителей чтобы разить короля людей."],
            [['foe_fear'],  u"(you win [fear]) \n Храбрый король рвётся в бой, но его конь слишком напуган - он встаёт на дыбы и сбрасывает наездника в грязь, оставляя его совершенно беззащитным."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s ловко уворачивается от острого наконечника копья и хлёстким ударом на противоходе вышибает короля из седла."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_type_cap)s и король людей со страшным грохотом сшибаются грудь на грудь. Августейший всадник опрокидывается вместе с конём, но и %(dragon_name)s получает ранение."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Таранный удар копья помноженный на вес и скорость коня со всадником отбрасывает дракона в сторону."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Противники сталкиваются под скрежет металла и ржание боевого коня, но силы примерно равны.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Король людей метким ударом сносит голову дракону, однако это ещё не конец."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n Король людей метким ударом сносит голову дракону. %(dragon_name_full)s умирает."]
        ]
    },
    
    'kraken': {
        'name': u"Кракен",  # название моба применяемое в описании
        'power': {'base': (6, 3)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 3)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'kraken',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Враг готовится к бою"],
            [['foe_fear'],  u"(you win [fear]) \n Враг бежит в страхе"],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s побеждает"],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Враг наностит дракону ранение, но %(dragon_name)s побеждает"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Враг наносит дракону серьёзную рану"],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Враг метким ударом сносит голову дракону"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран"]
        ]
    },

    'merman': {
        'name': u"Страж мелководья",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (1, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'merman',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Рыбо-человек готовит к бою сеть и трезубец. Он не сдастся просто так..."],
            [['foe_fear'],  u"(you win [fear]) \n Рыбохвостый в страхе уплывает на глубину, выронив трезубец."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Легко уйдя от удара трезубца, %(dragon_type)s мертвой хваткой впивается в рыбохвостого. Морская вода становится красной от крови."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Подводный воин встречает атаку дракона точным ударом трезубца, но даже раненый %(dragon_name)s способен растерзать его за несколько секунд."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Используя свою необычайную гибкость и маневренность рыбохвостый ухитряется ударить дракона своим трезубцем и уйти от ответного выпада."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Некоторое время оба противника маневрируют в толще воды, но никто не может знаять позиции выгодной для сближения и точного удара.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Разогнавшись несколькими ударами своего мощного хвоста подводный житель вонзает свой зазубренный трезубец глубоко в пасть дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран."]
        ]
    },

    'militia': {
        'name': u"Отряд ополчения",  # название моба применяемое в описании
        'power': {'base': (2, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'militia',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Вооруженные копьями, топорами и факелами ополченцы сбиваются в плотную толпу, подбадривая друг-друга агрессивными выкриками."],
            [['foe_fear'],  u"(you win [fear]) \n Толпа собравшихся было дать отопор чудовищу ополченцев разбегается в страхе, едва только %(dragon_name_full)s приближается к ним на расстояние удара."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Дезорганизованные ополченцы не способны долго сопротивляться натиску дракона. Некоторым удаётся убежать, но большинство остаются лежать бездыханными."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Ворвавшись в хлипкое построение ополченцев %(dragon_type)s устравивает настоящую резню. Однако люди сражаются на удивление храбро, после такой победы %(dragon_name)s вынужден зализывать раны."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n При достаточном количестве и боевом духе даже слабо обученные новобранцы становятся серьёзной боевой силой. Им удаётся ранить и отбросить дракона градом ударов своего немудрёного оружия."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s врывается в жидкое построение ополченцев, но те тут же бросаются в рассыпную. Пока он занимается одним врагом, другой заходит сзади. Крики и дым чадащих факелов сбивают с толку. Этот бой грозит затянуться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Джий детина с топором лесоруба улучив момент запрыгивает израненому дракону на спину и мощным ударом отсекает одну из его голов!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран. Крестьяне воспоют этот день в веках!"]
        ]
    },

    'mob': {
        'name': u"Крестьяне",  # название моба применяемое в описании
        'power': {'base': (1, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (5, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'mob',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Вооруженные вилами, дрынами и факелами крестьяне сбиваются в плотную толпу, подбадривая друг-друга агрессивными выкриками."],
            [['foe_fear'],  u"(you win [fear]) \n Толпа собравшихся было дать отопор чудовищу крестьян разбегается в страхе, едва только %(dragon_name_full)s приближается к ним на расстояние удара."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Дезорганизованные крестьяне не способны долго сопротивляться натиску дракона. Некоторым удаётся убежать, но большинство остаются лежать бездыханными."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Ворвавшись в толпу крестьян %(dragon_type)s устравивает настоящую резню. Однако люди сражаются на удивление храбро, после такой победы %(dragon_name)s вынужден зализывать раны."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n При достаточном количестве и боевом духе даже необученные крестьяне становятся серьёзной боевой силой. Им удаётся ранить и отбросить дракона градом ударов своего немудрёного оружия."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_type_cap)s врывается в толпу крестьян, но те тут же бросаются в рассыпную. Пока он занимается одним врагом, другой заходит сзади. Крики и дым чадащих факелов сбивают с толку. Этот бой грозит затянуться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Джий детина с топором лесоруба улучив момент запрыгивает израненому дракону на спину и мощным ударом отсекает одну из его голов!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран. Крестьяне воспоют этот день в веках!"]
        ]
    },

    'mounted_guard': {
        'name': u"Конные телохранители",  # название моба применяемое в описании
        'power': {'base': (5, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'mounted_guard',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Закованные в стальные доспехи кавалеристы разворачиваются цепью и опускают пики параллельно земле."],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s издаёт ужасающий рёв и кони бросаются в рассыпную, сбрасывая и топча собственных всадников."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Один за другим тяжелые всадники атакую дракона, но %(dragon_name)s ловко уклоняется от этих неуклюжих и прямолинейных атак. Щёлкая хвостом словно иполинским кнутом %(dragon_type)s вышибает кавалеристов из седла."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s способен опрокинуть всадника вместе с лошадью одним ударом, но их много, поэтому невредимым из битвы ему выйти не удаётся."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s отвлекается на одного из всадников и не замечает как второй проезжает совсем рядом, на всём скаку всаживая свою гранёную пику в бок ящера."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Всадники ловко маневрируют, избегая клыков дракона и пытаясь достать его своими длинными пиками. Такая тактика вряд ли принесёт им победу, зато сохраняет жизнь.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s сбивает бронированного скакуна с ног и бросается к всаднику чтобы растерзать его, но тот резво вскакивает на ноги и наносит точный удар остро отточенным мечём. Голова дракона падает на землю. Как хорошо что в запасе есть ещё головы..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В жаркой схватке %(dragon_type)s побеждает, но одна из его голов остаётся валяться на поле, отрубленная тяжелым кавалерийским палашом."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s сражается очаянно, но всадников слишком много. Убив много людей и коней, %(dragon_name_full)s в конце концов падает наземь, истекая кровью."]
        ]
    },


    'ogre': {
        'name': u"Людоед",  # название моба применяемое в описании
        'power': {'base': (7, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['poison_immunity'],  # особые модификаторы
        'image': 'ogre',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Великан-людоед сжимает в руках огромную дубину, больше похожую на вырванное с корнем дерево."],
            [['foe_fear'],  u"(you win [fear]) \n Разглядев врага людоед тушуется и отступает."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Неуклюжий великан наносит мощные но медленнные удары, от которых легко уклониться стоит лишь поймать ритм. Двигаясь совно струящаяся ртуть %(dragon_name)s нападает раз за разом, вырывая из жирного тела огра кровавые куски. У людоеда нет ни малейшего шанса..."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Не рискуя сражаться на дистанции удара дубины %(dragon_type)s накидывается на огра, сцепляясь вполотную. Это обеспечивает победу, хотя даже в таком положении великану удаётся нанести дракону несколько мощных ударов кулаками."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Размашистый удар гигантской дубины отбрасывает дракона в сторону. %(dragon_name)s шипит от боли."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Огр рычит и размахивает огромной дубиной словно тростинкой во все стороны. Сближаться с ним опасно и %(dragon_type)s вертится вокруг, выжидая удобного момента для нападения.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Удар комелем великанской дубинки настолько селен что ломает шею дракона и сносит одну из его голов начисто. К счастью %(dragon_name_full)s способен то пережить."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В жестокой схватке с людоедом %(dragon_type)s побеждает, но одна из его голов разбита могучим ударом великанской дубины."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_name)s сражается храбро, но людоед берет верх. Его огромная дубина взлетает и опускается раз за разом, пока ящер непревращается в жуткое месиво из крови и костей..."]
        ]
    },

    'old_knight': {
        'name': u"Старый рыцарь",  # название моба применяемое в описании
        'power': {'base': (4, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (2, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'knight/knight1',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Старый рыцарь водружает на голову похожий на ведро шлем и берёт в руки двуручный меч с потёртой рукоятью. Он полон решимости защитить свой дом."],
            [['foe_fear'],  u"(you win [fear]) \n Увидев с каким врагом ему предстоит сразиться, старый рыцарь бежит с поля боя побросав оружие."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s яростно атакует рыцаря, сминая его доспехи словно бумагу. Старик слишком медлителен чтобы победить в бою с драконом - его лучшие годы давно позади."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Хлёстким ударом хвоста %(dragon_name)s вышибает меч из рук старого рыцаря и набрасывается чтобы добить. Но прежде чем испустить дух, ветеран успевает воткнуть в брюхо дракону кинжал!"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Большой боевой опыт позволяет старому рыцарю очень точно рассчитать момент атаки. Едва %(dragon_type)s бросается вперёд, как его встречает точный взмах двуручного меча."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Большой боевой опыт позволяет старому рыцарю очень точно рассчитать момент атаки. Едва %(dragon_type)s бросается вперёд, как его встречает точный взмах двуручного меча. %(dragon_name_full)s теряет одну из голов."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран."]
        ]
    },


    'palace_guards': {
        'name': u"Гвардейцы",  # название моба применяемое в описании
        'power': {'base': (5, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'castle_guard',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Дворец охраняют элитные королевские гвардейцы. Они отважно выходят на сраждение с драконом, не желая отсиживаться за стенами."],
            [['foe_fear'],  u"(you win [fear]) \n При виде атакующего дракона элитные королевские гвардецы в страхе разбегаются кто куда. Ворота крепости остались открытыми нараспашку..."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s врывается в построение гвардейцев и начинает рвать их на куски. Даже королевские рыцари не могут оказать достойного сопротивления такому жуткому натиску."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s врывается в построение гвардейцев и начинает рвать их на куски. Тяжело вооруженные бойцы держатся достойно, но %(dragon_type)s хоть и раненый выходит из битвы пбедителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Применяя грамотную тактику взаимодействия, королевские гвардейцы ухитряются дать дракону серьёзный отпор и даже наносят ему ощутимые раны. Пара бойцов падает мертвыми, но остальные полны решимости."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Королевские гвардейцы сражаются отчаянно и на некоторое время им удаётся сдержать яростный напор дракона.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s атакует без оглядки и пропускает нескольких тяжело вооруженных гвардейцев себе за спину. Эта ошибка стоит ему головы. Одной из..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s жестоко изранен и победа над гвардейцами даётся ему нелегко. Одна из голов получила отрублена ударом тяжелого двуручного меча."],
            [['dragon_dead'], u"(you lose) \n Гвардейцы набрсываются все разом и отчаянно молотят дракона своими золочёными мечами. Израненный %(dragon_type)s в последнем порыве ярости ухитряется убить нескольких врагов, но их слишком много. %(dragon_name_full)s падает наземь и испускает последний дух."]
        ]
    },
    
    'shark': {
        'name': u"Акула",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (3, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'shark',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Акула плавает кругами и скалит зубы."],
            [['foe_fear'],  u"(you win [fear]) \n Акула пытается уплыть, но %(dragon_type)s плавает быстрее и настигает хищницу ставшую в одночасье его добычей."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Схватив акулу за жабры %(dragon_name)s полностью подавляет её сопртивление, ведь кроме как кусаться морская хищница ничего не умеет."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Два жутких морских хищника сплетаются в глубине терзая друг друга зубами. Солёная вода окрашивается кровью, но %(dragon_name)s выходит из схватки победителем."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Используя свою скорость и манеёвренность, акула скрывается в мутной толщи воды, а затем внезапно проплывает мимо на ходу выдирая у дракона кусок плоти!"],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Два жутких морских хищника кружат в толще воды, пытаясь зайти друг-другу со спины, но пока что они равны...",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Акула откусывает одну из голов дракона!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран."]
        ]
    },


    'ship': {
        'name': u"Корабль",  # название моба применяемое в описании
        'power': {'base': (3, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'ship',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"На палубе торгового корабля слышны отчаянные свистки боцманской дудки. Канониры спешно выкатывают пушки."],
            [['foe_fear'],  u"(you win [fear]) \n Подняв все паруса какие только есть, торговый корабль разворачивается по ветру и уходит на максимальной скорости прочь от дракона. Но он слишком тяжело гружен, так что это ошибка. После недолгой погони %(dragon_name_full)s. настигает и топит судно."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Скрывшись в толще вод %(dragon_name)s подплывает под днище корабля и взяв макимальный разгон пробивает в нём дыру. Теперь можно отлавливать пытающихся спастись моряков по одному."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s уходит на глубину, но недостаточно быстро. Торговый корабль успевает дать один залп и чугунное ядро ломает дракону ребро. Разъярённый %(dragon_type)s вырывает кусок из обшивки корабля ниже ватерлинии. Вода стремительно заполняет трюмы - судно обречёно."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Слаженный залп бортовых орудий накрывает дракона и отбрасывает его прочь, вздымая столбы бурлящей воды."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_name)s ныряет под корабль и пытается пробить дыру в обшивке ниже ватерлинии, но безуспешно.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Начинённая дымным порохом чугунная бомба попадает одной из голов дракона прямо в лоб. От такой раны будет трудно опавиться..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s забирается на палубу корабля и устраивает матросам кровавую баню. Люди в панике разбегаются и увлеченный погоней %(dragon_name)s слишком поздно замечает забравшегося на рею капитана. Тот прыгает сверху и сносит палашом одну из голов дракона. К сожалению для него, этого недостаточно для победы. Команда галеона обречена."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s слишком слаб чтобы выдержать ещё один залп корабельной артилерии. Измочаленный чугунными ядрами %(dragon_type)s  безвольно уходит на глубину, не в силах больше цепляться за жизнь."]
        ]
    },


    'steamgun': {
        'name': u"Паровая пушка",  # название моба применяемое в описании
        'power': {'base': (5, 5)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'steamgun',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Цверги возятся у паровой пушки подготавливая её к стрельбе."],
            [['foe_fear'],  u"(you win [fear]) \n Услышав громогласный рёв дракона рассчёт паровой пушки в ужасе разбегается и мощная боевая машина остаётся стоять бесполезной грудой хлама."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Двигаясь зигразами %(dragon_name)s приближается к паровой пушке избегая её смертоносных снарядов. Когда дистанция сокращаетяс до минимума рассчёт в панике пытается скрытья, но уже поздно..."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Решив одним ударом покончить с ненавистной боевой машиной %(dragon_type)s разносит её в в щепки, но взыв парового котла наносит больше вреда чем вся предыдущая стельба!"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Фугасный снаряд попадает точно в грудь дракона, отбрасывая его прочь от паровой пушки."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Паровая пушка раскочегарелась и ведёт непрерывный плотный огонь. %(dragon_name)s маневрирует не решаясь приблизиться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Один из мощных фугасных снарядов попадает прямо в голову дракона, разнося её в кровавые ошмётки."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Один из мощных фугасных снарядов попадает прямо в голову дракона, разнося её в кровавые ошмётки, однако %(dragon_name_full)s не останавливается и прорывается вплотную к пушке чтобы добраться до беззащитного рассчёта."],
            [['dragon_dead'], u"(you lose) \n Измочаленный фугасами %(dragon_name)s сбавляет скорость и спотыкается. Он не в силах больше сражаться. Послендний снаряд разывает его единственную живую голову в клочья."]
        ]
    },

    'templars': {
        'name': u"Крестоносцы",  # название моба применяемое в описании
        'power': {'base': (8, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'templars',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Закованные в стальные доспехи крестоносцы разворачиваются цепью и опускают пики параллельно земле."],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s издаёт ужасающий рёв и кони крестоносцев бросаются в рассыпную, сбрасывая и топча собственных всадников."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Один за другим крестоносцы атакую дракона, но %(dragon_name)s ловко уклоняется от этих неуклюжих и прямолинейных атак. Щёлкая хвостом словно иполинским кнутом %(dragon_type)s вышибает кавалеристов из седла."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s способен опрокинуть всадника вместе с лошадью одним ударом, но их много, поэтому невредимым из битвы ему выйти не удаётся."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s отвлекается на одного из крестоносцев и не замечает как второй проезжает совсем рядом, на всём скаку всаживая свою гранёную пику в бок ящера."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Крестоносцы ловко маневрируют, избегая клыков дракона и пытаясь достать его своими длинными пиками. Такая тактика вряд ли принесёт им победу, зато сохраняет жизнь.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s сбивает бронированного скакуна с ног и бросается к всаднику чтобы крестоносцы его, но тот резво вскакивает на ноги и наносит точный удар остро отточенным мечём. Голова дракона падает на землю. Как хорошо что в запасе есть ещё головы..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В жаркой схватке %(dragon_type)s побеждает, но одна из его голов остаётся валяться на поле, отрубленная благословлённым мечем."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s сражается очаянно, но крестоносцев слишком много. Убив много людей и коней, %(dragon_name_full)s в конце концов падает наземь, истекая кровью."]
        ]
    },

    'titan': {
        'name': u"Титан",  # название моба применяемое в описании
        'power': {'base': (8, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (8, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['lightning_immunity', 'slatk_2up'],  # особые модификаторы
        'image': 'titan',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Закованный в золотистый доспех титан призывает силы бури и грома. Он способен биться с равной силой магией и оружием!"],
            [['foe_fear'],  u"(you win [fear]) \n Даже богоподобный титан бежит в страхе когда его атакует %(dragon_name_full)s!"],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name)s прорывается сквозь снопы молний и ураганный ветер словно не замечая их. Титан прикрывается щитом и выставляет вперёд копьё, но %(dragon_type)s подсекает его подлым ударом хвоста, после чего набрасывается на потерявшего равновесие и беззащитного великана. "],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Небо темнеет и в воздухе разносится запах грозы, когда два исполина сталкиваются в смертельной битве. Титан разит молниями и волшебным копьём, нанося дракону раны, однако %(dragon_name_full)s оказывается сильнее. Поверженный гигант падает наземь, истекая ярко-синей кровью."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Титан мечет в дракона целый сноп искрящихся молний и сдувает его прочь порывом ураганно ветра."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Могучие порывы ветра защищают титана, не давая дракону приблизиться на расстояние удара.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Израненный %(dragon_type)s с трудом прорывается вплотную к великану сквозь порывы штормового ветра, но Титан встречает его метким ударом копья прямо в открытую пасть!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_name_full)s сражается из последних сил с невероятной яростью и злобой. Титан бьёт наверняка, пронзя одну из голов, но всё же не может остановить ярость дракона и падает на землю."],
            [['dragon_dead'], u"(you lose) \n Титан призывает силу бури в своё копьё и пронзает им израненного дракона. %(dragon_name_full)s темнеющим взором смотрит на торчащее в его груди чёрное древко, толстое словно вековой дуб."]
        ]
    },

    'town': {
        'name': u"Защитники города",  # название моба применяемое в описании
        'power': {'base': (4, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (6, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'town',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Защитники города занимают места на стенах. Они готовят копья, тяжелые камни и котлы с кипящей смолой."],
            [['foe_fear'],  u"(you win [fear]) \n Разглядев дракона получше защитники города дрогнули. Они в панике бегут со стен и прячутся кто-куда, а битва выиграна даже не начавшись."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Под градом почти безполезных камней, стрел и копий %(dragon_name_full)s подбирается к воротам и вложив весь свой вес в несколько таранных ударов, высаживает их. Оставшиеся без прикрытия воины на стенах беззащитны перед яростью дракона."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Под градом камней, стрел и копий %(dragon_name_full)s подбирается к воротам и вложив весь свой вес в несколько таранных ударов, высаживает их. Оружие защитников оставилиона теле дракона раны, но теперь когда врата пали его уже ничто не остановит."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Поток копий, камней и стрел обруженный защитниками города со стен и башен так силён, что дракону приходится отступить от ворот. Взять этот город не так просто..."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_type_cap)s налегает на ворота всем весом, пытаясь выбить их в то вреям как защитники города поливают его со стне потокм камней, стрел и копий. Но и то и другое совершенно бесполезно. Копья отскакиваю от прочной чешуи дракона, но и окованные сталью врата не желают поддаваться.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Пятеро дюжих защитников сбрасывают со стены толстенный ствол дерева, который придавливает одну из голов дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Пятеро дюжих защитников сбрасывают со стены толстенный ствол дерева, который придавливает одну из голов дракона, однако это им не помогает. Разъярённый %(dragon_type)s вышибает ворота и врывается на улицы города."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s слишком изранен и устал для такой битвы. Всего один метко сброшенный со стены камень прерывает его штурм. Отважные защитники города торжествуют победу, в то вреям как %(dragon_name_full)s издыхает у так и не поддавшихся напору врат."]
        ]
    },

    'treant': {
        'name': u"Чащобный страж",  # название моба применяемое в описании
        'power': {'base': (12, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (8, 2)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'treant',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Напоминающее по форме человеческое тело дерево выглядит устрашающе. Его узловатые руки-ветви тянутся к шее дракона."],
            [['foe_fear'],  u"(you win [fear]) \n Выворачивая из земли ноги-корни, человекоподобное дерево бросается наутёк, пытаясь скрыться в лесной чащие. За ним остаётся широкий след вспаханной земли."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s побеждает"],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Враг наностит дракону ранение, но %(dragon_name)s побеждает"],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Враг наносит дракону серьёзную рану"],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Бой продолжается некоторое время но никто не может взять верх",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Враг метким ударом сносит голову дракону"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран"],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает от полученных ран"]
        ]
    },

    'triton': {
        'name': u"Тритон",  # название моба применяемое в описании
        'power': {'base': (7, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (7, 1)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'triton',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Морской гигант поводит своим исполинским трезубцем и вода подчиняется его движению, завихряясь водоворотами и вскипая брулящей пеной. Тритон повелевает пучиной!"],
            [['foe_fear'],  u"(you win [fear]) \n Тритон вздымает свой волшебный трезубец и призывает огромный косяк тунца. Тела рыб скрывают его на минуту, а когда они уплывают прочь, его уже нигда не видно. Сбежал трус!"],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Тритон создаёт бурлящий водоворот пытаясь утянуть дракона на дно, но %(dragon_name)s преодолевает силу потока и впивается в ошарашенного тритона зубами."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Прорвавшись сквозь стремительный водоворот, %(dragon_name)s бросается на тритона. Тот ударяет трезубцем и удачно, однако разъярённого дракона это не останавивлает. %(dragon_name)s разрывает морского великана в клочья."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_name)s не в силах справиться с колдовским водоворотом тритона и бурлящая вода бросает его боком на острые рифы."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n %(dragon_name)s тщетно пытается пробиться к тритону, но бурлящий водоворот воды раз за разом относит его прочь и затягивает на глубину.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Тритон метко бьёт дракона своим трезубцем в шею, насаживая его на острия словно рыбу."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Два морских исполина стоят друг друга в схватке. С огромным трудом %(dragon_type)s побеждает, но одна из его голов умирает, пробитая насквозь огромным трезубцем тритона."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_name)s больше не в силах сопротивляться магическому водовороту. Неумолимый поток воды уносит его в холодную и тёмную глубину."]
        ]
    },

    'wizard': {
        'name': u"Чародей",  # название моба применяемое в описании
        'power': {'base': (5, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (1, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': ['sfatk_up', 'siatk_up', 'slatk_up'],  # особые модификаторы
        'image': 'wizard',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Волшебник делает странные пассы руками, накладывая на себя защитные заклинания."],
            [['foe_fear'],  u"(you win [fear]) \n Волшебник оценивает ситуацию и решает использовать экстренную телепортацию, чтобы убежать подальше от разъярённого дракона."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Колдун использует заклинание огненного шара, но колдовское пламя бессильно. Прорвавшись прямо сквозь огонь, %(dragon_type)s давит тщедушного старикашку как клопа!"],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Колдун стреляет стрелами чистой магической силы, с лёгкостью пробивающими чешую дракона. Но даже раненый %(dragon_name)s способен разорвать тщедушного старикашку на кровавые лоскуты."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Колдун призывает призрачный кулак огромных размеров, который припечатывает дракона ударом сверху тяжклым словно гружёная рудой вагонетка."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Колдун призывает каменного элементаля себе на защиту. %(dragon_name_full)s справляется с духом земли за считанные минуты, но волшебник всё ещё цел и невредим.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Волшебник призывает меч сотканный из чистой колдовской энергии. Клинок летает и рубит сам по себе, а его лезвие настолько остро что начисто отсекает одну из голов дракона."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n Волшебник призывает меч сотканный из чистой колдовской энергии. Клинок летает и рубит сам по себе, а его лезвие настолько остро что начисто отсекает одну из голов дракона. Однако колдуну это не помогает, выживший после сьтрашной раны %(dragon_name)s давит его как таракана."],
            [['dragon_dead'], u"(you lose) \n Израненный и ослабленный %(dragon_type)s представляет собой отличную мишень. Колдун вызывает сферу тотальной анигилляции 9-го уровня, которая пожирает тело ящера подобно миниатюрной чёрной дыре."]
        ]
    },

    'xbow': {
        'name': u"Арбалетчики",  # название моба применяемое в описании
        'power': {'base': (4, 0)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'xbow',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Арбалетчики спешно заряжают оружие, готовясь стрелять."],
            [['foe_fear'],  u"(you win [fear]) \n Арбалетчики даже не пытаются вступить в бой, а прсото разбегаются в ужасе."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Стремительно сократив дистанцию %(dragon_type)s врывается в жидкое построение арбалетчиков и раскидывает их словно тряпичные куклы."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n Проравшись сквозь слаженный залп арбалетчиков, %(dragon_type)s врывается в их построение и раскидывает людей словно тряпичные куклы. Тем не менее несколько арбалетных болтов пробили его шкуру и теперь придётся зализывать раны."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n Слаженный залп арабалетчиков оказывается настолько эффективен, что %(dragon_type)s вынужден умерить свой пыл."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Арбалетчики прячутся за естественными преградами ведя огонь из укрытия, достать их по одному можно но это займёт очень много времени.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n Тяжелая железная стрелка влетает точно в глаз дракону. Это ранение будет стоить ему одной головы!"],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n %(dragon_type_cap)s побеждает, но одна из его голов умирает от полученых ран."],
            [['dragon_dead'], u"(you lose) \n %(dragon_name_full)s умирает расстрелянный из тяжёлых арбалетов в упор."]
        ]
    },

    'xbow_rider': {
        'name': u"Конные арбалетчики",  # название моба применяемое в описании
        'power': {'base': (4, 1)},  # сила атаки моба (обычная, верная)
        'defence': {'base': (4, 0)},  # надежность защиты моба (обычная, верная)
        'modifiers': [],  # особые модификаторы
        'image': 'xbow_rider',  # фоновое изображение для драки в "img/scene/fight/%s.jpg"
        # набор описаний сцены боя
        'descriptions': [
            [['foe_intro'], u"Конные арбалетчики рассыпаются цепью, готовые к бою"],
            [['foe_fear'],  u"(you win [fear]) \n %(dragon_name_full)s издаёт ужасающий рёв и кони бросаются в рассыпную, сбрасывая и топча собственных всадников."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n Один за другим всадники разряжают свои арбалеты, но %(dragon_name)s даже не замечает летящих в него стрел. Одного за другим %(dragon_type)s сбивает всадников с ног и терзает их зубами."],
            [['foe_dead', 'dragon_wounded'], u"(difficult victory) \n %(dragon_name)s способен опрокинуть всадника вместе с лошадью одним ударом, но их много, поэтому невредимым из битвы ему выйти не удаётся."],
            [['foe_alive', 'dragon_wounded'], u"(wounded) \n %(dragon_type_cap)s отвлекается на одного из всадников и не замечает как второй проезжает совсем рядом, на всём скаку всаживая арбалетный болт в уязвимый бок ящера."],
            [['foe_alive', 'dragon_undamaged'], u"(stallmate) \n Всадники ловко маневрируют, избегая клыков дракона и пытаясь достать его выстрелами из арбалетов с изрядного расстояния. Такая тактика вряд ли принесёт им победу, зато сохраняет жизнь.",],
            [['foe_alive', 'lost_head'], u"(head lost) \n %(dragon_type_cap)s сбивает скакуна с ног и бросается к всаднику чтобы растерзать его, но тот резво вскакивает на ноги и наносит точный удар остро отточенным мечём. Голова дракона падает на землю. Как хорошо что в запасе есть ещё головы..."],
            [['foe_dead', 'lost_head'], u"(difficult victory) \n В жаркой схватке %(dragon_type)s побеждает, но одна из его голов остаётся валяться на поле, отрубленная тяжелым кавалерийским палашом."],
            [['dragon_dead'], u"(you lose) \n Израненный %(dragon_type)s сражается очаянно, но всадников слишком много. Убив много людей и коней, %(dragon_name_full)s в конце концов падает наземь, истекая кровью."]
        ]
    },

}