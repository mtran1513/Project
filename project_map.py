from project_class import Room
from project_class import Pokemon
from project_class import Trainer
import random

v_city = Room('Viridian City', {}, [])
route_1 = Room('route 1', {}, [])
oak = Room('oak\'s office', {}, [])
broom = Room('broom closet', {}, [])

v_city.doors({'south': route_1})
route_1.doors({'south': oak, 'north': v_city})
oak.doors({'north': route_1})

starters = []
bulb = Pokemon('bulbasaur', route_1, {'absorb': 5}, 'gary\'s grass starter')
squirt = Pokemon('squirtle', route_1, {'bubble': 5}, 'gary\'s water starter')
charm = Pokemon('charmander', route_1, {'ember': 5}, 'gary\'s fire starter')
weedle2 = Pokemon('weedle', v_forest1, {'poisonsting': 20}, 'bryce\'s hairy bug pokemon')
pika = Pokemon('pikachu', route_2, {'volttackle': 20}, 'mike\'s pikachu')
scyth = Pokemon('scyther', V_forest6, {'slash': 35}, 'dillon\'s mantis pokemon')
cubone = Pokemon('cubone', pcg7, {'bonemerang': 36}, 'grant\'s lonely pokemon')
onix = Pokemon('onix', pcg9, {'irontail': 40,}, 'brock\'s rock snake pokemon')
diglett = Pokemon('diglett', pcg4, {'dig': 35,}, 'david\'s mole pokemon')
butterfree = Pokemon('butterfree', v_forrest6, {'charm': 1}, 'zak\'s butterfly pokemon')

bulbasaur = Pokemon('bulbasaur', oak, {'absorb': 20}, 'The grass starter')
squirtle = Pokemon('squirtle', oak, {'bubble': 20}, 'The water starter')
charmander = Pokemon('charmander', oak, {'ember': 20}, 'The fire starter')
mew = Pokemon('mew', broom, {'psychic': 60, 'megapunch': 50}, 'mysterious pokemon')
pidgey = Pokemon('pidgey', route_1, {'gust': 20, 'tackle': 15}, 'tiny bird pokemon')
rattata = Pokemon('rattata', route_1, {'tackle': 20}, 'mouse pokemon')
caterpie = Pokemon('caterpie', v_forest2, {'tackle': 20}, 'worm pokemon')
weedle = Pokemon('weedle', v_forest2, {'posionsting': 20}, 'hairy bug pokemon')
metapod = Pokemon('metapod', v_forest3, {'harden': 5}, 'cocoon pokemon')
kakuna = Pokemon('kakuna', v_forest5, {'harden': 5}, 'cocoon  pokemon')
scyther = Pokemon('scyther', V_forest6, {'slash': 35, 'cut': 20}, 'mantis pokemon'
pikachu = Pokemon('pikachu', v_forest6, {'volttackle': 30, 'tackle': 20}, 'mouse  pokemon')

oak.add_pokemon(bulbasaur)
oak.add_pokemon(squirtle)
oak.add_pokemon(charmander)
broom.add_pokemon(mew)
starters.append(bulb)
starters.append(squirt)
starters.append(charm)

player = Trainer('ash')

rb1 = Trainer('gary')
rb1.weapon = random.choice(starters)
rb1.location = route_1
rb1.inventory = [potion] 

bt1 = Trainer('bug_trainer_bryce')
bt1.weapon = weedle2
bt1.location = v_forrest1

bt2 = Trainer('bug_trainer_dillon')
bt2.weapon = scyth
bt2.location = v_forrest4
bt2.inventory = [potion]

bt3 = Trainer('bug_trainer_zak')
bt3.weapon = butterfree
bt3.location = v_forrest6
bt3.inventory = [potion]

at2 = Trainer('ace_trainer_mike')
at2.weapon = pika
at2.location = route_2
at2.inventory = [super_potion]

hik = Trainer('hiker_david')
hik.weapon = diglett
hik.location = pcg4
hik.inventory = [potion]

at1 = Trainer('ace_trainer_grant')
at1.weapon = cubone
at1.location = pcg7
at1.inventory = [super_potion]

gl = Trainer('gym_leader_brock')
gl.weapon = onix
gl.location = pcg9
gl.inventory = [super_potion]

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
             elif 'posionsting' in move:
                et.attack(['attack', 'ash'], 'posionsting')
            elif 'slash' in move:
                et.attack(['attack', 'ash'], 'slash')
            elif 'charm' in move:
                et.attack(['attack', 'ash'], 'charm')
            elif 'volttackle' in move:
                et.attack(['attack', 'ash'], 'volttackle')
            elif 'dig' in move:
                et.attack(['attack', 'ash'], 'dig')
            elif 'bonemerang' in move:
                et.attack(['attack', 'ash'], 'bonemerang')\
            elif 'irontail' in move:
                et.attack(['attack', 'ash'], 'irontail')

