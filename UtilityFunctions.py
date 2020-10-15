# -*- coding: utf-8 -*-

# Funções para utilidades

from re import compile, IGNORECASE
from string import ascii_lowercase
from random import choice
import discord

def FindWholeWord(word):

    return compile(r'\b({0})\b'.format(word), flags = IGNORECASE).search

def RandStr(length: int):

    letters = ascii_lowercase
    return "".join(choice(letters) for i in range(length))

# Não utilizada
def IsMemberOnline(clientUser, member):

    return str(member.status) == "online" and member != clientUser and not member.bot