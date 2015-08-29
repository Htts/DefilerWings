# coding=utf-8
init python:
    from pythoncode.characters import Enemy, Talker
    from pythoncode.utils import weighted_random
    
label lb_location_plains_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))
    $ place = 'plain'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!!'
        return
        
    menu:
        'Prowl around':
            call lb_encounter_plains from _call_lb_encounter_plains
            return
        'Lonley farmstead':
            $ village_size = 1
            call lb_village from _call_lb_village
        'Small village':
            $ village_size = 2
            call lb_village from _call_lb_village_1
        'Village':
            $ village_size = 3
            call lb_village from _call_lb_village_2
        'Town':
            $ village_size = 4
            call lb_village from _call_lb_village_3
        'City':
            $ village_size = 5
            call lb_village from _call_lb_village_4
        'Go back':
            return
        
    return
    
label lb_encounter_plains:
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_enc_fair", 5),
        ("lb_enc_berries", 10),
        ("lb_enc_laundry", 10),
        ("lb_enc_bath", 10),
        ("lb_enc_militia", 10),
        ("lb_enc_mill", 10),
        ("lb_enc_granary", 10),
        ("lb_enc_sheepherd", 10),
        ("lb_enc_pigs", 10),
        ("lb_enc_cattle", 10),
        ("lb_enc_gooze", 10),
        ("lb_enc_redhood", 3),        
        ("lb_patrool_plains", 3 * game.mobilization.level),
        ("lb_enc_noting", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return
  
label lb_enc_redhood:
    python: #делаем аватарку волка для диалогового окна
        wolf = Talker(game_ref=game)
        wolf.avatar = "img/avahuman/wolf.jpg"
        wolf.name = 'Sergei "BBW" Wolkov'    
    if "redhood_done" in persistent.easter_eggs: #проверяем не было ли уже этого энкаунтера за всё время игры
        jump lb_encounter_plains #если уже был хотя бы раз, игнорируем и переходим к обычным встречам
    $ persistent.easter_eggs.append("redhood_done") #отмечаем что энкаунтер с красной шапочкой произошел
    "[game.dragon.fullname] notices a small figure in a bright red cape in the distance, straying off the forest path. She holds in her hand a heavy basket of pastries. Farmers don\'t usually wear red capes...[game.dragon.kind] decides to follow the girl, but she has already disappeared behind some trees, so he follows her smell."
    show expression 'img/bg/forest/1.jpg' as bg    
    "Judging from her trail, the red hooded girl met an unusual creature on the crossroads. The smell is strange, reminiscent of wet dog, human flesh, and the Mistress\'s spawn. The creature did not attack the girl, there is a spot with many footprints, and from there they went away seperately - but in the same direction. Interesting... "
    "The tracks of the red hooded girl lead to a clearing with a small house, very tidy for a home in a remote forest. Inside noises are heard - a girl\'s screams, a hollow roar, and overturned furniture. "
    nvl clear
    show expression 'img/scene/wolf_sex.jpg' as bg
    pause (50.0)
    "Peering through the window, [game.dragon.name] sees the aftermath of the fight. A huge anthropomorphic wolf brutally raping the girl in the red cape, next to the corpse of an old gray-haired woman. She squeals and struggles, but it only seems to inflame the wolf. With an incredibly happy expression on his face, he twists her hands behind her back and fucks her doggy style, growling. "
    "The long, sharp claws of the monster leave bloody rips in her delicate skin, as the wolf squeezes his paws in pleasure, filling her tormented womb with seed. Satisfied, the monster lies panting on the floor. His bleeding victim tries to crawl to the door, but the werewof isn\'t finished."
    "With an easy movement he grabs the girls thigh and pulls her back. The poor girl screams and begs him to stop, but the wolf just smiles with his tongue out. Roughly he grabs her delicious ass with his clawed feet, and with a visible effort, jams his impressive canine rod right in her anus. Judging from the force required, Fluffy just tore her sphincter to squeeze inside."
    nvl clear
    "Little Red Rding Hood squeals so loudly that the werewolf\'s ears flatten, but it does not stop his abuse. On the contrary, incensed by her bloody screams he bites his teeth into her right hand and tears it off. [game.dragon.name] knows from is own experience how to combine sex and a good breakfas, and the wolf crunches bone with such gusto that the dragon starts to salivate."
    "After a few minutes of this bloody feast the girl, or what is left of her, lays quiet on the floor. Satisfied and satiated, the wolf methodically bites off an undamaged leg, along with a large chunk of buttock. Then, taking human form and throwing the bloody trophy on his shoulder, he goes out and encounters the dragon."
    show expression 'img/bg/forest/1.jpg' as bg
    game.dragon "Hello. Are you one of my mother\'s flock? Somehow I don\'t recall you, brother..."
    wolf "(oh fuck, a dragon) Uuuuh… ahem... nyet. I\'m from Moscow. Sergei. Sergei Wolkov."
    game.dragon "That\'s the first time I\'ve heard of it. Do you always have such fun there in Moscow? It must be a cheerful place."
    wolf "Da, I rustled up lot of skirts in my time, but there now I can not go back. Fogs do not allow it. Listen...can go already, you have your business and I have mine, no reason to make the conversation?"
    game.dragon "Won\'t you part with a leg? I\'m a little hungry..."
    wolf "Nyet, I need to feed children. But in house is left something still, and old woman is almost whole."
    game.dragon "Very well. Children are sacred, we need the little freeloaders to keep the world running. Godspeed, Sergei Wolkov from Moscow."
    nvl clear
    "Nodding slighty to each other, the monsters went their seperate ways and continued their adventures."    

    return

label lb_enc_fair:
    $ txt = game.interpolate(random.choice(txt_enc_fair[0]))
    '[txt]'
    nvl clear
    menu:
        'Get the beauty':
            python:
                game.dragon.drain_energy()
                description = game.girls_list.new_girl('peasant')
                txt = game.interpolate(random.choice(txt_enc_fair[1]))
            '[txt]'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_3      
            return

        'Get the beast':
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('bull_champion', game_ref=game)
            call lb_fight from _call_lb_fight_2
            menu:
                'Сожрать призового быка' if game.dragon.hunger > 0:
                    'Бык съеден. -1 к голоду, +1 к похоти. Ярость обнуляется.'
                    $ game.dragon.reputation.points += 1
                    '[game.dragon.reputation.gain_description]'
                    python:
                        game.dragon.bloodiness = 0
                        if game.dragon.lust < 3:
                            game.dragon.lust += 1
                        game.dragon.hunger -= 1
                'Go away':
                    return
            return
            
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return
    
    return
    
    
label lb_enc_berries:
    'Girls at the edge of the woods gather berries and sing. But when the dragon appears, the singing gives way to wild squealing. Pretty girls scatter in all directions, dropping baskets of sugary ripe berries. One beauty doesn\'t won\'t let go of her basket for anything and runs slowly away - a girl so sweet should be loved! But it may be better not to catch the sweet tooth, and instead look for an innocent virgin to bring up offpsring.'
    nvl clear
    $ description = game.girls_list.new_girl('peasant')
    nvl clear
    menu:
        'Snatch a virgin':
            $ game.dragon.drain_energy()
            'Forgetting the useless berries, the [game.dragon.kind] rushes after the virgin girl. Althrough she runs from the lust obsessed lizard as fast as she can, the frightened maiden cannot escape.'
            nvl clear
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_4      
            return
            
        'Girl with berries' if game.girl.treasure:
            $ game.dragon.drain_energy()
            'Mmmm....meat in sweet sauce. The [game.dragon.name] daydreams and slobbers. The girl with the basket must be taken, she will be fun!'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl 'Oh, here, take the berries, but do not eat me, please! They are delicious, really! Here, raspberries, blueberries, strawberries....aaaah...do not lick me THERE! The berries are in the basket....'
            menu:
                'Strip and rob her':
                    $ description = game.girls_list.rob_girl()
                    game.girl.third "[game.dragon.name] roughly strips the girl\'s clothes and takes from her everything of value, including her cherished basket."
                    game.girl 'Mama, I\'m so ashamed... why tear my skirt?! Can I go now? Oh, pleeeeease...dragon...let me go!.'
                    menu:
                        'Play with the girl' if game.dragon.lust > 0:
                            nvl clear
                            show expression 'img/scene/berries.jpg' as bg
                            game.girl.third 'The [game.dragon.kind] rolls over on his back and grasps the peasant\'s hand in his flexible tail, making her move closer. The girl watches fascinated as from a fold of the dragon\'s belly his inhuman member swells up, covered in soft but menacing looking spikes.'
                            nvl clear
                            game.dragon 'If you want to live, do what I say.'
                            game.girl 'Okay, okay. Just don\'t eat me, please, I\'ll do anything.'
                            game.girl.third 'Following the dragon\'s instructions, [game.girl.name] takes a generous scoop of berries from the basket and smears herelf head to toe in their sticky juice. Another generous handful she pushes between her legs, stuffing a mix of beries into her tight vagina. Next, the [game.dragon.kind] orders the girl to tenderly smear the rest of the berry juice on his intimidating shaft.'
                            nvl clear
                            game.dragon 'Yes, that\'s right. Good girl. Now, sit on my chest, so I can see your sweet ass. The rules of the game: I will eat berries from your cunt, and you lick my cock clean. If you finish first, I\'ll let you go.'
                            game.girl.third 'The frightened peasant immediately began licking berries off the dragon\'s meat as if it was the most delicious thing in the world, choking and gasping. Happily [game.dragon.name] slowly opened his mouth, and wish relish launched his flexible forked tongue into her sticky, berry filled pussy. For some time the forest glade was filled with the sounds of intent chomping and squelching, but soon the berries stuffed in the girl ran out. [game.dragon.name] pushed his tongue even deeper into her dark and sticky passafe, all the way to the entrance of her convulsively contracting womb. Writhing in pain, [game.girl.name] continued trying in vain to lick off the last drops of berry juice from the base of the dragon\'s cock, even though it was too late.'
                            menu:
                                'Devour the maiden' if game.dragon.hunger > 0:
                                    play sound "sound/eat.ogg"
                                    nvl clear
                                    'Thanks to their snake blood, dragons are able to stretch their jaws incredibly wide and swallow prey whole. [game.dragon.name] did this without even taking his tongue out of his sweet juice smeared victim until she was entirely in his mouth.'
                                    python:
                                        if game.dragon.bloodiness > 0:
                                            game.dragon.bloodiness = 0
                                'Let her go':
                                    'The peasant runs away, trying to cover her naked, juice covered body with her hands.'
                            return
                        'Release':
                            'The naked peasant runs away, trying to cover her body with her hands.'
                            hide xxx
                            return
                'Take the berries and let her go':
                    '[game.dragon.name] snacks on the sweet berries and leaves. The confused peasant farmgirl looks at the crushed basket, and shakes her fist at impudent retreating dragon\'s ass.'
                    game.girl 'Уууу, you devil! I will tell the baron, he will send knights after you, worm!'
                    python:
                        if game.dragon.lust < 3:
                            game.dragon.lust += 1
                    return
                    
        'Let them be': 
            '[game.dragon.name] taking one of the abandoned baskets of berries for dessert, the dragon leaves.'
            $ game.dragon.gain_rage()
            return
    
    return
    
label lb_enc_shrooms: #TODO: Currently unfinished and unused. 
    'Girls at the edge of the woods harvest mushrooms. When the dragon rises up they scream and run away. One girl does not throw away her basket of mushrooms. Another girl smells like a virgin.'
    $ description = game.girls_list.new_girl('peasant')
    nvl clear
    menu:
        'Snatch the virgin':
            $ game.dragon.drain_energy()
            'After a short chase, the dragon catches the innocent girl.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_5      
            return
            
        'Girl with mushroms':
            $ game.dragon.drain_energy()
            'After a short chase, the dragon catches the girl with the mushrooms.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            game.girl 'Oh, please, just don\'t eat me!'
            menu:
                'Rob her' if game.girl.treasure:
                    $ description = game.girls_list.rob_girl()
                    game.girl.third "The dragon strips the girl naked and takes everything of value."
                    game.girl 'Can I go now?'
                    nvl clear
                    menu:
                        'Play with the girl' if game.dragon.lust > 0:
                            'The dragon forces the girl to give him a blowjob.'
                            $ game.dragon.lust -= 1
                            nvl clear
                            menu:
                                'Devour the girl' if game.dragon.hunger > 0:
                                    'The dragon makes the peasant fry the mushrooms, then he guts her, stuffs her with mushrooms, and devours her.'
                                    python:
                                        if game.dragon.bloodiness > 0:
                                            game.dragon.bloodiness = 0
                                        if game.dragon.lust < 3:
                                            game.dragon.lust += 1
                                        game.dragon.hunger -= 1
                                'Release her':
                                    'The naked peasant girl runs away, trying to cover her shame with her arms.'
                            return
                        'Devour the girl' if game.dragon.hunger > 0:
                            'The dragon makes the peasant fry the mushrooms, then he guts her, stuffs her with mushrooms, and devours her.'
                            python:
                                if game.dragon.bloodiness > 0:
                                    game.dragon.bloodiness = 0
                                if game.dragon.lust < 3:
                                    game.dragon.lust += 1
                                game.dragon.hunger -= 1
                            return
                        'Let her go':
                            'Голая крестьянка убегает пытаясь прикрыть срам руками.'
                            return
                'Play with the girl' if game.dragon.lust > 0:
                    'The dragon makes the girl strip naked and give him a blowjob.'
                    $ game.dragon.lust -= 1
                    nvl clear
                    menu:
                        'Devour the maiden' if game.dragon.hunger > 0:
                            'The dragon makes the peasant fry the mushrooms, then he guts her, stuffs her with mushrooms, and devours her.'
                            python:
                                if game.dragon.bloodiness > 0:
                                    game.dragon.bloodiness = 0
                                game.dragon.hunger -= 1
                        'Let her go':
                            'The naked peasant girl runs away, trying to cover her nudity with her hands.'
                    return
                'Devour the maiden' if game.dragon.hunger > 0:
                    'The dragon tears off the peasant\'s clothes, guts and stuffs her with mushrooms, and then devours her.'
                    python:
                        if game.dragon.bloodiness > 0:
                            game.dragon.bloodiness = 0
                        if game.dragon.lust < 3:
                            game.dragon.lust += 1
                        game.dragon.hunger -= 1
                'Take away the mushrooms and release her':
                    'The dragon snacks on the fresh mushrooms and leaves.'
                    python:
                        if game.dragon.lust < 3:
                            game.dragon.lust += 1
                    return
                    
        'Let them be': 
            '[game.dragon.name] takes one of the abandoned mushroom baskets as a snack and leaves.'
            $ game.dragon.gain_rage()
            return
    
    return

    
label lb_enc_laundry:
    'Loud splashing sounds and girlish laughter bring the dragon to a river bank. Women are washing clothes here, and among them there is bound to be at least one virgin worthy to bear offspring of the ancient blood...'
    nvl clear
    menu:
        'Snatch a virgin':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('peasant')
            '[game.dragon.name] runs snarling out of the bushes, and the women on the bank make heart-rending shrieks that pain the ears. Females scatter in all directions, but the dragon needs only one of them, and he easily catches her. It will take plenty of time before armed men run the scene, there is no hurry...'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_6      
            return        
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return    
    return
    
label lb_enc_bath:
    'Loud splashing sounds and girlish laughter bring the dragon to a river bank. Naked girls are swimming in a creek overgrown with reeds and water lillies. How nice, you won\'t even have to run...'
    nvl clear
    menu:
        'Snatch a girl from the river':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('peasant')
            'Humans are much better at running than swimming, so to snatch a girl splashing in the water is not difficult in the slightest.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_7      
        'Leave them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_militia:
    python:
        if game.mobilization.level <= 0:
            renpy.jump('lb_encounter_plains')
        else:
            renpy.jump('lb_enc_militia_true')
    return

label lb_enc_militia_true:
    show expression 'img/scene/fight/militia.jpg' as bg
    'On an open field, militia recruits are raining. They do not represent such a great threat as the experienced fighters, and they have nothing worth stealing. But if you do not disperse this mob, sooner or later they will join the ranks of the regular army and be nothing to trifle with...'
    nvl clear
    menu:
        'Fight the militia':
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('militia', game_ref=game)
            call lb_fight from _call_lb_fight_3
            '  There is no longer a militia preparing to fill the regular army. The few survivors fled in horror. Now it will be more difficult for the king to send out patrols.'
            $game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            $ game.mobilization.level -= 1
                        
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_mill:
    show expression 'img/bg/special/windmill.jpg' as bg
    'On top of the hill stands a tall wooden tower, with blades rotating from the force of the wind. Apparently this is some sort of human agricultural machinery. Not very interesting, but destroying it will be fun, and most importantly it will bring hunger and ruin to the area.'
    nvl clear
    menu:
        'Break down the mill' if game.dragon.size > 3:
            $ game.dragon.drain_energy()
            "[game.dragon.name] is big enough to contend with the forces of the rotating tower. The dragon rises to his full height, and with all his might pushes the tower down. From the crumbling structure a fat man covered in flour pops out, tumbling head over heels down the hill. Ruined pieces of the mill roll after him. If the people have nothing to eat, they will think less about fighting dragons!"
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Conjure a spark' if game.dragon.mana > 0:
            $ game.dragon.drain_energy()
            "[game.dragon.name] whispers a magic spell, calling forth fire. Immediately afterwards he raises his tail and walks away satisfied. It is well known what will happen - in a suspension of flour dust and air, the smallest spark will cause an violent detonation. The dragon doesn\'t even look back at the explosion!"
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            $ game.dragon.drain_mana()
            '[game.dragon.reputation.gain_description]'
        'Investigate' if game.dragon.size <= 3 and game.dragon.mana == 0:
            $ game.dragon.drain_energy()
            "[game.dragon.name] carefully surveys the unusual structure, investigating its purpose and weaknesses. People use this tower to rotate a stone, grinding grain into flour. [game.dragon.name] badly wishes to destroy it, but it stands too firmly. You will need either a body large enough to knock it down, or foul magic to send a curse inside it. "
            'Time lost in vain. The dragon leaves, no better off than before.'
        'Ignore' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_granary:
    show expression 'img/bg/plain/granary.jpg' as bg    
    'In the fields some distance from the villages is a large wooden structure. Judging by the smell, no one lives there, only grain lies inside. For some reason humans love eating grain...stupid humans. How can you live without meat?'
    nvl clear
    python:
        doit = False
        if 'fire_breath' in game.dragon.modifiers(): 
            doit = True
    menu:
        'Breath fire' if doit:
            $ game.dragon.drain_energy()
            "[game.dragon.name] spews a stream of liquid flame directly onto the thatched roof of the granary. The people will be unable to extinguish the fire, and when the grain is burned up, they will have less time to think about how to slay dragons, and more time to think about how they will fill their stomachs..."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
        'Conjure a spell of rot' if game.dragon.mana > 0:
            $ game.dragon.drain_energy()
            "Using an old formula of witchcraft, [game.dragon.name] throws a frag into the window of the barn. In just a few hours, mold grow on the grain and make it unusable. The people will have less to feed their troops, so the dragon and his offspring will live a little easier next year."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            $ game.dragon.drain_mana()
            '[game.dragon.reputation.gain_description]'
        'Investigate' if not doit and game.dragon.mana == 0:
            $ game.dragon.drain_energy()
            "[game.dragon.name] carefully examines the huge barn. There is enough good grain here to feed a city. Burning everything to ground would make the people starve, but there\'s no ignition source..."
        'Ignore' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return

label lb_enc_gooze:
    'A barefoot little country girl grazes geese. She is too young to give birth, but the thought of a nice breakfast is quite appealing.'
    nvl clear
    menu:
        'Eat the geese' if game.dragon.hunger > 0:
            '[game.dragon.name] catches and swallows a fat goose, but the others fly away.'
            python:
                game.dragon.drain_energy()
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness -= 1
        'Eat the girl' if game.dragon.hunger > 0:
            '[game.dragon.name] eats the girl alive, crunching through thin bones.'
            $ game.dragon.drain_energy()
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        'Massacre' if game.dragon.bloodiness >= 5:
            $ game.dragon.drain_energy()
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            '[game.dragon.name] lets loose, killing the girl and every goose he can catch.'    
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_pigs:
    'Across from a field of wheat, a herd of pigs graze in an oak grove. The swineherd who watches them is fast asleep under a tree, face covered with a straw hat. But among the pigs is another, much more vigilant guard - a large, angry wolfhound.'
    $ game.foe = Enemy('dog', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Attack the herd' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_4
            'By the time the dog is defeated, the pigs and swineherd have had time to disperse, but to escape from a dragon is a foolish idea - [game.dragon.name] has a perfect scent, and never loses track of his chosen victim. Soon one fat pig in the herd is getting smaller.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        'Massacre the herd' if game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_5
            'Having torn the dog to shreds, [game.dragon.name] catches and kills the swineherd. The pigs are running away, but they do not matter.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return    
    
    return    

label lb_enc_sheepherd:
    'In green hills covered with lush grass, an old shepherd grazes his sheep. Spotting the approaching dragon, the wise old man chooses to run far away, but his faithful sheepdog seems ready to guard the herd until its last breath.'
    $ game.foe = Enemy('dog', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Attack the herd' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_6
            'During the fight with the dog the sheep scattered, but their white wool is easy to spot on distant hills. Catching a lamb for dinner is easy.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        'Massacre the herd' if game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_7
            '[game.dragon.name] catches and kills a few sheep, but has no desire to eat. Sometimes you\'ve got to let off steam and unleash primitive fury.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return    
    
    return


label lb_enc_cattle:
    'Well, what is a countryside without grazing cattle? [game.dragon.name] goes to the cowherd and asks for lunch. The boy flees in terror, but one of the bulls, the largest, is determined to protect the herd.'
    $ game.foe = Enemy('bull', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Attack the herd' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_8
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
            '[game.dragon.name] tears the bull into pieces and swallows chunks of steaming meat, quickly becoming stuffed.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
        'Massacre the herd' if game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_9
            '[game.dragon.name] kills a few cows and scatters the herd, though he has no desire to eat - he is simply angry.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return    
    
    return

label lb_enc_noting:
    show expression 'img/bg/special/village_burned.jpg' as bg          
    'There is only desolation and ruin. Humans and animals once lived here, but now no one remains. Around there are only destroyed houses and farmland overgrown with tall weeds.'
    python:
        if game.dragon.bloodiness < 5: 
            game.dragon.gain_rage()
    return


# разные деревни
label lb_village:
    python:
        a = 10 + game.poverty.value - village_size
        chance = random.randint(1, a)
        if chance > 10:
            village_size = 0
        txt1 = village['overview'][village_size]
    show expression 'img/bg/special/village.jpg' as bg     
    '[txt1]'
    $ game.foe = Enemy(village['deffence'][village_size], game_ref=game)    
    $ chances = show_chances(game.foe)    
    nvl clear
    menu:
        'Impose a tribute' if village_size > 0 and game.dragon.fear > village_size:
            $ game.dragon.drain_energy()
            show expression 'img/bg/special/fear.jpg' as bg
            if village_size == 1:
                'The villagers give up their only cow. [game.dragon.name] eats it.'
                python:
                    if game.dragon.bloodiness > 0 and game.dragon.hunger > 0: 
                        game.dragon.bloodiness = 0
                        game.dragon.hunger -= 1
            elif village_size == 2:
                'The villagers give the dragon a young peasant girl.'
                $ description = game.girls_list.new_girl('peasant')
                nvl clear
                game.girl.third "[description]"
                call lb_nature_sex from _call_lb_nature_sex_8                   
            elif village_size == 3:
                'The mayor\'s wife gives up her most expensive jewelery:'
                python:
                    count = 1
                    alignment = 'human'
                    min_cost = 10
                    max_cost = 250
                    obtained = "Tribute from a village."
                    trs = treasures.gen_treas(count, data.loot['jeweler'], alignment, min_cost, max_cost, obtained)
                    trs_list = game.lair.treasury.treasures_description(trs)
                    trs_descrptn = '\n'.join(trs_list)
                    game.lair.treasury.receive_treasures(trs)
                '[trs_descrptn]'
            elif village_size == 4:
                'The villagers collect money from each household to pay tribute to the dragon:'
                python:
                    count = 1
                    alignment = 'human'
                    min_cost = 100
                    max_cost = 500
                    t_list = ['farting']
                    obtained = "Tribute from a village.."
                    trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                    trs_list = game.lair.treasury.treasures_description(trs)
                    trs_descrptn = '\n'.join(trs_list)
                    game.lair.treasury.receive_treasures(trs)
                '[trs_descrptn]'
            else:
                'The townsmen give the dragon their most beautiful maiden.'
                $ description = game.girls_list.new_girl('citizen')
                nvl clear
                game.girl.third "[description]"
                call lb_nature_sex from _call_lb_nature_sex_9        
            
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'

        'Rob them' if village_size > 0:
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_10
            'Поселение успешно разграблено. Добыча:'
            python:
                count = random.randint(5, 10)
                alignment = 'human'
                min_cost = 5 * village_size
                max_cost = 25 * village_size
                obtained = "Это предмет из разграбленного людского поселения."
                trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        
        'Raise' if village_size > 0:
            $ game.dragon.drain_energy()
            $ game.foe = Enemy(village['deffence'][village_size], game_ref=game)
            call lb_fight from _call_lb_fight_11
            'Поселение разорено. Разруха в стране растёт. В разрушенных домах и на телах убитых нашлись кое-какие ценности:'
            python:
                count = random.randint(5, 10)
                alignment = 'human'
                min_cost = 5 * village_size
                max_cost = 25 * village_size
                obtained = "Это предмет из разграбленного людского поселения."
                trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
            python:
                game.lair.treasury.receive_treasures(trs)
                game.poverty.value += 1
                game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
    
        'Get out' if game.dragon.bloodiness < 5 and village_size > 0:
            $ game.dragon.gain_rage()
            
        'Get out' if village_size == 0:
            python:
                if game.dragon.bloodiness < 5: 
                    game.dragon.gain_rage()
        
    return

label lb_patrool_plains:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'archer'
            dtxt = 'Along the outskirts of the village a bearded man patrols with a longbow. The local sheriff sent him to protect the village.'
        elif chance < 7:
            patrool = 'xbow_rider'
            dtxt = 'On the country road a detatchement of light cavalry are patrolling. They can respond quickly to any threat, whether it is bandits, monsters, or even a dragon.'
        elif chance < 11:
            patrool = 'heavy_cavalry'
            dtxt = 'The draogn runs into a detachment of heavy cavalry. The people in the region are so frightened, they\'ve begun to send knights to the borders.'
        elif chance < 16:
            patrool = 'griffin_rider'
            dtxt = 'A shrill cry is heard from heaven - a rider on a gryphon swoops down from the sky, having spotted the shine of dragonscale in the fields.'
        else:
            patrool = 'angel'
            dtxt = '%s is forced to close his eyes from a bright glare. A loud announcement: "Die, vile offspring of sin!". This guardian angel was sent by heaven to protect the people.' % game.dragon.name
    '[dtxt]'
    python:
        game.foe = Enemy(patrool, game_ref=game)
        battle_status = battle.check_fear(game.dragon, game.foe)
    if 'foe_fear' in battle_status:
        $ narrator(game.foe.battle_description(battle_status, game.dragon))
        return
    $ game.dragon.drain_energy()
    call lb_fight(skip_fear=True) from _call_lb_fight_12
    return
