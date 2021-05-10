# -*- coding: utf-8 -*-

'''
Funções para utilidades
'''

from re import search, IGNORECASE
from string import ascii_lowercase
from random import choice


def find_word(word, string):
    '''
    Encontra o string caso ele seja uma palavra entre espaços
    '''

    return search(r"\b{0}\b".format(word), string, flags=IGNORECASE)


def rand_str(length: int):
    '''
    Gera um string aleatório dentro do comprimento definido
    '''

    letters = ascii_lowercase
    return "".join(choice(letters) for _ in range(length))
