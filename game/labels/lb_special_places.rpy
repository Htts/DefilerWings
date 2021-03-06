# coding=utf-8
#spellchecked

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
label lb_special_places:
    nvl clear
    python:
        special_places_menu = []
        for special_place in game.dragon.special_places.keys():
            # Add to the list of investigated points of interest
            special_stage = game.dragon.special_places[special_place]
            special_places_menu.append((data.special_places[special_stage][0], special_stage))
        special_places_menu.append(('Back', 'back'))
        special_stage = renpy.display_menu(special_places_menu)
        
        if special_stage == 'back':
            pass
        else:
            renpy.call(data.special_places[special_stage][1])
    return
    
label lb_enchanted_forest:
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    'Even knowing the way to the enchanted forest, it is not easy to pass through a magic elven veil. A powerful spell will be needed.'
    menu:
        'Open the elvenpath (magic)' if game.dragon.mana > 0:
            $ game.dragon.drain_mana()
            '[game.dragon.fullname] uses black magic to break the veil of illusion, confusion, and sleep that the elves hide their possessions under. Unnoticed, the deadly [game.dragon.kind] comes under the shadow of the ancient trees.'
            nvl clear
            call lb_enchanted_forest_enter from _call_lb_enchanted_forest_enter
        'Go back':
            return
        
    return
            

label lb_enchanted_forest_enter:        
    stop music fadeout 1.0
    play music "mus/forest.ogg"    
    menu:
        'Prowl around':
            $ choices = [
                ("lb_enchanted_forest_elfgirl", 10),
                ("lb_enchanted_forest_druid", 10),
                ]
            $ enc = weighted_random(choices)
            $ renpy.call(enc)
    
        'Defile the Tree of Life':
            call lb_enchanted_forest_grove from _call_lb_enchanted_forest_grove
            
    return

label lb_enchanted_forest_elfgirl:
    '[game.dragon.name] smells the mouthwatering aroma that comes only from innocence, beauty, and magic. This is a forest enchantress of the people of the goddess Danu, the elves. No flesh is more sweet and desirable, but because of her witchcraft it will not be easy to capture her.'
    $ game.foe = Enemy('elf_witch', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Fight the Fey':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_25
            'Despite her fierce resistance, the sorceress is mostly unharmed. She is helpless and untouched...for now.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            $ description = game.girls_list.new_girl('elf')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_14      
        
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
    return

label lb_enchanted_forest_druid:
    '[game.dragon.name] does not remain unnoticed for long. On the path of the dragon, a druid armed with a gnarled leafy stick materializes. He does not look particularly impressive, but it is an illusion. The very strength of the forest is on the side of this priest of Danu.'
    $ game.foe = Enemy('druid', game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Fight the Druid':
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('druid', game_ref=game)
            call lb_fight from _call_lb_fight_26
            $ game.dragon.reputation.points += 3
            'Druid defeated. [game.dragon.reputation.gain_description]'
            '[game.dragon.name] finds something valuable on the corpse:'
            python:
                count = random.randint(1, 2)
                alignment = 'elf'
                min_cost = 25
                max_cost = 500
                obtained = "This item belong to the druid - guard of the enchanted forest.."
                trs = treasures.gen_treas(count, data.loot['knight'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()   
    return

label lb_enchanted_forest_grove:
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_enfr[1]))
    '[txt]'    
    $ game.foe = Enemy('treant', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Fight the Treant':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_27
            $ txt = game.interpolate(random.choice(txt_place_enfr[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]' 
            nvl clear
            call lb_enchanted_forest_grove_rob from _call_lb_enchanted_forest_grove_rob
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enchanted_forest_grove_rob:
    $ game.dragon.add_event('ravage_sacred_grove')
    python:
        count = random.randint(5, 10)
        alignment = 'elf'
        min_cost = 500
        max_cost = 3000
        obtained = "This is from the royal treasury of the elves of the enchanted forest."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Defile the Sacred Grove':
            show expression 'img/bg/lair/elfruin.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_enfr[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_enfr[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('elf')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_15    
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
                                        
        'Remember this place and depart':
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
            
    return
    
label lb_dead_grove:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_enfr[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('forest_heart')
            $ game.dragon.del_special_place('enchanted_forest')
        
        'Go away':
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
    
    return

# Knight's manor
label lb_manor_found:
    show expression 'img/bg/special/castle1.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_manor[0]))
    '[txt]'
    jump lb_manor
    
label lb_manor:
    show expression 'img/bg/special/castle1.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_manor[1]))
    '[txt]'    
    $ game.foe = Enemy('old_knight', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Challenge the old knight':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_28
            $ txt = game.interpolate(random.choice(txt_place_manor[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            call lb_manor_rob from _call_lb_manor_rob
        'Remember this place and go' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('manor', 'manor_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_manor_rob:
    python:
        count = random.randint(1, 5)
        alignment = 'knight'
        min_cost = 10
        max_cost = 250
        obtained = "Looted from the knightly manor."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the manor':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_manor[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_manor[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_16     
            $ game.dragon.add_special_place('manor', 'manor_empty')
                                        
        'Remember this place and go':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return
            
label lb_manor_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_manor[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('manor')
        
        'Go away':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return

# Деревянный замок
label lb_wooden_fort_found:
    show expression 'img/bg/special/castle2.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[0]))
    '[txt]'
    jump lb_wooden_fort
    
label lb_wooden_fort:
    show expression 'img/bg/special/castle2.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[1]))
    '[txt]'    
    $ game.foe = Enemy('footman', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Siege the motte and bailey':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_29
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'            
            nvl clear
            call lb_wooden_fort_rob from _call_lb_wooden_fort_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_wooden_fort_rob:
    python:
        count = random.randint(2, 6)
        alignment = 'knight'
        min_cost = 25
        max_cost = 500
        obtained = "Looted from the wooden fort."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the keep':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_17 
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return
            
label lb_wooden_fort_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('wooden_fort')
        
        'Go away':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return

# Укреплённый монастырь
label lb_abbey_found:
    show expression 'img/bg/special/castle3.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_abbey[0]))
    '[txt]'
    jump lb_abbey
    
label lb_abbey:
    show expression 'img/bg/special/castle3.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_abbey[1]))
    '[txt]'    
    $ game.foe = Enemy('templars', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Storm the abbey':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_30
            $ txt = game.interpolate(random.choice(txt_place_abbey[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'  
            nvl clear
            call lb_abbey_rob from _call_lb_abbey_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('abbey', 'abbey_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_abbey_rob:
    python:
        count = random.randint(4, 10)
        alignment = 'cleric'
        min_cost = 10
        max_cost = 500
        obtained = "Looted from the convent."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the abbey':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_18 
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return
            
label lb_abbey_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_abbey[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('abbey')
        
        'Go away':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return

# Каменная крепость
label lb_castle_found:
    show expression 'img/bg/special/castle4.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_castle[0]))
    '[txt]'
    jump lb_castle
    
label lb_castle:
    show expression 'img/bg/special/castle4.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_castle[1]))
    '[txt]'    
    $ game.foe = Enemy('castle_guard', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Siege the castle':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_31
            $ txt = game.interpolate(random.choice(txt_place_castle[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'                
            nvl clear
            call lb_castle_rob from _call_lb_castle_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('castle', 'castle_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_castle_rob:
    python:
        count = random.randint(3, 8)
        alignment = 'knight'
        min_cost = 100
        max_cost = 1000
        obtained = "Looted from the fortress."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the citadel':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_19     
            $ game.dragon.add_special_place('castle', 'castle_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return
            
label lb_castle_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_castle[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('castle')
        
        'Go away':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return

# Королевский замок
    
label lb_palace_found:
    show expression 'img/bg/special/castle5.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_palace[0]))
    '[txt]'
    jump lb_palace
    
label lb_palace:
    show expression 'img/bg/special/castle5.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_palace[1]))
    '[txt]'    
    $ game.foe = Enemy('palace_guards', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Attack the royal palace':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_32
            $ txt = game.interpolate(random.choice(txt_place_palace[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'                 
            nvl clear
            call lb_palace_rob from _call_lb_palace_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('palace', 'palace_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_palace_rob:
    python:
        count = random.randint(5, 10)
        alignment = 'knight'
        min_cost = 250
        max_cost = 2500
        obtained = "Looted from the royal palace."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the palace':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_20     
            $ game.dragon.add_special_place('palace', 'palace_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return
            
label lb_palace_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_palace[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('palace')
        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return

# Ogre\'s home
    
label lb_enc_ogre:
    'The dragon wanders for some time through the woods...'
    show expression 'img/bg/special/cave_enter.jpg' as bg
    'And stumbles upon the entrance to a cave spacious enough for a lair. Judging by the smell, an ogre has already made one.'
    jump lb_enc_fight_ogre
    
label lb_enc_fight_ogre:   
    $ game.foe = Enemy('ogre', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Challenge the ogre':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_33
            '[game.dragon.name] is victorious.'
            jump lb_enc_explore_ogre_den
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ogre', 'enc_ogre')
            $ game.dragon.gain_rage()
    return
    
label lb_enc_explore_ogre_den:
    menu:
        'Rob the den':
            'In the cave a frightened giantess is hiding. Either a daughter or the wife of the ogre whose body is lying outside.'
            $ description = game.girls_list.new_girl('ogre')
            nvl clear
            game.girl.third "[description]"
            call lb_gigant_sex from _call_lb_gigant_sex     
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
            return
 
label lb_enc_create_ogre_lair:
    menu:
        'The cave where the ogre lived is now empty. Here you could make a den, not a very nice one, but still better than an open ravine in a thicket.'
        'Make a lair here':
            $ game.create_lair('ogre_den')
            $ game.dragon.del_special_place('ogre')
            return
        'Remember this place and leave':
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
            return
            

# Frost giant\'s home  

label lb_jotun_found:
    'High in the mountains, where everything is covered with ice and snow, there is a giant ice palace. Interesting...'
    nvl clear
    jump lb_jotun
    
label lb_jotun:   
    show expression 'img/bg/lair/icecastle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_jotun[0]))
    '[txt]'
    $ game.foe = Enemy('jotun', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Challenge the Jotun':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_34
            jump lb_jotun_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('jotun', 'jotun_full')
            $ game.dragon.gain_rage()
    return
    
label lb_jotun_rob:
    menu:
        'Rob the Icy Citadel':
            $ txt = game.interpolate(random.choice(txt_place_jotun[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('ice')
            nvl clear
            game.girl.third "[description]"
            call lb_gigant_sex from _call_lb_gigant_sex_1     
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
            return
 
label lb_jotun_empty:
    show expression 'img/bg/lair/icecastle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_jotun[2]))
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('ice_citadel')
            $ game.dragon.del_special_place('jotun')
        'Remember this place and leave':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
    return 
    
# Жильё огненного великана
    
label lb_ifrit_found:
    'Above a volcanic crater rises a tower of black obsidian. I wonder who lives there...'
    nvl clear
    jump lb_ifrit
    
label lb_ifrit:   
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_ifrit[0]))
    '[txt]'
    $ game.foe = Enemy('ifrit', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Challenge the fire giant':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_35
            jump lb_ifrit_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ifrit', 'ifrit_full')
            $ game.dragon.gain_rage()
    return
    
label lb_ifrit_rob:
    menu:
        'Rob the volcanic forge':
            $ txt = game.interpolate(random.choice(txt_place_ifrit[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('fire')
            nvl clear
            game.girl.third "[description]"
            call lb_gigant_sex from _call_lb_gigant_sex_2     
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
            return
 
label lb_ifrit_empty:
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_ifrit[2]))
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('vulcanic_forge')
            $ game.dragon.del_special_place('ifrit')
        'Remember this place and leave':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
    return 

    
# Жильё тритона
    
label lb_triton_found:
    'The dragon swims along the coast...'
    show expression 'img/bg/lair/underwater.jpg' as bg
    'And discoveres an underwater arch, decorated with corals and seashells. The doorway is big enough for even a sperm whale to swim through.'
    nvl clear
    jump lb_triton
    
label lb_triton:   
    show expression 'img/bg/lair/underwater.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_triton[0]))
    '[txt]'
    $ game.foe = Enemy('triton', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Challenge the Triton':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_36
            jump lb_triton_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('triton', 'triton_full')
            $ game.dragon.gain_rage()
    return
    
label lb_triton_rob:
    menu:
        'Rob the underwater mansion':
            $ txt = game.interpolate(random.choice(txt_place_triton[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('siren')
            nvl clear
            game.girl.third "[description]"
            call lb_gigant_sex from _call_lb_gigant_sex_3    
            $ game.dragon.add_special_place('triton', 'triton_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('triton', 'triton_empty')
            return
 
label lb_triton_empty:
    show expression 'img/bg/lair/underwater.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_triton[2]))
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('underwater_mansion')
            $ game.dragon.del_special_place('triton')
        'Go away':
            $ game.dragon.add_special_place('triton', 'triton_empty')
    return 
    
# Жильё титана
    
label lb_titan_found:
    'The dragon rises above the clouds...'
    show expression 'img/bg/special/cloud_castle.jpg' as bg
    'And discovers a floating island and beautiful castle. I wonder who built it...'
    nvl clear
    jump lb_titan
    
label lb_titan:   
    show expression 'img/bg/special/cloud_castle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_titan[0]))
    '[txt]'
    $ game.foe = Enemy('titan', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Challenge the Titan':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_37
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'   
            jump lb_titan_rob
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('titan', 'titan_full')
            $ game.dragon.gain_rage()
    return
    
label lb_titan_rob:
    menu:
        'Rob the cloud castle':
            $ txt = game.interpolate(random.choice(txt_place_titan[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('titan')
            nvl clear
            game.girl.third "[description]"
            call lb_gigant_sex from _call_lb_gigant_sex_4  
            $ game.dragon.add_special_place('titan', 'titan_empty')
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('titan', 'titan_empty')
            return
 
label lb_titan_empty:
    show expression 'img/bg/lair/cloud_castle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_titan[2]))
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('cloud_castle')
            $ game.dragon.del_special_place('titan')
        'Go away':
            $ game.dragon.add_special_place('titan', 'titan_empty')
    return 
    
# Подгорное царство цвергов

label lb_backdor:
    show expression 'img/bg/special/backdor.jpg' as bg
    'The secret door to the kingdom of the dwarves is indicated on the drawings found in the stronghold as the "backdoor". In contrast to the main gate there are no defenses, and anyone who knows the secret can get in. Of course, they still have to face an army of dwarves, but getting to them is easier than trying to pass through the main fortifications.'  
    nvl clear
    menu:
        'Go through the "backdoor"!':
            stop music fadeout 1.0
            play music "mus/moria.ogg"
            $ renpy.music.queue(get_random_files('mus/ambient'))           
            show expression 'img/bg/special/moria.jpg' as bg
            'Pressing an inconspicuous stone in the right place, [game.dragon.name] opens a secret passage into the dwarven kingdom. There won\'t be a second chance at this, if the dragon retreats the dwarves will seal up their "backdoor" and strengthen it more thoroughly.'
            $ game.dragon.add_special_place('backdor', 'backdor_sealed')
            jump lb_dwarf_army    
        'More preparation is needed...':
            return
            
    return


label lb_backdor_sealed:
    show expression 'img/bg/special/backdor.jpg' as bg
    'There was a secret passage to the dwarven kingdom here, but during the attack the dwarves brought down the tunnel and covered it with stones. The little miners love their explosions...'
    nvl clear
    return
    
label lb_frontgates:
    'Fortified impregnable bulwarks, these impressive metal gates firmly close the only(?) entry into the dwarven kingdom. There are incredible treasures hidden in its depths, the likes of which are not possessed by any kings on the surface, but only someone very powerful could break inside.'
    show expression 'img/bg/special/gates_dwarf.jpg' as bg
    nvl clear
    menu:
        'Crush the Mountain Gates' if game.dragon.size > 3:
            'The pathetic fortifications of the fat little gnomes cannot resist the violent offspring of the Mistress. [game.dragon.fullname] is huge and powerful enough to break through the gates and into the dwarven kingdom. But now there is no going back - if the dwarves are not driven out now, they will rebuild stronger than ever.'
            $ game.dragon.add_special_place('backdor', 'backdor_sealed')
            $ game.dragon.drain_energy()
            call lb_golem_guard from _call_lb_golem_guard
        'Flee':
            'Hanging around the front gate of the dwarves is not a good idea, they might fire something.'
            $ game.dragon.gain_rage()
        
    return
    
label lb_golem_guard:
    stop music fadeout 1.0
    play music "mus/moria.ogg"
    $ renpy.music.queue(get_random_files('mus/ambient')) 
    show expression 'img/bg/special/moria.jpg' as bg
    'Even after the gate collapses, dust and pebbles continue to pour from the ceiling. Footsteps of the gate guard echo through the central galley - a fully forged and tempered mechanical giant. There are few creatures on the surface equal to it in strength...'
    $ game.foe = Enemy('golem', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Fight the Iron Golem':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_38
            jump lb_dwarf_army
        'Flee' if game.dragon.bloodiness < 5:
            'Today they are lucky, but even if they rebuild the gate, they won\'t be left alone for long...'
            $ game.dragon.gain_rage()
    
    return
    
label lb_dwarf_army:
    'Like a deadly hurricane [game.dragon.fullname] rushes into the inner chambers of the dwarven kingdom. However, the dwarves are still not defenseless, the dragon stumbles into the path of a hastily assembled strike force...'
    $ game.foe = Enemy('dwarf_guards', game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Massacre':
            call lb_fight from _call_lb_fight_39
            'Now that the main forces of the dwarves are defeated and demoralized, it is necessary to choose where the final blow will be struck. The housing quarter is almost defenseless and there the dwarves can be killed before they have time to escape. On the other hand, the most important valuables are kept lower, in the main treasury. If you do not pay a visit there now, the cunning dwarves will make out with every last coin.'
            menu:
                'Down to the treasury!':
                    call lb_dwarf_treashury from _call_lb_dwarf_treashury
                    
                'Rob the halls':
                    call lb_dwarf_houses from _call_lb_dwarf_houses
                    
                'Flee':
                    'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
                    $ game.dragon.gain_rage()
                    
        'Run, tail between legs':
            'Today shorty is lucky, but even if they restore the gate, they will not be left alone for long...'
            $ game.dragon.gain_rage()
    return
    
label lb_dwarf_houses:
    'Although most of the dwarves run around in panic trying to save themselves and their belongings, many clutch crowbars, picks, and axes, ready to repulse the enemy...'
    $ game.foe = Enemy('dwarf_citizen', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Fight the dwarves':
            call lb_fight from _call_lb_fight_40
            call lb_dwarf_ruins from _call_lb_dwarf_ruins
        'Flee':
            'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
            $ game.dragon.gain_rage()        
    return
    
label lb_dwarf_treashury:
    'Realizing that their kingdom is on the brink of collapse, the dwarves are trying to save the largest valuables, and the treasures of the king. There are not many fighters among them, but there is one worth an entire army - clad in armor to the eyes, a dwarven champion stands forth, brandishing a massive and sharp axe.'
    $ game.foe = Enemy('dwarf_champion', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Fight the champion':
            call lb_fight from _call_lb_fight_41
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'     
            call lb_dwarf_rob from _call_lb_dwarf_rob
        'Flee':
            'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
            $ game.dragon.gain_rage()      
    return

label lb_dwarf_rob:
    python:
        count = random.randint(12,15)
        alignment = 'dwarf'
        min_cost = 500
        max_cost = 5000
        obtained = "Looted from the king\'s treasury under the mountain."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the Great Treasury':
            show expression 'img/bg/hoard/base.jpg' as bg
            'The vile dwarves managed to take many things away, but even what is left is dazzling. Nowhere else is there such a rich hoard!'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            call lb_dwarf_ruins from _call_lb_dwarf_ruins_1
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
    return
            
label lb_dwarf_ruins:
    show expression 'img/bg/special/moria.jpg' as bg
    'There once lived dwarves here, but now this place is desolate and abandoned. Inside, you can make a specious and well-defended lair.'
    menu:
        'Make a lair here':
            $ game.create_lair('underground_palaces')
            $ game.dragon.del_special_place('frontgates')
            $ game.dragon.del_special_place('backdor')
        'Go away':
            $ game.dragon.add_special_place('frontgates', 'frontgates_open')
    return 
