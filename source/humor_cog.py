# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de humor.
'''

from random import randint

from discord.ext import commands
from discpybotframe.utilities import DiscordUtilities
from discpybotframe.cog import Cog


class HumorCog(Cog):

    '''
    Cog dos comandos de humor.
    '''

    def __init__(self, bot) -> None:
        super().__init__(bot)
        self.bot.log('HumorCog', 'Humor command system initialized')

    @commands.command(name='corno')
    async def cuck_level(self, ctx) -> None:
        '''
        Retorna o nível de corno.
        '''

        self.bot.log('HumorCog', f'<cuck_level> (Author: {ctx.author.name})')

        if len(ctx.message.mentions) == 0:
            await DiscordUtilities.send_message(ctx, '🐮 Nível de corno', f'*Você é {randint(0, 100)}%* corno', '')
        else:
            await DiscordUtilities.send_message(ctx,
                                                '🐮 Nível de corno',
                                                f'*{ctx.message.mentions[0].mention} é {randint(0, 100)}%* corno',
                                                '')
