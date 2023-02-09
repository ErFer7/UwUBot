# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de humor
'''

from datetime import datetime
from random import randint

from discord.ext import commands
from discpybotframe.utilities import DiscordUtilities


class HumorCog(commands.Cog):

    '''
    Cog dos comandos de humor
    '''

    _bot: None

    def __init__(self, bot) -> None:
        self._bot = bot
        print(f"[{datetime.now()}][Humor]: Sistema de comandos de humor inicializado")

    @commands.command(name="corno")
    async def cuck_level(self, ctx) -> None:
        '''
        Retorna o nível de corno
        '''

        print(f"[{datetime.now()}][Humor]: <corno> (Autor: {ctx.author.name})")

        if len(ctx.message.mentions) == 0:
            await DiscordUtilities.send_message(ctx, "🐮 Nível de corno", f"*Você é {randint(0, 100)}%* corno", '')
        else:
            await DiscordUtilities.send_message(ctx,
                                                "🐮 Nível de corno",
                                                f"*{ctx.message.mentions[0].mention} é {randint(0, 100)}%* corno",
                                                '')
