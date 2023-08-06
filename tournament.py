# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from tkinter import *


# root = Tk()
# fr = Frame(root)
# root.geometry('800x600')
# canv = Canvas(root, bg='white')
# canv.pack(fill=BOTH, expand=1)

# self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
#
#
# def set_coords(self):
#     canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


def annoying_input_int(message =''): #input of answers for dragons and quess_troll
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer

def input_simple_number(message =''):
    answer = None
    while answer == None:
        try:
            answer = input(message)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer

def input_factors_of_number(message =''):
    answer = None
    while answer == None:
        try:
            answer = []
            answer_0 = input(message).split(',')
            for i in range(len(answer_0)):
                answer.append(int(answer_0[i]))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer

def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        if type(dragon) == GreenDragon or type(dragon) == RedDragon or type(dragon) == BlackDragon or type(dragon) == GuessTroll:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')

        elif type(dragon) == IfSimpleTroll:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = input_simple_number('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')

        elif type(dragon) == FactorsTroll:
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = input_factors_of_number('Ответ:')

                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                break
            print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 6
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 6)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
