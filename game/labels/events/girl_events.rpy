# coding=utf-8
init python:
    from pythoncode import girls_data
    
label lb_event_girl_escape:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    $ game.girls_list.description('escape', True)  # Description of the rescue
    return

label lb_event_girl_spawn(spawn_type):
    $ spawn_image = "img/scene/spawn/%s.jpg" % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    python:
        spawn_description = game.girls_list.description(spawn_type)  # description of the type of birth 
        if not spawn_description:
            if 'elite' in girls_data.spawn_info[spawn_type]['modifier']:
                spawn_description = game.girls_list.description('spawn_elite')
            else:
                spawn_description = game.girls_list.description('spawn_common')
    game.girl.third "[spawn_description]"
    return

label lb_event_girl_free_spawn(spawn_type):
    $ spawn_image = 'img/scene/spawn/%s.jpg' % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    $ free_spawn_description = game.girls_list.description('free_spawn')  # description of birth from free girl
    game.girl.third "[free_spawn_description]"
    return

label lb_event_girl_hunger_death:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    $ game.girls_list.description('hunger_death', True)  # description of girl's death from starvation
    return

label lb_event_girl_kill:
    hide bg
    show expression 'img/scene/girl_death.jpg' as bg
    nvl clear
    $ game.girls_list.description('kill', True)  # girl dies in childbirth
    return