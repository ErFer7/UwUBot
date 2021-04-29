# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de humor
'''

from datetime import datetime
from random import randint

import discord

from discord.ext import commands

class HumorCog(commands.Cog):

    '''
    Cog dos comandos de humor
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Humor]: Sistema de comandos de humor inicializado")

    @commands.command(name = "corno")
    async def fake_cuck_level(self, ctx):

        '''
        Retorna que a pessoa tem 100% de nível de corno
        '''

        print(f"[{datetime.now()}][Humor]: <corno> (Autor: {ctx.message.author.name})")

        if len(ctx.message.mentions) == 0:

            embed = discord.Embed(description = f"🐮 **{ctx.message.author.mention} é:**\n\n" \
                                                "*100%* corno",
                                  color = discord.Color.dark_blue())

            await ctx.send(embed = embed)
        else:

            embed = discord.Embed(description = f"🐮 **{ctx.message.mentions[0].mention} é:**\n\n" \
                                                "*100%* corno",
                                  color = discord.Color.dark_blue())

            await ctx.send(embed = embed)

    @commands.command(name = "cronos")
    async def cuck_level(self, ctx):

        '''
        Retorna o nível de corno
        '''

        print(f"[{datetime.now()}][Humor]: <crono> (Autor: {ctx.message.author.name})")

        if len(ctx.message.mentions) == 0:

            embed = discord.Embed(description = f"🐮 **{ctx.message.author.mention} é:**\n\n" \
                                                f"*{randint(0, 100)}%* corno",
                                  color = discord.Color.dark_blue())

            await ctx.send(embed = embed)
        else:

            embed = discord.Embed(description = f"🐮 **{ctx.message.mentions[0].mention} é:**\n\n" \
                                                f"*{randint(0, 100)}%* corno",
                                  color = discord.Color.dark_blue())

            await ctx.send(embed = embed)
