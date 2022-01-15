# -*- coding:utf-8 -*-

'''
Módulo para a cog dos comandos de voz
'''

import os

from datetime import datetime
from os import listdir
from os.path import isfile, join

import discord

from discord.ext import commands


class VoiceCog(commands.Cog):

    '''
    Cog dos comandos de voz
    '''

    def __init__(self, bot):

        self.bot = bot

        print(f"[{datetime.now()}][Voz]: Sistema de comandos de voz inicializado")

    @commands.command(name="conectar", aliases=("connect", "entrar", "join"))
    async def join(self, ctx):
        '''
        Entra em uma chamada
        '''

        print(f"[{datetime.now()}][Voz]: <conectar> (Autor: {ctx.message.author.name})")

        voice_channel = ctx.message.author.voice.channel

        if voice_channel is not None:

            if ctx.voice_client is None or not ctx.voice_client.is_connected():

                embed = discord.Embed(description="❱❱❱ **Entrando**",
                                      color=discord.Color.dark_blue())

                await ctx.send(embed=embed)

                await voice_channel.connect()
            else:

                embed = discord.Embed(description="❌  **Já estou conectado**",
                                      color=discord.Color.red())

                await ctx.send(embed=embed)
        else:

            embed = discord.Embed(description="❌  **Não tenho nenhum canal pra me conectar**",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command(name="desconectar", aliases=("disconnect", "sair", "leave"))
    async def leave(self, ctx):
        '''
        Sai da chamada
        '''

        print(f"[{datetime.now()}][Voz]: <desconectar> (Autor: {ctx.message.author.name})")

        if ctx.voice_client is not None and ctx.voice_client.is_connected():

            embed = discord.Embed(description="❱❱❱ **Saindo**",
                                  color=discord.Color.dark_blue())

            await ctx.send(embed=embed)

            await ctx.voice_client.disconnect()
        else:

            embed = discord.Embed(description="❌  **Não estou conectado**",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command(name="tocar", aliases=("play", 'p'))
    async def play(self, ctx, audio=None):
        '''
        Toca um áudio
        '''

        print(f"[{datetime.now()}][Voz]: <tocar> (Autor: {ctx.message.author.name})")

        if ctx.voice_client is not None and ctx.voice_client.is_connected():

            if ctx.voice_client.is_playing():

                embed = discord.Embed(description="❱❱❱ **Procurando novo áudio**",
                                      color=discord.Color.dark_blue())

                await ctx.send(embed=embed)

                ctx.voice_client.stop()

            if audio is not None:

                audio_files = [i for i in listdir("Audio") if isfile(join("Audio", i))]

                file_was_found = False

                for file in audio_files:

                    if audio == file[:-4]:

                        file_was_found = True

                        source = os.path.join("Audio", str(file))
                        executable = os.path.join("System", "ffmpeg.exe")

                        ctx.voice_client.play(discord.FFmpegPCMAudio(source=source,
                                                                     executable=executable))

                        embed = discord.Embed(description="🎵  **Tocando...**",
                                              color=discord.Color.dark_blue())

                        await ctx.send(embed=embed)

                if not file_was_found:

                    embed = discord.Embed(description="❌  **Arquivo não encontrado**",
                                          color=discord.Color.red())

                    await ctx.send(embed=embed)
            else:

                embed = discord.Embed(description="❌  **Comando inválido**\n\n"
                                      "*Uso correto*\n~tocar <áudio>",
                                      color=discord.Color.red())
                await ctx.send(embed=embed)
        else:

            embed = discord.Embed(description="❌  **Não estou conectado**",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command(name="parar", aliases=("stop", 's'))
    async def stop(self, ctx):
        '''
        Para o áudio
        '''

        print(f"[{datetime.now()}][Voz]: <parar> (Autor: {ctx.message.author.name})")

        if ctx.voice_client is not None and ctx.voice_client.is_connected():

            if ctx.voice_client.is_playing():

                embed = discord.Embed(description="❱❱❱ **Parando o áudio**",
                                      color=discord.Color.dark_blue())

                await ctx.send(embed=embed)

                ctx.voice_client.stop()
            else:

                embed = discord.Embed(description="❌  **Não tem nada tocando**",
                                      color=discord.Color.red())

                await ctx.send(embed=embed)
        else:

            embed = discord.Embed(description="❌  **Não estou conectado**",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)
