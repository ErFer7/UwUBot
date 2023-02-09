# -*- coding: utf-8 -*-

'''
Módulo que contém a lógica interna do bot.
'''

from datetime import datetime
from typing import Callable
from os.path import join

import discord

from discpybotframe.bot import CustomBot
from discpybotframe.admin_cog import AdminCog
from discpybotframe.help_cog import HelpCog
from discpybotframe.event_cog import EventCog
from discpybotframe.settings_cog import SettingsCog
from discpybotframe.voice import VoiceController

from source.guild import Guild
from source.humor_cog import HumorCog
from source.rpg_cog import RPGCog
from source.text_cog import TextCog
from source.utilities_cog import UtilitiesCog
from source.voice_cog import VoiceCog


class Bot (CustomBot):

    '''
    Bot customizado.
    '''

    # Atributo público
    voice_controller: VoiceController

    def __init__(self,
                 command_prefix: str,
                 help_command: Callable,
                 name: str,
                 version: str) -> None:

        intents = intents = discord.Intents.all()
        super().__init__(command_prefix,
                         help_command,
                         name,
                         join("system", "internal_settings.json"),
                         intents,
                         version)
        self.voice_controller = VoiceController(self, join("system", "ffmpeg.exe"))

    # Métodos assícronos
    async def setup_hook(self) -> None:
        print(f"[{datetime.now()}][System]: Adding cogs...")

        help_text = ''

        with open(join("system", "help.txt"), 'r', encoding="utf-8") as help_file:
            help_text = help_file.read()

        await self.add_cog(AdminCog(self, "Até o outro dia."))
        await self.add_cog(HelpCog(help_text))
        await self.add_cog(SettingsCog(self))
        await self.add_cog(EventCog(self))
        await self.add_cog(HumorCog(self))
        await self.add_cog(RPGCog(self))
        await self.add_cog(TextCog(self))
        await self.add_cog(UtilitiesCog(self))
        await self.add_cog(VoiceCog(self))

    def load_guilds(self) -> None:
        print(f"[{datetime.now()}][System]: Loading guilds definitions")

        for guild in self.guilds:
            self._guilds[str(guild.id)] = Guild(guild.id, self)
