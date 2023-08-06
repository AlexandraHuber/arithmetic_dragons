# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon): #addition
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon): #substraction
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon): #multiplication
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest



#FIXME Далее можете ввести новых атакующих юнитов:
    """тролля, который задаёт вопрос "Угадай число от 1 до 5"
    тролля, который задаёт вопрос на простоту числа
    тролля, который просит разложить число на множители и перечислить их через запятую
    """

class GuessTroll(Dragon): #troll asks a hero to guess a number from 1 to 5
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'quess_troll'

    def question(self):
        x = randint(1,4)
        self.__quest = 'quess a number between 1 and 3'
        self.set_answer(x)
        return self.__quest

class IfSimpleTroll(Dragon): #test for a simplisity of a number
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'if_simple_troll'

    def question(self):
        x = randint(1,100)
        self.__quest = f"Is {str(x)} a prime number? Answer in a format True/False"
        self.set_answer(str(is_prime(x)))
        return self.__quest

class FactorsTroll(Dragon): #question for factors of a number
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'factors_troll'

    def question(self):
        x = randint(1,11)
        self.__quest = f"Say me all factors of {str(x)}"
        self.set_answer(factor(x)) #FIXME
        return self.__quest
enemy_types = [GreenDragon, RedDragon, BlackDragon, GuessTroll, IfSimpleTroll, FactorsTroll]

# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return print('No')
#   return print('Yes')
# print(type(is_prime(27)))

def factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

print(factor(10))
# print(" ".join(str(x) for x in factor(8)))

# def input_factors_of_number(message):
#     answer = None
#     while answer == None:
#         try:
#             answer = []
#             answer_0 = input(message).split(',')
#             for i in range(len(answer_0)):
#                 answer.append(int(answer_0[i]))
#         except ValueError:
#             print('Вы ввели недопустимые символы')
#     return answer
#
# print(input_factors_of_number('message'))