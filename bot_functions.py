# -*- coding: utf-8 -*-

'''
Funções para utilidades.

Esse módulo será removido e substituído pelo bot_methods.
'''

from re import search, IGNORECASE


def find_word(word, string):
    '''
    Encontra o string caso ele seja uma palavra entre espaços.
    '''

    return search(r"\b{0}\b".format(word), string, flags=IGNORECASE)
