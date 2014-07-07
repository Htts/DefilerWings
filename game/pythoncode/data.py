#!/usr/bin/env python
# coding=utf-8

import collections

class FighterModifier(object):
    """
    Базовый класс для разнообразных модификаторов.
    К примеру: даров владычицы, снаряжения рыцарей, заклинаний и.т.д.
    """

    def __init__(self, attack=('base', (0, 0)), protection=('base', (0, 0))):
        self.attack = attack
        self.protection = protection

    def __contains__(self, item):
        return item in self.__dict__

    def attack_filter(self, attack):
        return attack


class DragonModifier(FighterModifier):
    """
    Класс для разнообразных модификаторов.
    К примеру: даров владычицы, снаряжения рыцарей, заклинаний и.т.д.
    """

    def __init__(self, attack=('base', (0, 0)), protection=('base', (0, 0)), magic=0, fear=0, energy=0):
        super(DragonModifier, self).__init__(attack=attack, protection=protection)
        self.magic = magic
        self.fear = fear
        self.max_energy = energy

class Container(collections.defaultdict):
    '''
    Класс-хранилище разнообразных свойст/модификаторов
    '''
    def __init__(self,id,data=None,*args,**kwargs):
        super(Container, self).__init__(*args,**kwargs)
        self.id = id
        if data is not None:
        
            for key, value in data.items():
                self.add(key, value)
    
    def add(self, id, data):
        '''
        :param id: Идентификатор свойства/модификатора
        :param data: dict, содержащий парамерты этого свойства/модификатор
        '''
        if id not in self:
            if type(data) is dict:
                self[id] = Container(id, data)
            else:
                self[id] = data
        else:
            raise Exception("Already in container")
    
    def sum(self, parameter):
        '''
        :param parameter: Значение, по которому нужно суммировать аттрибуты. Суммирование проводится
                          рекурсивно.
        '''
        total = 0
        if parameter in self:
            try:
                total += self[parameter]
            except ValueError:
                pass
        for i in self:
            if type(self[i]) == 'pythoncode.data.Container':
                total += self[i].sum(parameter)
        return total
    
    def __missing__(key):
        return None

thief_abilities = Container("thief_abilities",
                            { 
                              "climber":      { "name": "Альпинист" },
                              "diver":        { "name": "Ныряльщик" },
                              "greedy":       { "name": "Жадина" },
                              "mechanic":     { "name": "Механик" },
                              "magicproof":   { "name": "Знаток магии" },
                              "poisoner":     { "name": "Отравитель" },
                              "assassin":     { "name": "Ассасин" },
                              "night_shadow": { "name": "Ночная тень" },
                              "trickster":    { "name": "Ловкач" }
                            }
                           )
thief_items = Container("thief_items",
                        {
                          "plan":                 {"name": "План ограбления",
                                                   "level": 1},
                          "scheme":               {"name": "Схема тайных проходов"},
                          "sleep_dust":           {"name": "Сонный порошок"},
                          "bottomless_sac":       {"name": "Бездонный мешок",
                                                   "dropable": True},
                          "antidot":              {"name": "Антидот"},
                          "enchanted_dagger":     {"name": "Зачарованный кинжал",
                                                   "dropable": True},
                          "ring_of_invisibility": {"name": "Кольцо-невидимка",
                                                   "dropable": True},
                          "flying_boots":         {"name": "Летучие сандалии",
                                                   "dropable": True},
                          "cooling_amulet":       {"name": "Охлаждающий амулет",
                                                   "dropable": True},
                          "warming_amulet1":      {"name": "Согревающий амулет",
                                                   "dropable": True}
                        })

thief_titles = [ "Мародер", "Грабитель", "Взломшик", "Расхититель гробниц", "Мастер вор" ]

attack_types = ['base', 'fire', 'ice', 'poison', 'sound', 'lightning']
protection_types = ['base', 'scale', 'shield', 'armor']

fighter_mods = dict()
fighter_mods[u"щит"] = FighterModifier(protection = ('base', (1, 0)))
fighter_mods[u"меч"] = FighterModifier(attack = ('base', (2,1)))
fighter_mods[u"броня"] = FighterModifier(protection = ('base', (0,1)))
fighter_mods[u"копьё"] = FighterModifier(attack = ('base', (1,1)))
fighter_mods[u"спутник"] = FighterModifier(attack = ('base', (1,0)), protection = ('base', (1,0)))
fighter_mods[u"скакун"] = FighterModifier(attack = ('base', (1,0)))
# Типы голов(цвета)
dragon_heads = dict()
dragon_heads['green'] = []
dragon_heads['red'] = ['fire_breath', 'fire_immunity']
dragon_heads['white'] = ['ice_breath', 'ice_immunity']
dragon_heads['blue'] = ['can_swim']
dragon_heads['black'] = ['black_power', 'poison_breath']  # black_power -- +1 атака
dragon_heads['iron'] = ['iron_scale', 'sound_breath']  # iron_scale -- +1 защита
dragon_heads['copper'] = ['copper_scale', 'can_dig']  # copper_scale -- +1 защита
dragon_heads['silver'] = ['silver_magic', 'lightning_immunity']
dragon_heads['gold'] = ['gold_magic', 'greedy']  # greedy -- -2 к шансам вора
dragon_heads['shadow'] = ['shadow_magic', 'fear_of_dark']  # fear_of_dark -- +2 к страху

dragon_gifts = dict()

# Заклинания
spell_list = dict()
# заговоры -- дают иммунитет к атаке выбранного типа
spell_list['fire_protection'] = ['fire_immunity']
spell_list['ice_protection'] = ['ice_immunity']
spell_list['poison_protection'] = ['poison_immunity']
spell_list['lightning_protection'] = ['lightning_immunity']
spell_list['fire_protection'] = ['fire_immunity']
spell_list['sound_protection'] = ['sound_immunity']
# сердца -- дают дыхание нужного типа
spell_list['fire_heart'] = ['fire_breath']
spell_list['ice_heart'] = ['ice_breath']
spell_list['poison_heart'] = ['poison_breath']
spell_list['thunder_heart'] = ['sound_breath']
spell_list['lightning_heart'] = ['lightning_breath']
# прочие
spell_list['wings_of_wind'] = ['wings_of_wind']
spell_list['aura_of_horror'] = ['aura_of_horror']
spell_list['unbreakable_scale'] = ['virtual_head']

dragon_modifiers = dict()
dragon_modifiers['fire_immunity'] = DragonModifier()
dragon_modifiers['ice_immunity'] = DragonModifier()
dragon_modifiers['poison_immunity'] = DragonModifier()
dragon_modifiers['lightning_immunity'] = DragonModifier()
dragon_modifiers['sound_immunity'] = DragonModifier()

dragon_modifiers['fire_breath'] = DragonModifier(attack=('fire', (0, 1)))
dragon_modifiers['ice_breath'] = DragonModifier(attack=('ice', (0, 1)))
dragon_modifiers['poison_breath'] = DragonModifier(attack=('poison', (0, 1)))
dragon_modifiers['sound_breath'] = DragonModifier(attack=('sound', (0, 1)))
dragon_modifiers['lightning_breath'] = DragonModifier(attack=('lightning', (0, 1)))
dragon_modifiers['black_power'] = DragonModifier(attack=('base', (1, 0)))
dragon_modifiers['iron_scale'] = DragonModifier(protection=('scale', (1, 0)))
dragon_modifiers['copper_scale'] = DragonModifier(protection=('scale', (1, 0)))
dragon_modifiers['silver_magic'] = DragonModifier(magic=1)
dragon_modifiers['gold_magic'] = DragonModifier(magic=1)
dragon_modifiers['shadow_magic'] = DragonModifier(magic=1)
dragon_modifiers['fear_of_dark'] = DragonModifier(fear=2)
dragon_modifiers['aura_of_horror'] = DragonModifier(fear=1)
dragon_modifiers['wings_of_wind'] = DragonModifier(energy=1)
#
dragon_modifiers['size'] = DragonModifier(attack=('base', (1, 0)), protection=('base', (1, 0)), fear=1)
dragon_modifiers['paws'] = DragonModifier(attack=('base', (1, 0)), energy=1)
dragon_modifiers['wings'] = DragonModifier(protection=('base', (1, 0)), energy=1)
dragon_modifiers['tough_scale'] = DragonModifier(protection=('scale', (0, 1)))
dragon_modifiers['clutches'] = DragonModifier(attack=('base', (0, 1)))
dragon_modifiers['fangs'] = DragonModifier(attack=('base', (2, 0)), fear=1)
dragon_modifiers['horns'] = DragonModifier(protection=('base', (2, 0)), fear=1)
dragon_modifiers['ugly'] = DragonModifier(fear=2)
dragon_modifiers['poisoned_sting'] = DragonModifier(attack=('poison', (1, 1)))
dragon_modifiers['cunning'] = DragonModifier(magic=1)


thief_items = dict()
knight_items = dict()
knight_abilities = dict()


def get_modifier(name):
    if name in dragon_modifiers:
        return dragon_modifiers[name]
    elif name in fighter_mods:
        return fighter_mods[name]
    raise NotImplementedError
