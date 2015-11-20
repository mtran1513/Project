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
mew = Pokemon('mew', broom, {'psychic': 60, 'megapunch': 50}, 'mysterious pokemon')
pidgey = Pokemon('pidgey', route_1, {'gust': 20, 'tackle': 15}, 'tiny bird pokemon')
rattata = Pokemon('rattata', route_1, {'tackle': 20}, 'mouse pokemon')
caterpie = Pokemon('caterpie', v_forest2, {'tackle': 20}, 'worm pokemon')
weedle = Pokemon('weedle', v_forest2, {'posionsting': 20}, 'hairy bug pokemon')
metapod = Pokemon('metapod', v_forest3, {'stringshot': 10}, 'cocoon pokemon')
kakuna = Pokemon('kakuna', v_forest5, {'harden': 5}, 'cocoon  pokemon')
pikachu = Pokemon('pikachu', v_forest6, {'shock': 30, 'tackle': 20}, 'mouse  pokemon')
Scyther = Pokemon('Scyther', V_forest6, {'slash': 35, 'cut': 25}, 'mantis pokemon')

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
