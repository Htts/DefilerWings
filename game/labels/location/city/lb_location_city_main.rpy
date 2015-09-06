# coding=utf-8
init python:
    from pythoncode import treasures
    from pythoncode.characters import Enemy
        
label lb_location_city_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))        
    $ place = "city_gates"
    hide bg
    show place as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        'Even dragons have to sleep sometime. Especially dragons!'
        return      
        
    'The capital of the kingdom of men'
    menu:
        'Disguise yourself as a human' if game.dragon.mana > 0:
            'Spending some precious magic power, the dragon turns into a man and goes into the city.'
            $ game.dragon.drain_mana()
            nvl clear
            call lb_city_walk from _call_lb_city_walk
        'Storm the gates' if not game.dragon.can_fly:
            'Seeing the approach of danger, the watchful guards close the gate, preventing a battle.'
            call lb_city_gates from _call_lb_city_gates
        'Fly in' if game.dragon.can_fly:
            'Easily passing over the wall, the [game.dragon.kind] reaches the heart of the city. Fortifications will not save them from a flying enemy.'
            call lb_city_raze from _call_lb_city_raze
        'Get away':
            return
            
    return

label lb_city_gates:
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('city', game_ref=game)
    call lb_fight from _call_lb_fight_68
    call lb_city_raze from _call_lb_city_raze_1
    return

label lb_city_raze:
    'The defenseless city is ready to feel the rage of the Mistress\'s offspring.'
    nvl clear
    menu:
        'Royal palace':
            call lb_city_palace_atk from _call_lb_city_palace_atk

        'Marketplace':
            call lb_city_market_atk from _call_lb_city_market_atk

        'Cathedral':
            call lb_city_cathedral_atk from _call_lb_city_cathedral_atk
            
        'Rich district':
            call lb_city_jew_atk from _call_lb_city_jew_atk
            
        'Go back':
            return
            
    return

label lb_city_walk:
    show expression 'img/bg/city/inside.jpg' as bg
    'The mysterious stranger walks past the watching guards and enters the bustling city.'
    nvl clear

    menu:
        'Royal palace':
            call lb_city_palace from _call_lb_city_palace

        'Marketplace':
            call lb_city_market from _call_lb_city_market

        'Cathedral':
            call lb_city_cathedral from _call_lb_city_cathedral
            
        'Jeweler\'s shop':
            call lb_city_jewler from _call_lb_city_jewler
            
        'Go back':
            return
            
    return

label lb_city_palace:
    'A proud citadel on a hill in the city center. The king\'s winter residence is here. From inside come the seductive aromas of noble maidens. Vigilant guards stand at the gate.'
    $ game.foe = Enemy('palace_guards', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Attack':
            call lb_city_palace_atk from _call_lb_city_palace_atk_1
        'Go back':
            call lb_city_walk from _call_lb_city_walk_1
    
    return

label lb_city_palace_atk:
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('palace_guards', game_ref=game)
    $ chances = show_chances(game.foe)
    call lb_fight from _call_lb_fight
    'With the defenders of the citadel in disarray, the dragon has the chance to rape and pillage.'
    $ game.dragon.reputation.points += 3
    '[game.dragon.reputation.gain_description]'
    menu:
        'Defile a noble lady':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('princess')
            '[game.dragon.fullname] preys upon noble maidens.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex     
        'Plunder and murder':
            $ game.dragon.drain_energy()
            python:
                count = random.randint(4, 9)
                alignment = 'knight'
                min_cost = 200
                max_cost = 2000
                obtained = "This is from the royal treasury."
                trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'With a bloodthirsty roar [game.dragon.fullname] sweeps through the corridors of the palace killing all in his path, and looting everything he takes a fancy to:' 
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
        'Flee':
            'Having decided not to tempt fate and instead use the commotion for a safe withdrawl, [game.dragon.kind] leaves the city.'
    return

label lb_city_market:
    show expression 'img/bg/city/market.jpg' as bg
    'The market square is full of humans. They buy and sell all sorts of unnecessary things like potatos and clothing. The foolish mortals have no idea that their most terrifying nightmare is here. They are vulnerable to a surprise attack.'
    nvl clear
    menu:
        'Drop the disguise':
            call lb_city_market_atk from _call_lb_city_market_atk_1
        'Go back':
            call lb_city_walk from _call_lb_city_walk_2

    return

label lb_city_market_atk:
    show expression 'img/bg/city/market.jpg' as bg
    'The dragon regains its true form, and the people flee in terror.'
    nvl clear
    menu:
        'Massacre':
            $ game.dragon.drain_energy()
            play sound "sound/eat.ogg"
            show expression 'img/scene/fire.jpg' as bg
            'These inhabitants vainly believed that they were safe behind city walls. [game.dragon.fullname] has a fun time making sure they see their error. Blood, guts, gore...' #Translator: Can't translate the third word. "Кровь, кишки, распидорасило..."
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'
        'Defile a merchant\'s daughter':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('citizen')
            'Nobles are certainly not found in the market, but the daughters of the rich appear here. [game.dragon.fullname] catches a maiden.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_1     
        'Go back':
            return
    return

label lb_city_cathedral:
    'A huge gothic cathedral, towering over the city. No other building can match the heights of the cathedral bell tower and its spire.'
    nvl clear
    menu:
        'Pillage the Cathedral':
            'The mysterious stranger comes through the archway and transforms into a monster in front of the congregation.'
            call lb_city_cathedral_atk from _call_lb_city_cathedral_atk_1

        'Go back':
            call lb_city_walk from _call_lb_city_walk_4
    return

label lb_city_cathedral_atk:
    $ game.dragon.drain_energy()
    python:
        count = random.randint(4, 10)
        alignment = 'cleric'
        min_cost = 10
        max_cost = 500
        obtained = "This is from the city cathedral."
        trs = treasures.gen_treas(count, data.loot['church'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    'With demonic laughter [game.dragon.fullname] bursts into the sanctuary, killing all in his path, and taking loot:'
    '[trs_descrptn]'
    $ game.lair.treasury.receive_treasures(trs)
    $ game.dragon.reputation.points += 5
    '[game.dragon.reputation.gain_description]'    
    return

label lb_city_jewler:
    'In this quarter the most affluent craftsmen work. Armorers, jewlers, cabinetmakers. All around are intoxicating treasures and noblewomen shopping. Unfortunately, guards stand on every corner.'
    $ game.foe = Enemy('city_guard', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Buy jewels':
            $ new_item = game.lair.treasury.craft(**data.craft_options['jeweler_buy'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Purchased: [test_description]."
            call lb_city_jewler from _call_lb_city_jewler_1
        'Sell jewels':
            menu:
                'Most expensive' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.most_expensive_jewelry_index
                'Cheapest' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.cheapest_jewelry_index
                'Random' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = random.randint(0, len(game.lair.treasury.jewelry) - 1)
                'All of them' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = None
                'Cancel':
                    call lb_city_jewler from _call_lb_city_jewler_2
            python:
                if (item_index is None):
                    description = u"Sell all jewels for %s?" % (
                        treasures.number_conjugation_rus(game.lair.treasury.all_jewelries, u"farthing"))
                else:
                    description = u"%s.\nSell jewel for %s?" % (
                        game.lair.treasury.jewelry[item_index].description().capitalize(),
                        treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost, u"farthing"))
            menu:
                "[description]"
                'Sell':
                    python:
                        if (item_index is None):
                            description = u"All jewelery sold for %s" % (
                                treasures.number_conjugation_rus(game.lair.treasury.all_jewelries, u"farthing"))
                            game.lair.treasury.money += game.lair.treasury.all_jewelries
                            game.lair.treasury.jewelry = []
                        else:
                            description = u"%s.\nSold for %s" % (
                                game.lair.treasury.jewelry[item_index].description().capitalize(),
                                treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost, u"farthing"))
                            game.lair.treasury.money += game.lair.treasury.jewelry[item_index].cost
                            game.lair.treasury.jewelry.pop(item_index)

                    call lb_city_jewler from _call_lb_city_jewler_3
                'Do not sell':
                    call lb_city_jewler from _call_lb_city_jewler_4
        'Make jewel':
            $ new_item = game.lair.treasury.craft(**data.craft_options['jeweler_craft'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Crafted: [test_description]."
            call lb_city_jewler from _call_lb_city_jewler_5
        'Drop the disguise':
            call lb_city_jew_atk from _call_lb_city_jew_atk_1
        'Go to the main street':
            call lb_city_walk from _call_lb_city_walk_5
    return


label lb_city_jew_atk:
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('city_guard', game_ref=game)
    call lb_fight from _call_lb_fight_1
    'There is not a living guard left in the quarter. People flee from the dragon in a panic and try to save their valuables. [game.dragon.name] examines the scene of destruction and chaos. A fat jeweler drags a heavy wooden box. A noble girl runs away squealing. A burning shop filled with precious bars and jewels is about to collapse.' 
    $ game.dragon.reputation.points += 3
    '[game.dragon.reputation.gain_description]'
    menu:
        'Rob the jeweler':
            python:
                count = random.randint(3, 10)
                alignment = 'human'
                min_cost = 10
                max_cost = 500
                obtained = "This is from the jeweler."
                trs = treasures.gen_treas(count, data.loot['jeweler'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'Robbing the bumbling jeweler is like taking candy from a child. In the box are interesting things:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]' 
    
        'Rape the noble virgin':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('princess')
            'The dragon catches the noble maiden.'
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_2     
            return
            
        'Get jewels from burning shop':
            python:
                count = random.randint(3, 10)
                alignment = 'human'
                min_cost = 10
                max_cost = 1000
                obtained = "This is from the goldsmith's shop."
                trs = treasures.gen_treas(count, data.loot['raw_material'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'Acting quickly, the dragon snatches valuables before they are buried under the rubble:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]' 
    
    return
    