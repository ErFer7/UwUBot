# -*- coding: utf-8 -*-

'''
Módulo que contém a lógica interna do bot
'''

import os
import json
import discord

from discord.ext import commands

class CustomBot(commands.Bot):

    '''
    Bot customizado
    '''

    error_list: list
    is_ready: bool

    def __init__(self, command_prefix, help_command, intents):

        super().__init__(command_prefix = command_prefix,
                         help_command = help_command,
                         intents = intents)

        self.error_list = []
        self.is_ready = False

class Guild():

    '''
    Definição de um server
    '''

    id: int
    settings: dict
    guild: discord.guild
    main_channel: discord.channel

    def __init__(self, id, bot):

        self.id = id

        if os.path.exists(os.path.join("Guilds", f"{self.id}.json")):

            with open(os.path.join("Guilds", f"{self.id}.json"), 'r+') as settings_file:

                settings_json = settings_file.read()

            self.settings = json.loads(settings_json)
        else:

            self.settings = {"Guild ID" : self.id, "Main channel ID": 0, "Chronometer" : False, "Chronometer initial time" : 0}
        
        self.guild = bot.get_guild(self.settings["Guild ID"])
        self.main_channel = bot.get_channel(self.settings["Main channel ID"])

        if self.main_channel is None:

            self.main_channel = self.guild.channels[0]
    
    def write_settings(self):

        with open(os.path.join("Guilds", f"{self.id}.json"), 'w+') as settings_file:

            settings_json = json.dumps(self.settings)
            settings_file.write(settings_json)
    
    def update_main_channel(self, bot):

        self.main_channel = bot.get_channel(self.settings["Main channel ID"])

        if self.main_channel is None:

            self.main_channel = self.guild.channels[0]
