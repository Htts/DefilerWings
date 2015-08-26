# coding=utf-8
# Here we keep game texts
python early:
    from pythoncode import data
     
    chance_win_texts = {
        0: "{color=#ff0000}miserable{/color}",
        10: "{color=#ff00ff}low{/color}",
        30: "{color=#0000ff}acceptable{/color}",
        60: "{color=#EAC117}good{/color}",
        90: "{color=#00ff00}splendid{/color}"
    }
    
    chance_wound_texts = {
        0: "{color=#00ff00}minimal{/color}",
        10: "{color=#EAC117}acceptable{/color}",
        30: "{color=#0000ff}average{/color}",
        60: "{color=#ff00ff}considerable{/color}",
        90: "{color=#ff0000}immense{/color}"
    }
    
    def show_chances(foe):
        """
        Вывод шансов победы и ранения дракона для игрока 
        """
        chance = battle.victory_chance(game.dragon, foe)
        chance_win = data.get_description_by_count(chance_win_texts, chance)

        chance = battle.victory_chance(foe, game.dragon)
        chance_wound = data.get_description_by_count(chance_wound_texts, chance)
        
        return " Chance to win: %s.\n Danger: %s." % (chance_win, chance_wound)

    # Описания дракона
    hunger_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Overfed{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Full{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Hungry{/color}{/font}',
        3: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Starving{/color}{/font}'
    }

    lust_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Exhaused{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Aroused{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Horny{/color}{/font}',
        3: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Lustful{/color}{/font}'
    }

    bloodlust_texts = [
        '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Placid{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ccccff}Calm{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Tense{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Annoyed{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Angry{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Furious{/color}{/font}'
    ]

    health_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Half-dead{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Wounded{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Healthy{/color}{/font}'
    }

    womennum = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
    
    # Описания эффекта события на дурную славу
    reputation_rise = [
        'People will notice this evil deed.',
        'News of the dragon\'s notorious acts spread throughout the Kingdom.',
        'Today the dragon gained great infamy.',
        'All inhabitants of the kingdom will hear about this action and be terrified.',
        'Such a terrible act will live in legends for hundreds of years.'
    ]

    # Описание деревень
    village = {
        'overview': [
            u'Abandoned settlement',
            u'Single farm. The people here have no protection except a large chained dog.',
            u'Small village. Seeing the approach of the dragon people grab any materials at hand which can be used as improvised weapons, and look for safety in numbers.',
            u'Village. A ship\'s bell rings desperately as the dragon is noticed from afar. Residents quickly organize into militias.',
            u'Large village. The bell of a church urges people to take cover, and a detachment of crossbowmen files onto the main street.',
            u'Town. As the dragon approaches the gates are hastily closed, and warriors armed with bows and spears rise up on the walls.'
        ],
        'deffence': [
            'dog',
            'dog',
            'mob',
            'militia',
            'xbow',
            'town',
        ]
    }

# Прыдстория игры
    intro_text = '{font=fonts/AnticvarShadow.ttf}{size=+10}    Long ago, in ancient times, the world was young and unspoiled. All five nations lived in peace and harmony, developing and prospering. The men of the plains planted endless fields of golden wheat, and on the hills they planted blooming gardens of sweet fruit. The children of the goddess Danu, wise and beautiful elves, wove maigc patterns of songs and moonlight deep in the vast forests. Skilled dwarves forged metal, and cut gems that shone like stars in the shadow of carved stone palaces. Mermaids played carelessly with silver fish and danced under the blue surface of the ocean. And even the giants, old as the world itself, did not harm the small nations, but instructed them in ancient knowledge.   {vspace=30}Those days passed without a trace, when evil came into the world. Nobody is sure where she came from. Naked, winged, beautiful, she was as lovely as a noon daydream and as terrible as a midnight nightmare. Tradition says she came out of the milk white morning fog that thickened in the depths of an impassible windbreak. Others believe she came from the pit of hell itself.   {vspace=30} Able to take on any shape, seductive or terrifying, she brought decay and strife. In an insatiable lust she sought out everyone she could find. She craved all male seed, from proud kings to peasants and filthy animals. In unnatural unions legions of creatures were spawned, deformed and vicious, cruel, greedy, and full of sin.  {vspace=30}With fear and hatred, the Mistress of Darkness forged an army and marched it to the free nations to enslave the whole world. The ruthless army of darkess left behind only corpses, ashes, and barren earth.     {vspace=30}But five free nations fought back. Gathering together, an army of men, elves, dwarves, mermaids, and giants defeated the dark forces and drove the Mistress\'s spawn into a barren volcanic land far to the east. Since then, to protect themselves, men have built impregnable fortress cities with high walls and towers, dwarves have created machines and engines of war, and elves have put spells of concealment on their groves and guards on their boundaries. Even carefree mermaids wield tridents and nets, ready to repel an attack.      {vspace=30}Looking at this irresistable alliance the Mistress vowed to create a monster of such power that no one in the world could stand before it. Breathing the poisonous fumes of the southern marshes, she took up the fattest snake which she could find and set aide three large eggs, from which she hatched a monster the likes of which had never been seen on the earth - a dragon.    {vspace=30}   All mortal sins merged into these creatures. The violent and bloodthirsty dragons know nothing of mercy and compassion. Their pride and envy makes them seek infamy, destroying all that is beautiful and spreading pain. In their insatiable lust they defile innocent girls, who like the Mistress give birth to more degenerate monsters. Voracious, they devour men, animals, fish and birds. Greedily they rake silver and gold into their fetid caves, hoarding treasure and sleeping it on for years, indulging in sloth and complacency.       {vspace=30}The first of the dragons were not very mighty, not much more than huge swamp snakes. But Mistress repeatedly selects the best, and incestuous, abominable intercourse generates new and constantly mutating offpsring. All larger, stronger, more vicious, and more insidious. If their race is not stopped, the day will come when the highest wall and largest army cannot stand against their might. Even the god-like titans in their strongholds could not sleep easy. But for now, hope is still alive... {/size}{/font}'

	
    # Названия мест
    toptxt = {
        'plain': u'THE COUNTRYSIDE \n\n'
    }

    # Тексты для энкаунтеров
    txt_enc_fair = [
        ['%(dragon_name)s notices colorful tents in a meadow. It\'s a big fair, which has brought together all the people from surrounding villages. Here they trade, talk, and show off their best animals and most eligible brides. Do something to make money!],
        ['%(dragon_name)s bursts into a crowd of peasants and utters a thunderous roar. People flee in terror, but the snake does not spend time chasing them all down, he needs only one woman - the most beautiful virgin, who had hoped to find a good groom. It\'s time for her to find out who is the best man in this village!']
    ]

# Тексты для особых мест
    txt_place_manor = [
        ['Not far from the road is a fortified stone manor - the manor of a poor knight. Inside could be some gold or a woman, so it pays to look closely.'],
        ['%(dragon_name)s sniffs. Inside, there is the clear scent of a virgin of noble blood and a little treasure. But it won\'t be gotten just yet, servants have noticed the approach of the dragon and now the owner of the manor hurriedly puts on his armor. The Old Knight won\'t give up without a fight!'],
        ['Ignoring the terrified fleeing servants, %(dragon_name)s searches the mansion in for valuables:'],
        ['In a spacious and brightly lit room on the second floor, the trembling daughter of the slain knight hides under the bed. But %(dragon_name)s can smell innocent flesh many miles away.'],
        ['The fortifications did not save the now-deserted mansion from your looting, but strong walls can serve as a good protection for a dragon\'s treasure. A small enough dragon could arrange a cozy lair in the wine cellar, you just have to squeeze through the narrow door.'],
        ['%(dragon_name)s gives a victory roar. No one else stands in his way and the knightly manor is defenseless.']
    ]

    txt_place_wooden_fort = [
        ['On a hill near the road stands a wooden fort. %(dragon_name)s decides to scout out what\'s inside.'],
        ['This wooden fort was build in the usual way - a large courtyard surrounded by a moat and palisade, dominated by the tower built on a man-made mound. The garrison consists of ordinary foot soldiers, and the owner isn\'t present. From the top floor of the tower comes the scent of a virgin.'],
        ['The resistance of the defenders is broken. Just a minute is needed to tear down the gates of the tower on the hill and burst inside. Servants flee in terror, but %(dragon_name)s pays them no attention, methodically stripping the place of everything of value:'],
        ['On the top floor of the front room, a young maiden and a old nurse woman huddle in fear in the corner. %(dragon_nam_full)s smacks the old woman with a flick on the tail and turns his head to the girl.'],
        ['The wooden walls are in poor condition, but the tower on the hill still stands. In the main hall you can make a den and dump treasures, and keep captive maidens on the upper floors. Not a great place for a den, but better than a ravine or a hole in the ground.'],
        ['%(dragon_name)s gives a victory roar. No one else stands in the way, the fort on the hill is now defenseless.']
    ]
    
    txt_place_abbey = [
        ['In the distance are seen walls and towers, but it\'s not a fortress - it\'s a fortified monastery. Monks often collect treasures, almost like dragons. It is much more than they are able to protect, so it\'s worth a look.'],
        ['Pretty rich and well fortified convent. From inside comes the smell of gold, silver, and innocent women, but also something else...Knights Crusaders.'],
        ['The foolish nuns gathered everything of value in asingle room - near the altar where they pray. %(dragon_name)s takes the church\'s loot:'],
        ['At the rear of the monastery cells are nuns. Most of them are virgins, although many are old and rotten, but here and there is a special sweet smell. Focusing on it, %(dragon_name)s finds in the farthest cell a maiden of noble blood, who took vows of chastity as a nun - but now a quite different fate awaits!'],
        ['The old convent has strong and high walls, and a large dining room spacious enough to allow for a large den, even for a dragon. It may be a good idea to settle here.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the monastery is now defenseless.']
    ]

    txt_place_castle = [
        ['%(dragon_name)s spies a huge stone fortress from afar.'],
        ['Such heavily fortified castles with high walls and towers in the kingdom are rare. The dragon\'s instincts tell him there is a treasury full of gold and precious stones, and in the high tower noble maidens are languishing. It should be entertained, but the garrison will be hard to defeat.'],
        ['The central stronghold of the castle was protected by a sturdy gate that proved hard to break. Inside are valuable treasures:'],
        ['On the top floor of the front room, a young maiden and a old nurse woman huddle in fear in the corner. %(dragon_nam_full)s smacks the old woman with a flick on the tail and turns his head to the girl.'],
        ['The great stone castle has intact fortifications and many spacious rooms - an almost perfect place for the dragon\'s lair.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the mighty fortress is now defenseless.']
    ]
    
    txt_place_palace = [
        ['In the distance you can see a majestic fortified palace, this is clearly something worth attention!'],
        ['It appears that %(dragon_name)s found a royal castle. Such a mighty stronghold in the land of free people is very rare, and its owner must be a very rich lord. Of course many interesting things are inside... and a lot of protection.'],
        ['%(dragon_type)s quickly rushes to the treasury, eagerly shovelling piles of jewelry:'],
        ['Every self respecting palace must have a princess languishing, and of course there she is, on the top floor of the tallest tower.'],
        ['This recently depopulated palace is huge and perfectly placed. If you make your lair here, people will tremble at the mere mention of the name of the dragon who was so powerful that he took it for himself!'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the royal palace is now defenseless.']
    ]
    
    txt_place_enfr = [
        ['An elven castle. Bingo!'],
        ['The sacred tree of the elve, grown from a gift of the goddess Danu, is huge and immense. In its branches, under the roots and in the hollows, elves have arranged a splendid palace in which the king and queen reside. Inside reside many treasures, but a large forest guard protects this place, and will be difficult to combat.'],
        ['Elves carry their treasures on themselves, and here there are enough of them to borrow a few things from:'],
        ['%(dragon_name)s finds the Queen of the Elves.'],
        ['Now the grove is empty, but the old magic still glimmers in the trunk of the great tree, protecting the surrounding area. Here you can make a secret lair.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the elven forest palace is now defenseless.']
    ]
    
    txt_enc_forest_guardian = [
        ['%(dragon_name_full)s is wandering through the woods. Suddenly...'],
        ['A border guard with a bow appears. Elves carefully guard their sacred groves. Maybe he knows the way to the enchanted land.'],
        ['%(dragon_name)s triumphs. But trying to find the secret path that the guardian was protecting does not work...'],
        ['%(dragon_name)s cunning interrogation has revealed information about the secret paths, allowing him to enter the enchanted forest of the elves.']
    ]
    
    txt_place_jotun = [
        ['In this gigantic palace, built of blocks of ice, a frost giant - Jotun - lives in seclusion. Inside is the smell of treasure and a big woman, and this would be a great place for a lair. But the giant vigilantly guards his home.'],
        ['In the depths of the den is a frost giantess. Her womb would be an exceptional place for dragon seed.'],
        ['The ice citadel is now empty. Here you can make a perfect lair, with the protection of ice walls, steep mountains, and piercing frosty wind.']
    ]
    
    txt_place_ifrit = [
        ['Fortified forge, built of black obsidian blocks, located in the crater of an active volcano. Judging by the smell there is something valuable - but the fire giants - Ifrit - will not give up their treasures without a fight.'],
        ['The fire giantess tries to put up a fight, but it is much weaker than the men and not armed, so the Dragon can do with her whatever he wants.'],
        ['The volcanic forge of the molten giants is now empty. Here you can make a great den, because it is protected by thick walls, cliffs, and the unbearable heat of the magma lake.']
    ]

    txt_place_triton = [
        ['This is the underwater palace of Triton - the sea giant. Surely he has amassed a sizeabe treasure, but a giant is a serious opponent.'],
        ['In the luxuriously furnished underwater apartments, a giantess with a fish tail waits for her fate. It\'s a chance to produce mighty sea creatures!'],
        ['The umansion where the proud Triton once lived can be a good den for a water dragon. Few will be able to reach the underwater entrance.']
    ]
    
    txt_place_titan = [
        ['This island flies about the clouds thanks to the magic power of the lighting giant - Titan. The catle itself is striking in its monumental size and luxury. Surely untold riches await inside, but the Titans are one of the mightest enemies that one can face.'],
        ['The dragon goes to the scent of a woman. According to the custom of princesses, the giantess is sitting in a room on the top of the tower. It looks like she did not even hear the sounds of the battle down below!'],
        ['This is now an empty castle, once belonging to the mighty Titan. The old magic still keeps the island in the sky, floating above the clouds. Such a spacious, durable, and unreachable structure, it is difficult to imagine a better den.']
    ]
    
    #Сцены секса с госпожой в человеческом облике
    txt_human_mistress_fuck = {}
    txt_human_mistress_fuck['dragon remains'] = ['This is an error, the current dragon is dead',]
    txt_human_mistress_fuck['serpent'] = ['Mistress descended from her throne, at the same time taking human form and a suitable size - half that of her son. So that he could feel big and strong, but at the same time do what he was there to do. \n The sepent opened his mouth and licked his lips in anticipation, he had long dreamed of this moment. Snaking forward, %(dragon_name)s crawled to his feet and wrapped around Mistress with his body, climbing higher and higher with each turn until level with the bright scarlet lips of the woman. She groaned, squeezed by his strong scaly body, and the snake immediately launched his forked tongue into her mouth. Unwrapping the coils of its tail, the serpent moved between her legs as the Mistress spread them, both thrusting together simultaneously. \n The scaly serpent squeezed hard enough to crush any mortal woman, but Mistress only moaned in pleasure as she felt her son ram his inhuman member into her wet narrow folds. This passionate mating is repeated over and over again for many days and nights, until it becomes clear that in the womb of the Mistress new dragon eggs are maturing.',]
    txt_human_mistress_fuck['lindwurm'] = ['The mistress descended from her throne and looking her son straight into the eyes said, \"I\m yours. Do what you want. Throwing off his timidity, the lizard furiously roared and lashed out at the woman he desired for so long. Knocking her down with a well-aimed blow of the tail, he pushed her head to the grown and then roughly entered into her coveted womb. Though the Mistress had no foreplay before the penetration, inside it was hot and wet. For a second the dragon thought, was she also yearning for this moment, or did she only use magic to imitate lust? But the thought quickly vanished with the pleasure of animal penetration into her fertile but hitherto forbidden womb. The rapacious lizard vowed to rape his mother again and again, until the sperm poured from her everywhere, even from her ears...',]
    txt_human_mistress_fuck['flying serpent'] = ['%(dragon_name_full)s spread his mighty wings and soared to a high ceiling of the throne room. Mistress went to the center of the room and held her hands up, calling her son for a loving embrace. %(dragon_type)s dived at her like a hawk to its prey. The impact of bodies was so strong that the demonnss fell to the ground under the weight of the serpent. Quickly he wrapped his membranous wings around her lithe body, so that nothing could be seen from outside. \n But within the leathery cocoon boiled animal passion. \n Under the wings the writhing bodies paused as the serpent gave his first discharge in the womb of his mother, but not for long. A minute later, he spread his wings, and holding her in his scaly embrace soared once again to the ceiling. \n The serpent and the woman indulged in incestuous lovemaking on the floor, in the air, on land and in water countless times, but he did not release her from his embrance until her belly was round and heavy with new ripening snakes... ',]
	txt_human_mistress_fuck['hydra'] = ['%(dragon_name_full)s crept to the foot of the throne and stretched his neck to look at the Mistress from every side. In response, she held out her hands with a smile and put them on two of his snouts, holding onto them tightly. Realizing his mother\'s idea %(dragon_type)s rolled onto his back so that his cock pointed straight up a sharpened stake for an execution, while the demoness holding his muzzles was raised up in the air. %(dragon_name)s spread his necks sharply apart, and Mistress plunged down and was penetrated by the genitals of the beast. The two issued a cry of mixed pain and pleasure.  %(dragon_type)s twisted the writhing witch around on his cock, and lifted her again, amazed at how deeply he had driven into such a small body.\n In this bouncing dance %(dragon_name)s and his lustful mother spent many hot nights, until hebelly began to bulge from the ripening eggs of the next generation.',]
    txt_human_mistress_fuck['wyvern'] = ['Having took the form of an innocent and seductive maiden, Mistress faced the dragon and took off her clothes.  %(dragon_name_full)s grabbed her with his powerful wings, embracing her. Her hands slipped down the sharp scales of his chest, stomach, moving downwards to grope his cock.   %(dragon_name)s impatiently pushed his mother down and felt her greedily take his spine covered member into her slimy lips. Nobody would have believed that such an impressive organ would fit in sucha  small mouth, but the Mistress is capable of it. The proportions were made to fit within a milimiter, so that the moist pink flesh of her throat is completely filled by her son. In such a situation Mistress could neither breathe not moan, and could only stretch the muscles of her throat and move her head to enhance the pleasure of her son. \n In passionate embraces they will spend many more days and nights...',]
    txt_human_mistress_fuck['dragon'] = ['Приняв облик соблазнительной и невинной девы Владчица встала перед драконом и скинула свои одежды.  %(dragon_name_full)s обхватил её своими могучими крыльями и прижал к себе. Её руки заскользили по острой чешуе на его груди, животу, вниз нащупывая рванувшийся им на встречу из складчатой сумки половой орган.  %(dragon_name)s в нетерпении толкнул мать вниз и почувствовал как она жадно хватает губами его слизистый, покрытый мягкими шипами член. Никто бы не поверил что такой внушительный агрегат поместится в такой маленький ротик, но Владычица способна и не на такое. Пропорции её облика были подобраны с точностью до миллиметра, так чтобы влажная розовая плоть её сына заполнила всё горло целиком и с максимальной возможной плотностью. В такой положении Госпожа не могла ни дышать ни стонать, а могла лишь напрягать мышцы гортани и двигать головой чтобы усилить ощущения сына. \n В страстных объятьях они проведут ещё много сладких дней и ночей...',]
    txt_human_mistress_fuck['multi headed flying serpent'] = ['%(dragon_name_full)s расправил свои могучие крылья и взлетел к высокому потолку тронного зала. Владычица вышла в центр помещения и протянула руки вверх, призывая своего сына в любящие объятья. %(dragon_type)s спикировал на неё словно степной ястреб на добычу. Удар падающего сверху тела был так силён, что демоница рухнула на пол под весом змея. Тот быстро оплёл её своим гибким телом и замотал в кокон своих перепончатых крыльев, так что снаружи не было видно практически ничего. Но зато внутри этого кожистого кулька кипела животная страсть. \n Бугрящиеся и перекатывающиеся под крыльями тела замерли, когда змей испустил свой первый заряд в лоно матери, но не на долго. Через минуту он расправил крылья и не разжимая чешуйчатых объятий вновь взмыл под потолок, увлекая за совой свою любовницу. \n Змей и женщина предавались кровосмесительной любви на полу, в воздухе, на земле и в воде бессчётное количество раз, но ни разу не разомкнули объятья до тех пор, пока её живот не стал круглым и тяжёлым от зреющих внутри новых змеёнышей...',]
    txt_human_mistress_fuck['multi headed wyvern'] = ['%(dragon_name_full)s подобрался к подножию трона и вытянул шеи так чтобы разглядывать Владычицу с разу с нескольких сторон. В ответ она с улыбкой протянула руки и положила их на две его клыкастые морды, крепко сжимая пальцы. Поняв задумку матери %(dragon_type)s] перевернулся на спину так что его уд смотрел теперь точно вверх словно отточенный для казни деревянный кол, в то время как держащаяся за его морды демоница поднялась высоко в воздух. %(dragon_name)s резко развёл шеи в стороны и Владычица рухнула вниз, слёту напоровшись на мясистый детородный орган зверя. Двое издали вопль смешанной боли и наслаждения.  %(dragon_type)s обвил корчащуюся на его елдаке ведьму своими длинными шеями и  приподнял её, чтобы насадить снова, поражаясь тому насколько глубоко такое не крупное вроде бы тело способно вогнать в себя этот внушительный орган. \n Сплетаясь в танце страти %(dragon_name)s и его похотливая мать провели много горячих ночей, пока её живот не стал расти от зреющих внутри яиц нового поколения.',]
    txt_human_mistress_fuck['multi headed dragon'] = ['%(dragon_name_full)s подобрался к подножию трона и вытянул шеи так чтобы разглядывать Владычицу с разу с нескольких сторон. В ответ она с улыбкой протянула руки и положила их на две его клыкастые морды, крепко сжимая пальцы. Поняв задумку матери %(dragon_type)s перевернулся на спину так что его уд смотрел теперь точно вверх словно отточенный для казни деревянный кол, в то время как держащаяся за его морды демоница поднялась высоко в воздух. %(dragon_name)s резко развёл шеи в стороны и Владычица рухнула вниз, слёту напоровшись на мясистый детородный орган зверя. Двое издали вопль смешанной боли и наслаждения.  %(dragon_type)s обвил корчащуюся на его елдаке ведьму своими длинными шеями и  приподнял её, чтобы насадить снова, поражаясь тому насколько глубоко такое не крупное вроде бы тело способно вогнать в себя этот внушительный орган. \n Сплетаясь в танце страти %(dragon_name)s и его похотливая мать провели много горячих ночей, пока её живот не стал расти от зреющих внутри яиц нового поколения.',]
    
    #Сцены секса с госпожой в драконьем облике
    txt_dragon_mistress_fuck = {}
    txt_dragon_mistress_fuck['dragon remains'] = ['Это ошибка, текущий дракон мертв.',]
    txt_dragon_mistress_fuck['serpent'] = ['Владычица поднялась со своего железного трона и двинулась к сыну. Её тело неуловимо исказилось и вытянулось, принимая удлинённую форму. Два змея встали поднялись на хвостах и стали раскачиваться друг напротив друга, а затем сплели шеи. %(dragon_name)s выпустил свой раздвоенный язык, который тут же встретил такой же язык госпожи. \n Непостижимый для человеческих глаз, медленный и всепоглощающий танец любви двух великих змиев продлился много часов и дней...',]
    txt_dragon_mistress_fuck['lindwurm'] = ['Владычица крепко сжала подлокотники своего железного трона и %(dragon_name_full)s увидел как её изящные кисти преобразились в украшенные когтями чешуйчатые лапы. Вертикальные зрачки пересекли желтые глаза пополам и из её изменившегося горла раздалось призывное клокотание. Любой человек бежал бы в ужасе от этого зрелища, но %(dragon_type)s бросился вперёд, чтобы прикоснуться к единственной женщине на свете достойной стать матерью его детей. \n Жуткие ящеры набросились друг на друга, словно враги и от скрежета чешуи задрожали витражи в стрельчатых окнах большого зала. %(dragon_name)s повалил владычицу на землю и силой вошел в неё, схватив клыками за бронированный загривок. Их яростная страсть расцвела и излилась потоком, чтобы смениться нежностью чешуйчатых объятий. А затем вновь перетечь в сплетение когтей и чешуи. Так волна за волной шторм любви будет бушевать в тронном зале до тех пор пока во чреве демонической рептилии не зародится новая жизнь... ',]
    txt_dragon_mistress_fuck['hydra'] = ['Владычица крепко сжала подлокотники своего железного трона и %(dragon_name_full)s увидел как её изящные кисти преобразились в украшенные когтями чешуйчатые лапы. Вертикальные зрачки пересекли желтые глаза пополам и из её изменившегося горла раздалось призывное клокотание. Любой человек бежал бы в ужасе от этого зрелища, но %(dragon_type)s бросился вперёд, чтобы прикоснуться к единственной женщине на свете достойной стать матерью его детей. \n Жуткие ящеры набросились друг на друга, словно враги и от скрежета чешуи задрожали витражи в стрельчатых окнах большого зала. %(dragon_name)s повалил владычицу на землю и силой вошел в неё, схватив клыками за бронированный загривок. Их яростная страсть расцвела и излилась потоком, чтобы смениться нежностью чешуйчатых объятий. А затем вновь перетечь в сплетение когтей и чешуи. Так волна за волной шторм любви будет бушевать в тронном зале до тех пор пока во чреве демонической рептилии не зародится новая жизнь... ',]
    txt_dragon_mistress_fuck['flying serpent'] = ['Владычица поднялась со своего железного трона и двинулась к сыну. Её тело неуловимо исказилось и вытянулось, принимая удлинённую форму. Два змея встали поднялись на хвостах и стали раскачиваться друг напротив друга, а затем сплели шеи. %(dragon_name)s выпустил свой раздвоенный язык, который тут же встретил такой же язык госпожи. \n Непостижимый для человеческих глаз, медленный и всепоглощающий танец любви двух великих змиев продлился много часов и дней...',]
    txt_dragon_mistress_fuck['wyvern'] = ['Глаза Владычицы загорелись магическим огнём. Ее тело удлинялось, а на коже стали обрисовываться чешуйки. Ногти выросли, принимая очертания когтей. В ее глазах горел все тот же огонь, но теперь это была опасная крылатая тварь, королева ночи и Мать его Потомства, его Мать и Госпожа. Он жаждал ее, блуждая взглядом по столь манящей его чешуе, по сравнению с этими вольными девушками, она была Богиней. \n  Владычица бросилась на дракона, приглушенно рыча. Кроткий укус в шею и ответное рычание самца. Он перевернулся и оказался сверху, уже открыто пожирая глазами каждый изгиб ее тела, чувствуя свое напряжение. Его член уже был готов ворваться в эту ночную бестию, плавно покачиваясь между лап, покрытый сеткой вен и блестящий в свете Луны, проникающем через окно.​ Драконесса резко обхватила его лапами и потянула к себе, он блаженно раскрыл свои могучие крылья и припал к ее шее, покусывая ее. Горячий орган прикоснулся к ее щели и Дракон не сдержался. Столько лет он наводил ужас на поселения вольных, убивая их, насилуя, грабя, сжигая их дома. Все, ради нее. И каждый раз, мучая очередную несчастную жертву, он мечтал лишь о ней. С могучим рыком Дракон двинулся навстречу и его член погрузился в горящее нутро Владычицы, будто во врата самой Бездны. Она взрыкнула в ответ и насадилась до конца, жадно принимая в себя самца. Дракон чуть привстал, блаженно раставляя свои крылья, и тут же задвигался, резко и глубоко проникая в свою Госпожу, что извивалась и рычала от каждого проникновения члена этого монстра, выплескивая из своей норки все новые порции сока их любви. Долго продолжаться это не могло, Дракон ждал не один год. И вскоре чертоги мрачной обители наполнились громким ревом драконьей пары. Он полностью вогнал свой уд в ее горячее и столь жадно обхватывающее его естество, и из него ударило семя, порождая еще более кошмарного монстра во глуби чрева Владычицы. ',]
    txt_dragon_mistress_fuck['dragon'] = ['Глаза Владычицы загорелись магическим огнём. Ее тело удлинялось, а на коже стали обрисовываться чешуйки. Ногти выросли, принимая очертания когтей. В ее глазах горел все тот же огонь, но теперь это была опасная крылатая тварь, королева ночи и Мать его Потомства, его Мать и Госпожа. Он жаждал ее, блуждая взглядом по столь манящей его чешуе, по сравнению с этими вольными девушками, она была Богиней. \n  Владычица бросилась на дракона, приглушенно рыча. Кроткий укус в шею и ответное рычание самца. Он перевернулся и оказался сверху, уже открыто пожирая глазами каждый изгиб ее тела, чувствуя свое напряжение. Его член уже был готов ворваться в эту ночную бестию, плавно покачиваясь между лап, покрытый сеткой вен и блестящий в свете Луны, проникающем через окно.​ Драконесса резко обхватила его лапами и потянула к себе, он блаженно раскрыл свои могучие крылья и припал к ее шее, покусывая ее. Горячий орган прикоснулся к ее щели и Дракон не сдержался. Столько лет он наводил ужас на поселения вольных, убивая их, насилуя, грабя, сжигая их дома. Все, ради нее. И каждый раз, мучая очередную несчастную жертву, он мечтал лишь о ней. С могучим рыком Дракон двинулся навстречу и его член погрузился в горящее нутро Владычицы, будто во врата самой Бездны. Она взрыкнула в ответ и насадилась до конца, жадно принимая в себя самца. Дракон чуть привстал, блаженно раставляя свои крылья, и тут же задвигался, резко и глубоко проникая в свою Госпожу, что извивалась и рычала от каждого проникновения члена этого монстра, выплескивая из своей норки все новые порции сока их любви. Долго продолжаться это не могло, Дракон ждал не один год. И вскоре чертоги мрачной обители наполнились громким ревом драконьей пары. Он полностью вогнал свой уд в ее горячее и столь жадно обхватывающее его естество, и из него ударило семя, порождая еще более кошмарного монстра во глуби чрева Владычицы. ',]
    txt_dragon_mistress_fuck['multi headed flying serpent'] = ['Владычица поднялась со своего железного трона и двинулась к сыну. Её тело неуловимо исказилось и вытянулось, принимая удлинённую форму. Два змея встали поднялись на хвостах и стали раскачиваться друг напротив друга, а затем сплели шеи. %(dragon_name)s выпустил свой раздвоенный язык, который тут же встретил такой же язык госпожи. \n Непостижимый для человеческих глаз, медленный и всепоглощающий танец любви двух великих змиев продлился много часов и дней...',]
    txt_dragon_mistress_fuck['multi headed wyvern'] = ['Владычица крепко сжала подлокотники своего железного трона и %(dragon_name_full)s увидел как её изящные кисти преобразились в украшенные когтями чешуйчатые лапы. Вертикальные зрачки пересекли желтые глаза пополам и из её изменившегося горла раздалось призывное клокотание. Любой человек бежал бы в ужасе от этого зрелища, но %(dragon_type)s бросился вперёд, чтобы прикоснуться к единственной женщине на свете достойной стать матерью его детей. \n Жуткие ящеры набросились друг на друга, словно враги и от скрежета чешуи задрожали витражи в стрельчатых окнах большого зала. %(dragon_name)s повалил владычицу на землю и силой вошел в неё, схватив клыками за бронированный загривок. Их яростная страсть расцвела и излилась потоком, чтобы смениться нежностью чешуйчатых объятий. А затем вновь перетечь в сплетение когтей и чешуи. Так волна за волной шторм любви будет бушевать в тронном зале до тех пор пока во чреве демонической рептилии не зародится новая жизнь... ',]
    txt_dragon_mistress_fuck['multi headed dragon'] = ['Глаза Владычицы загорелись магическим огнём. Ее тело удлинялось, а на коже стали обрисовываться чешуйки. Ногти выросли, принимая очертания когтей. В ее глазах горел все тот же огонь, но теперь это была опасная крылатая тварь, королева ночи и Мать его Потомства, его Мать и Госпожа. Он жаждал ее, блуждая взглядом по столь манящей его чешуе, по сравнению с этими вольными девушками, она была Богиней. \n  Владычица бросилась на дракона, приглушенно рыча. Кроткий укус в шею и ответное рычание самца. Он перевернулся и оказался сверху, уже открыто пожирая глазами каждый изгиб ее тела, чувствуя свое напряжение. Его член уже был готов ворваться в эту ночную бестию, плавно покачиваясь между лап, покрытый сеткой вен и блестящий в свете Луны, проникающем через окно.​ Драконесса резко обхватила его лапами и потянула к себе, он блаженно раскрыл свои могучие крылья и припал к ее шее, покусывая ее. Горячий орган прикоснулся к ее щели и Дракон не сдержался. Столько лет он наводил ужас на поселения вольных, убивая их, насилуя, грабя, сжигая их дома. Все, ради нее. И каждый раз, мучая очередную несчастную жертву, он мечтал лишь о ней. С могучим рыком Дракон двинулся навстречу и его член погрузился в горящее нутро Владычицы, будто во врата самой Бездны. Она взрыкнула в ответ и насадилась до конца, жадно принимая в себя самца. Дракон чуть привстал, блаженно раставляя свои крылья, и тут же задвигался, резко и глубоко проникая в свою Госпожу, что извивалась и рычала от каждого проникновения члена этого монстра, выплескивая из своей норки все новые порции сока их любви. Долго продолжаться это не могло, Дракон ждал не один год. И вскоре чертоги мрачной обители наполнились громким ревом драконьей пары. Он полностью вогнал свой уд в ее горячее и столь жадно обхватывающее его естество, и из него ударило семя, порождая еще более кошмарного монстра во глуби чрева Владычицы. ',]

    #Сообщеения для битвы армий
    reinforcement_ask = 'Госпожа, мои войска несут слишком большие потери, а я сам не могу сейчас рисковать на передовой. Умоляю, помогите нам сокрушить врагов!'
    reinforcement_agree = 'Быть посему. Смотри и ужасайся ибо я смету врагов с лица земли как ураган сметает сухие осенние листья!'
    reinforcement_refuse = 'Разве зря мы готовили могучую армию? Разве зря я пестовала драконий столько веков? Хватит ныть - иди и принеси мне победу либо умри пытаясь!!!'
    
    
    #СОВЕТЫ ВЛАДЫЧИЦЫ
    txt_advice = ['Самые безопасные места для начала это сельская местность и леса. Но учти, что с ростом мобилизации там появятся патрули и они будут тем сильнее, чем больше военных сил собрали люди. Мобилизация требует времени.',
    'Если ищешь великанов, то самых слабых из них, огров-людоедов можно найти в лесных пещерах. Тритоны обитают в воде, Ифриты и Йотуны - высоко в горах, и они очень сильны. Но могущественее всех Титаны - они живут за облаками, на летающих островах-крепостях.',
    'Если бродить по дорогам людей, то можно найти их укрепления - рыцарские усадьбы, деревянные и каменные замки, монастыри... Это крепкие орешки, но внутри много сокровищ и благородные девы. А ещё из разграбленного замка можно сделать замечательное логово.',
    'Где-то в лесу живут альвы, народ Дану. Их девы очень хороши, но альвы защищают свои владения магией. Попробуй поймать и допросить кого-то из стражей границ остроухих. Они иногда выходят за магическую завесу.',
    'Обязательно посети остров контрабандистов. Там королевский закон почти не действует. Там ты сможешь продать краденные сокровища чтобы получить звонкие монеты, только учти что цены у них грабительские. Еще в притоне контрабандистов можно найти наёмников для охраны логова или борьбы с мобилизацией.',
    'Чтобы взететь в небо нужны крылья. Или заклинание полёта. С высоты можно разглядеть укрепления людей - замки в которых они держат сокровища и благородных дев. Впрочем эти места можно и на дорогах найти, зато взлетев над облаками у тебя будет шанс обнаружить летающий остров Титанов.',
    'В море живут русалки, но их дети будут годны лишь для охраны подводных логов и ничего более. Зато там можно грабить торговые корабли. Но чтобы добраться до кораблей и русалок надо уметь дышать под водой. Жабры помогут. Так же как и специальное заклинание.',
    'В своём логове ты можешь использовать разные заклинания. Конечно если тебе хватит на это коварства. Но не спеши использовать всё коварство как только проснёшься. Магия может пригодиться для того чтобы сменить облик или наложить проклятье на людские припасы.',
    'Крестьянку поймать очень просто, но они способны порождать лишь ядовитых тварей, бесполезных для армии тьмы. Вот горожанки уже интерснее, но их труднее найти. Вот тебе хороший совет - воспользуйся коварством, обратись в человека и похить горожанку на городском рынке.',
    'Обязательно навести деревню гремлинов. Эти ребята плохие вояки, но хорошие мастера по камню, дереву и металлу - не хуже цвергов. А ещё они жадные до золота. Ты можешь нанять их в качестве слуг или заплатить им за улучшения для логова. Они даже могут изготавливать ювелирные изделия, если есть материалы.',
    'Я не хочу чтобы ты водился с ведьмой что живёт на кладбище. Она слишком много о себе мнит - хочет стать такой же могущественной как я. За твоё семя она предложит тебе колдовские услуги, но лучше потрать свою мужскую силу на размножение чем на эту шлюху-колдунью. Она выдоит тебя до суха и ты не сможешь никого обрюхатить.',
    'В городе есть что пограбить, но ворота хорошо охраняются. Через них можно перелететь на крыльях или пройти внутри обернувшись человеком - если хватит коварства. В форме человека можно даже договориться с ювелирами - они дают лучшую цену за сокровища чем контрабандисты и могут кое что продать за деньги.',
    'Если ты обрюхатишь девицу и отпустишь её на волю, то ваше отродье будет терроризировать людей увеличивая разруху. Но лучше держать беременную деву под замком в логове, тогда ты сможешь взять отродье на службу или отправить в армию тьмы. Только не забудь что кто-то должен ухаживать за будущей мамашей пока ты спишь.',
    'Когда выполнишь задание, ты можешь прийти ко мне за наградой сразу. Но можешь и подождать конца срока, ничего страшного. Так ты накопишь деньги для снабжения моей армии и наплодишь больше монстров. Очень важно чтобы в нашей армии было много разных существ.',
    'Мой совет: \n Воруй \n @ \n Убивай',
    'Некоторые встречи бывают реже других. Например на дороге ты чаще встретишь крестьянина с сеном, чем богатый караван. Если встреча не интересна, не трать времени и сил зря, сдержи свою ярость до лучшего момента.',
    'С ростом мобилизации по всему королевству начнут бродить патрули - тем более сильные чем выше мобилизация. Но даже слабый патруль доставит тебе неприятности - ведь ты потратишь на них своё время и силы, а толку никакого. Большая разруха тоже не к добру - руины да пепелища ведь не ограбишь, верно?',
    'Рыцари и воры могут иметь очень разную силу. Чем выше твоя дураная слава, тем более опасных противников привлечёт твоё логово. Будь осторожен, следи за ними и вовремя предпринимай контр-меры.',
    'Если ты не совершаешь зла, хотя и мог бы - например отпускаешь бесполезную девку чтобы не тратить попусту времени и силы, ты будешь раздражаться. В итоге ярость помешает тебе контролировать себя и ты не сможешь сдержаться, будешь атаковать каждого встречного. Сожри кого-нибудь живьём и ярость уйдёт на время.',
    'В горах можно отыскать входы в подземное царство цвергов, таящее несметные сокровища. Кроме того там есть множество шахт где добывают драгоценные металлы и самоцветы из которых гремлины могут сделать тебе дорогие ювелирные изделия.']
    
    """
    Шаблон
    txt_ = [[
        '',
        ],
    
        ['',
        ],
    
        ['',
        ],
    
        ['',
        ],
        ]
    """