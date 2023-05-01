# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de utilidade.
'''

from datetime import datetime
from random import randint, choice
from string import ascii_lowercase

from discord.ext import commands
from discpybotframe.utilities import DiscordUtilities
from discpybotframe.cog import Cog

class UtilitiesCog(Cog):

    '''
    Cog dos comandos de utilidade.
    '''

    def __init__(self, bot) -> None:
        super().__init__(bot)
        self.bot.log('UtilitiesCog', 'Utility command system initialized')

    @commands.command(name='rng')
    async def random_number(self, ctx, min_str=None, max_str=None) -> None:
        '''
        Gera um número aleatório.
        '''

        self.bot.log('UtilitiesCog', f'<random_number> (Author: {ctx.author.name})')

        input_is_valid = False
        min_int = 0
        max_int = 0

        try:

            min_int = int(min_str)
            max_int = int(max_str)

            if min_int <= max_int:
                input_is_valid = True
            else:
                raise ValueError
        except ValueError:
            await DiscordUtilities.send_message(ctx, 'Comando inválido', '', '', True)

        if input_is_valid:
            await DiscordUtilities.send_message(ctx, 'Número gerado', f'*{randint(min_int, max_int)}*', '')

    @commands.command(name='rsg')
    async def random_string(self, ctx, size_str=None) -> None:
        '''
        Gera um string aleatório.
        '''

        self.bot.log('UtilitiesCog', f'<random_string> (Author: {ctx.author.name})')

        input_is_valid = False
        size = 0

        try:

            size = int(size_str)

            if size <= 1980:
                input_is_valid = True
            else:
                raise ValueError
        except ValueError:
            await DiscordUtilities.send_message(ctx, 'Comando inválido', '', '', True)

        if input_is_valid:
            random_string = ''.join(choice(ascii_lowercase) for _ in range(size))
            await DiscordUtilities.send_message(ctx, 'String gerado', f'*{random_string}*', '')

    @commands.command(name='usuário', aliases=('user', 'u'))
    async def user_info(self, ctx):
        '''
        Obtém informações do usuário.
        '''

        self.bot.log('UtilitiesCog', f'<user_info> (Author: {ctx.author.name})')

        user = None
        joined_at = ''

        if len(ctx.message.mentions) == 0:

            user = ctx.message.author
            joined_at = str(ctx.guild.get_member(ctx.message.author.id).joined_at)
        else:

            user = self._bot.get_user(ctx.message.mentions[0].id)
            joined_at = str(ctx.guild.get_member(ctx.message.mentions[0].id).joined_at)

        if user is not None:

            await DiscordUtilities.send_message(ctx,
                                                f'Informações sobre {user.name}:',
                                                f'*ID:* {user.id}\n'
                                                f'*Discriminante:* {user.discriminator}\n'
                                                f'*Bot:* {user.bot}\n'
                                                f'*Sistema:* {user.system}\n'
                                                f'*Entrou no servidor em:* {joined_at}\n',
                                                '')
            await ctx.send(user.avatar)
        else:
            await DiscordUtilities.send_message(ctx, 'Usuário não encontrado', '', '', True)

    # Só deixo aqui por desencargo de consciência
    # Feito por Francisco Gamba (@Ffran33)
    @commands.command(name='playlist')
    async def playlist_link(self, ctx) -> None:
        '''
        Envia uma playlist.
        '''

        self.bot.log('UtilitiesCog', f'<playlist> (Author: {ctx.author.name})')

        url = 'https://open.spotify.com/playlist/5oi7roA6H7tyTjF4Xt0xM6?si=hGKMl78_RRGGgO3If2hosg'
        await DiscordUtilities.send_message(ctx, '???', 'Tá aqui a braba', '@Ffran33', False, url)
