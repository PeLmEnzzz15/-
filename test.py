import random 
import time 
from data import *
from helpers import *



name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input("Выберите действие: 1 - В бой\n2 - тренировка\n3 - инфо об игроке\n4- инфо о текущем противнике ")
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == len(enemies):
            print("Поздравляю, вы победили всех противников!")
            break
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        display_player()
        print()
    elif action == '4':
        display_enemy(current_enemy)
        print()
    print()