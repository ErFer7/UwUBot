# -*- coding: utf-8 -*-

'''
Funções para utilidades
'''

import time

from re import compile, IGNORECASE # (!) Checar a redefinição de compile
from string import ascii_lowercase
from random import randint, choice

def FindWholeWord(word):

    '''
    Encontra o string caso ele seja uma palavra entre espaços
    '''

    return compile(r'\b({0})\b'.format(word), flags = IGNORECASE).search

def RandStr(length: int):

    '''
    Gera um string aleatório dentro do comprimento definido
    '''

    letters = ascii_lowercase
    return "".join(choice(letters) for _ in range(length))

def time_format(time_ns: int):

    return time.strftime('%H:%M:%S', time.gmtime(time_ns // 1000000000))
