# coding=utf-8
#spellchecked
init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
        
label lb_location_sea_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'sea'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
        
    if not game.dragon.can_swim: 
        '[game.dragon.name] paws at the salty seawater. If only he knew how to breathe underwater...'
    else:
        call lb_encounter_sea from _call_lb_encounter_sea
    return
    
label lb_encounter_sea:
    $ choices = [
        ("lb_enc_fishers", 10),
        ("lb_enc_yacht", 10),
        ("lb_enc_bark", 10),
        ("lb_enc_tuna", 10),
        ("lb_enc_shark", 10),
        ("lb_triton_found", 10),
        ("lb_enc_galeon", 10),
        ("lb_enc_diver", 10),
        ("lb_enc_mermaid", 10),
        ("lb_enc_merfolks", 10),
        ("lb_enc_mermaids", 10),
        ("lb_enc_shipwreck", 10),
        ("lb_patrool_sea", 3 * game.mobilization.level)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)

    return 
    
label lb_enc_tuna:
    '[game.dragon.fullname] notices a large school of tuna fish floating downstream. Some of the most well fed fishes are as fat as village bulls. Surely they are even tastier!'
    nvl clear
    menu:
        'Eat the tuna' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] catches and devours the largest fish in the group. The blood soon attracts numerous sharks, but seeing who is eating, they immediately swim away.'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
        'Slaughter the whole school' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            'Swimming at top speed [game.dragon.name] crashes into the school of fish, breaking it apart. He frantically beats the water with teeth and claws, cutting the fish into ribbons and turning the water red with clouds of bloods. As if out of nowhere, bloodthirsty sharks appear, adding to the chaos and slaughter. A good way to release rage, who would have thought that you could go so much pleasure from a single shoal?'    
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_shark:
    'Swimming towards the dragon is a majestic great white shark. She really is an outstanding specimen, no less than six meters in length. It seems she considers herself the queen of these waters.'
    nvl clear
    menu:
        'Fight the shark':
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('shark', game_ref=game)
            call lb_fight from _call_lb_fight_20
            if game.dragon.hunger > 0:
                'The hungry [game.dragon.type] tears the defeated sharks into pieces and swallows the biggest one, while smaller sharks appear to fight for the scraps.'
                python:
                    if game.dragon.bloodiness > 0:
                        game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('shark_meat')
            else:
                '[game.dragon.fullname] is not hungry right now, so he leaves the wounded shark to the mercy of its smaller brethren, who have come smelling blood.'
        'Dive deeper' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_fishers:
    '[game.dragon.fullname] stumbles upon a fishing boat headed to port. Their deck is loaded with fish.'
    nvl clear
    menu:
        'Snatch the fish' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            'The fishermen cry in surprise and horror as a head protrudes from the water and grabs a fish right out of their boat. And then another and another, until the vessel reaches the shore. Perhaps the fishermen would have jumped into the sea in fear, if they didn\'t know that there are even more dangerous things lurking there.'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Topple the boat' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            '[game.dragon.kind] leaps out of the water like a frolicking dolphin and falls on the boat with all his weight, so that it breaks down the middle with a crunch, throwing up a cloud of spray and pitching the fishermen off the side. He bites into one to attract sharks to finish the job. Maybe someone will come along and save them...'    
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_yacht:
    'Along the coast an expensive pleasure yacht leisurely floats. Judging by the smell there is a virgin girl aboard, probably the daughter of a rich merchant or maybe even a nobleman! In any case, it\'s fair prey for the lord of these waters.'
    nvl clear
    menu:
        'Snatch the girl from the deck':
            $ chance = random.choice(['citizen', 'citizen', 'citizen', 'princess'])
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl(chance)
            'Carefully, so the yacht does not see it coming, the [game.dragon.kind] swims by the boat on a parallel course, waiting for the right moment. And he does not have to wait long. A beautiful young [game.girl.type] comes out on the deck and leans on the railing, watching fish frolic on the waves. Without hesitating, [game.dragon.name] grabs her and drags her through the sea and onto the beach, in a cozy quiet place suitable for a romantic dinner... '
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_12      
        'Let her be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
    
label lb_enc_bark:
    'Knowing that trade routes lie along the coast, the [game.dragon.kind] decides to swim along one of them and runs into a heavily laden ship. Judging by the small, it carries a cargo of wine, oil, and spices from countries overseas. Certainly on board there must be ringing coins to decorate the dragon\'s hoard...'
    menu:
        'Extort money':
            python:
                game.dragon.drain_energy()
                passing_tool = random.randint(1, 20)
                gold_trs = treasures.Coin('dubloon', passing_tool)
                game.lair.treasury.receive_treasures([gold_trs])
            'Deciding not to tempt fate, the captain gives the dragon some gold dubloons, so that the ship can past unharmed.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Sink the ship' if game.dragon.bloodiness >= 5:
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('ship', game_ref=game)
            call lb_fight from _call_lb_fight_21
            'While the ship slowly lists and sinks and the surviving crew try to save their lives, [game.dragon.name] carefully searches the cargo hold and captain\'s cabin, taking every coin.'
            python:
                count = random.randint(5, 15)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000
                obtained = "Simple coins."
                trs = treasures.gen_treas(count, ['taller', 'dubloon'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
            '[trs_descrptn]'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
        
label lb_enc_galeon:
    'Large sails appear on the horizon, belonging to a heavily armed galleon. On such vessels the king\'s men carry gold from the new world. And the holds of this vessel are not empty. To make them empty will not be easy... '
    $ game.foe = Enemy('battleship', game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Sink the galleon':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_22
            python:
                count = random.randint(10, 25)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['gold']
                obtained = "Simple gold."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
            'In the galleon\'s hold the [game.dragon.kind] finds heavy metal bars, with the emblem of the king certifying high purity:'
            '[trs_descrptn]'
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            
        'Swim away' if game.dragon.bloodiness < 5:
            'The golden cargo is incredibly tempting, but ships like this are well armed. And no matter how much you desire gold, being alive is more important.'       
            $ game.dragon.gain_rage()
    return
    
label lb_enc_diver:
    'These warm clear waters are are a chosen spot for pearl divers. Time after time, they dive to the bottom, looking for the valuable contents of shells. [game.dragon.fullname]  knows that to rob them will be useless, the poor creatures consider themselves lucky if they find one pearl in a whole day\'s work. But the dragon is attracted by pickings of another sort. A tanned diver with powerful legs and a the strong smell of virginity is no less attractive than treasure. This could make a healthy mate...'
    nvl clear
    menu:
        'Snatch the swimmer':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('peasant')
            'The dragon catches the diver.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_13      
        'Go away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_mermaid:
    'At the shore on a large rock sits a little mermaid, running a shiny pearl comb through her long hair. It looks like she\'s waiting for her prince to come...or a dragon.'
    nvl clear
    menu:
        'Catch the little mermaid':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('mermaid')
            'The dragon catches the mermaid.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_water_sex from _call_lb_water_sex      
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
    
label lb_enc_merfolks:
    'A mermaid and merman are floating in the water, holding hands. He is heavily armed and unlikely to give up his girlfriend without a fight. '
    $ game.foe = Enemy('merman', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Attack the fisherman':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_23
            $ description = game.girls_list.new_girl('mermaid')
            'The dragon catches the mermaid.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_water_sex from _call_lb_water_sex_1      
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()       
    return
    
label lb_enc_mermaids:
    'Around a mermaid sea creatures are dancing in a circle.'
    nvl clear
    menu:
        'Catch the mermaid':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('mermaid')
            '[game.dragon.name] swims below the stone the mermaid is on and raises his head right in front of the frightened virgin. He pulls her tail and she falls horrified right into arms of the sea serpent.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_water_sex from _call_lb_water_sex_2      
        'Swim away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()       
    return
     
label lb_enc_shipwreck:
    'Deep at the bottom of the ocean a ship sunken in a storm lies wreck. Finding it would have been impossible if not for the persistent golden smell coming from somewhere in its algae overgrown holds. Dragon\'s simply cannot ignore the smell of gold. Even underwater.'
    nvl clear
    python:
        tr_lvl = random.randint(1, 100)
        count = random.randint(1, 10)
        alignment = 'human'
        min_cost = 1 * tr_lvl
        max_cost = 10 * tr_lvl
        obtained = "This was from the sunken ship."
        trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Dive for treasure':
            $ game.dragon.drain_energy()
            'Peeling off rotten boards from the wreck, [game.dragon.fullname] reaches its valuable content. In the dark flooded hold rests a treasure chest, and inside the chest:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            
        'No time for this' if game.dragon.bloodiness < 5:
            'Of course treasure is useful but dragons have better things to do.  What could be more interesting? It\'s difficult to even imagine... WHAT COULD BE MORE IMPORTANT THAN TREASURE???!'
    return
    
label lb_patrool_sea:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'merman'
            dtxt = 'In the coastal waters is a merman patrolling with a trident. He is nothing but shark bait.'
        elif chance < 7:
            patrool = 'merman'
            dtxt = 'In the coastal waters is a merman patrolling with a trident. He is nothing but shark bait.'
        elif chance < 11:
            patrool = 'griffin_rider'
            dtxt = 'A shrill cry is heard from heaven - a rider on a griffon swoops down from on high, having caught sight of glossy dragon scales on the smooth surface of the water.'
        elif chance < 16:
            patrool = 'battleship'
            dtxt = 'Along the shores of the inhabited areas, an armed ship prowls. The people have begun to take the protection of their coasts seriously.'
        else:
            patrool = 'triton'
            dtxt = 'Usually in the deep sea a serpent does not meet any enemies besides the occasional crazy shark, but this time, fate brought him to a mighty sea giant. A triton is armed and likely came hunting for the reptile vexing his subjects.'
    '[dtxt]'
    python:
        game.foe = Enemy(patrool, game_ref=game)
        battle_status = battle.check_fear(game.dragon, game.foe)
    if 'foe_fear' in battle_status:
        $ narrator(game.foe.battle_description(battle_status, game.dragon))
        return
    $ game.dragon.drain_energy()
    call lb_fight(skip_fear=True) from _call_lb_fight_24
    return
