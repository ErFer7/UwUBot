# -*- coding: utf-8 -*-

'''
Módulo que contém a lógica interna do bot
'''

import os
import json

from time import time_ns
from random import seed
from datetime import datetime

import discord

from discord.ext import commands


class CustomBot(commands.Bot):

    '''
    Bot customizado
    '''

    name: str
    version: str
    guild_dict: dict

    def __init__(self, command_prefix, help_command, name, version):

        intents = discord.Intents.all()
        intents.presences = True
        intents.members = True

        super().__init__(command_prefix=command_prefix,
                         help_command=help_command,
                         intents=intents)

        self.name = name
        self.version = version
        self.guild_dict = {}

    async def setup(self):

        '''
        Inicialização e setup do bot
        '''

        print(f"[{datetime.now()}][Sistema]: Inicializando {self.name} {self.version}")
        print(f"[{datetime.now()}][Sistema]: Inicializando o RNG")

        seed(time_ns())

        print(f"[{datetime.now()}][Sistema]: Esperando o sistema...")
        await self.wait_until_ready()

        print(f"[{datetime.now()}][Sistema]: Carregando definições dos servidores")
        for guild in self.guilds:

            self.guild_dict[str(guild.id)] = Guild(guild.id, self)

        print(f"[{datetime.now()}][Sistema]: Sistema pronto")

        print(f"[{datetime.now()}][Sistema]: {self.name} {self.version} pronto para operar")
        print(f"[{datetime.now()}][Sistema]: Logado como {self.user.name}, no id: {self.user.id}")

        await self.change_presence(activity=discord.Game(name="Tua mãe na cama"))


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

            self.settings = {"Guild ID": self.id,
                             "Main channel ID": 0,
                             "Chronometer": False,
                             "Chronometer initial time": 0}

        self.guild = bot.get_guild(self.settings["Guild ID"])
        self.main_channel = bot.get_channel(self.settings["Main channel ID"])

        if self.main_channel is None:

            self.main_channel = self.guild.channels[0]

        print(f"[{datetime.now()}][Sistema]: Servidor {self.id} inicializado")

    def write_settings(self):
        '''
        Escreve as configurações do servidor
        '''

        with open(os.path.join("Guilds", f"{self.id}.json"), 'w+') as settings_file:

            settings_json = json.dumps(self.settings, indent=4)
            settings_file.write(settings_json)

        print(f"[{datetime.now()}][Sistema]: Servidor {self.id} registrado")

    def update_main_channel(self, bot):
        '''
        Atualiza o canal principal
        '''

        self.main_channel = bot.get_channel(self.settings["Main channel ID"])

        if self.main_channel is None:

            self.main_channel = self.guild.channels[0]

        print(f"[{datetime.now()}][Sistema]: Canal principal do servidor {self.id} atualizado")
