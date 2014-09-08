init python:
    from pythoncode import battle

label lb_fight:
    show expression game.foe.img as foeimg
    $ battle_status = battle.check_fear(game.dragon, game.foe)
    $ description = game.foe.battle_description(battle_status, game.dragon)
    "[description]"
    
    if 'foe_alive' in battle_status:
        $ chance_win = battle.victory_chance(game.dragon, game.foe)
        $ chance_wound = battle.victory_chance(game.foe, game.dragon)
        "Шанс победы дракона: [chance_win] %%, шанс ранения дракона: [chance_wound] %%"

    while 'foe_alive' in battle_status:
        $ battle_status = battle.battle_action(game.dragon, game.foe)
        $ description = game.foe.battle_description(battle_status, game.dragon)
        "[description]" 
        if 'dragon_dead' in battle_status:
            #TODO замена текущего дракона с возможностью выбора потомка
            "Дракон умер - да здравствует Дракон!"
            $ game.dragon = game.dragon.children()[0]
            $ game.dragon.avatar = get_dragon_avatar(game.dragon.heads[0])
            jump lb_location_lair_main
            
        if 'foe_alive' in battle_status:
            menu:
                'Продолжать бой':
                    pass
                    
                'Отступить':
                    if type(game.foe) == core.Knight:
                        #TODO потеря логова, магнитофона импортного, куртки замшевой. Двух!
                        jump lb_location_lair_main
                    else:
                        "Вы бежали в логово"
                        hide foeimg
                        nvl clear
                        $ renpy.pop_return()
                        jump lb_location_lair_main
    hide foeimg
    nvl clear
    return
