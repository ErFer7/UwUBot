# -*- coding: utf-8 -*-

'''
Bot para Discord - 2020/06/26 - Eric Fernandes Evaristo
Projeto: Bot-Project
Bot: PyGR

ATUALMENTE EM REFATORAÇÃO
'''

import sys
import asyncio
import urllib.parse

from random import randint
from datetime import datetime
from string import ascii_lowercase

import discord

from unidecode import unidecode

import legacy
import pygr_functions

from bot_system import CustomBot
from admin_cog import AdminCog
from help_cog import HelpCog
from time_cog import TimeCog
from settings_cog import SettingsCog
from rpg_cog import RPGCog
from voice_cog import VoiceCog

# Token. Não compartilhe!
TOKEN = "NzI2MTM5MzYxMjQxODU4MTU5.XvY99A.Fh8e071wE-eqGo2tndUlAG3vuCU"

# Variáveis globais
NAME = "PyGR"
VERSION = "3.10"
ADM_ID = 382542596196663296

# Corrige o erro de saída temporáriamente.
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Inicializa intents
intents = discord.Intents.all()
intents.presences = True
intents.members = True

bot = CustomBot(command_prefix = "~",
                help_command = None,
                intents = intents,
                name = NAME,
                version = VERSION)

#region Commands
#region Utilities
# Envia a resposta do Wolfram Alpha
@bot.command(name = "wolf")
async def Wolfram(ctx, *search):

    print("[{0}][Comando]: Wolf (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    query = " ".join(search)
    url = "https://www.wolframalpha.com/input/?i=" + urllib.parse.quote(query)

    await ctx.send(url)

# Gera um número aleatório
@bot.command(name = "rng")
async def RandomNumber(ctx, minStr = None, maxStr = None):

    print("[{0}][Comando]: RNG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        input_is_valid = False
        min_int = 0
        max_int = 0

        try:

            min_int = int(minStr)
            max_int = int(maxStr)

            if min_int <= max_int:

                input_is_valid = True
            else:

                raise ValueError
        except ValueError:

            await ctx.send("```Input inválido```")

        if input_is_valid:

            await ctx.send("```{0}```".format(randint(min_int, max_int)))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Gera um string aleatório
@bot.command(name = "rsg")
async def RandomString(ctx, sizeStr = None):

    print("[{0}][Comando]: RSG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:
        
        input_is_valid = False
        size = 0

        try:

            size = int(sizeStr)

            if size <= 1994:

                input_is_valid = True
            else:

                raise ValueError
        except ValueError:

            await ctx.send("```Input inválido```")

        if input_is_valid:

            await ctx.send("```{0}```".format(pygr_functions.RandStr(size)))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Exibe os dados de um usuário
@bot.command(name = "usuário")
async def UserInfo(ctx):

    print("[{0}][Comando]: Usuário (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        user: discord.user
        joined_at = ""

        if len(ctx.message.mentions) == 0:

            user = ctx.message.author
            joined_at = str(ctx.guild.get_member(ctx.message.author.id).joined_at)
        else:

            user = bot.get_user(ctx.message.mentions[0].id)
            joined_at = str(ctx.guild.get_member(ctx.message.mentions[0].id).joined_at)

        if user is not None:

            await ctx.send("```Estas são as informações para: {0}\nId: {1}\nDiscriminador: {2}\nBot: {3}\nSistema: {4}\nEntrou no servidor em: {5}```".format(user.name, user.id, user.discriminator, user.bot, user.system, joined_at))
            await ctx.send(user.avatar_url)
        else:

            await ctx.send("```O usuário não foi encontrado```")

    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Envia a playlist do server - EXPERIMENTAL
# Feito pelo grande Francisco Gamba (@Ffran33)
@bot.command(name = "playlist")
async def Playlist_Link(ctx):

    print("[{0}][Comando]: Playlist (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        await ctx.send("Tá aqui a braba: [playlist](https://open.spotify.com/playlist/5oi7roA6H7tyTjF4Xt0xM6?si=hGKMl78_RRGGgO3If2hosg) ou https://open.spotify.com/playlist/5oi7roA6H7tyTjF4Xt0xM6?si=hGKMl78_RRGGgO3If2hosg")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)
#endregion

#region Humor
# Medidor de corno
@bot.command(name = "corno")
async def CuckLevel(ctx):

    print("[{0}][Comando]: Crono (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if len(ctx.message.mentions) == 0:
        
        await ctx.send("{0} é {1}\\% crono".format(ctx.message.author.mention, randint(0, 100)))
    else:

        await ctx.send("{0} é {1}\\% crono".format(ctx.message.mentions[0].mention, randint(0, 100)))

# Análise da partida
@bot.command(name = "valorant")
async def ValorantAnalysis(ctx):

    print("[{0}][Comando]: Valorant (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    team_A = 0
    team_B = 0

    if randint(0, 1) == 0:

        team_A = 13
    else:

        team_B = 13

    if team_A == 13:

        team_B = randint(0, 12)
    else:

        team_A = randint(0, 12)
    
    await ctx.send("```Resultado: {0} a {1}```".format(team_A, team_B))

# Transforma um string em emojis
@bot.command(name = "emoji")
async def Emojify(ctx, *string):

    print("[{0}][Comando]: Emojificar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        message = " ".join(string).lower()
        normalized_message = unidecode(message)
        emojified_message = ""

        for c in normalized_message:

            if c == " ":

                emojified_message += "   "
            elif c == "0":

                emojified_message += " :zero:"
            elif c == "1":

                emojified_message += " :one:"
            elif c == "2":

                emojified_message += " :two:"
            elif c =="3":

                emojified_message += " :three:"
            elif c == "4":

                emojified_message += " :four:"
            elif c == "5":

                emojified_message += " :five:"
            elif c == "6":

                emojified_message += " :six:"
            elif c == "7":

                emojified_message += " :seven:"
            elif c == "8":

                emojified_message += " :seven:"
            elif c == "9":

                emojified_message += " :seven:"
            elif c in ascii_lowercase:

                emojified_message += " :regional_indicator_{0}:".format(c)
        
        if len(emojified_message) <= 2000:

            await ctx.send(emojified_message)
        else:

            await ctx.send("```A mensagem é muito grande!```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Aleatoriza um string entre caixa alta e baixa
@bot.command(name = "zoas")
async def Mock(ctx, *str):

    print("[{0}][Comando]: Zoas (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        message = " ".join(str).lower()
        mocked_message = ""

        for c in message:

            if randint(0, 1) == 0:

                mocked_message += c.upper()
            else:

                mocked_message += c.lower()

        if len(mocked_message) <= 2000:

            await ctx.send(mocked_message)
        else:

            await ctx.send("```A mensagem é muito grande!```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)
#endregion
#endregion

#region Events
# Mensagem recebida
@bot.event
async def on_message(message):

    try:
        
        print("[{0}][Mensagem]: [{1}] de [{2}] no canal [{3}]".format(datetime.now(), message.content, message.author.name, message.channel))

        # Inibe leitura das próprias mensagens
        if message.author == bot.user:
            return
        
        # Comandos
        await bot.process_commands(message)

        if bot.user.mentioned_in(message):

            print("[{0}][Mensagem]: Bot Mencionado".format(datetime.now()))

            awnser = legacy.Interact(message)

            if awnser is not None:

                await awnser
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Conexão concluída
@bot.event
async def on_connect():
    print("[{0}][Sistema]: Conectado".format(datetime.now()))

# Conexão encerrada
@bot.event
async def on_disconnect():
    print("[{0}][Sistema]: Desconectado".format(datetime.now()))

# Conexão resumida
@bot.event
async def on_resumed():
    print("[{0}][Sistema]: Resumido".format(datetime.now()))

# Erro
@bot.event
async def on_error(event, *args, **kwargs):

    print("[{0}][Erro]: Erro interno".format(datetime.now()))

# Quando um usuário muda o seu perfil
@bot.event
async def on_member_update(before, after):

    try:

        print("[{0}][Sistema]: Membro [{1}] ficou [{2}] no servidor [{3}]".format(datetime.now(), after.name, after.status, after.guild.name))

    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)
#endregion

# Execução do bot
bot.add_cog(AdminCog(bot, ADM_ID))
bot.add_cog(HelpCog(bot))
bot.add_cog(TimeCog(bot))
bot.add_cog(SettingsCog(bot))
bot.add_cog(RPGCog(bot))
bot.add_cog(VoiceCog(bot))
bot.loop.create_task(bot.setup())
bot.run(TOKEN)
