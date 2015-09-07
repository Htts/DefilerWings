# coding=utf-8
#spellchecked, proofread
init python:
    from pythoncode import treasures
    
label lb_location_smuggler_main:
    nvl clear
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'smugglers'
    show expression 'img/bg/special/smugglers.jpg' as bg
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] need some sleep!'
        return

    # Стоимость года работы охранников
    $ guards_cost = data.lair_upgrades['smuggler_guards']['cost']
    
    menu:
        'Hire mercenaries' if 'smuggler_guards' not in game.lair.upgrades and 'regular_guards' not in game.lair.upgrades:
            "Hired thugs will prevent arrogant thieves from pilfering the dragon\'s treasure. Just [guards_cost] farthings per year."
            menu:
                "Sign the contract" if guards_cost <= game.lair.treasury.wealth:
                    $ game.lair.upgrades.add('smuggler_guards', deepcopy(data.lair_upgrades['smuggler_guards']))
                    "Hired thugs will guard the lair while the dragon sleeps."
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_2 
                "Refuse":
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_3 
        'Sell trinkets' if len(game.lair.treasury.jewelry) > 0:
            nvl clear
            menu:
                'Most valuable':
                    $ item_index = game.lair.treasury.most_expensive_jewelry_index
                'Cheapest' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.cheapest_jewelry_index
                'Random' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = random.randint(0, len(game.lair.treasury.jewelry) - 1)
                'Sell all' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = None
                'Cancel':
                    jump lb_location_smuggler_main 
            python:
                if (item_index is None):
                    description = u"Sell all for %s?" % (
                        treasures.number_conjugation_rus(game.lair.treasury.all_jewelries * 75 // 100, u"farthing"))
                else:
                    description = u"%s.\n Sell for %s?" % (
                        game.lair.treasury.jewelry[item_index].description().capitalize(),
                        treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost * 75 // 100, u"farthing"))
            menu:
                "[description]"
                'Sell':
                    python:
                        if (item_index is None):
                            description = u"Sell all jewelry for %s?" % (
                                treasures.number_conjugation_rus(game.lair.treasury.all_jewelries  * 75 // 100, u"farthing"))
                            game.lair.treasury.money += game.lair.treasury.all_jewelries  * 75 // 100
                            game.lair.treasury.jewelry = []
                        else:
                            description = u"%s.\n Sold for %s" % (
                                game.lair.treasury.jewelry[item_index].description().capitalize(),
                                treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost * 75 // 100, u"farthing"))
                            game.lair.treasury.money += game.lair.treasury.jewelry[item_index].cost * 75 // 100
                            game.lair.treasury.jewelry.pop(item_index)
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_5 
                'Keep':
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_6 
        'Finance terrorists' if game.mobilization.level > 0:
            show expression 'img/scene/thief.jpg' as bg
            $ terror_cost = game.mobilization.level * 100
            'The troops of the kingdom are too organized and alert for you to do evil with impunity.  But if you provide local bandits with money for weapons, equipment, and supplies, they can become a threat that will distract the patrolling soldiers. [terror_cost] farthings will be enough to increase internal strife and make supply convoys disappear.'
            menu:
                'Pay [terror_cost] to terrorists' if terror_cost <= game.lair.treasury.money:
                    $ game.lair.treasury.money -= terror_cost
                    $ game.mobilization.level -= 1
                    'Following the dragon\'s orders, the bandits will set fire to food warehouses, poison wells, and capture supply convoys. The ability of the kingdom to mobilize will be reduced.'
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main
                'It is not worth it':
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_1
        'Information on thief' if game.thief is not None:
            "There are a lot of rumors and people in the know. Just pour drinks and tongues will loosen, and no one will remember that they are talking to a lizard."
            nvl clear
            menu:
                "Beer for all (10 f.)" if game.lair.treasury.money >= 10:
                    python:
                        game.lair.treasury.money -= 10
                        if game.thief is not None:
                            game.thief.third('[game.thief.name] \n\n' + game.thief.description())
                        else:
                            narrator("There is no thief plotting to take your gold.")
                "Decline" if game.lair.treasury.money < 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_7 
                "Go away." if game.lair.treasury.money >= 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_8 
        'Sabotage thief' if game.thief is not None:
            $ price = game.dragon.reputation.level * 50
            $ game.thief.third("For a bribe of %d farthings the thieves\' informants will not tell their boss the dragon\'s location." % price)
            menu:
                "Pay [price] f." if game.lair.treasury.money >= price:
                    $ game.lair.treasury.money -= price
                    $ game.thief.retire()
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_9 
                "Decline" if game.lair.treasury.money < price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_10 
                "Go away." if game.lair.treasury.money >= price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_11 
        'Information on knight' if game.knight is not None:
            "There are a lot of rumors and informants here. Just pour some drinks and tongues will loosen, and no one will remember that they are talking to a giant lizard."
            nvl clear
            menu:
                "Beer for all (10 f.)" if game.lair.treasury.money >= 10:
                    python:
                        game.lair.treasury.money -= 10
                        if game.knight is not None:
                            game.knight.third('[game.knight.name] \n\n' + game.knight.description())
                        else:
                            narrator("It seems that no knights are trying to kill you.")
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_12 
                "Decline" if game.lair.treasury.money < 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_13 
                "Go away." if game.lair.treasury.money >= 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_14 
        'Pay to rob the knight' if game.knight is not None:
            $ price = game.knight.enchanted_equip_count * 100
            $ narrator("Robbing a famous knight is a dangerous business, and a difficult one. But thieves will do anything for money. Put %d farthings on the table, and it will be a cinch!" % price)
            nvl clear
            menu:
                "Pay [price] f." if game.lair.treasury.money >= price:
                    $ game.lair.treasury.money -= price
                    $ game.knight.equip_basic()
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_15 
                "Decline" if game.lair.treasury.money < price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_16 
                "Go away." if game.lair.treasury.money >= price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_17 
        'Go away':
            return
            
    return
    