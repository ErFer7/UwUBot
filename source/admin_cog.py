# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de administrador.
'''
import os

from datetime import datetime

from discord.errors import HTTPException
from discord.ext import commands

from source.utilities import DiscordUtilities


class AdminCog(commands.Cog):

    '''
    Cog dos comandos de adminstrador.
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Admin]: Sistema de comandos do administrador inicializado")

    @commands.command(name="off")
    async def shutdown(self, ctx):
        '''
        Desliga o bot
        '''

        print(f"[{datetime.now()}][Admin]: <off> (Autor: {ctx.author.name})")

        if ctx.author.id not in self.bot.admins_id:

            await DiscordUtilities.send_message(ctx,
                                                "Comando inválido",
                                                "Você não tem permissão para usar este comando",
                                                "shutdown",
                                                True)
            return

        if ctx.author.id in self.bot.admins_id:

            # Envia uma mensagem de saída
            await DiscordUtilities.send_message(ctx, "Encerrando", "Até o outro dia", "shutdown")

            # Salva todos os servidores
            print(f"[{datetime.now()}][Admin]: Registrando as definições dos servidores")

            for key in self.bot.guild_dict:
                self.bot.guild_dict[key].write_settings()

            # Encerra o bot
            print(f"[{datetime.now()}][Admin]: Encerrando")
            await self.bot.close()

    @commands.command(name="info")
    async def info(self, ctx):
        '''
        Exibe informações
        '''

        print(f"[{datetime.now()}][Admin]: <info> (Autor: {ctx.author.name})")

        print(f"[{datetime.now()}][Admin]: <info> (Autor: {ctx.author.name})")

        description = f'''⬩ **{self.bot.name} {self.bot.version}** - Criado em 26/06/2020

                          ⬩ **Loop HTTP:** {self.bot.loop}

                          ⬩ **Latência interna:** {self.bot.latency}

                          ⬩ **Servidores conectados:** {len(self.bot.guilds)}

                          ⬩ **Instâncias de voz:** {self.bot.voice_clients}'''

        await DiscordUtilities.send_message(ctx, "Informações", description, "info")

    @commands.command(name="save")
    async def save(self, ctx):
        '''
        Salva os servidores
        '''

        print(f"[{datetime.now()}][Admin]: <save> (Autor: {ctx.author.name})")

        if ctx.author.id not in self.bot.admins_id:

            await DiscordUtilities.send_message(ctx,
                                                "Comando inválido",
                                                "Você não tem permissão para usar este comando",
                                                "save",
                                                True)
            return

        self.bot.guild_dict[str(ctx.guild.id)].write_settings()

        await DiscordUtilities.send_message(ctx, "Salvando", "Os dados salvos são únicos para cada servidor", "save")

    @commands.command(name="get_channel_content")
    async def get_channel_content(self, ctx):
        '''
        Gera um arquivo com o conteúdo do canal
        '''

        print(f"[{datetime.now()}][Admin]: <get_channel_content> (Autor: {ctx.author.name})")

        if ctx.author.id not in self.bot.admins_id:

            await DiscordUtilities.send_message(ctx,
                                                "Comando inválido",
                                                "Você não tem permissão para usar este comando",
                                                "get_channel_content",
                                                True)
            return

        try:
            message_history = await ctx.channel.history(limit=None).flatten()
        except HTTPException:

            print(f"[{datetime.now()}][Comando]: Erro HTTP, mensagens não carregadas.")
            return

        messages = []

        for message in message_history:
            messages.append(f"[{message.author}]: {message.content}\n")

        messages.reverse()

        with open(os.path.join("System", "Admin Data", f"{ctx.channel.id}_extract.txt"),
                    "w+",
                    encoding="utf-8") as extracted_content:

            for message in messages:
                extracted_content.write(message)

        print(f"[{datetime.now()}][Comando]: Operação de extração concluída.")
