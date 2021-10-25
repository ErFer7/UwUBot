# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de texto
'''

from datetime import datetime
from string import ascii_lowercase
from random import randint

import discord
from discord.errors import HTTPException

from discord.ext import commands
from unidecode import unidecode


class TextCog(commands.Cog):

    '''
    Cog dos comandos de texto
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Texto]: Sistema de comandos de texto inicializado")

    @commands.command(name="case")
    async def case(self, ctx, option, *string):
        '''
        Muda a capitalização do texto
        '''

        print(f"[{datetime.now()}][Comando]: <case> (Autor: {ctx.author.name})")

        if option is None or string is None:

            embed = discord.Embed(description="❌  **Uso incorreto*\n\n",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        message = " ".join(string)

        match option:
            case "up":
                message = message.upper()
            case "down":
                message = message.lower()
            case "swap":
                message = message.swapcase()

        await ctx.send(message)

    @commands.command(name="contar", aliases=("count", "conte"))
    async def count(self, ctx, target, *string):
        '''
        Conta quantos caracteres há no texto
        '''

        print(f"[{datetime.now()}][Comando]: <contar> (Autor: {ctx.author.name})")

        if target is None or string is None:
            embed = discord.Embed(description="❌  **Uso incorreto*\n\n",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        message = " ".join(string).lower()
        count = message.count(target)

        embed = discord.Embed(description=f"❱❱❱ **O string {target} foi encontrada {count}"
                              " vezes no texto** ",
                              color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

    @commands.command(name="substituir", aliases=("replace", "subs"))
    async def replace(self, ctx, old, new, *string):
        '''
        Substitui um sub-string
        '''

        print(f"[{datetime.now()}][Comando]: <substituir> (Autor: {ctx.author.name})")

        if old is None or new is None or string is None:

            embed = discord.Embed(description="❌  **Uso incorreto*\n\n",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        message = " ".join(string)
        await ctx.send(message.replace(old, new))

    @commands.command(name="emojificar", aliases=("emoji", "emojifier"))
    async def emojify(self, ctx, *string):
        '''
        Transforma o texto em emojis
        '''

        print(f"[{datetime.now()}][Texto]: <emojificar> (Autor: {ctx.author.name})")

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

            embed = discord.Embed(description="❌  **A mensagem é muito grande**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command(name="emojificar2", aliases=("emoji2", "emojifier2"))
    async def emojify_block(self, ctx, *string):
        '''
        Transforma o texto em um bloco de emojis (Originou de um bug, mas era muito bom)
        '''

        print(f"[{datetime.now()}][Texto]: <emojificar> (Autor: {ctx.author.name})")

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

            embed = discord.Embed(description="❌  **A mensagem é muito grande**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command(name="zoar", aliases=("mock", "zoas"))
    async def mock(self, ctx, *string):
        '''
        Zoa o texto
        '''

        print(f"[{datetime.now()}][Comando]: <zoas> (Autor: {ctx.author.name})")

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

            embed = discord.Embed(description="❌  **A mensagem é muito grande**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command(name="contar_canal", aliases=("channel_count", "ct"))
    async def channel_count(self, ctx, target):
        '''
        Conta quantas vezes a mensagem apareceu no canal
        '''

        print(f"[{datetime.now()}][Comando]: <contar_canal> (Autor: {ctx.author.name})")

        if target is None:
            embed = discord.Embed(description="❌  **Uso incorreto*\n\n",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(description="❱❱❱ **Aguarde o processo**",
                              color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

        try:
            message_history = await ctx.channel.history(limit=None).flatten()
        except HTTPException:

            print(f"[{datetime.now()}][Comando]: Erro HTTP, mensagens não carregadas.")

            embed = discord.Embed(description="❌  **Erro de conexão**\n\n",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return

        count = 0

        for message in message_history:
            count += message.content.count(target)

        embed = discord.Embed(description=f"❱❱❱ **O string {target} foi encontrada {count}"
                              f" vezes no texto. {len(message_history)} mensagens foram analisadas**",
                              color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
