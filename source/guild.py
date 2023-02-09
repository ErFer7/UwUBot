# -*- coding: utf-8 -*-

'''
Módulo para os servers.
'''

from datetime import datetime

from discpybotframe.guild import CustomGuild


class Guild(CustomGuild):

    '''
    Definição de um server.
    '''

    def __init__(self, identification: int, bot) -> None:
        super().__init__(identification, {}, bot)
        print(f"[{datetime.now()}][System]: Custom guild initialization completed")
