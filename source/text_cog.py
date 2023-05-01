# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de texto
'''

from string import ascii_lowercase
from random import randint

from discord.errors import HTTPException

from discord.ext import commands
from unidecode import unidecode

from discpybotframe.utilities import DiscordUtilities
from discpybotframe.cog import Cog

class TextCog(Cog):

    '''
    Cog dos comandos de texto.
    '''

    def __init__(self, bot) -> None:
        super().__init__(bot)
        self.bot.log('TextCog', 'Text command system initialized')

    @commands.command(name='case')
    async def case(self, ctx, option, *string) -> None:
        '''
        Muda a capitalização do texto.
        '''

        self.bot.log('TextCog', f'<case> (Author: {ctx.author.name})')

        if option is None or string is None:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', '', '', True)
            return

        message = ' '.join(string)

        match option:
            case 'up':
                message = message.upper()
            case 'down':
                message = message.lower()
            case 'swap':
                message = message.swapcase()

        await ctx.send(message)

    @commands.command(name='contar', aliases=('count', 'conte'))
    async def count(self, ctx, target, *string) -> None:
        '''
        Conta quantos caracteres há no texto
        '''

        self.bot.log('TextCog', f'<count> (Author: {ctx.author.name})')

        if target is None or string is None:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', '', '', True)
            return

        message = ' '.join(string).lower()
        count = message.count(target)

        await DiscordUtilities.send_message(ctx,
                                            'Contagem',
                                            f'**O string {target} foi encontrada {count}'
                                            ' vezes no texto** ' ,
                                            '')

    @commands.command(name='substituir', aliases=('replace', 'subs'))
    async def replace(self, ctx, old, new, *string) -> None:
        '''
        Substitui um sub-string
        '''

        self.bot.log('TextCog', f'<replace> (Author: {ctx.author.name})')

        if old is None or new is None or string is None:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', '', '', True)
            return

        message = ' '.join(string)
        await ctx.send(message.replace(old, new))

    @commands.command(name='emojificar', aliases=('emoji', 'emojifier'))
    async def emojify(self, ctx, *string) -> None:
        '''
        Transforma o texto em emojis
        '''

        self.bot.log('TextCog', f'<emojify> (Author: {ctx.author.name})')

        message = ' '.join(string).lower()
        normalized_message = unidecode(message)
        emojified_message = ''

        char_dict = {'0': ' :zero:',
                     '1': ' :one:',
                     '2': ' :two:',
                     '3': ' :three:',
                     '4': ' :four:',
                     '5': ' :five:',
                     '6': ' :six:',
                     '7': ' :seven:',
                     '8': ' :eight:',
                     '9': ' :nine:',
                     ' ': '   '}

        for char in normalized_message:

            if char in '0123456789 ':

                emojified_message += char_dict[char]
            elif char in ascii_lowercase:

                emojified_message += f' :regional_indicator_{char}:'

        if len(emojified_message) <= 2000:
            await ctx.send(emojified_message)
        else:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', 'A mensagem é muito grande', '', True)

    @commands.command(name='emojificar2', aliases=('emoji2', 'emojifier2'))
    async def emojify_block(self, ctx, *string) -> None:
        '''
        Transforma o texto em um bloco de emojis (Originou de um bug, mas era muito bom)
        '''

        self.bot.log('TextCog', f'<emojify_block> (Author: {ctx.author.name})')

        message = ' '.join(string).lower()
        normalized_message = unidecode(message)
        striped_message = normalized_message.replace(' ', '')
        emojified_message = ''
        diagonal_message = ''

        char_dict = {'0': ':zero:',
                     '1': ':one:',
                     '2': ':two:',
                     '3': ':three:',
                     '4': ':four:',
                     '5': ':five:',
                     '6': ':six:',
                     '7': ':seven:',
                     '8': ':eight:',
                     '9': ':nine:'}

        for char in striped_message:

            if char in '0123456789':

                emojified_message += char_dict[char]
            elif char in ascii_lowercase:

                emojified_message += f':regional_indicator_{char}:'

            diagonal_message += emojified_message + '\n'

        if len(diagonal_message) <= 2000:
            await ctx.send(diagonal_message)
        else:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', 'A mensagem é muito grande', '', True)

    @commands.command(name='zoar', aliases=('mock', 'zoas'))
    async def mock(self, ctx, *string) -> None:
        '''
        Zoa o texto
        '''

        self.bot.log('TextCog', f'<mock> (Author: {ctx.author.name})')

        message = ' '.join(string).lower()
        mocked_message = ''

        for char in message:

            if randint(0, 1) == 0:

                mocked_message += char.upper()
            else:

                mocked_message += char.lower()

        if len(mocked_message) <= 2000:
            await ctx.send(mocked_message)
        else:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', 'A mensagem é muito grande', '', True)

    @commands.command(name='contar_canal', aliases=('channel_count', 'ct'))
    async def channel_count(self, ctx, target) -> None:
        '''
        Conta quantas vezes a mensagem apareceu no canal
        '''

        self.bot.log('TextCog', f'<channel_count> (Author: {ctx.author.name})')

        if target is None:
            await DiscordUtilities.send_message(ctx, 'Uso incorreto', '', '', True)
            return

        await DiscordUtilities.send_message(ctx, 'Aguarde', '', '')

        try:
            messages = [message async for message in ctx.channel.history(limit=None)]
        except HTTPException:
            self.bot.log('TextCog', 'HTTP Error, messages not loaded.')
            await DiscordUtilities.send_message(ctx, 'Erro de conexão', '', '', True)
            return

        count = 0

        for message in messages:
            count += message.content.count(target)

        await DiscordUtilities.send_message(ctx,
                                            'Contagem',
                                            f'**O string \'{target}\' foi encontrada {count}'
                                            f' vezes no texto. {len(messages)} mensagens foram analisadas**',
                                            '')
