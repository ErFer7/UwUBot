# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de texto
'''

from datetime import datetime
from string import ascii_lowercase
from random import randint

import discord

from discord.ext import commands
from unidecode import unidecode

class TextCog(commands.Cog):

    '''
    Cog dos comandos de texto
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Texto]: Sistema de comandos de texto inicializado")

    @commands.command(name = "emojificar", aliases = ("emoji", "emojifier"))
    async def emojify(self, ctx, *string):

        '''
        Transforma o texto em emojis
        '''

        print(f"[{datetime.now()}][Texto]: Emojificar (Autor: {ctx.author.name})")

        message = ' '.join(string).lower()
        normalized_message = unidecode(message)
        emojified_message = ''

        char_dict = {'0': " :zero:",
                     '1': " :one:",
                     '2': " :two:",
                     '3': " :three:",
                     '4': " :four:",
                     '5': " :five:",
                     '6': " :six:",
                     '7': " :seven:",
                     '8': " :eight:",
                     '9': " :nine:",
                     ' ': "   "}

        for char in normalized_message:

            if char in "0123456789 ":

                emojified_message += char_dict[char]
            elif char in ascii_lowercase:

                emojified_message += f" :regional_indicator_{char}:"

        if len(emojified_message) <= 2000:

            await ctx.send(emojified_message)
        else:

            embed = discord.Embed(description = "❌  **A mensagem é muito grande**\n\n",
                                  color = discord.Color.red())

            await ctx.send(embed = embed)

    @commands.command(name = "emojificar2", aliases = ("emoji2", "emojifier2"))
    async def emojify_block(self, ctx, *string):

        '''
        Transforma o texto em um bloco de emojis (Originou de um bug, mas era muito bom)
        '''

        print(f"[{datetime.now()}][Texto]: Emojificar (Autor: {ctx.author.name})")

        message = ' '.join(string).lower()
        normalized_message = unidecode(message)
        striped_message = normalized_message.replace(' ', '')
        emojified_message = ''
        diagonal_message = ''

        char_dict = {'0': ":zero:",
                     '1': ":one:",
                     '2': ":two:",
                     '3': ":three:",
                     '4': ":four:",
                     '5': ":five:",
                     '6': ":six:",
                     '7': ":seven:",
                     '8': ":eight:",
                     '9': ":nine:"}

        for char in striped_message:

            if char in "0123456789":

                emojified_message += char_dict[char]
            elif char in ascii_lowercase:

                emojified_message += f":regional_indicator_{char}:"

            diagonal_message += emojified_message + '\n'

        if len(diagonal_message) <= 2000:

            await ctx.send(diagonal_message)
        else:

            embed = discord.Embed(description = "❌  **A mensagem é muito grande**\n\n",
                                  color = discord.Color.red())

            await ctx.send(embed = embed)

    @commands.command(name = "zoar", aliases = ("mock", "zoas"))
    async def mock(self, ctx, *string):

        '''
        Zoa o texto
        '''

        print(f"[{datetime.now()}][Comando]: Zoas (Autor: {ctx.author.name})")

        message = " ".join(string).lower()
        mocked_message = ""

        for char in message:

            if randint(0, 1) == 0:

                mocked_message += char.upper()
            else:

                mocked_message += char.lower()

        if len(mocked_message) <= 2000:

            await ctx.send(mocked_message)
        else:

            embed = discord.Embed(description = "❌  **A mensagem é muito grande**\n\n",
                                  color = discord.Color.red())

            await ctx.send(embed = embed)
