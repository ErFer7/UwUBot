# -*- coding: utf-8 -*-

'''
Funções para utilidades
'''

from re import compile, IGNORECASE # (!) Checar a redefinição de compile
from string import ascii_lowercase
from random import choice

def FindWholeWord(word):

    """ Encontra o string caso ele seja uma palavra entre espaços
    """

    return compile(r'\b({0})\b'.format(word), flags = IGNORECASE).search

def RandStr(length: int):

    """ Gera um string aleatório dentro do comprimento definido
    """

    letters = ascii_lowercase
    return "".join(choice(letters) for i in range(length))