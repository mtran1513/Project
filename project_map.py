from project_class import Room
from project_class import Pokemon
from project_class import Trainer
import random

v_city = Room('Viridian City', {}, [])
route_1 = Room('route 1', {}, [])
oak = Room('oak\'s office', {}, [])

oak.doors({'north': route_1})
route_1.doors({'south': oak, 'north': v_city})
v_city.doors({'south': route_1})

starters = []
all_pokes = []
bulb = Pokemon('bulbasaur', route_1, {'absorb': 5}, 'gary\'s grass starter')
squirt = Pokemon('squirtle', route_1, {'bubble': 5}, 'gary\'s water starter')
charm = Pokemon('charmander', route_1, {'ember': 5}, 'gary\'s fire starter')
bulbasaur = Pokemon('bulbasaur', oak, {'absorb': 20}, 'The grass starter')
squirtle = Pokemon('squirtle', oak, {'bubble': 20}, 'The water starter')
charmander = Pokemon('charmander', oak, {'ember': 20}, 'The fire starter')
oak.add_pokemon(bulbasaur)
oak.add_pokemon(squirtle)
oak.add_pokemon(charmander)
starters.append(bulb)
starters.append(squirt)
starters.append(charm)

player = Trainer('ash')

rb1 = Trainer('gary')
rb1.weapon = random.choice(starters)
rb1.location = route_1


trainer_list = []
a = list(globals().values())
for item in a:
    if isinstance(item, Trainer):
        trainer_list.append(item)
        
def move_others():
    for et in trainer_list:
        if et.name != 'ash' and et.location == player.location:
            print('\nTrainer {} challenges you!\n'.format(et.name))
            move = et.weapon.damage.keys()
            if 'absorb' in move:
                et.attack(['attack', 'ash'], 'absorb')
            elif 'bubble' in move:
                et.attack(['attack', 'ash'], 'bubble')
            elif 'ember' in move:
                et.attack(['attack', 'ash'], 'ember')
