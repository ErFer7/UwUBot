# -*- coding: utf-8 -*-

'''
Módulo que contém a lógica interna do bot
'''

import os
import json
import discord

from datetime import datetime
from discord.ext import commands

class CustomBot(commands.Bot):

    error_list: list
    is_ready: bool

    def __init__(self, command_prefix, help_command, intents):

        super().__init__(command_prefix = command_prefix,
                         help_command = help_command,
                         intents = intents)

        self.error_list = []
        self.is_ready = False

class Guild():

    id: int
    settings: dict

    def __init__(self, id):

        self.id = id

        if os.path.exists(os.path.join("Guilds", "{0}.json".format(id))):

            with open(os.path.join("Guilds", "{0}.json".format(id)), 'r+') as settings_file:

                settings_json = settings_file.read()

            self.settings = json.loads(settings_json)
        else:

            self.settings = {"TESTSET" : 0}
    
    def write_settings(self):

        with open(os.path.join("Guilds", "{0}.json".format(self.id)), 'w+') as settings_file:

            settings_json = json.dumps(self.settings)
            settings_file.write(settings_json)
