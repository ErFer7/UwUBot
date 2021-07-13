# -*- coding:utf-8 -*-

'''
Módulo para o sistema de interação.
'''

import discord


class InteractionProcessor():

    '''
    Processa interações dinâmicamente.
    '''

    temper: float
    interactions: list

    def __init__(self):

        self.temper = 0.0

    def process_message(self, message: str):
        '''
        Processa a mensagem
        '''


class Interaction():

    '''
    Representa uma conversa
    '''

    channel: discord.channel
    members: list
    subject: str
