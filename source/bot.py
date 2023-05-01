# -*- coding: utf-8 -*-

'''
Módulo que contém a lógica interna do bot.
'''

from os.path import join

import discord

from discord.ext.commands import HelpCommand

from discpybotframe.bot import Bot
from discpybotframe.admin_cog import AdminCog
from discpybotframe.help_cog import HelpCog
from discpybotframe.guild import Guild

from source.humor_cog import HumorCog
from source.rpg_cog import RPGCog
from source.text_cog import TextCog
from source.utilities_cog import UtilitiesCog


class CustomBot (Bot):

    '''
    Bot customizado.
    '''

    def __init__(self,
                 command_prefix: str,
                 help_command: HelpCommand,
                 name: str,
                 version: str) -> None:

        intents = intents = discord.Intents.all()
        super().__init__(command_prefix,
                         help_command,
                         name,
                         join('system', 'internal_settings.json'),
                         intents,
                         version)

    # Métodos assícronos
    async def setup_hook(self) -> None:
        self.log('CustomBot', 'Adding cogs...')

        help_text = ''

        with open(join('system', 'help.txt'), 'r', encoding='utf-8') as help_file:
            help_text = help_file.read()

        await self.add_cog(AdminCog(self, 'Até o outro dia.'))
        await self.add_cog(HelpCog(self, help_text))
        await self.add_cog(HumorCog(self))
        await self.add_cog(RPGCog(self))
        await self.add_cog(TextCog(self))
        await self.add_cog(UtilitiesCog(self))

    def add_guild(self, guild_id: int) -> None:
        self.custom_guilds[str(guild_id)] = Guild(guild_id, self)

    def remove_guild(self, guild_id: int) -> None:
        del self.custom_guilds[str(guild_id)]
