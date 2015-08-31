#Translator: There is some very sick shit going on in this file. 
#It seems like a system for making randomly generated treasures read properly in russian,
#which has noun declension and gender. 
#So if you randomly generate a treasure it might be a female "tiara" or a male "scepter" or something
#And then if you randomly say that the tiara is a "polished" tiara you have to choose the female form of polished. 
#And then if you use the noun in different sentences like "The tiara lies on the floor" or "The girl holds her tiara" you have to use different version of "tiara". 
#The only part of this code that serves english is the part that differentiates between singular (it) and they (plural)

#The plan:
#Step 1: 
#replace every "he" "she" with an "it" or "they" (for plural)
#replace all the russian variations with a simple repeated english noun
#Step 2:
#By playing the game, see if we need to add some extra words. Like putting an "of" in front of every word where it says "prepositional".
#Step 3: rip out all of the code that becomes unnecessary due to steps 1 and 2.  
#step 4: may god have mercy on our souls

# coding=utf-8

import random

from renpy import store
from renpy.exports import call_screen
from copy import deepcopy
                
from utils import weighted_random
from data import achieve_target, get_description_by_count

"""Dictionary for gems. Keys- the names of the stones. Values- tuples of form (chance of, value of)"""
gem_types = {
    "amber": (5, 3),
    "crystal": (5, 5),
    "beryll": (4, 10),
    "tigereye": (4, 10),
    "granite": (3, 20),
    "tourmaline": (3, 20),
    "aqua": (3, 20),
    "pearl": (3, 10),
    "black_pearl": (3, 15),
    "elven_beryll": (2, 50),
    "topaz": (2, 50),
    "sapphire": (2, 50),
    "ruby": (2, 50),
    "emerald": (2, 25),
    "goodruby": (1, 100),
    "goodemerald": (1, 100),
    "star": (1, 100),
    "diamond": (1, 75),
    "black_diamond": (1, 100),
    "rose_diamond": (1, 100),
}

"""As above, but for type of material"""
material_types = {
    "jasper": (5, 1),
    "turquoise": (5, 1),
    "jade": (5, 1),
    "malachite": (5, 1),
    "coral": (4, 5),
    "ivory": (4, 10),
    "agate": (3, 5),
    "shell": (3, 5),
    "horn": (1, 25),
}

"""словарь для описания типов материалов,
ключи - названия материалов,
значения - словарь для различных падежей русского названия материала"""
material_description_rus = {
    "jasper": {
        'nominative': u'jasper',
        'genitive': u'jasper'
    },
    "turquoise": {
        'nominative': u'turquoise',
        'genitive': u'turquoise'
    },
    "jade": {
        'nominative': u'jade',
        'genitive': u'jade'
    },
    "malachite": {
        'nominative': u'malachite',
        'genitive': u'malachite'
    },
    "coral": {
        'nominative': u'coral',
        'genitive': u'coral'
    },
    "ivory": {
        'nominative': u'ivory',
        'genitive': u'ivory'
    },
    "agate": {
        'nominative': u'agate',
        'genitive': u'agate'
    },
    "shell": {
        'nominative': u'shell',
        'genitive': u'shell'
    },
    "horn": {
        'nominative': u'horn',
        'genitive': u'horn'
    },
}

"""словарь для описания размеров материалов,
ключи - названия размера материалов,
значения - словарь для русского прилагательного, соответствующего размеру"""
material_size_description_rus = {
    'small': {
        'he': {
            'nominative': u"small ",
            'ablative': u"small "
        },
        'she': {
            'nominative': u"small ",
            'ablative': u"small "
        },
        'they': {
            'nominative': u"small ",
            'genitive': u"small ",
            'ablative': u"small "
        }
    },
    'common': {  # этот размер не отображается
        'he': {
            'nominative': u"",
            'ablative': u""
        },
        'she': {
            'nominative': u"",
            'ablative': u""
        },
        'they': {
            'nominative': u"",
            'genitive': u"",
            'ablative': u""
        }
    },
    'large': {
        'he': {
            'nominative': u"large ",
            'ablative': u"large "
        },
        'she': {
            'nominative': u"large ",
            'ablative': u"large "
        },
        'they': {
            'nominative': u"large ",
            'genitive': u"large ",
            'ablative': u"large "
        }
    },
    'exceptional': {
        'he': {
            'nominative': u"exceptional ",
            'ablative': u"exceptional "
        },
        'she': {
            'nominative': u"exceptional ",
            'ablative': u"exceptional "
        },
        'they': {
            'nominative': u"exceptional ",
            'genitive': u"exceptional ",
            'ablative': u"exceptional "
        }
    }
}
"""словарь для описания степени обработки драгоценных камней,
ключи - названия степени обработки,
значения - словарь для соответствующего русского прилагательного"""
gem_cut_description_rus = {
    ' ': {
        'he': {  # эта полировка не отображается
            'nominative': u'',
            'ablative': u''
        },
        'she': {
            'nominative': u'',
            'ablative': u''
        },
        'they': {
            'nominative': u'',
            'genitive': u'',
            'ablative': u''
        }
    },
    'rough': {
        'he': {
            'nominative': u'rough ',
            'ablative': u''  # 'ablative' не отображается, чтобы не портить описание вещи
        },
        'they': {
            'nominative': u'rough ',
            'genitive': u"rough ",
            'ablative': u''
        }
    },
    'polished': {
        'he': {
            'nominative': u'polished ',
            'ablative': u'polished '
        },
        'they': {
            'nominative': u'polished ',
            'genitive': u'polished ',
            'ablative': u'polished '
        }
    },
    'faceted': {
        'he': {
            'nominative': u'faceted ',
            'ablative': u'faceted '
        },
        'they': {
            'nominative': u'faceted ',
            'genitive': u'faceted ',
            'ablative': u'faceted '
        }
    }
}

"""Словарь для драгоценных камней,
ключ - тип драгоценного камня,
значение - словарь с русским названием драгоценного камня в разных падежах"""
gem_description_rus = {
    "amber": {
        'he': {
            'nominative': u"amber",
            'genitive': u"amber",
            'ablative': u"amber"
        },
        'they': {
            'genitive': u"amber",
            'ablative': u"amber"
        }
    },
    "crystal": {
        'he': {
            'nominative': u'crystal',
            'genitive': u"crystal",
            'ablative': u'crystal'
        },
        'they': {
            'genitive': u"crystal",
            'ablative': u'crystal'
        }
    },
    "beryll": {
        'he': {
            'nominative': u'beryll',
            'genitive': u"beryll",
            'ablative': u'beryll'
        },
        'they': {
            'genitive': u"beryll",
            'ablative': u'beryll'
        }
    },
    "tigereye": {
        'he': {
            'nominative': u'tigereye',
            'genitive': u"tigereye",
            'ablative': u'tigereye'
        },
        'they': {
            'genitive': u"tigereye",
            'ablative': u'tigereye'
        }
    },
    "granite": {
        'he': {
            'nominative': u'granite',
            'genitive': u"granite",
            'ablative': u'granite'
        },
        'they': {
            'genitive': u"granite",
            'ablative': u'granite'
        }
    },
    "tourmaline": {
        'he': {
            'nominative': u'tourmaline',
            'genitive': u"tourmaline",
            'ablative': u'tourmaline'
        },
        'they': {
            'genitive': u"tourmaline",
            'ablative': u'tourmaline'
        }
    },
    "aqua": {
        'he': {
            'nominative': u'aqua',
            'genitive': u"aqua",
            'ablative': u'aqua'
        },
        'they': {
            'genitive': u"aqua",
            'ablative': u'aqua'
        }
    },
    "pearl": {
        'he': {
            'nominative': u'pearl',
            'genitive': u"pearl",
            'ablative': u'pearl'
        },
        'she': {
            'nominative': u'pearl',
            'genitive': u"pearl",
            'ablative': u'pearl'
        },
        'they': {
            'genitive': u"pearl",
            'ablative': u'pearl'
        }
    },
    "black_pearl": {
        'he': {
            'nominative': u'black pearl',
            'genitive': u'black pearl',
            'ablative': u'black pearl'
        },
        'she': {
            'nominative': u'black pearl',
            'genitive': u'black pearl',
            'ablative': u'black pearl'
        },
        'they': {
            'genitive': u"black pearl",
            'ablative': u'black pearl'
        }
    },
    "elven_beryll": {
        'he': {
            'nominative': u'elven beryll',
            'genitive': u"elven beryll",
            'ablative': u'elven beryll'
        },
        'they': {
            'genitive': u"elven beryll",
            'ablative': u'elven beryll'
        }
    },
    "topaz": {
        'he': {
            'nominative': u'topaz',
            'genitive': u"topaz",
            'ablative': u'topaz'
        },
        'they': {
            'genitive': u"topaz",
            'ablative': u'topaz'
        }
    },
    "sapphire": {
        'he': {
            'nominative': u'sapphire',
            'genitive': u"sapphire",
            'ablative': u'sapphire'
        },
        'they': {
            'genitive': u"sapphire",
            'ablative': u'sapphire'
        }
    },
    "ruby": {
        'he': {
            'nominative': u'ruby',
            'genitive': u"ruby",
            'ablative': u'ruby'
        },
        'they': {
            'genitive': u"ruby",
            'ablative': u'ruby'
        }
    },
    "emerald": {
        'he': {
            'nominative': u'emerald',
            'genitive': u"emerald",
            'ablative': u'emerald'
        },
        'they': {
            'genitive': u"emerald",
            'ablative': u'emerald'
        }
    },
    "goodruby": {
        'he': {
            'nominative': u'fine ruby',
            'genitive': u"fine ruby",
            'ablative': u'fine ruby'
        },
        'they': {
            'genitive': u"fine ruby",
            'ablative': u'fine ruby'
        }
    },
    "goodemerald": {
        'he': {
            'nominative': u'fine emerald',
            'genitive': u"fine emerald",
            'ablative': u'fine emerald'
        },
        'they': {
            'genitive': u"fine emerald",
            'ablative': u'fine emerald'
        }
    },
    "star": {
        'he': {
            'nominative': u'star sapphire',
            'genitive': u"star sapphire",
            'ablative': u'star sapphire'
        },
        'they': {
            'genitive': u"star sapphire",
            'ablative': u'star sapphire'
        }
    },
    "diamond": {
        'he': {
            'nominative': u'diamond',
            'genitive': u"diamond",
            'ablative': u'diamond'
        },
        'they': {
            'genitive': u"diamond",
            'ablative': u'diamond'
        }
    },
    "black_diamond": {
        'he': {
            'nominative': u'black diamond',
            'genitive': u"black diamond",
            'ablative': u'black diamond'
        },
        'they': {
            'genitive': u"black diamond",
            'ablative': u'black diamond'
        }
    },
    "rose_diamond": {
        'he': {
            'nominative': u'rose diamond',
            'genitive': u"rose diamond",
            'ablative': u'rose diamond'
        },
        'they': {
            'genitive': u"rose diamond",
            'ablative': u'rose diamond'
        }
    },
}
"""словарь для типов металлов, ключ - металл, значение - ценность"""
metal_types = {
    "silver": 1,
    "gold": 10,
    "mithril": 25,
    "adamantine": 30,
}
"""key- type of treasure,
value - (base price, gender, can make out of metal(bool), can make out of semi-precious material (bool), can forge an image on(bool), can decorate (bool))"""
treasure_types = {  # допилить типы сокровищ
    "dish": (5, "it", True, False, False, False, True),
    "goblet": (4, "it", True, False, False, True, True),
    "cup": (3, "it", False, True, False, False, True),
    "casket": (5, "it", True, True, False, True, True),
    "statue": (10, "it", True, True, True, False, False),
    "tabernacle": (5, "it", True, True, False, True, True),
    "icon": (10, "it", True, False, True, False, False),
    "tome": (10, "it", True, False, False, True, True),
    "comb": (2, "it", True, True, False, False, True),
    "phallus": (3, "it", True, True, False, False, True),
    "mirror": (4, "it", True, True, False, True, True),
    "band": (3, "it", True, False, False, False, False),
    "diadem": (10, "it", True, False, False, True, False),
    "tiara": (15, "it", True, False, False, True, False),
    "earring": (1, "it", True, False, False, True, False),
    "necklace": (5, "it", True, False, False, True, False),
    "pendant": (3, "it", True, False, False, False, True),
    "ring": (2, "it", True, True, False, False, False),
    "broch": (3, "it", True, False, False, True, False),
    "gemring": (5, "it", True, True, False, True, False),
    "seal": (3, "it", True, True, False, False, True),
    "armbrace": (3, "it", True, True, False, True, True),
    "legbrace": (4, "it", True, True, False, True, True),
    "crown": (15, "it", True, False, False, True, False),
    "scepter": (15, "it", True, False, False, True, False),
    "chain": (3, "it", True, False, False, False, False),
    "brooch": (2, "it", True, False, False, False, True),
}
"""словарь для описания типов драгоценностей,
ключ - тип драгоценностей,
значение - словарь с русским названием драгоценности в разных падежах"""
treasure_description_rus = {  # допилить типы сокровищ
    "dish": {'nominative': u'dish', 'ablative': u'dish'},
    "goblet": {'nominative': u'goblet', 'ablative': u'goblet'},
    "cup": {'nominative': u'cup', 'ablative': u'cup'},
    "casket": {'nominative': u'casket', 'ablative': u'casket'},
    "statue": {'nominative': u'statue', 'ablative': u'statue'},
    "tabernacle": {'nominative': u'tabernacle', 'ablative': u'tabernacle'},
    "icon": {'nominative': u'icon', 'ablative': u'icon'},
    "tome": {'nominative': u'tome', 'ablative': u'tome'},
    "comb": {'nominative': u'comb', 'ablative': u'comb'},
    "phallus": {'nominative': u'phallus', 'ablative': u'phallus'},
    "mirror": {'nominative': u'mirror', 'ablative': u'mirror'},
    "band": {'nominative': u'band', 'ablative': u'band'},
    "diadem": {'nominative': u'diadem', 'ablative': u'diadem'},
    "tiara": {'nominative': u'tiara', 'ablative': u'tiara'},
    "earring": {'nominative': u'earring', 'ablative': u'earring'},
    "necklace": {'nominative': u'necklace', 'ablative': u'necklace'},
    "pendant": {'nominative': u'pendant', 'ablative': u'pendant'},
    "ring": {'nominative': u'ring', 'ablative': u'ring'},
    "broch": {'nominative': u'broch', 'ablative': u'broch'},
    "gemring": {'nominative': u'gemring', 'ablative': u'gemring'},
    "seal": {'nominative': u'seal', 'ablative': u'seal'},
    "armbrace": {'nominative': u'armbrace', 'ablative': u'armbrace'},
    "legbrace": {'nominative': u'legbrace', 'ablative': u'legbrace'},
    "crown": {'nominative': u'crown', 'ablative': u'crown'},
    "scepter": {'nominative': u'scepter', 'ablative': u'scepter'},
    "chain": {'nominative': u'chain', 'ablative': u'chain'},
    "brooch": {'nominative': u'brooch', 'ablative': u'brooch'},
}
"""словарь для описания типов металлов, ключ - тип металла, значение - русское названия драгоценности в разных родах"""
metal_description_rus = {
    'silver': {
        'he': u"silver",
        'she': u"silver",
        'it': u"silver",
        'they': u"silver",
        'prepositional': u"silver",
        'genitive' : u"silver",
    },
    'gold': {
        'he': u"gold",
        'she': u"gold",
        'it': u"gold",
        'they': u"gold",
        'prepositional': u"gold",
        'genitive' : u"gold",
    },
    'mithril': {
        'he': u"mithril",
        'she': u"mithril",
        'it': u"mithril",
        'they': u"mithril",
        'prepositional': u"mithril",
        'genitive' : u"mithril",
    },
    'adamantine': {
        'he': u"adamantine",
        'she': u"adamantine",
        'it': u"adamantine",
        'they': u"adamantine",
        'prepositional': u"adamantine",
        'genitive' : u"adamantine",
    },
}
"""словарь для изображений, ключ - тип культуры, значение - кортеж из вариантов изображений"""
image_types = { 
    'human': (
        'abstract_ornament', 'concentric_circles', 'round_dance', 'fire-breathing_dragon', 'flying_dragon',
        'wingless_dragon', 'snake_with_a_crown', 'winged_serpent', 'cocatrice', 'basilisk',
        'dragon_entwine_naked_girl', 'battle_dragon_with_knight', 'dancing_girls', 'bathing_girl',
        'children_playing', 'rider_with_bow', 'horseman_with_spear_and_shield', 'dead_knight_with_sword'),
    'knight': (
        'proud_motto', 'battle_scene', 'coat_of_arms_with_rearing_unicorn', 'coat_of_arms_with_head_of_boar',
        'coat_of_arms_with_three_lilies', 'coat_of_arms_with_roaring_lion', 'coat_of_arms_with_proud_eagle',
        'coat_of_arms_with_procession_giraffe', 'coat_of_arms_with_crossed_swords',
        'coat_of_arms_with_shield_and_sword'),
    'cleric': (
        'saying_of_holy_scriptures', 'scene_of_holy_scriptures', 'saint_with_halo', 'angel_with_flaming_sword',
        'angel_winning_serpent', 'raising_hands_angel', 'six-winged_seraph', 'holy_maiden_and_child',
        'holy_maiden_stretches_hands', 'weeping_maiden'),
    'elf': (
        'floral_ornament', 'elegant_runes', 'running_deer', 'bear_with_raised_legs', 'wolf_hunting', 'sneaking_manul',
        'two_songbirds', 'moon_and_stars', 'branched_oak', 'blooming_vine', 'spreading_maple', 'weeping_willow',
        'dancing_nymphs', 'nymph_with_cup', 'nymph_collecting_fruits', 'nymph_playing_harp', 'winged_maiden',
        'satyr_playing_flute', 'forest_guard_bow'),
    'dwarf': (
        'geometric_pattern', 'runic_ligature', 'hammer_and_crown', 'dwarfs_holding_over_his_head_anvil',
        'armed_dwarfs_tramples_goblin', 'crossed_axes', 'entwined_rings', 'helmet_with_horns',
        'krotocherv', 'dwarfs', 'urist_makdvarf', 'dragon_smaug'),
    'merman': (
        'wavy_pattern', 'frolicking_fish', 'seahorse', 'newt_lifting_trident', 'triton_and_siren_holding_hands',
        'mermaid_brushing_hair', 'playing_mermaid', 'mermaid_playing_with_pearl', 'awesome_sea_serpent',
        'flying_seagull', 'wriggling_octopus', 'kraken_drowning_sea_vessel', 'sailing_ship'),
}
"""словарь для описания изображений,
ключ - вариант изображения,
значение - словарь из рода изображения и описания изображения в различных падежах"""
image_description_rus = {
    'abstract_ornament': {
        'gender': 'it',
        'nominative': u'abstract decoration',
        'accusative': u'abstract decoration',
    },
    'concentric_circles': {
        'gender': 'it',
        'nominative': u'concentric circles',
        'accusative': u'concentric circles',
    },
    'round_dance': {
        'gender': 'it',
        'nominative': u'ring dance',
        'accusative': u'ring dance',
    },
    'fire-breathing_dragon': {
        'gender': 'it',
        'nominative': u'fire-breathing dragon',
        'accusative': u'fire-breathing dragon',
    },
    'flying_dragon': {
        'gender': 'it',
        'nominative': u'flying dragon',
        'accusative': u'flying dragon',
    },
    'wingless_dragon': {
        'gender': 'it',
        'nominative': u'wingless dragon',
        'accusative': u'wingless dragon',
    },
    'snake_with_a_crown': {
        'gender': 'it',
        'nominative': u'crowned snake',
        'accusative': u'crowned snake',
    },
    'winged_serpent': {
        'gender': 'it',
        'nominative': u'winged serpent',
        'accusative': u'winged serpent',
    },
    'cocatrice': {
        'gender': 'it',
        'nominative': u'cocatrice',
        'accusative': u'cocatrice',
    },
    'basilisk': {
        'gender': 'it',
        'nominative': u'basilisk',
        'accusative': u'basilisk',
    },
    'dragon_entwine_naked_girl': {
        'gender': 'it',
        'nominative': u'dragon, entwined with a naked girl',
        'accusative': u'dragon, entwined with a naked girl',
    },
    'battle_dragon_with_knight': {
        'gender': 'it',
        'nominative': u'dragon battling a knight',
        'accusative': u'dragon battling a knight',
    },
    'dancing_girls': {
        'gender': 'it',
        'nominative': u'dancing girls',
        'accusative': u'dancing girls',
    },
    'bathing_girl': {
        'gender': 'it',
        'nominative': u'bathing girls',
        'accusative': u'bathing girls',
    },
    'children_playing': {
        'gender': 'it',
        'nominative': u'children playing',
        'accusative': u'children playing',
    },
    'rider_with_bow': {
        'gender': 'it',
        'nominative': u'rider with a bow',
        'accusative': u'rider with a bow',
    },
    'horseman_with_spear_and_shield': {
        'gender': 'it',
        'nominative': u'horseman with a shield and spear',
        'accusative': u'horseman with a shield and spear',
    },
    'dead_knight_with_sword': {
        'gender': 'it',
        'nominative': u'dead knight with a sword',
        'accusative': u'dead knight with a sword',
    },
    'proud_motto': {
        'gender': 'it',
        'nominative': u'proud motto',
        'accusative': u'proud motto',
    },
    'battle_scene': {
        'gender': 'it',
        'nominative': u'battle scene',
        'accusative': u'battle scene',
    },
    'coat_of_arms_with_rearing_unicorn': {
        'gender': 'it',
        'nominative': u'coat of arms with a rearing unicorn',
        'accusative': u'coat of arms with a rearing unicorn',
    },
    'coat_of_arms_with_head_of_boar': {
        'gender': 'it',
        'nominative': u'coat of arms with a boar\'s head',
        'accusative': u'coat of arms with a boar\'s head',
    },
    'coat_of_arms_with_three_lilies': {
        'gender': 'it',
        'nominative': u'coat of arms with three lilies',
        'accusative': u'coat of arms with three lilies',
    },
    'coat_of_arms_with_roaring_lion': {
        'gender': 'it',
        'nominative': u'coat of arms with a rearing lion',
        'accusative': u'coat of arms with a rearing lion',
    },
    'coat_of_arms_with_proud_eagle': {
        'gender': 'it',
        'nominative': u'coat of arms with a proud eagle',
        'accusative': u'coat of arms with a proud eagle',
    },
    'coat_of_arms_with_procession_giraffe': {
        'gender': 'it',
        'nominative': u'coat of arms with a processing giraffe',
        'accusative': u'coat of arms with a processing giraffe',
    },
    'coat_of_arms_with_crossed_swords': {
        'gender': 'it',
        'nominative': u'coat of arms with a crossed swords',
        'accusative': u'coat of arms with a crossed swords',
    },
    'coat_of_arms_with_shield_and_sword': {
        'gender': 'it',
        'nominative': u'coat of arms with a sword and shield',
        'accusative': u'coat of arms with a sword and shield',
    },
    'saying_of_holy_scriptures': {
        'gender': 'it',
        'nominative': u'verse from holy scripture',
        'accusative': u'verse from holy scripture',
    },
    'scene_of_holy_scriptures': {
        'gender': 'it',
        'nominative': u'scene from holy scripture',
        'accusative': u'scene from holy scripture',
    },
    'saint_with_halo': {
        'gender': 'it',
        'nominative': u'saint with a halo',
        'accusative': u'saint with a halo',
    },
    'angel_with_flaming_sword': {
        'gender': 'it',
        'nominative': u'angel with a flaming sword',
        'accusative': u'angel with a flaming sword',
    },
    'angel_winning_serpent': {
        'gender': 'it',
        'nominative': u'angel defeating a serpent',
        'accusative': u'angel defeating a serpent',
    },
    'raising_hands_angel': {
        'gender': 'it',
        'nominative': u'angel raising his hands',
        'accusative': u'angel raising his hands',
    },
    'six-winged_seraph': {
        'gender': 'it',
        'nominative': u'six-winged seraph',
        'accusative': u'six-winged seraph',
    },
    'holy_maiden_and_child': {
        'gender': 'it',
        'nominative': u'holy maiden and child',
        'accusative': u'holy maiden and child',
    },
    'holy_maiden_stretches_hands': {
        'gender': 'it',
        'nominative': u'holy maiden with outstretched hands',
        'accusative': u'holy maiden with outstretched hands',
    },
    'weeping_maiden': {
        'gender': 'it',
        'nominative': u'weeping maiden',
        'accusative': u'weeping maiden',
    },
    'floral_ornament': {
        'gender': 'it',
        'nominative': u'floral pattern',
        'accusative': u'floral pattern',
    },
    'elegant_runes': {
        'gender': 'it',
        'nominative': u'elegant runes',
        'accusative': u'elegant runes',
    },
    'running_deer': {
        'gender': 'it',
        'nominative': u'running deer',
        'accusative': u'running deer',
    },
    'bear_with_raised_legs': {
        'gender': 'it',
        'nominative': u'bear with raised legs',
        'accusative': u'bear with raised legs',
    },
    'wolf_hunting': {
        'gender': 'it',
        'nominative': u'wolf hunting',
        'accusative': u'wolf hunting',
    },
    'sneaking_manul': {
        'gender': 'it',
        'nominative': u'crouching cat',
        'accusative': u'crouching cat',
    },
    'two_songbirds': {
        'gender': 'it',
        'nominative': u'two songbirds',
        'accusative': u'two songbirds',
    },
    'moon_and_stars': {
        'gender': 'it',
        'nominative': u'moon and stars',
        'accusative': u'moon and stars',
    },
    'branched_oak': {
        'gender': 'it',
        'nominative': u'branched oak',
        'accusative': u'branched oak',
    },
    'blooming_vine': {
        'gender': 'it',
        'nominative': u'blooming vine',
        'accusative': u'blooming vine',
    },
    'spreading_maple': {
        'gender': 'it',
        'nominative': u'spreading maple',
        'accusative': u'spreading maple',
    },
    'weeping_willow': {
        'gender': 'it',
        'nominative': u'weeping willow',
        'accusative': u'weeping willow',
    },
    'dancing_nymphs': {
        'gender': 'it',
        'nominative': u'dancing nymphs',
        'accusative': u'dancing nymphs',
    },
    'nymph_with_cup': {
        'gender': 'it',
        'nominative': u'nymph with a cup',
        'accusative': u'nymph with a cup',
    },
    'nymph_collecting_fruits': {
        'gender': 'it',
        'nominative': u'nymph collecting fruits',
        'accusative': u'nymph collecting fruits',
    },
    'nymph_playing_harp': {
        'gender': 'it',
        'nominative': u'nymph playing a harp',
        'accusative': u'nymph playing a harp',
    },
    'winged_maiden': {
        'gender': 'it',
        'nominative': u'winged maiden',
        'accusative': u'winged maiden',
    },
    'satyr_playing_flute': {
        'gender': 'it',
        'nominative': u'satyr playing a flute',
        'accusative': u'satyr playing a flute',
    },
    'forest_guard_bow': {
        'gender': 'it',
        'nominative': u'forest guard with a bow',
        'accusative': u'forest guard with a bow',
    },
    'geometric_pattern': {
        'gender': 'it',
        'nominative': u'geometric pattern',
        'accusative': u'geometric pattern',
    },
    'runic_ligature': {
        'gender': 'it',
        'nominative': u'runic patterns',
        'accusative': u'runic patterns',
    },
    'hammer_and_crown': {
        'gender': 'it',
        'nominative': u'hammer and crown',
        'accusative': u'hammer and crown',
    },
    'dwarfs_holding_over_his_head_anvil': {
        'gender': 'it',
        'nominative': u'dwarf holding an anvil over his head',
        'accusative': u'dwarf holding an anvil over his head',
    },
    'armed_dwarfs_tramples_goblin': {
        'gender': 'it',
        'nominative': u'armed dwaves trampling a goblin',
        'accusative': u'armed dwaves trampling a goblin',
    },
    'crossed_axes': {
        'gender': 'it',
        'nominative': u'crossed axes',
        'accusative': u'crossed axes',
    },
    'entwined_rings': {
        'gender': 'it',
        'nominative': u'entwined rings',
        'accusative': u'entwined rings',
    },
    'helmet_with_horns': {
        'gender': 'it',
        'nominative': u'horned helmet',
        'accusative': u'horned helmet',
    },
    'krotocherv': {
        'gender': 'it',
        'nominative': u'moleworm',
        'accusative': u'moleworm',
    },
    'dwarfs': {
        'gender': 'it',
        'nominative': u'dwarves. The dwarves are working.',
        'accusative': u'dwarves. The dwarves are working.',
    },
    'urist_makdvarf': {
        'gender': 'it',
        'nominative': u'Urist McDwarf. Urist McDwarf is eating a masterwork yak cheese. '
                      u'The artwork relates to the eating of yak cheese by the dwarf Urist McDwarf '
                      u'in the early spring of 1076.',
        'accusative': u'Urist McDwarf. Urist McDwarf is eating a masterwork yak cheese. '
                      u'The artwork relates to the eating of yak cheese by the dwarf Urist McDwarf '
                      u'in the early spring of 1076.',
    },
    'dragon_smaug': {
        'gender': 'it',
        'nominative': u'the dragon Smaug and the dwarf Thorin. Thorin clasps his hands. Smaug is in a threatening posture.'
                      u'This artwork relates to the murder of the King Under the Mountain in Erebor in the late summer of 2770.',
        'accusative': u'the dragon Smaug and the dwarf Thorin. Thorin clasps his hands. Smaug is in a threatening posture.'
                      u'This artwork relates to the murder of the King Under the Mountain in Erebor in the late summer of 2770.',
    },
    'wavy_pattern': {
        'gender': 'it',
        'nominative': u'wavy pattern',
        'accusative': u'wavy pattern',
    },
    'frolicking_fish': {
        'gender': 'it',
        'nominative': u'frolicking fish',
        'accusative': u'frolicking fish',
    },
    'seahorse': {
        'gender': 'it',
        'nominative': u'seahorse',
        'accusative': u'seahorse',
    },
    'newt_lifting_trident': {
        'gender': 'it',
        'nominative': u'newt lifting a trident',
        'accusative': u'newt lifting a trident',
    },
    'triton_and_siren_holding_hands': {
        'gender': 'it',
        'nominative': u'triton and siren holding hands',
        'accusative': u'triton and siren holding hands',
    },
    'mermaid_brushing_hair': {
        'gender': 'it',
        'nominative': u'mermaid brushing her hair',
        'accusative': u'mermaid brushing her hair',
    },
    'playing_mermaid': {
        'gender': 'it',
        'nominative': u'playing mermaid',
        'accusative': u'playing mermaid',
    },
    'mermaid_playing_with_pearl': {
        'gender': 'it',
        'nominative': u'mermaid playing with a pearl',
        'accusative': u'mermaid playing with a pearl',
    },
    'awesome_sea_serpent': {
        'gender': 'it',
        'nominative': u'mighty sea serpent',
        'accusative': u'mighty sea serpent',
    },
    'flying_seagull': {
        'gender': 'it',
        'nominative': u'flying seagull',
        'accusative': u'flying seagull',
    },
    'wriggling_octopus': {
        'gender': 'it',
        'nominative': u'wriggling octopus',
        'accusative': u'wriggling octopus',
    },
    'kraken_drowning_sea_vessel': {
        'gender': 'it',
        'nominative': u'kraken drowning a sea vessel',
        'accusative': u'kraken drowning a sea vessel',
    },
    'sailing_ship': {
        'gender': 'it',
        'nominative': u'sailing ship and waves',
        'accusative': u'sailing ship and waves',
    },
}
"""словарь для описания качества драгоценности,
 ключ - качество,
 значение - словарь с русским названием качества в разных родах"""
quality_description_rus = { 
    'rough': {
        'he': u"rough ",
        'she': u"rough ",
        'it': u"rough ",
    },
    'common': {  # у обычного описание опускается
        'he': u"",
        'she': u"",
        'it': u"",
    },
    'skillfully': {
        'he': u"skillfully made ",
        'she': u"skillfully made ",
        'it': u"skillfully made ",
    },
    'mastery': {
        'he': u"masterfully made ",
        'she': u"masterfully made ",
        'it': u"masterfully made ",
    },
}
"""словарь для описания украшения, ключ - тип украшения, значение - словарь с русским словом в разных родах"""
decoration_description_rus = {
    'decoration': {
        'he': u"decorated",
        'she': u"decorated",
        'it': u"decorated",
    },
    'spangled': {
        'he': u"spangled",
        'she': u"spangled",
        'it': u"spangled",
    },
    'inlaid': {
        'he': u"inlaid",
        'she': u"inlaid",
        'it': u"inlaid",
    },
    'image': {
        'he': u"depicting",
        'she': u"depicting",
        'it': u"depicting",
        'they': u"depicting",
    },
}
"""словарь для описания типа украшения на русском"""
decorate_types_description_rus = {
    'incuse': u"incuse",
    'engrave': u"engraving",
    'etching': u"etching",
    'carving': u"carving"
}
"""словарь для вывода описаний массы сокровищ на русском"""
treasures_mass_description_rus = {
    'coin': {
        0: u"coins",
        100: u"handful of coins",
        1000: u"pile of coins",
        10000: u"mountain of coins",
        100000: u"mountains of coins",
    },
    'material': {
        0: u"materials",
        100: u"handful of materials",
        1000: u"pile of materials",
        10000: u"mountain of materials",
        100000: u"mountains of materials",
    },
    'gem': {
        0: u"gemstones",
        100: u"handful of gems",
        1000: u"pile of gems",
        10000: u"mountain of gems",
        100000: u"mountains of gems",
    },
    'jewelry': {
        0: u"trinkets",
        100: u"handful of trinkets",
        1000: u"pile of trinkets",
        10000: u"mountain of trinkets",
        100000: u"mountains of trinkets",
    },
    'wealth': {
        0: u"The treasury is virtually empty. ",
        100: u"In the treasury is a pittance that any respectable dragon would be ashamed of. ",
        1000: u"In the treasure there is not much to look at. ",
        10000: u"In the treasury is quite a decent pile of treasure, no longer something to be ashamed of. ",
        100000: u"There is reason to be proud of the treasury. Only the best dragons manage to collect such a mountain of wealth.",
        1000000: u"Mountains of treasure - the pride of the richest dragon in the world. ",
    },
}

number_conjugation_end = {
    1: {'nominative': (u"", u"", u"")},
    2: {'nominative': (u"", u"", u"")},
}


def number_conjugation_type(number):
    if (number % 10 == 1) and (number % 100 != 11):
        return 0
    elif (1 < number % 10 < 5) and (number % 100 < 11 or number % 100 > 21):
        return 1
    else:
        return 2


def number_conjugation_rus(number, add_name, word_form='nominative', word_type=1):
    description_end = number_conjugation_end[word_type][word_form][number_conjugation_type(number)]
    return u"%s %s%s" % (number, add_name, description_end)


def capitalize_first(string):
    return string.capitalize()


def weighted_select(d):
    weight = random.random() * sum(v[0] for k, v in d.items())
    for k, v in d.items():
        if weight < v[0]:
            return k
        weight -= v[0]
    return d.keys()[random.randint(0, len(d.keys()))]


class Ingot(object):  # класс для генерации слитков
    weights = (1, 4, 8, 16)
    weights_description_rus = {1: u"tiny", 4: u"small", 8: u"heavy", 16: u"massive"}

    def __init__(self, metal_type):
        self.metal_type = metal_type
        self.metal_cost = metal_types[metal_type]
        self.weight = random.choice(self.weights)

    @property
    def cost(self):
        return self.metal_cost * self.weight

    def __repr__(self):
        return "%s pound %s ingot" % (self.weight, self.metal_type)

    def description(self, language='rus'):
        if language == 'rus':
            if self.weight in self.weights:
                return u"%s %s ingot" % (
                    self.weights_description_rus[self.weight], metal_description_rus[self.metal_type]['he'])
            else:
                return u"Gross weight of the %s ingots %s" % (
                    metal_description_rus[self.metal_type]['they'], number_conjugation_rus(self.weight, u"pounds"))
        else:
            return self.__repr__()

    @staticmethod
    def number_conjugation(metal_type, metal_weight):
        """
        Функция для вывода описания слитков металла по типу металла и его количеству
        """
        if metal_weight in Ingot.weights:
            return u"%s %s ingot" % (
                Ingot.weights_description_rus[metal_weight], metal_description_rus[metal_type]['he'])
        else:
            return u"Gross weight of the %s bars %s" % (
                metal_description_rus[metal_type]['they'], number_conjugation_rus(metal_weight, u"фунт"))


class Coin(object):
    coin_types = {"farthing": (1, 1), "taller": (1, 10), "dubloon": (1, 100)}
    coin_description_rus = {"farthing": u"farthing", "taller": u"taller", "dubloon": u"dubloon"}
    """
    Монеты.
    """

    def __init__(self, name, amount):
        self.amount = amount  # количество монеток
        self.name = name
        self.value = Coin.coin_types[self.name][1]

    @property
    def cost(self):
        return self.amount * self.value

    def __repr__(self):
        return str(self.amount) + " " + "%s(s)" % self.name

    def description(self, language='rus'):
        if language == 'rus':
            return number_conjugation_rus(self.amount, Coin.coin_description_rus[self.name], 'nominative')
        else:
            return self.__repr__()

    @staticmethod
    def number_conjugation(coin_type, coin_count):
        """
        Функция для вывода описания монет по типу и количеству монет
        """
        return number_conjugation_rus(coin_count, Coin.coin_description_rus[coin_type])


class Gem(object):  # класс для генерации драг.камней
    cut_dict = {
        " ": (0, 1),
        "polished": (50, 2),
        "rough": (30, 1),
        "faceted": (20, 3)
    }
    size_dict = {
        "small": (40, 1),
        "common": (50, 5),
        "large": (8, 25),
        "exceptional": (2, 100)
    }

    def __init__(self, g_type, size, cut):
        self.g_type = g_type  # Тип камня
        self.size = size  # размер
        self.size_mod = Gem.size_dict[size][1]  # модификатор размера
        """степень обработки"""
        if self.g_type == "pearl" or self.g_type == "black_pearl":
            self.cut = " "
        else:
            self.cut = cut
        self.cut_mod = Gem.cut_dict[cut][1]  # модификатор обработки
        self.base = gem_types[self.g_type][1]  # базовая ценность, зависит от типа
        # проверяем возможность инкрустации:
        if self.size == 100:
            self.can_be_incrusted = False
        else:
            self.can_be_incrusted = True
        if self.size_mod >= 25:
            self.amount = 1
        else:
            if self.size_mod == 5:
                self.amount = 5
            else:
                self.amount = 20

    @property
    def cost(self):  # цена камня, складывается из базы(зависит от типа), размера и степени обработки
        return self.base * self.size_mod * self.cut_mod * self.amount

    def __repr__(self):
        return "%s %s %s" % (self.size, self.cut, self.g_type)

    def __eq__(self, other):
        if isinstance(other, Gem):
            return other and self.g_type == other.g_type and self.cut == other.cut \
                and self.size == other.size
        else:
            return

    def description(self, custom=False, case='nominative', gender='it', language='rus'):
        """
        Создает описание для драгоценного камня
        :custom: - если False - добавляет в описание "горсть"/"несколько" для мелких/обычных камней и
            меняет соответствующим образом род и падеж камней
        :case: - в каком падеже описываются камни
        :gender: - какого рода камни - 'he' (мужского), 'she' (женского) или 'they' (множественное число)
        """
        if language == 'rus':
            if not custom and (self.size == 'small' or self.size == 'common'):
                case = 'genitive'
                gender = 'they'
                if self.size == 'small':
                    return u"a handful of small %s%s" % (
                        gem_cut_description_rus[self.cut][gender][case], gem_description_rus[self.g_type][gender][case])
                else:
                    return u"several %s%s" % (
                        gem_cut_description_rus[self.cut][gender][case], gem_description_rus[self.g_type][gender][case])
            else:
                gender = 'it'
                return u"%s%s%s" % (
                    material_size_description_rus[self.size][gender][case],
                    gem_cut_description_rus[self.cut][gender][case],
                    gem_description_rus[self.g_type][gender][case])
        else:
            return self.__repr__()

    @staticmethod
    def number_conjugation(gem_type, gem_count):
        """
        Функция для вывода описания камней по типу (в формате тип/размер/огранка)
        и количеству (без учета умножения мелких/обычных камней)
        """
        gem_param = gem_type.split(';')
        if gem_param[1] == 'small' or gem_param[1] == 'common':  # умножаем мелкие/обычные камни
            if gem_param[1] == 'small':
                gem_count *= 25
            else:
                gem_count *= 5
        conjugation_type = number_conjugation_type(gem_count)  # определяем тип сопряжения
        # определяем род, некрасивый вариант - лучше использовать словарь:
        gender = 'it'
        # выводим результат для каждого типа сопряжения
        # единственное число - именительный падеж, род копируется
        if conjugation_type == 0:
            if gem_count != 1:  # если камень один - не ставим число
                return u"%s %s%s%s" % (gem_count, material_size_description_rus[gem_param[1]][gender]['nominative'],
                                       gem_cut_description_rus[gem_param[2]][gender]['nominative'],
                                       gem_description_rus[gem_param[0]][gender]['nominative'])
            else:
                return u"%s%s%s" % (material_size_description_rus[gem_param[1]][gender]['nominative'],
                                    gem_cut_description_rus[gem_param[2]][gender]['nominative'],
                                    gem_description_rus[gem_param[0]][gender]['nominative'])
        # маломножественная форма - родительный падеж, тип в единственном числе, прилагательные - во множественном
        elif conjugation_type == 1:
            return u"%s %s%s%s" % (gem_count, material_size_description_rus[gem_param[1]]['they']['genitive'],
                                   gem_cut_description_rus[gem_param[2]]['they']['genitive'],
                                   gem_description_rus[gem_param[0]][gender]['genitive'])
        # множественное число - родительный падеж множественного числа
        elif conjugation_type == 2:
            gender = 'they'
            return u"%s %s%s%s" % (gem_count, material_size_description_rus[gem_param[1]][gender]['genitive'],
                                   gem_cut_description_rus[gem_param[2]][gender]['genitive'],
                                   gem_description_rus[gem_param[0]][gender]['genitive'])


def generate_gem(count, *args):
    """функция для генерации камней, 1 обязательный аргумент - количество камней
    которое нужно сгенерировать, чтобы задать размер и/или качество обработки
    вызываем с аргументом {"size":("размер", "размер", ...} или {"cut":("качество, "качество", ...)}
    число будет использоваться для определения ценности
    камня, чтобы задать типы камней, вызываем с аргументом "тип камня" или
    ["тип камня", "тип камня", ...]
    на пример generate_gem(5, {"size":("common", "small")}, ["ruby", "star", "aqua"],
                       "diamond")
    создаст 5 разных камней размера common или small случайного качества огранки, 
    тип каждого будет выбран из заданных, шансы появления которых относительно
    друг друга указанны в словаре gem_types"""
    gems = []
    if len(args) != 0:
        cut = {}
        size = {}
        new_dict = {}
        for i in args:
            if isinstance(i, dict):
                if i.keys()[0] == "size":
                    for v in i["size"]:
                        if v in Gem.size_dict:
                            size[v] = Gem.size_dict[v]
                elif i.keys()[0] == "cut":
                    for v in i["cut"]:
                        if v in Gem.cut_dict:
                            cut[v] = Gem.cut_dict[v]
            elif isinstance(i, list):
                for item in i:
                    if item in gem_types:
                        new_dict[item] = gem_types[item]
            elif isinstance(i, basestring):
                if i in gem_types:
                    new_dict[i] = gem_types[i]
        while count > 0:
            if len(cut) == 0:
                cut = Gem.cut_dict
            if len(size) == 0:
                size = Gem.size_dict
            if len(new_dict) == 0:
                new_dict = gem_types
            gems.append(Gem(weighted_select(new_dict), weighted_select(size), weighted_select(cut)))
            count -= 1
        return gems
    for i in xrange(count):
        gems.append(Gem(weighted_select(gem_types), weighted_select(Gem.size_dict), weighted_select(Gem.cut_dict)))
    return gems


class Material(object):  # класс для генерации материалов
    size_dict = {"small": (40, 1), "common": (50, 5), "large": (8, 25), "exceptional": (2, 100)}

    def __init__(self, m_type, size):
        self.m_type = m_type  # название
        self.base = material_types[m_type][1]  # базовая цена
        self.size = size  # размер
        self.size_mod = Material.size_dict[size][1]  # модификатор размера

    @property
    def cost(self):  # определяем цену материала(зависит от размера и типа)
        return self.size_mod * self.base

    def __repr__(self):
        return "%s %s" % (self.size, self.m_type)

    def __eq__(self, other):
        if isinstance(other, Material):
            return other and self.m_type == other.m_type and self.size == other.size
        else:
            return

    def description(self, language='rus'):
        if language == 'rus':
            return u"%piece %s" % (material_size_description_rus[self.size]['it']['nominative'],
                                    material_description_rus[self.m_type]['genitive'])
        else:
            return self.__repr__()

    @staticmethod
    def number_conjugation(material_type, material_count):
        """
        Функция для вывода описания камней по типу (в формате тип/размер) и количеству
        """
        material_param = material_type.split(';')
        conjugation_type = number_conjugation_type(material_count)  # определяем тип сопряжения
        # выводим результат для каждого типа сопряжения
        if conjugation_type == 0:  # единственное число - именительный падеж, род копируется
            if material_count != 1:  # если материал один - не ставим число
                return u"%s %piece %s" % (
                    material_count, material_size_description_rus[material_param[1]]['he']['nominative'],
                    material_description_rus[material_param[0]]['genitive'])
            else:
                return u"%piece %s" % (material_size_description_rus[material_param[1]]['he']['nominative'],
                                        material_description_rus[material_param[0]]['genitive'])
        elif conjugation_type == 1:
            return u"%s %piece %s" % (
                material_count, material_size_description_rus[material_param[1]]['they']['genitive'],
                material_description_rus[material_param[0]]['genitive'])
        elif conjugation_type == 2:
            return u"%s %piece %s" % (
                material_count, material_size_description_rus[material_param[1]]['they']['genitive'],
                material_description_rus[material_param[0]]['genitive'])


def generate_mat(count, *args):
    """принцип работы такойже как для драг.камней"""
    mats = []
    if len(args) != 0:
        size = {}
        new_dict = {}
        for i in args:
            if isinstance(i, dict):
                if i.keys()[0] == "size":
                    # size = {v: Material.size_dict[v] for v in i["size"] if v in Material.size_dict}
                    for v in i["size"]:
                        if v in Material.size_dict:
                            size[v] = Material.size_dict[v]
            elif isinstance(i, list):
                for item in i:
                    if item in material_types:
                        new_dict[item] = material_types[item]
            elif isinstance(i, basestring):
                if i in material_types:
                    new_dict[i] = material_types[i]
        for i in xrange(count):
            if len(size) == 0:
                size = Material.size_dict
            if len(new_dict) == 0:
                new_dict = material_types
            mats.append(Material(weighted_select(new_dict), weighted_select(size)))
        return mats
    for i in xrange(count):
        mats.append(Material(weighted_select(material_types), weighted_select(Material.size_dict)))
    return mats


class Treasure(object):  # класс для сокровищ
    decorate_types = {"incuse": (33,), "engrave": (33,), "etching": (33,), "carving": (0,)}
    quality_types = {"common": (60, 2), "skillfully": (20, 3), "rough": (10, 1), "mastery": (10, 5)}

    def __init__(self, treasure_type, alignment):
        """все значения заносятся из словаря treasure_types"""
        self.treasure_type = treasure_type
        self.base_price = treasure_types[self.treasure_type][0]
        self.gender = treasure_types[self.treasure_type][1]
        self.metal = treasure_types[self.treasure_type][2]
        self.nonmetal = treasure_types[self.treasure_type][3]
        self.image = treasure_types[self.treasure_type][4]
        self.incrustable = treasure_types[self.treasure_type][5]
        self.decorable = treasure_types[self.treasure_type][6]
        self.alignment = alignment
        """дальше генерируем характеристики в зависимости от типа сокровища"""
        self.random_mod = random.randint(0, self.base_price * 10)
        if random.randint(1, 100) <= 50 and self.incrustable:
            self.spangled = generate_gem(1, {"size": ('common',)})[0]
            # размер 'common' - хак, чтобы не писалось "мелкими":
        else:
            self.spangled = None
        if random.randint(1, 100) <= 15 and self.incrustable:
            self.inlaid = generate_gem(1, {"size": ('common',)})[0]
        else:
            self.inlaid = None
        if random.randint(1, 100) <= 5 and self.incrustable:
            self.huge = generate_gem(1, {"size": ('large',)})[0]
        else:
            self.huge = None

        def metals_available():  # проверяем принадлежность к расе(из каких металов может быть сделано)
            if self.alignment == "human" or self.alignment == "cleric" or self.alignment == "knight":
                return {"silver": (70,), "gold": (30,)}
            elif self.alignment == "elf" or self.alignment == "merman":
                return {"gold": (70,), "mithril": (30,)}
            elif self.alignment == "dwarf":
                return {"gold": (70,), "adamantine": (30,)}

        def material():
            if self.metal and self.nonmetal:
                rnd = random.randint(1, 100)
                if rnd > 50:
                    return weighted_select(material_types)
                else:
                    return weighted_select(metals_available())
            elif self.metal:
                return weighted_select(metals_available())
            else:
                return weighted_select(material_types)

        self.material = material()  # выбираем материал

        def decorate():
            if self.decorable:
                rnd = random.randint(1, 100)
                if rnd <= 15:
                    rnd = random.randint(1, 100)
                    if rnd <= 50:
                        self.decoration_image = random.choice(image_types[self.alignment])
                        if self.material in material_types:
                            return "carving"
                        else:
                            return weighted_select(Treasure.decorate_types)
                    else:
                        return None
                else:
                    return None

        self.decoration = decorate()  # выбираем орнамент
        if self.image:
            self.decoration_image = random.choice(image_types[self.alignment])

        def q_choice():  # прокидываем качество вещи
            if self.alignment == "human" or self.alignment == "cleric" or self.alignment == "knight":
                return weighted_select(Treasure.quality_types)
            else:
                holder = deepcopy(Treasure.quality_types)
                holder.__delitem__('rough')
                return weighted_select(holder)

        self.quality = q_choice()
        self.obtained = u""

    def incrustation(self, gem):  # метод для икрустации камней
        if not self.incrustable:
            return "Can't be incrusted"
        if gem.size == "small":
            if self.spangled is None:
                self.spangled = gem
            return
        if gem.size[1] == "common":
            if self.inlaid is None:
                self.inlaid = gem
            return
        if gem.size[1] == "huge":
            if self.huge is None:
                self.huge = gem
            return

    @property  # качество вещи
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
        if value in Treasure.quality_types:
            self.quality_mod = Treasure.quality_types[value][1]

    @property  # тип материала
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value
        if self.material in material_types:
            self.mat_price = material_types[self._material][1]
        else:
            self.mat_price = metal_types[self._material]

    @property  # тип орнамента
    def decoration(self):
        return self._decoration

    @decoration.setter
    def decoration(self, value):
        self._decoration = value
        if value is None:
            self.dec_mod = 1
        else:
            self.dec_mod = 2  # равен двум если есть орнамент

    @property  # цена вставленных камней
    def incrustation_cost(self):
        holder = 0
        if self.spangled is not None:
            # из-за хака с размерами нужно умножить на реальный размер и поделить на "хакнутый"
            holder += self.spangled.cost * Gem.size_dict['small'][1] // Gem.size_dict['common'][1]
        if self.inlaid is not None:
            holder += self.inlaid.cost
        if self.huge is not None:
            holder += self.huge.cost
        return holder

    def craft_cost(self, base_cost, price_multiplier):  
        """
        Цена создания/покупки
        :param base_cost: базовая стоимость работы (для ремесла)
        :param price_multiplier: увеличение цены (для покупки, в процентах)
        :return: созданная вещь либо None в случае отмены
        """
        price = self.cost * price_multiplier // 100
        price += base_cost
        if self.spangled:
            price += base_cost
        if self.inlaid:
            price += base_cost
        if self.huge:
            price += base_cost
        if self.decoration:
            price += 2 * base_cost
        return price

    @property
    def cost(self):  # цена сокровища
        return \
            self.base_price * self.quality_mod * self.dec_mod * self.mat_price + \
            self.incrustation_cost + self.random_mod

    def __repr__(self):
        return "%s%s" % (self.material, self.treasure_type)

    def description(self, language='rus'):
        if language == 'rus':
            quality_str = quality_description_rus[self.quality][self.gender]  # мастерство исполнения
            treasure_str = treasure_description_rus[self.treasure_type]['nominative']  # тип драгоценности
            # совмещаем мастерство исполнения, тип и материал, из которого изготовлено
            if self.material in metal_types.keys():
                if self.treasure_type == 'icon' or self.treasure_type == 'tome':
                    desc_str = u"%s%s %s of" % (
                        quality_str, treasure_str, metal_description_rus[self.material]['prepositional'])
                else:
                    desc_str = u"%s%s %s" % (
                        quality_str, metal_description_rus[self.material][self.gender], treasure_str)
            else:
                desc_str = u"%s%s из %s" % (
                    quality_str, treasure_str, material_description_rus[self.material]['genitive'])

            if self.image:
                desc_str += u", showing %s" % image_description_rus[self.decoration_image]['accusative']  
                # только изображение
            else:
                # добавляем различные украшения
                enchant_list = []
                if self.spangled:  # усыпанное камнями
                    enchant_list.append(u"%s %s" % (decoration_description_rus['spangled'][self.gender],
                                                    self.spangled.description(True, 'ablative', 'they')))
                if self.inlaid:  # инкрустированное камнями
                    enchant_list.append(u"%s %s" % (decoration_description_rus['inlaid'][self.gender],
                                                    self.inlaid.description(True, 'ablative', 'they')))
                if self.huge:  # с крупным камнем
                    # только ради "крупной (чёрной) жемчужины":
                    enchant_list.append(u"с %s" % self.huge.description(True, 'ablative'))
                if self.decoration:  # украшенное чеканкой/гравировкой/травлением/резьбой
                    enchant_list.append(u"%s %s" % (decoration_description_rus['decoration'][self.gender],
                                                    decorate_types_description_rus[self.decoration]))
                if len(enchant_list) == 1:
                    if not self.huge:
                        desc_str += u","  # добавляем "с крупным камнем" без запятой
                    desc_str += u" %s" % enchant_list[0]
                elif len(enchant_list) > 1:
                    while len(enchant_list) > 1:
                        desc_str += u", %s" % enchant_list[0]  # добавляем через запятую украшения
                        del enchant_list[0]
                    desc_str += u" и %s" % enchant_list[0]  # последнее добавляется союзом "и"
                if self.decoration:  # если есть изображение - ставим точку и описываем его
                    image_description = image_description_rus[self.decoration_image]  # упрощение доступа к свойству
                    desc_str = u"%s. На %s %s %s" % (desc_str, treasure_description_rus[self.treasure_type]['ablative'],
                                                     decoration_description_rus['image'][image_description['gender']],
                                                     image_description['nominative'])
            return desc_str
        else:
            return self.__repr__()


def gen_treas(count, t_list, alignment, min_cost, max_cost, obtained):
    """Генерируем рандомное сокровище
    функция генерации сокровищ,
    count - количество сокровищ,
    t_list - список строк-имен сокровищ,
    alignmet - принадлежность к определенной культуре(одно из: human, cleric, knight, merman, elf, dwarf),
    min_cost - минимальная цена сокровища,
    max_cost - максимальная цена сокровища"""
    treasures_list = []
    while count > 0:
        treas_holder = random.choice(t_list)
        if treas_holder in gem_types:
            treasures_list.extend(generate_gem(1, treas_holder))
        elif treas_holder in material_types:
            treasures_list.extend(generate_mat(1, treas_holder))
        elif treas_holder in metal_types:
            treasures_list.append(Ingot(treas_holder))
        elif treas_holder in Coin.coin_types:
            rnd = random.randint(min_cost, max_cost)
            treasures_list.append(Coin(treas_holder, rnd / Coin.coin_types[treas_holder][1]))
        elif treas_holder in treasure_types:
            t = Treasure(treas_holder, alignment)
            t.obtained = obtained
            treasures_list.append(t)
        else:
            raise Exception("No treasure")
        if not min_cost < treasures_list[-1].cost < max_cost:
            treasures_list.pop()
            count += 1
        count -= 1
    return treasures_list


class Treasury(store.object):
    def __init__(self):
        self.farthing = 0  # медная монетка
        self.taller = 0  # серебряная монетка
        self.dubloon = 0  # золотая монетка
        # списки строк
        self.materials = {}  # словарь с количеством материала
        self.metals = {}  # словарь с количеством металла
        self.jewelry = []  # список драгоценностей
        self.equipment = []
        self.gems = {}  # словарь с количеством драгоценных камней
        # TODO: multiple same equipment
        self.thief_items = []

    @property
    def money(self):
        return self.farthing + 10 * self.taller + 100 * self.dubloon

    @money.setter
    def money(self, value):
        if value < 0:  # Защита от ухода денег в минус
            raise NotImplementedError(u"Денег недостаточно для выполнения операции")
        money_diff = value - self.money  # считаем разницу между прошлым значением и новым
        if money_diff < 0:
            # разница отрицательна или ноль - производим вычитание
            money_diff = -money_diff  # для удобства получаем число, которое необходимо вычесть
            if self.farthing < money_diff % 10:
                # медных монет недостаточно для выплаты, меняем серебряную
                self.taller -= 1
                self.farthing += 10
            self.farthing -= money_diff % 10
            money_diff //= 10
            if self.taller < money_diff % 10:
                if (self.farthing // 10 + self.taller) < money_diff % 10:
                    # серебряных монет даже с учетом медных недостаточно для выплаты, меняем золотую
                    self.dubloon -= 1
                    self.taller += 10
                else:
                    # серебряных монет с учетом медных достаточно для выплаты, меняем по максимуму медные на серебряные
                    self.taller += self.farthing // 10
                    self.farthing %= 10
            self.taller -= money_diff % 10
            money_diff //= 10
            if self.dubloon < money_diff % 10:
                # золотых монет недостаточно для выплаты
                self.taller += self.farthing // 10  # меняем по максимуму медные на серебряные
                self.farthing %= 10
                self.dubloon += self.taller // 10  # меняем по максимуму серебряные на золотые
                self.taller %= 10
            self.dubloon -= money_diff
        else:
            # разница положительна - производим добавление монет по разрядам
            self.dubloon += money_diff // 100
            money_diff %= 100
            self.taller += money_diff // 10
            self.farthing += money_diff % 10

    @property
    def wealth(self):
        """
        Стоимость всех сокровищ дракона
        """
        calc_wealth = self.money  # деньги
        for metal in self.metals.iterkeys():  # металлы
            calc_wealth += self.metals[metal] * metal_types[metal]
        for material_i in self.materials.iterkeys():  # материалы
            material = material_i.split(';')
            calc_wealth += self.materials[material_i] * material_types[material[0]][1] * \
                           Material.size_dict[material[1]][1]
        for gem_i in self.gems.iterkeys():  # драгоценные камни
            gem = gem_i.split(';')
            calc_wealth += self.gems[gem_i] * gem_types[gem[0]][1] * Gem.size_dict[gem[1]][1] * Gem.cut_dict[gem[2]][1]
        for treas_i in xrange(len(self.jewelry)):  # украшения
            calc_wealth += self.jewelry[treas_i].cost
        return calc_wealth

    def receive_treasures(self, treasure_list):
        """
        Помещает сокровища в сокровищницу
        :param treasure_list: Список сокровищ, помещаемых в сокровищницу
        """
        for treas in treasure_list:
            achieve_target(treas.cost, "treasure")#Событие для ачивок
            if isinstance(treas, Coin):
                # сохраняется число медных, серебряных и золотых монет в соответствующих переменных
                if treas.name == 'farthing':
                    self.farthing += treas.amount
                elif treas.name == 'taller':
                    self.taller += treas.amount
                else:
                    self.dubloon += treas.amount
            elif isinstance(treas, Ingot):
                # сохраняется в словаре metals, где ключ - название металла, а значение - его вес в фунтах
                if treas.metal_type in self.metals:
                    self.metals[treas.metal_type] += treas.weight
                else:
                    self.metals[treas.metal_type] = treas.weight
            elif isinstance(treas, Material):
                # сохраняется в словаре materials, где
                # ключ - "название материала;размер материала", а
                # значение - число материалов такого типа и размера
                type_str = treas.m_type + ';' + treas.size
                if type_str in self.materials:
                    self.materials[type_str] += 1
                else:
                    self.materials[type_str] = 1
            elif isinstance(treas, Gem):
                # сохраняется в словаре gems, где
                # ключ - "название драгоценности;размер драгоценности;обработка драгоценности", а
                # значение - число камней такого типа, размера и обработки
                type_str = treas.g_type + ';' + treas.size + ';' + treas.cut
                if type_str in self.gems:
                    self.gems[type_str] += 1
                else:
                    self.gems[type_str] = 1
            elif isinstance(treas, Treasure):
                self.jewelry.append(treas)
        achieve_target(self.wealth, "wealth")#Событие для ачивок

    @staticmethod
    def treasures_description(treasure_list):
        """
        :param treasure_list: Список сокровищ, для которых требуется получить описание
        :return: Возвращает список с описанием сокровищ
        """
        treas_list = deepcopy(treasure_list)
        description_list = []
        # Группируем монеты, слитки, драгоценные камни и материалы
        coin_list = {}
        ingot_list = {}
        gem_list = {}
        material_list = {}
        for treas_i in reversed(xrange(len(treasure_list))):
            treas = treas_list[treas_i]
            if isinstance(treas, Coin):
                if treas.name in coin_list:
                    coin_list[treas.name] += treas.amount
                else:
                    coin_list[treas.name] = treas.amount
                del treas_list[treas_i]
            elif isinstance(treas, Ingot):
                if treas.metal_type in ingot_list:
                    ingot_list[treas.metal_type] += treas.weight
                else:
                    ingot_list[treas.metal_type] = treas.weight
                del treas_list[treas_i]
            elif isinstance(treas, Gem):
                type_str = treas.g_type + ';' + treas.size + ';' + treas.cut
                if type_str in gem_list:
                    gem_list[type_str] += 1
                else:
                    gem_list[type_str] = 1
                del treas_list[treas_i]
            elif isinstance(treas, Material):
                type_str = treas.m_type + ';' + treas.size
                if type_str in material_list:
                    material_list[type_str] += 1
                else:
                    material_list[type_str] = 1
                del treas_list[treas_i]
        for treas in coin_list.iterkeys():
            description_list.append(Coin.number_conjugation(treas, coin_list[treas]) + '.')
        for treas in ingot_list.iterkeys():
            description_list.append(capitalize_first(Ingot.number_conjugation(treas, ingot_list[treas])) + '.')
        for treas in gem_list.iterkeys():
            if gem_list[treas] > 1:
                description_list.append(capitalize_first(Gem.number_conjugation(treas, gem_list[treas])) + '.')
            else:
                description_list.append(capitalize_first(Gem(*treas.split(';')).description()) + '.')
        for treas in material_list.iterkeys():
            if material_list[treas] > 1:
                description_list.append(capitalize_first(
                    Material.number_conjugation(treas, material_list[treas])) + '.')
            else:
                description_list.append(capitalize_first(Material(*treas.split(';')).description()) + '.')
            # Выводим остальное
        for treas in treas_list:
            # TODO: найти откуда в списке сокровищ при воровстве может быть None
            if treas:
                description_list.append(capitalize_first(treas.description()) + '.')
        return description_list

    def take_ingot(self, ingot_type, weight=1):
        """
        :param ingot_type: название металла
        :param weight: вес, который мы хотели бы взять 
        :return: Возвращает тип Ingot с указанным весом или максимально возможным, либо None,
            если такого металла в сокровищнице нет
        """
        if ingot_type in self.metals and self.metals[ingot_type] > 0:  # проверяем есть ли такой металл в сокровищнице
            ingot = Ingot(ingot_type)  # создаем ingot
            # делаем вес слитка равным указанному весу или максимуму в сокровищнице:
            if weight < self.metals[ingot_type]:
                ingot.weight = weight
            else:
                ingot.weight = self.metals[ingot_type]
            self.metals[ingot_type] -= ingot.weight  # вычитаем вес слитка из сокровищницы
            if self.metals[ingot_type] == 0:
                del self.metals[ingot_type]  # удаляем тип материала из списка сокровищницы
            return ingot
        elif ingot_type in self.metals:
            del self.metals[ingot_type]  # удаляем тип металла из списка сокровищницы
        return None

    def take_material(self, material_name):
        """
        :param material_name: описание материала в формате 'тип;размер'
        :return: Возвращает тип Material или None, если такого материала в сокровищнице нет
        """
        # проверяем есть ли такой материал в сокровищнице
        if material_name in self.materials and self.materials[material_name] > 0:
            material_param = material_name.split(';')  # парсим строку
            material = Material(*material_param)  # получаем экземпляр класса с нужными параметрами
            self.materials[material_name] -= 1  # вычитаем один материал из списка сокровищницы
            if self.materials[material_name] == 0:
                del self.materials[material_name]  # удаляем тип материала из списка сокровищницы
            return material
        elif material_name in self.materials:
            del self.materials[material_name]  # удаляем тип материала из списка сокровищницы
        return None

    def take_gem(self, gem_name):
        """
        :param gem_name: описание камня в формате 'тип;размер;обработка'
        :return: Возвращает тип Gem или None, если таких камней в сокровищнице нет
        """
        if gem_name in self.gems and self.gems[gem_name] > 0:  # проверяем есть ли такой камень в сокровищнице
            gem_param = gem_name.split(';')  # парсим строку
            gem = Gem(*gem_param)  # получаем экземпляр класса с нужными параметрами
            self.gems[gem_name] -= 1  # вычитаем один камень из списка сокровищницы
            return gem
        elif gem_name in self.gems:
            del self.gems[gem_name]  # удаляем тип камня из списка сокровищницы
        return None

    def take_coin(self, coin_name, coin_count=1):
        """
        :param coin_name: название монеты
        :param coin_count: сколько монет нам бы хотелось взять
        :return: Возвращает тип Coin с указанным числом монет или максимально возможным, либо None,
            если таких монет в сокровищнице нет
        """
        if coin_name == 'farthing' and self.farthing > 0:
            if coin_count > self.farthing:
                coin_count = self.farthing
            self.farthing -= coin_count
        elif coin_name == 'taller' and self.taller > 0:
            if coin_count > self.taller:
                coin_count = self.taller
            self.taller -= coin_count
        elif coin_name == 'dubloon' and self.dubloon > 0:
            if coin_count > self.dubloon:
                coin_count = self.dubloon
            self.dubloon -= coin_count
        else:
            return None
        return Coin(coin_name, coin_count)

    def rob_treasury(self, treasure_count=1):
        """
        :param treasure_count: Количество сокровищ, которые необходимо взять из сокровищницы
        :return: Список самых дорогих сокровищ, взятых из сокровищницы
        """
        treasure_list = []  # список сокровищ, которые не приглянулись вору
        abducted_list = []  # список награбленного
        threshold_value = 0  # минимальная стоимость, которая будет взята

        def update_list(test_treasure):  
            """
            функция добавления награбленного в список, возвращает истину в случае успешного добавления
            """
            if not test_treasure:
                return False  # попытка взять несуществующую вещь
            elif threshold_value < test_treasure.cost:
                test_cost = test_treasure.cost  # сохраняем цену для скорости
                test_i = len(abducted_list)  # новый индекс - последний в списке
                while test_i > 0 and abducted_list[test_i - 1].cost < test_cost:
                    test_i -= 1  # сортировка
                abducted_list.insert(test_i, test_treasure)  # вставляем в нужную позицию
                if len(abducted_list) > treasure_count:  # убираем из списка вещь с наименьшей ценой
                    treasure_list.append(abducted_list.pop())
                    self.threshold_value = abducted_list[-1].cost
                return True
            else:
                # стоимость добавляемого меньше пороговой, возвращаем сокровище обратно в сокровищницу
                treasure_list.append(test_treasure)
                return False

        # цикл по всем сокровищам, начиная с конца списка, для соответствия индекса количеству вещей в списке
        for _ in reversed(xrange(len(self.jewelry))):
            # достаем сокровище из конца списка - там должны быть более дорогие сокровища и
            # пробуем добавить их в список награбленного
            update_list(self.jewelry.pop())
        self.jewelry.extend(treasure_list)  # возвращаем сокровища в сокровищницу после поиска самых дорогих
        treasure_list = []  # очищаем список возвращаемого
        for gem_type in self.gems.keys():  # просматриваем список типов камней
            while update_list(self.take_gem(gem_type)):
                pass  # пока в список добавляются камни - добавляем
        for metal_type in self.metals.keys():  # аналогично, просматриваем список типов слитков
            while update_list(self.take_ingot(metal_type, 8)):
                pass  # пока в список добавляются слитки - добавляем
        for coin_type in Coin.coin_types.keys():  # аналогично, просматриваем список типов монет
            while update_list(self.take_coin(coin_type, 100)):
                pass  # пока в список добавляются монеты - добавляем
        for material_type in self.materials.keys():  # аналогично, просматриваем список типов материалов
            while update_list(
                    self.take_material(material_type)):
                pass  # пока в список добавляются материалы - добавляем
        self.receive_treasures(treasure_list)  # возвращаем сокровища в сокровищницу
        return abducted_list

    def gem_name_count(self, gem_name):
        """
        :param gem_name: Тип драгоценных камней (в формате 'тип;размер;обработка'), для которого необходимо подсчитать
            количество камней в сокровищнице
        :return: количество камней такого типа в сокровищнице с учетом того, что мелкие идут группами по 25, а
            обычные - по 5
        """
        gem_count = self.gems[gem_name]  # берем данные о количестве из словаря
        gem_param = gem_name.split(';')  # парсим строку
        if gem_param[1] == 'small':
            gem_count *= 25
        elif gem_param[1] == 'common':
            gem_count *= 5
        return gem_count

    @property
    def gems_list(self):
        """
        :return: строка с описанием количества драгоценных камней в сокровищнице
        """
        gem_str = u"В сокровищнице находится:\n"
        gem_list = sorted(self.gems.keys())  # список драгоценных камней, отсортированных по типу/размеру/огранке
        for gem_name in gem_list:
            if self.gems[gem_name]:  # проверка наличия камней такого типа в сокровищнице
                gem_str += u"%s.\n" % capitalize_first(Gem.number_conjugation(gem_name, self.gems[gem_name]))
        return gem_str

    @property
    def materials_list(self):
        """
        :return: строка с описанием количества материалов в сокровищнице
        """
        material_str = u"In the treasury is:\n"
        metal_list = sorted(self.metals.keys())
        for metal_name in metal_list:
            metal_weight = self.metals[metal_name]
            if metal_weight:
                material_str += u"%s.\n" % capitalize_first(Ingot.number_conjugation(metal_name, metal_weight))
        mat_list = sorted(self.materials.keys())
        for mat_name in mat_list:
            if self.materials[mat_name]:
                material_str += u"%s.\n" % capitalize_first(
                    Material.number_conjugation(mat_name, self.materials[mat_name]))
        return material_str

    @property
    def most_expensive_jewelry_index(self):
        """
        Индекс самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            most_expensive_i = 0
            most_expensive_cost = self.jewelry[most_expensive_i].cost
            for jewelry_i in xrange(len(self.jewelry)):
                if self.jewelry[jewelry_i].cost > most_expensive_cost:
                    most_expensive_cost = self.jewelry[jewelry_i].cost
                    most_expensive_i = jewelry_i
            return most_expensive_i
        else:
            return -1

    @property
    def cheapest_jewelry_index(self):
        """
        Индекс самого дешёвого украшения в сокровищнице
        """
        if len(self.jewelry):
            cheapest_i = 0
            cheapest_cost = self.jewelry[cheapest_i].cost
            for jewelry_i in xrange(len(self.jewelry)):
                if self.jewelry[jewelry_i].cost < cheapest_cost:
                    cheapest_cost = self.jewelry[jewelry_i].cost
                    cheapest_i = jewelry_i
            return cheapest_i
        else:
            return -1

    @property
    def most_expensive_jewelry_cost(self):
        """
        Стоимость самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            return self.jewelry[self.most_expensive_jewelry_index].cost
        else:
            return 0

    @property
    def most_expensive_jewelry(self):
        """
        Описание самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            most_expensive_i = self.most_expensive_jewelry_index
            return u"%s.\nValue of ornament: %s.\n%s" % (
                capitalize_first(self.jewelry[most_expensive_i].description()),
                number_conjugation_rus(self.jewelry[most_expensive_i].cost, u"фартинг"),
                self.jewelry[most_expensive_i].obtained)
        else:
            return u"No ornaments in the treasury"

    @property
    def cheapest_jewelry(self):
        """
        Описание самого дешёвого украшения в сокровищнице
        """
        if len(self.jewelry):
            cheapest_i = self.cheapest_jewelry_index
            return u"%s.\Value of ornament: %s.\n%s" % (
                capitalize_first(self.jewelry[cheapest_i].description()),
                number_conjugation_rus(self.jewelry[cheapest_i].cost, u"фартинг"),
                self.jewelry[cheapest_i].obtained)
        else:
            return u"No ornaments in the treasury."

    @property
    def random_jewelry(self):
        if len(self.jewelry):
            random_jewelry = random.choice(self.jewelry)
            return u"%s.\Value of ornament: %s.\n%s" % (capitalize_first(random_jewelry.description()),
                                                           number_conjugation_rus(random_jewelry.cost, u"фартинг"),
                                                           random_jewelry.obtained)
        else:
            return u"No ornaments in the treasury."

    @property
    def all_jewelries(self):
        """
        Стоимость всех украшений дракона
        """
        calc_all_jewelries = 0
        for treas_i in xrange(len(self.jewelry)):  
            calc_all_jewelries += self.jewelry[treas_i].cost
        return calc_all_jewelries

    @staticmethod
    def get_mass_description(description_key, mass):
        """ 
        :param description_key: ключ для словаря treasures_mass_description_rus
        :param mass: число, для которой нужно подобрать описание
        :return: описание массы в сокровищнице
        """
        if mass > 0:
            return get_description_by_count(treasures_mass_description_rus[description_key], mass)
        else:
            return u""

    @property
    def coin_mass(self):
        """
        :return: масса монет в сокровищнице
        """
        return self.farthing + self.taller + self.dubloon

    @property
    def coin_mass_description(self):
        """
        :return: описание массы монет в сокровищнице
        """
        return Treasury.get_mass_description('coin', self.coin_mass)

    @property
    def metal_mass(self):
        """
        :return: вес металла в сокровищнице
        """
        metal_weight = 0
        for metal_i in self.metals.values():
            metal_weight += metal_i
        return metal_weight

    @property
    def materials_mass_description(self):
        """
        :return: описание массы материалов и металлов в сокровищнице
        """
        return Treasury.get_mass_description('material', self.metal_mass + self.material_mass)

    @property
    def gem_mass(self):
        """
        :return: масса драгоценных камней в сокровищнице
        """
        gem_summ = 0
        for gem_i in self.gems.keys():
            gem_size = gem_i.split(';')
            gem_size = gem_size[1]
            if gem_size == 'small':
                gem_summ += 25
            elif gem_size == 'common':
                gem_summ += 15
            elif gem_size == 'large':
                gem_summ += 5
            else:
                gem_summ += 7
        return gem_summ

    @property
    def gems_mass_description(self):
        """
        :return: описание массы драгоценных камней в сокровищнице
        """
        return Treasury.get_mass_description('gem', self.gem_mass)

    @property
    def material_mass(self):
        """
        :return: масса материала в сокровищнице
        """
        mat_summ = 0
        for mat_i in self.materials.keys():
            mat_size = mat_i.split(';')
            mat_size = mat_size[1]
            mat_summ += Material.size_dict[mat_size][1]
        return mat_summ

    @property
    def jewelry_mass(self):
        """
        :return: масса украшений в сокровищнице
        """
        jewelry_summ = 0
        for jewelry_i in self.jewelry:
            jewelry_summ += jewelry_i.base_price
        return jewelry_summ

    @property
    def jewelry_mass_description(self):
        """
        :return: описание массы драгоценных камней в сокровищнице
        """
        return Treasury.get_mass_description('jewelry', self.jewelry_mass)
        
    @property
    def wealth_description(self):
        """
        :return: описание всех сокровищ в сокровищнице
        """
        wealth = self.wealth
        if wealth > 0:
            wealth_str = Treasury.get_mass_description('wealth', wealth)
            wealth_str += u"Total value of treasure: " + number_conjugation_rus(wealth, u"farthings") + u"."
            return wealth_str 
        else:
            return u"Treasury is empty."

    def get_salary(self, amount):
        """
        :param amount: требуемая сумма, фартингов
        :return: список того, что взяли, чтобы получить сумму, либо None, если в сокровищнице недостаточно денег.
        """
        # TODO: Сделать рефакторинг без использования `self`
        self.salary_list = []  # список сокровищ, которые можно взять в качестве платы
        self.salary_item = None  # предмет, который можно взять в качестве платы
        self.min_salary_value = 0  # цена предмета
        self.max_salary_value = 0  # цена списка сокровищ
        self.treasure_list = []  # список сокровищ, которые не приглянулись гремлинам

        def update_list(test_treasure):
            """
            функция добавления в список, возвращает истину если нужно добавить такую же вещь
            """
            if not test_treasure:
                return False  # попытка взять несуществующую вещь
            elif test_treasure.cost >= amount:
                # стоимость сокровища больше или равно необходимой суммы, можно взять только его в качестве оплаты
                if self.min_salary_value == 0:
                    # это первая вещь, которая стоит дороже, чем нам нужно - берём её
                    self.min_salary_value = test_treasure.cost
                    self.salary_item = test_treasure
                elif self.min_salary_value > test_treasure.cost:
                    # это не первая вещь, которая стоит дороже, чем нам нужно - берём её только если она дешевле прошлой
                    self.treasure_list.append(self.salary_item)  # возвращаем прошлую вещь в сокровищницу
                    self.min_salary_value = test_treasure.cost  # берём новую
                    self.salary_item = test_treasure
                else:
                    self.treasure_list.append(test_treasure)  # возвращаем вещь в сокровищницу
                return False  # больше такой не нужно
            else:
                # стоимость сокровища меньше необходимой суммы, придётся "скрести по сусекам"
                if self.max_salary_value < amount:
                    # стоимость списка недостаточно, добавляем ещё
                    self.max_salary_value += test_treasure.cost
                    self.salary_list.append(test_treasure)
                    return True
                else:
                    # стоимость списка достаточно, больше ничего не нужно
                    self.treasure_list.append(test_treasure)  # возвращаем вещь в сокровищницу
                    return False

        if self.wealth >= amount:
            if self.money >= amount:
                self.money -= amount
                self.salary_list.append(Coin('farthing', amount))
                return self.salary_list  # взяли деньгами сколько нужно
            else:
                for coin_type in Coin.coin_types.keys():  # просматриваем список типов монет
                    while update_list(self.take_coin(coin_type)):
                        pass  # пока в список добавляются монеты - добавляем
                # цикл по всем сокровищам, начиная с конца списка, для соответствия индекса количеству вещей в списке
                for _ in reversed(xrange(len(self.jewelry))):
                    # достаем сокровище из конца списка - там должны быть более дорогие сокровища и
                    # пробуем добавить их в список
                    update_list(self.jewelry.pop())
                for gem_type in self.gems.keys():  # просматриваем список типов камней
                    while update_list(self.take_gem(gem_type)):
                        pass  # пока в список добавляются камни - добавляем
                for metal_type in self.metals.keys():  # аналогично, просматриваем список типов слитков
                    while update_list(self.take_ingot(metal_type)):
                        pass  # пока в список добавляются слитки - добавляем
                for material_type in self.materials.keys():  # аналогично, просматриваем список типов материалов
                    while update_list(self.take_material(material_type)):
                        pass  # пока в список добавляются материалы - добавляем
                if self.max_salary_value > self.min_salary_value:
                    if self.salary_list:
                        self.treasure_list.extend(self.salary_list)  # возвращаем список в сокровищницу - не пригодился
                    self.salary_list = [self.salary_item]
                elif self.salary_list:
                    self.treasure_list.append(self.salary_item)  # возвращаем предмет в сокровищницу - не пригодился
                self.receive_treasures(self.treasure_list)  # возвращаем сокровища в сокровищницу
                return self.salary_list
        else:
            return None

    def check_gem_size(self, gem_size):
        """
        Функция для проверки есть ли в сокровищнице камень требуемого размера
        :param gem_size: размер камня для проверки
        :return: есть (True) или нет (False) в сокровищнице камень указанного размера
        """
        for gem_type in self.gems:
            if gem_type.split(';')[1] == gem_size:
                return True
        return False

    def available_materials(self, is_crafting, item_type):
        """
        Функция для проверки есть ли материал, из которого можно сделать вещь такого типа
        :param item_type: тип вещи, который хочется смастерить
        :param is_crafting: материалы дракона (True) или все доступные (False)
        :return: список материалов, из которых можно сделать вещь
        """
        materials = []
        if treasure_types[item_type][2]:
            # вещь можно сделать из металла, добавляем доступный список металлов
            if is_crafting:
                # все типы металлов у дракона
                materials += self.metals.keys()
            else:
                # все типы металлов в игре
                materials += metal_types.keys()
        if treasure_types[item_type][3]:
            # вещь можно сделать из поделочного материала, добавляем доступный список материалов
            if is_crafting:
                # все типы материалов у дракона
                for material_type in self.materials.keys():
                    # убираем повторы из-за возможной разницы в размерах поделочных материалов
                    material_name = material_type.split(';')[0]
                    if material_name not in materials:
                        materials.append(material_name)
            else:
                # все типы материалов в игре
                materials += material_types.keys()
        return materials

    def is_craft_possible(self, item_type, alignment):
        """
        Функция для проверки достаточно ли материалов в сокровищнице для изготовления вещи
        :param item_type: тип вещи, который хочется смастерить
        :param alignment: стиль вещи, которую хочется смастерить
        :return: достаточно (True) или нет (False) материалов для создания вещи
        """
        craft_possible = self.available_materials(True, item_type)
        if treasure_types[item_type][4]:
            # если сам предмет - изображение - нужен какой-то стиль
            craft_possible = craft_possible and alignment
        return craft_possible

    def craft_select_item(self, is_crafting, alignment):
        """
        Функция для вывода меню выбора типа покупаемой/создаваемой вещи
        :param is_crafting: создаётся из материалов дракона (True) или покупается (False)
        :return: выбранный тип вещи либо None в случае отмены
        """
        treasure_list = sorted(treasure_types.keys(), key=lambda treas: treasure_description_rus[treas]['nominative'])
        # получаем список возможных сокровищ
        if is_crafting:
            # если идёт создание вещи - ставим первыми в списке вещи, которые можем сделать
            craft_possible = []
            craft_impossible = []
            for treasure_type in treasure_list:
                if self.is_craft_possible(treasure_type, alignment):
                    craft_possible.append(treasure_type)
                else:
                    craft_impossible.append(treasure_type)
            treasure_list = craft_possible + craft_impossible
        menu_choice = None
        row_count = 10  # количество кнопок с отображаемым типом сокровища для создания/покупки
        position = 0  # начальное значение 
        while menu_choice not in treasure_list:
            # цикл для выбора типа сокровища для создания/покупки
            if row_count < len(treasure_list):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(treasure_list))):
                treasure_type = treasure_list[i]
                treas_name = treasure_description_rus[treasure_type]['nominative'].capitalize()
                if is_crafting:
                    menu_options.append((treas_name, treasure_type, True, self.is_craft_possible(treasure_type, alignment)))
                else:
                    menu_options.append((treas_name, treasure_type, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(treasure_list):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(treasure_list))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"cancel", 'return', True, True)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
            elif menu_choice == 'return':
                return None
        return menu_choice

    def craft_select_material(self, materials):
        """
        Функция для вывода меню выбора из списка
        :param materials: список материалов для выбора
        :return: выбранный вариант из списка либо None в случае отмены
        """
        menu_choice = None
        row_count = 10  # количество кнопок для отображения списка материалов
        position = 0  # начальное значение 
        while menu_choice not in materials:
            # цикл для выбора типа материала
            if row_count < len(materials):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(materials))):
                material_type = materials[i]
                if material_type in metal_types.keys():
                    # получаем название материала на русском
                    option_name = u"Из %s" % metal_description_rus[material_type]['genitive']
                else:
                    option_name = u"Из %s" % material_description_rus[material_type]['genitive']
                menu_options.append((option_name, material_type, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(materials):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(materials))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"", 'blank', True, False)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
        return menu_choice

    def craft_select_gem(self, is_crafting, gem_size):
        """
        Функция для вывода меню выбора камня для инкрустации из всех доступных вариантов
        После выбора автоматически вставляет (или убирает) камень нужного размера
        :param gem_size: размер камня для инкрустации
        :param is_crafting: из сокровищницы дракона (True) или покупается (False)
        :return: камень для инкрустации
        """
        menu_choice = None
        row_count = 10  # количество кнопок для отображения списка материалов
        position = 0  # начальное значение
        gem_list = []
        if is_crafting:
            # подходящие камни из сокровищницы дракона
            for gem_type in self.gems:
                # добавляем камни требуемого размера в список
                gem_params = gem_type.split(';')
                if gem_params[1] == gem_size:
                    if gem_size == 'small':
                        # изменение размера для хака описания
                        gem_params[1] = 'common'
                    gem_list.append(Gem(*gem_params))
        else:
            # все типы камней в игре
            gem_params = [None, gem_size, None]
            if gem_size == 'small':
                # изменение размера для хака описания
                gem_params[1] = 'common'
            gem_types_keys = sorted(gem_types.keys(), key=lambda gt: gem_description_rus[gt]['he']['nominative'])
            for gem_type in gem_types_keys:
                gem_params[0] = gem_type
                if gem_type == "pearl" or gem_type == "black_pearl":
                    gem_params[2] = " "
                    gem_list.append(Gem(*gem_params))
                else:
                    for gem_cut in ('rough', 'polished', 'faceted'):
                        gem_params[2] = gem_cut
                        gem_list.append(Gem(*gem_params))
        while menu_choice is None or (menu_choice == 'inc') or (menu_choice == 'dec'):
            # цикл для выбора типа камня
            if row_count < len(gem_list):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(gem_list))):
                menu_options.append((gem_list[i].description(custom=True).capitalize(), i, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(gem_list):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(gem_list))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"No stone", 'clear', True, True)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
        if menu_choice == 'clear':
            return None
        else:
            return gem_list[menu_choice]

    def craft(self, is_crafting=False, quality=['random'], alignment=['random'], base_cost=0, price_multiplier=100):
        """
        Функция для вывода меню покупки/создания вещи
        :param is_crafting: создаётся из материалов дракона (True) или покупается (False)
        :param quality: список для выбора возможного качества создаваемой вещи, 
            может быть rough, common, skillfully, mastery, 
            либо random для случайного выбора из этих вариантов с весовыми коэффициентами
        :param alignment: список для выбора возможного стиля декорации создаваемой вещи, 
            может быть human, knight, cleric, elf, dwarf, merman,
            либо random для случайного выбора из этих вариантов,
            либо None, если сделать орнамент невозможно
        :param base_cost: базовая стоимость работы (для ремесла)
        :param price_multiplier: увеличение цены (для покупки, в процентах)
        :return: созданная вещь либо None в случае отмены
        """
        if 'random' in alignment or not alignment:
            alignment = image_types.keys()
        alignment = random.choice(alignment)
        treasure_type = self.craft_select_item(is_crafting, alignment)
        if treasure_type is None:
            return None
        # случайный выбор стиля вещи из списка
        item = Treasure(treasure_type, alignment)
        quality_options = {
            'rough': u"с rough crafting",
            'common': u"с normal crafting",
            'skillfully': u"с skillful crafting",
            'mastery': u"с masterful crafting",
            'random': u"со random crafting"
        }
        item.quality = quality[0]
        # первоначальный выбор качества - первый в списке
        materials = self.available_materials(is_crafting, treasure_type)
        item.material = self.craft_select_material(materials)
        item.spangled = None
        item.inlaid = None
        item.huge = None
        item.decoration = None
        item.decoration_image = None
        menu_choice = None
        while menu_choice is not 'create':
            menu_options = [(u"cancel", 'return', True, True)]
            treasure_name = treasure_description_rus[treasure_type]['nominative'].capitalize()
            menu_options += [(treasure_name, treasure_type, True, False)]
            # тип вещи - не может быть изменен
            menu_options += [(quality_options[item.quality], 'quality', True, len(quality) > 1)]
            # качество вещи
            if item.material in metal_types.keys():
                material_name = u"из %s" % metal_description_rus[item.material]['genitive']
            else:
                material_name = u"из %s" % material_description_rus[item.material]['genitive']
            menu_options += [(material_name, 'material', True, True)]
            # материал вещи
            if treasure_types[treasure_type][5]:
                # проверка на возможность инкрустации
                if item.spangled:
                    spangled_description = decoration_description_rus['spangled'][treasure_types[treasure_type][1]]
                    spangled_description += u" " + item.spangled.description(True, 'ablative', 'they')
                    menu_options += [(spangled_description, 'spangled', True, True)]
                else:
                    menu_options += [(u"no spangles", 'spangled', True, not is_crafting or self.check_gem_size('small'))]
                if item.inlaid:
                    inlaid_description = decoration_description_rus['inlaid'][treasure_types[treasure_type][1]]
                    inlaid_description += u" " + item.inlaid.description(True, 'ablative', 'they')
                    menu_options += [(inlaid_description, 'inlaid', True, True)]
                else:
                    menu_options += [(u"no inlay", 'inlaid', True, not is_crafting or self.check_gem_size('common'))]
                if item.huge:
                    huge_description = u"c " + item.huge.description(True, 'ablative')
                    menu_options += [(huge_description, 'huge', True, True)]
                else:
                    menu_options += [(u"no large gem", 'huge', True, not is_crafting or self.check_gem_size('large'))]
            if alignment and item.decorable:
                if item.decoration:
                    decor_image = decoration_description_rus['image'][image_description_rus[item.decoration_image]['gender']]
                    decor_image += u" " + image_description_rus[item.decoration_image]['nominative']
                else:
                    decor_image = u"no image"
                menu_options += [(decor_image, 'decoration', True, True)]
            if is_crafting:
                if item.craft_cost(base_cost, price_multiplier) > 0:
                    price_msg = number_conjugation_rus(item.craft_cost(base_cost, price_multiplier), u"farthings")
                    craft_msg = u"Craft for %s (you have %s)" % (price_msg, self.money)
                else:
                    craft_msg = u"Craft"
            else:
                price_msg = number_conjugation_rus(item.craft_cost(base_cost, price_multiplier), u"фартинг")
                craft_msg = u"Craft for %s (you have %s)" % (price_msg, self.money)
            menu_options += [(craft_msg, 'create', True, item.craft_cost(base_cost, price_multiplier) <= self.money)]
            menu_choice = call_screen("dw_choice", menu_options)
            # показ меню
            if menu_choice == 'return':
                return None
            elif menu_choice == 'quality':
                menu_options = []
                for quality_type in quality:
                    menu_options += [(quality_options[quality_type], quality_type, True, True)]
                item.quality = call_screen("dw_choice", menu_options)
            elif menu_choice == 'material':
                item.material = self.craft_select_material(materials)
            elif menu_choice == 'spangled':
                item.spangled = self.craft_select_gem(is_crafting, 'small')
            elif menu_choice == 'inlaid':
                item.inlaid = self.craft_select_gem(is_crafting, 'common')
            elif menu_choice == 'huge':
                item.huge = self.craft_select_gem(is_crafting, 'large')
            elif menu_choice == 'decoration':
                menu_options = [(u"Decorate with image", 'yes', True, True)]
                menu_options += [(u"No image", 'no', True, True)]
                menu_choice = call_screen("dw_choice", menu_options)
                if menu_choice == 'yes':
                    item.decoration_image = random.choice(image_types[item.alignment])
                    if item.material in material_types:
                        item.decoration = 'carving'
                    else:
                        item.decoration = weighted_select(Treasure.decorate_types)
                else:
                    item.decoration = None
                    item.decoration_image = None
        if item.quality =='random':
            # случайный выбор качества вещи
            quality_list = (('rough', 25), ('common', 50), ('skillfully', 20), ('mastery', 10),)
            item.quality = weighted_random(quality_list)
        self.money -= item.craft_cost(base_cost, price_multiplier)
        if is_crafting:
            # если делается из материалов дракона - убираем материалы из сокровищницы
            if item.material in material_types:
                material = None
                materials_size = sorted(Material.size_dict.keys(), key=lambda mat_size: Material.size_dict[mat_size][1]) 
                # сортировка по размеру, т.к. дракон жадный - зачем отдавать большой кусок, если можно сделать из любого?
                for material_size in materials_size:
                    # ищем из какого бы куска изготовить вещь
                    if not material:
                        material = self.take_material(item.material + u";" + material_size)
            else:
                self.take_ingot(item.material)
            if item.spangled:
                self.take_gem(item.spangled.g_type + u';small;' + item.spangled.cut)
            if item.inlaid:
                self.take_gem(item.inlaid.g_type + u';common;' + item.inlaid.cut)
            if item.huge:
                self.take_gem(item.huge.g_type + u';large;' + item.huge.cut)
            if item.image:
                item.decoration_image = random.choice(image_types[item.alignment])
        return item