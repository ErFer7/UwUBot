# -*- coding:utf-8 -*-

'''
Módulo para a cog dos eventos
'''

from datetime import datetime

from discord.ext import commands

from legacy import Interact

class EventCog(commands.Cog):

    '''
    Cog dos eventos
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Evento]: Sistema de eventos inicializado")

    @commands.Cog.listener()
    async def on_message(self, message):

        '''
        Evento de mensagens
        '''

        print(f"[{datetime.now()}][Evento]: " \
        f"[{message.content}] de [{message.author.name}] no canal [{message.channel}]")

        # Inibe leitura das próprias mensagens
        if message.author == self.bot.user:
            return

        if self.bot.user.mentioned_in(message):

            print("[{0}][Evento]: Bot Mencionado".format(datetime.now()))

            awnser = Interact(message)

            if awnser is not None:

                await awnser

    @commands.Cog.listener()
    async def on_connect(self):

        print(f"[{datetime.now()}][Evento]: Conectado")

    @commands.Cog.listener()
    async def on_disconnect(self):

        print(f"[{datetime.now()}][Evento]: Desconectado")

    @commands.Cog.listener()
    async def on_resumed(self):

        print(f"[{datetime.now()}][Evento]: Resumido")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):

        print(f"[{datetime.now()}][Evento]: " \
              f"Membro [{after.name}] ficou [{after.status}] no servidor [{after.guild.nam}]")
