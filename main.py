# -*- coding: utf-8 -*-

'''
Bot para Discord - 2020/06/26 - Eric Fernandes Evaristo
Projeto: Bot-Project
Bot: PyGR
'''
# Atualmente em refatoração

import os
import asyncio
import discord
import urllib.parse
import pygr_core
import legacy
import pygr_functions

from time import time_ns, sleep
from random import randint, seed
from datetime import datetime
from os import listdir
from os.path import isfile, join
from string import ascii_lowercase
from discord.ext.tasks import loop
from unidecode import unidecode

# Token. Não compartilhe!
TOKEN = "NzI2MTM5MzYxMjQxODU4MTU5.XvY99A.Fh8e071wE-eqGo2tndUlAG3vuCU"

# Variáveis globais
NAME = "PyGR"
VERSION = "3.9.7-15"
ADM_ID = 382542596196663296

# Inicializa intents
intents = discord.Intents.all()
intents.presences = True
intents.members = True

guilds = {}

bot = pygr_core.CustomBot(command_prefix = "~", help_command = None, intents = intents)

#region Commands
#region System Commands
@bot.group()
async def sys(ctx):

    print("[{0}][Comando]: <sys> (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.invoked_subcommand is None:

        embed = discord.Embed(description = "❌  **Comando inválido**\n\n*Opções possíveis:*\n⬩ off\n⬩ info\n⬩ save", color = discord.Color.red())
        await ctx.send(embed = embed)

# Desliga
@sys.command(name = "off")
async def shutdown(ctx):

    print("[{0}][Sub-Comando]: <off> (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.message.author.id == ADM_ID:
        
        embed = discord.Embed(description = "❱❱❱ **Encerrando**\n\n*Até o outro dia*", color = discord.Color.dark_blue())
        await ctx.send(embed = embed)

        print("[{0}][Sistema]: Registrando as definições dos servidores".format(datetime.now()))

        for key in guilds:

            print("[{0}][Sistema]: Definições do servidor {1} registradas".format(datetime.now(), guilds[key].id))
            guilds[key].write_settings()

        print("[{0}][Sistema]: Erros = {1}".format(datetime.now(), bot.error_list))
        print("[{0}][Sistema]: Encerrando".format(datetime.now()))

        await bot.close()
    else:

        embed = discord.Embed(description = "❌  **Comando inválido**\n\n*Você não tem permissão para usar este comando*", color = discord.Color.red())
        await ctx.send(embed = embed)

# Informações
@sys.command(name = "info")
async def info(ctx):

    print("[{0}][Sub-Comando]: Info (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    header = "**{0} {1}** - Criado em 26/06/2020".format(NAME, VERSION)
    websocket = "**Websocket:** {0}".format(bot.ws)
    http_loop = "**Loop HTTP:** {0}".format(bot.loop)
    latency = "**Latência interna:** {0}".format(bot.latency)
    guild_count = "**Servidores conectados:** {0}".format(len(bot.guilds))
    voice_clients = "**Instâncias de voz:** {0}".format(bot.voice_clients)

    embed = discord.Embed(description = "❱❱❱ **Informações**\n\n⬩ {0}\n\n⬩ {1}\n\n⬩ {2}\n\n⬩ {3}\n\n⬩ {4}\n\n⬩ {5}".format(header, websocket, http_loop, latency, guild_count, voice_clients), color = discord.Color.dark_blue())
    await ctx.send(embed = embed)

@sys.command(name = "save")
async def save(ctx):

    print("[{0}][Sub-Comando]: Save (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    guilds[str(ctx.guild.id)].write_settings()

    embed = discord.Embed(description = "❱❱❱ **Salvando...**", color = discord.Color.dark_blue())
    await ctx.send(embed = embed)
#endregion

#region Utilities
# Ajuda
@bot.command(name = "ajuda")
async def custom_help(ctx):

    print("[{0}][Comando]: Ajuda (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    embed = discord.Embed(description = "❱❱❱ **Ajuda**\n\n*Comandos:*\n\n⬩ sys off\n⬩ sys info\n⬩ ajuda\n⬩ tempo cronômetro", color = discord.Color.dark_blue())
    await ctx.send(embed = embed)

# Mede o tempo
@bot.group(name = "tempo", aliases = ("tm", "tp"))
async def time(ctx):

    print("[{0}][Comando]: Tempo (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.invoked_subcommand is None:

        embed = discord.Embed(description = "❌  **Comando inválido**\n\n*Opções possíveis:*\n⬩ cronômetro", color = discord.Color.red())
        await ctx.send(embed = embed)

@time.command(name = "cronômetro", aliases = ("cronometro", "crono", "cr"))
async def chronometer(ctx):

    print("[{0}][Sub-Comando]: Cronômetro (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if guilds[str(ctx.guild.id)].settings["Chronometer"]:

            guilds[str(ctx.guild.id)].settings["Chronometer"] = False
            delta = time_ns() - guilds[str(ctx.guild.id)].settings["Chronometer initial time"]
            guilds[str(ctx.guild.id)].settings["Chronometer initial time"] = 0
            embed = discord.Embed(description = "🕒  **Tempo marcado:**\n\n{0}".format(pygr_functions.time_format(delta)), color = discord.Color.green())
            await ctx.send(embed = embed)
        else:

            guilds[str(ctx.guild.id)].settings["Chronometer"] = True
            guilds[str(ctx.guild.id)].settings["Chronometer initial time"] = time_ns()
            embed = discord.Embed(description = "🕒  **Marcando o tempo**", color = discord.Color.dark_blue())
            await ctx.send(embed = embed)
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Modificador de canal
@bot.command(name = "canal")
async def channel_modifier(ctx, channel_arg = None):

    print("[{0}][Comando]: Canal (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if guilds[str(ctx.guild.id)].settings["Main channel ID"] is not None:

            try:
                
                id_int = int(channel_arg)
            except ValueError:

                id_int = -1

            if id_int != -1:

                found_channel = False
                print("[{0}][Sistema]: Procurando canais pelo ID".format(datetime.now()))

                for channel in guilds[str(ctx.guild.id)].guild.channels:

                    print("[{0}][Sistema]: Canal listado = {1}".format(datetime.now(), str(channel.id)))

                    if channel.id == id_int:

                        print("[{0}][Sistema]: Canal encontrado".format(datetime.now()))
                        guilds[str(ctx.guild.id)].settings["Main channel ID"] = id_int
                        found_channel = True
                        break
                
                if found_channel:

                    await ctx.send("```Canal atualizado```")
                else:

                    await ctx.send("```Canal não encontrado```")
            else:

                await ctx.send("```ID inválido```")
        else:

            await ctx.send("```Tá errado, uso correto: !canal [id]```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Utilidades do RPG
@bot.command(name = "rpg")
async def RPG_utilities(ctx, arg = None, type_arg = None, level_arg = None):

    print("[{0}][Comando]: RPG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if arg is not None:

        if arg.startswith("d"):

            result = 0
            valid_command = False

            if arg == "d4":

                result = randint(1, 4)
                valid_command = True
            elif arg == "d6":

                result = randint(1, 6)
                valid_command = True
            elif arg == "d8":

                result = randint(1, 8)
                valid_command = True
            elif arg == "d10":

                result = randint(1, 10)
                valid_command = True
            elif arg == "d12":

                result = randint(1, 12)
                valid_command = True
            elif arg == "d20":

                result = randint(1, 20)
                valid_command = True
            elif arg == "d100":

                result = randint(1, 100)
                valid_command = True
                
            if valid_command:

                await ctx.send("```Você rolou um dado {0}, resultado: {1}```".format(arg, result))
            else:

                await ctx.send("```Comando inválido pora```")  
        elif arg == "item":

            if type_arg is not None:

                if type_arg == "arma" or type_arg == "armadura" or type_arg == "objeto":

                    if level_arg is not None:

                        try:

                            level = float(level_arg)
                        except ValueError:

                            await ctx.send("```Comando inválido pora```")
                            
                        if level >= 0.0 and level <= 30.0:

                            if type_arg == "arma":

                                await ctx.send(RPGItemGenerator("weapon", level))
                            elif type_arg == "armadura":

                                await ctx.send(RPGItemGenerator("armor", level))
                            else:

                                await ctx.send(RPGItemGenerator("object", level))
                        else:

                            return ctx.send("```Comando inválido pora```")
                    else:

                        await ctx.send("```Tá errado. Uso: ~rpg item {0} [nível (0 - 30)]```".format(type_arg))
                else:

                    await ctx.send("```Tá errado. Uso: ~rpg item [tipo de item] [nível (0 - 30)]```")
            else:

                await ctx.send("```Tá errado. Uso: ~rpg item [tipo de item] [nível (0 - 30)]```")
        else:

            await ctx.send("```Tá errado. Uso: ~rpg [dado/item]```")
    else:

        await ctx.send("```Tá errado. Uso: ~rpg [dado/item]```")

# Conectar
@bot.command(name = "conectar")
async def Join(ctx):

    print("[{0}][Comando]: Conectar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if ctx.message.author.voice:

            if ctx.voice_client is None or not ctx.voice_client.is_connected():

                await ctx.send("```Entrando```")
                await ctx.author.voice.channel.connect()
            else:

                await ctx.send("```Já tô conectado```")
        else:

            await ctx.send("```Não tenho nenhum canal pra me conectar.```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

# Desconectar
@bot.command(name = "desconectar")
async def Leave(ctx):

    print("[{0}][Comando]: Desconectar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client is not None and ctx.voice_client.is_connected():

        await ctx.send("```Saindo```")
        await ctx.voice_client.disconnect()
    else:

        await ctx.send("```Não tô conectado```")

# Envia a resposta do Wolfram Alpha
@bot.command(name = "wolf")
async def Wolfram(ctx, *search):

    print("[{0}][Comando]: Wolf (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:
        
        query = " ".join(search)
        url = "https://www.wolframalpha.com/input/?i=" + urllib.parse.quote(query)

        await ctx.send(url)
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

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

            await ctx.send("```{0}```".format(RandStr(size)))
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

# Tocar
@bot.command(name = "tocar")
async def Play(ctx, audio = None):

    print("[{0}][Comando]: Tocar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client is not None and ctx.voice_client.is_connected():

        if ctx.voice_client.is_playing():

            await ctx.send("```Procurando novo áudio...```")
            ctx.voice_client.stop()
            
        if audio is not None:

            audio_files = [i for i in listdir("Audio") if isfile(join("Audio", i))]

            file_was_found = False
            for file in audio_files:

                if audio == file[:-4]:

                    file_was_found = True
                    ctx.voice_client.play(discord.FFmpegPCMAudio(source = "Audio\\{0}".format(file), executable = "C:\\Users\\ericf\\Documents\\Programas\\FFMpeg\\ffmpeg-4.3-win64-static\\bin\\ffmpeg.exe"))

                    await ctx.send("```Arquivo encontrado, tocando...```")

            if not file_was_found:

                await ctx.send("```Arquivo não encontrado```")
        else:

            await ctx.send("```Tá errado. Uso correto: ~tocar [audio]```")
    else:

        await ctx.send("```Não tô conectado```")

# Parar
@bot.command(name = "parar")
async def Stop(ctx):

    print("[{0}][Comando]: Parar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client is not None and ctx.voice_client.is_connected():

        if ctx.voice_client.is_playing():

            await ctx.send("```Parando o áudio```")
            ctx.voice_client.stop()
        else:

            await ctx.send("```Não tem nada tocando```")
    else:

        await ctx.send("```Não tô conectado```")

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

#region Loops
# Loop do sistema
@loop(seconds = 1)
async def SystemControl():

    try:

        pass
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

@SystemControl.before_loop
async def SystemControlBefore():

    try:

        print("[{0}][Sistema]: Inicializando {1} {2}".format(datetime.now(), NAME, VERSION))
        print("[{0}][Sistema]: Inicializando o RNG".format(datetime.now()))

        seed(time_ns())

        print("[{0}][Sistema]: Esperando o sistema...".format(datetime.now()))

        await bot.wait_until_ready()

        print("[{0}][Sistema]: Carregando definições dos servidores".format(datetime.now()))

        for guild in bot.guilds:

            print("[{0}][Sistema]: Servidor {1} em processamento".format(datetime.now(), guild.id))
            guilds[str(guild.id)] = (pygr_core.Guild(guild.id, bot))

        bot.is_ready = True
        print("[{0}][Sistema]: Sistema pronto".format(datetime.now()))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)
#endregion

#region Events
# Bot pronto
@bot.event
async def on_ready():

    try:

        print("[{0}][Sistema]: {1} {2} pronto para operar".format(datetime.now(), NAME, VERSION))
        print("[{0}][Sistema]: Logado como {1}, no id: {2}".format(datetime.now(), bot.user.name, bot.user.id))

        await bot.change_presence(activity = discord.Game(name = "Tua mãe na cama"))
    except Exception as error:
            
        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        bot.error_list.append(error)

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

        # Protótipo de moderação
        if message.content.startswith("-") and message.channel.id != 724437879744626748:

            await message.delete()
            await message.channel.send("```diff\n- OPA CARA, ACHA QUE ISSO AQUI É BAGUNÇA\n Use o canal \"nlogônia\" para comandos com o bot.```")

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
SystemControl.start()
bot.run(TOKEN)
sleep(0.1)