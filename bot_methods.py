# -*- coding:utf-8 -*-

'''
Módulo para o armazenamento de métodos
'''

from datetime import datetime

import discord


class DiscordUtilities():

    '''
    Utilidades
    '''

    @staticmethod
    def make_embed():
        '''
        Cria um embed padronizado.
        '''

        embed = discord.Embed(title="TESTE",
                              type="rich",
                              url='',
                              timestamp=datetime.now(),
                              description="❱❱❱ **Teste**",
                              color=discord.Color.dark_blue())

        embed.set_author(
            name="PyGR",
            icon_url="https://i.pinimg.com/originals/86/c1/66/86c166d70a154a7ddc82d71257e442df.jpg")

        embed.set_footer(
            text="Rodapé",
            icon_url="https://logodownload.org/wp-content/uploads/2017/11/discord-logo-4-1.png")

        embed.set_thumbnail(url="https://cpmr-islands.org/wp-content/uploads/sites/4/2019/07/test.png")

        return embed
