# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de rpg.
'''

from random import randint

from discord.ext import commands
from discpybotframe.utilities import DiscordUtilities
from discpybotframe.cog import Cog

from source.validation import CustomArgumentFormat, CustomArgumentType, Validator


class RPGCog(Cog):

    '''
    Cog dos comandos de rpg.
    '''

    def __init__(self, bot) -> None:
        super().__init__(bot)
        self.bot.log('RPGCog', 'RPG command system initialized')

    @commands.command(name='dado', aliases=('d', 'dice'))
    async def dice(self, ctx, *args) -> None:
        '''
        Rola um dado.
        '''

        self.bot.log('RPGCog', f'<dice> (Author: {ctx.author.name})')

        validator = Validator(self.bot, ctx, 'dado', 'Comando inválido', args)
        validator.require_arg_format((CustomArgumentFormat(CustomArgumentType.DICE),), False)  # type: ignore

        if not await validator.validate_command():
            return

        result = ''

        for arg in args:

            amount, num = 0, 0

            if not arg.startswith('d'):
                amount, num = map(int, arg.split('d'))
            else:
                amount = 1
                num = int(arg[1:])

            dice_res = []

            for _ in range(amount):
                dice_res.append(randint(1, num))

            result += arg + ' = ' + ', '.join(list(map(str, dice_res))) + '\n'

        await DiscordUtilities.send_message(ctx, '🎲 Dados jogados', result, 'dado')
