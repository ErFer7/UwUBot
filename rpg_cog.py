# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de rpg
'''

from datetime import datetime
from random import randint

import discord

from discord.ext import commands


class RPGCog(commands.Cog):

    '''
    Cog dos comandos de rpg
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][RPG]: Sistema de comandos de rpg inicializado")

    @commands.command(name="dado", aliases=('d', "dice"))
    async def dice(self, ctx, *args):

        '''
        Rola um dado
        '''

        print(f"[{datetime.now()}][RPG]: <dice> (Autor: {ctx.author.name})")

        valid = True
        result = "🎲  **Dados jogados**\n\n"

        if len(args) > 0:

            for arg in args:

                amount, num = 0, 0

                if not arg.startswith('d'):

                    amount, num = map(int, arg.split('d'))
                else:

                    amount = 1
                    num = int(arg[1:])

                if amount > 0 and num in (4, 6, 8, 10, 12, 20, 100):

                    dice_res = []

                    for _ in range(amount):

                        dice_res.append(randint(1, num))

                    result += arg + " = " + ', '.join(list(map(str, dice_res))) + '\n'
                else:

                    valid = False
                    break
        else:

            valid = False

        if len(result) > 2048:

            valid = False

        if valid:

            embed = discord.Embed(description=result, color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
        else:

            embed = discord.Embed(description="❌  **Comando inválido**\n\n"
                                  "*Uso correto*\n"
                                  "~dado <Lista de dados; Ex: 2d8 4d6>",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
