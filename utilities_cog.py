# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de utilidade
'''

import urllib.parse

from datetime import datetime
from random import randint

import discord

from discord.ext import commands

from bot_functions import rand_str


class UtilitiesCog(commands.Cog):

    '''
    Cog dos comandos de utilidade
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Utilidade]: Sistema de comandos de utilidade inicializado")

    @commands.command(name="wolfram", aliases=("wolf", "resolver", "solve"))
    async def wolfram_alpha(self, ctx, *search):

        '''
        Envia uma pesquisa no wolfram
        '''

        print(f"[{datetime.now()}][Utilidade]: <wolfram> (Autor: {ctx.author.name})")

        query = " ".join(search)
        url = "https://www.wolframalpha.com/input/?i=" + urllib.parse.quote(query)

        embed = discord.Embed(title="**Resultado:**",
                              url=url,
                              color=discord.Color.dark_blue())

        await ctx.send(embed=embed)

    @commands.command(name="rng")
    async def random_number(self, ctx, min_str=None, max_str=None):

        '''
        Gera um número aleatório
        '''

        print(f"[{datetime.now()}][Utilidade]: <rng> (Autor: {ctx.author.name})")

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

            embed = discord.Embed(description="❌  **Comando inválido**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

        if input_is_valid:

            embed = discord.Embed(description="❱❱❱ **Número gerado:**\n\n"
                                  f"*{randint(min_int, max_int)}*",
                                  color=discord.Color.dark_blue())

            await ctx.send(embed=embed)

    @commands.command(name="rsg")
    async def random_string(self, ctx, size_str=None):

        '''
        Gera um string aleatório
        '''

        print(f"[{datetime.now()}][Utilidade]: <rsg> (Autor: {ctx.author.name})")

        input_is_valid = False
        size = 0

        try:

            size = int(size_str)

            if size <= 1980:

                input_is_valid = True
            else:

                raise ValueError
        except ValueError:

            embed = discord.Embed(description="❌  **Comando inválido**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

        if input_is_valid:

            embed = discord.Embed(description="❱❱❱ **String gerado:**\n\n"
                                  f"*{rand_str(size)}*",
                                  color=discord.Color.dark_blue())

            await ctx.send(embed=embed)

    @commands.command(name="usuário", aliases=("user", 'u'))
    async def user_info(self, ctx):

        '''
        Obtém informações do usuário
        '''

        print(f"[{datetime.now()}][Utilidade]: <usuário> (Autor: {ctx.author.name})")

        user = None
        joined_at = ""

        if len(ctx.message.mentions) == 0:

            user = ctx.message.author
            joined_at = str(ctx.guild.get_member(ctx.message.author.id).joined_at)
        else:

            user = self.bot.get_user(ctx.message.mentions[0].id)
            joined_at = str(ctx.guild.get_member(ctx.message.mentions[0].id).joined_at)

        if user is not None:

            embed = discord.Embed(description=f"❱❱❱ **Informações sobre {user.name}:**\n\n"
                                  f"*ID:* {user.id}\n"
                                  f"*Discriminante:* {user.discriminator}\n"
                                  f"*Bot:* {user.bot}\n"
                                  f"*Sistema:* {user.system}\n"
                                  f"*Entrou no servidor em:* {joined_at}\n",
                                  color=discord.Color.dark_blue())

            await ctx.send(embed=embed)
            await ctx.send(user.avatar_url)
        else:

            embed = discord.Embed(description="❌  **Usuário não encontrado**\n\n",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    # Feito pelo grande Francisco Gamba (@Ffran33)
    @commands.command(name="playlist")
    async def playlist_link(self, ctx):

        '''
        Envia uma playlist
        '''

        print(f"[{datetime.now()}][Utilidade]: <playlist> (Autor: {ctx.author.name})")

        url = "https://open.spotify.com/playlist/5oi7roA6H7tyTjF4Xt0xM6?si=hGKMl78_RRGGgO3If2hosg"

        embed = discord.Embed(title="**Tá aqui a braba**",
                              url=url,
                              color=discord.Color.dark_blue())

        await ctx.send(embed=embed)
