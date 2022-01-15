# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de tempo
'''

from datetime import datetime
from time import time_ns, strftime, gmtime

import discord

from discord.ext import commands


class TimeCog(commands.Cog):

    '''
    Cog dos comandos de tempo
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Tempo]: Sistema de comandos de tempo inicializado")

    @commands.command(name="cronômetro", aliases=("cronometro", "cr"))
    async def chronometer(self, ctx):
        '''
        Cronometra o tempo
        '''

        print(f"[{datetime.now()}][Tempo]: <cronômetro> (Autor: {ctx.author.name})")

        key = str(ctx.guild.id)

        if self.bot.guild_dict[key].settings["Chronometer"]:

            self.bot.guild_dict[key].settings["Chronometer"] = False

            delta = time_ns() - self.bot.guild_dict[key].settings["Chronometer initial time"]
            formated_delta = strftime('%H:%M:%S', gmtime(delta // 1000000000))

            self.bot.guild_dict[key].settings["Chronometer initial time"] = 0

            embed = discord.Embed(description=f"🕒  **Tempo marcado:**\n\n{formated_delta}",
                                  color=discord.Color.green())

            await ctx.send(embed=embed)
        else:

            self.bot.guild_dict[key].settings["Chronometer"] = True
            self.bot.guild_dict[key].settings["Chronometer initial time"] = time_ns()
            embed = discord.Embed(description="🕒  **Marcando o tempo**",
                                  color=discord.Color.dark_blue())

            await ctx.send(embed=embed)
