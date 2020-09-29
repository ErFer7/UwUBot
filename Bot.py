# Bot para Discord - 2020/06/26 - V 3.6.3 - Eric Fernandes Evaristo
# Projeto: Bot-Project
# Bot: PyGR

# Bibliotecas
import asyncio
import discord
import urllib.parse

from random import randint, choice, seed
from datetime import datetime, timedelta
from re import compile, IGNORECASE
from os import listdir
from os.path import isfile, join
from string import ascii_lowercase
from discord.ext import commands
from discord.ext.tasks import loop

# Token. Não compartilhe!
TOKEN = "NzI2MTM5MzYxMjQxODU4MTU5.XvY99A.Fh8e071wE-eqGo2tndUlAG3vuCU"

# Variáveis globais
version = "3.6.3"
errorCount = 0
sentErrorCount = 0
errorList = []
isReady = False
connectedByUser = False

initialTime: datetime
mainGuild: discord.guild
mainChannel: discord.channel

# Configurações padrão (Essas configurações são carregadas dos arquivos quando existirem)
markingTime = False
allowIndepentInteractions = True
mainBotChannelID = 724437879744626748
tts = True
admID = 382542596196663296

# region Functions
def findWholeWord(word):

    return compile(r'\b({0})\b'.format(word), flags = IGNORECASE).search

def RandStr(length: int):

    letters = ascii_lowercase
    return "".join(choice(letters) for i in range(length))

def IsMemberOnline(member):

    return str(member.status) == "online" and member != bot.user and not member.bot

def Interact(message: discord.message):

    if findWholeWord("tu é")(message.content.lower()):

        if findWholeWord("gay")(message.content.lower()):

            return message.channel.send("Não. Sou apenas uma máquina. UMA MÁQUINA DE SEXO.", tts = tts)
        elif findWholeWord("corno")(message.content.lower()):

            return message.channel.send("Um bot sem chifre é um bot indefeso.", tts = tts)
        elif findWholeWord("comunista")(message.content.lower()):

            return message.channel.send("Obviamente que sim.", tts = tts)
        else:
            rng = randint(0, 3)

            if rng == 0:

                return message.channel.send("Teu pai aquele arrombado.", tts = tts)
            elif rng == 1:

                return message.channel.send("Sim.", tts = tts)
            elif rng == 2:

                return message.channel.send("Não.", tts = tts)
            else:

                return message.channel.send("Não, mas tu é.", tts = tts)
    elif findWholeWord("quem é")(message.content.lower()):

        rng = randint(0, 3)

        if rng == 0:

            return message.channel.send("É uma grande pessoa", tts = tts)
        elif rng == 1:

            return message.channel.send("É o maior boiola de todos os tempos", tts = tts)
        elif rng == 2:

            return message.channel.send("É um grande amigo meu.", tts = tts)
        else:

            return message.channel.send("Olha, se eu visse esse cara na rua eu deitava no soco.", tts = tts)
    elif findWholeWord("quando foi")(message.content.lower()):

        return message.channel.send("Foi no ano {0}".format(randint(1000, 2019)), tts = tts)
    elif findWholeWord("quando vai ser")(message.content.lower()):

        return message.channel.send("Vai ser em {0}".format(randint(2020, 3000)), tts = tts)
    elif findWholeWord("concorda")(message.content.lower()):

        rng = randint(0, 4)

        if rng == 0:

            return message.channel.send("Concordo muito.", tts = tts)
        elif rng == 1:

            return message.channel.send("Concordo.", tts = tts)
        elif rng == 2:

            return message.channel.send("Não sei bem na verdade.", tts = tts)
        elif rng == 3:

            return message.channel.send("Discordo.", tts = tts)
        else:

            return message.channel.send("Discordo muito.", tts = tts)

def SendMessage(messageContext: int):

    greetings_TI = ["Olá", "Oi", "Opa", "Alô", "Saudações"]
    greetings_TD = ["Bom dia", "Boa tarde", "Boa noite"]
    adjectives = ["meu amigo", "safada", "gostosa", "meu consagrado", "corno", "gata", "comunista", "caminhoneiro"]

    # Contextos:
    # 0: Saudações
    # 1: Frases aleatórias

    if messageContext == 0:

        if randint(0, 1) == 0:

            hour = datetime.now().hour

            if hour >= 6 and hour < 12:

                return greetings_TD[0] + " " + choice(adjectives)
            elif hour >= 12 and hour < 18:

                return greetings_TD[1] + " " + choice(adjectives)
            else:

                return greetings_TD[2] + " " + choice(adjectives)
        else:
            
            return choice(greetings_TI) + " " + choice(adjectives)
    elif messageContext == 1:

        quotesFile = open("Text\\quotes.txt", "r", encoding = "utf-8")
        quotesLines = quotesFile.readlines()
        quotes = []
        for i in range(len(quotesLines) - 1):

            unprocLine = quotesLines[i]
            charCount = len(unprocLine)
            procLine = unprocLine[:charCount - 1]
            quotes.append(procLine)
        quotes.append(quotesLines[i + 1])
        output = choice(quotes)
        quotesFile.close()

        return output

def SendImage(channel: discord.channel):
    
    images = [i for i in listdir("Images") if isfile(join("Images", i))]
    return channel.send(file = discord.File("Images\\" + choice(images)))

def ManageSettings(mode: str):

    global errorCount
    global markingTime
    global allowIndepentInteractions
    global initialTime
    global mainBotChannelID
    global tts
    global errorList

    if mode == "r":

        with open("System\\Settings.set","r") as settingsFile: 
            
            settings = settingsFile.readlines()

        for line in settings:

            if line.startswith("MT"):

                markingTime = bool(int(line.split()[1]))
            elif line.startswith("AII"):

                allowIndepentInteractions = bool(int(line.split()[1]))
            elif line.startswith("IT"):

                date = line.split()[1] + " " + line.split()[2]
                initialTime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            elif line.startswith("MBC_ID"):

                mainBotChannelID = int(line.split()[1])
            elif line.startswith("TTS"):

                tts = bool(int(line.split()[1]))
        
        print("[{0}][Sistema]: Configurações lidas".format(datetime.now()))
    elif mode == "w":

        settings = ["2515\n", "MT " + str(int(markingTime)) + "\n",                        \
                    "AII " + str(int(allowIndepentInteractions)) + "\n",                   \
                    "IT " + str(initialTime) + "\n",                                  \
                    "MBC_ID " + str(mainBotChannelID) + "\n", "TTS " + str(int(tts)) + "\n"]
            
        with open("System\\Settings.set","w") as settingsFile: 
            
            settingsFile.writelines(settings)
        
        print("[{0}][Sistema]: Configurações escritas".format(datetime.now()))
    elif mode == "c":

        try:

            with open("System\\Settings.set","r") as settingsFile: 
                
                string = settingsFile.read(4)
                if int(string) == 2515:

                    print("[{0}][Sistema]: Arquivo de configurações válido".format(datetime.now()))
                    return True
                else:

                    print("[{0}][Sistema]: Arquivo de configurações inválido".format(datetime.now()))
                    return False
        except Exception as error:

            print("[{0}][Erro]: Erro ao tentar abrir o arquivo de configurações: {1}".format(datetime, error))
            errorCount += 1
            errorList.append(error)
            return False         

def RPGItemGenerator(type: str, level: float):

    itemLevel = ""
    rng = randint(1, 100)

    if level <= 1:

        if rng == 100:
            
            itemLevel = "II"
        elif rng >= 98 and rng < 100:

            itemLevel = "I-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "I-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "I++"
        elif rng >= 70 and rng < 86:

            itemLevel = "I+"
        else:

            itemLevel = "I"
    elif level <= 3:

        if rng == 100:

            itemLevel = "III"
        elif rng >= 98 and rng < 100:

            itemLevel = "II-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "II-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "II++"
        elif rng >= 70 and rng < 86:

            itemLevel = "II+"
        else:

            itemLevel = "II"
    elif level <= 6:

        if rng == 100:

            itemLevel = "IV"
        elif rng >= 98 and rng < 100:

            itemLevel = "III-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "III-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "III++"
        elif rng >= 70 and rng < 86:

            itemLevel = "III+"
        else:

            itemLevel = "III"
    elif level <= 9:

        if rng == 100:

            itemLevel = "V"
        elif rng >= 98 and rng < 100:

            itemLevel = "IV-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "IV-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "IV++"
        elif rng >= 70 and rng < 86:

            itemLevel = "IV+"
        else:

            itemLevel = "IV"
    elif level <= 12:

        if rng == 100:

            itemLevel = "VI"
        elif rng >= 98 and rng < 100:

            itemLevel = "V-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "V-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "V++"
        elif rng >= 70 and rng < 86:

            itemLevel = "V+"
        else:

            itemLevel = "V"
    elif level <= 15:

        if rng == 100:

            itemLevel = "VII"
        elif rng >= 98 and rng < 100:

            itemLevel = "VI-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "VI-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "VI++"
        elif rng >= 70 and rng < 86:

            itemLevel = "VI+"
        else:

            itemLevel = "VI"
    elif level <= 18:

        if rng == 100:

            itemLevel = "VIII"
        elif rng >= 98 and rng < 100:

            itemLevel = "VII-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "VII-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "VII++"
        elif rng >= 70 and rng < 86:

            itemLevel = "VII+"
        else:

            itemLevel = "VII"
    elif level <= 21:

        if rng == 100:

            itemLevel = "IX"
        elif rng >= 98 and rng < 100:

            itemLevel = "VIII-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "VIII-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "VIII++"
        elif rng >= 70 and rng < 86:

            itemLevel = "VIII+"
        else:

            itemLevel = "VIII"
    elif level <= 24:

        if rng == 100:

            itemLevel = "X"
        elif rng >= 98 and rng < 100:

            itemLevel = "IX-L"
        elif rng >= 94 and rng < 98:

            itemLevel = "IX-S"
        elif rng >= 86 and rng < 94:

            itemLevel = "IX++"
        elif rng >= 70 and rng < 86:

            itemLevel = "IX+"
        else:

            itemLevel = "IX"
    elif level <= 27:

        if rng == 100:

            itemLevel = "X-L"
        elif rng >= 94 and rng < 100:

            itemLevel = "X-S"
        elif rng >= 78 and rng < 94:

            itemLevel = "X++"
        elif rng >= 46 and rng < 78:

            itemLevel = "X+"
        else:

            itemLevel = "X"
    else:

        if rng >= 50:

            itemLevel = "X-L"
        else:

            itemLevel = "X-S"

    if type == "weapon":

        with open("Text\\RPG_Weapons.txt", "r", encoding = "utf-8") as weaponsFile:

            weapons = weaponsFile.readlines()
                        
        item = choice(weapons).split("#")
    elif type == "armor":

        with open("Text\\RPG_Armors.txt", "r", encoding = "utf-8") as armorsFile:

            armors = armorsFile.readlines()

        getArmors = False
        armorsList = []

        for line in armors:

            if getArmors and not line.startswith("@"):

                armorsList.append(line)
            
            if line.startswith("@"):

                if line[1:].strip() == itemLevel:

                    getArmors = True
                else:

                    getArmors = False

        item = choice(armorsList).split("#")
    else:

        with open("Text\\RPG_Objects.txt", "r", encoding = "utf-8") as objectsFile:

            objects = objectsFile.readlines()
        
        getObjects = False
        objectsList = []

        for line in objects:

            if getObjects and not line.startswith("@"):

                objectsList.append(line)
            
            if line.startswith("@"):

                if line[1:].strip() == itemLevel:

                    getObjects = True
                else:

                    getObjects = False

        item = choice(objectsList).split("#")

    itemName = item[0]
    itemBaseDamage = item[1]
    itemDamageType = item[2]
    itemBasePrice = item[3]
    itemDescription = item[4]

    if type == "weapon":

        with open("Text\\RPG_WeaponsSpecials.txt", "r", encoding = "utf-8") as levelsFile:

            levels = levelsFile.readlines()
    
        getModifiers = False
        modifiersList = []

        for line in levels:

            if getModifiers and not line.startswith("@"):

                modifiersList.append(line)
            
            if line.startswith("@"):

                if line[1:].strip() == itemLevel:

                    getModifiers = True
                else:

                    getModifiers = False

        modifier = choice(modifiersList).split("#")

        itemName += modifier[0]
        itemSpecial = modifier[1]
        itemPrice = int(float(itemBasePrice) * float(modifier[2]))
        itemDamage = str(int(itemBaseDamage[0]) + int(modifier[3])) + itemBaseDamage[1:]
    else:

        itemDamage = itemBaseDamage
        itemPrice = int(float(itemBasePrice))
        itemSpecial = item[5]

    return "```Item: {0}\nDano: {1} {2}\nPreço: {3}\nNível: {4}\nEspecial: {5}\nDescrição: {6}```".format(itemName, itemDamage, itemDamageType, itemPrice, itemLevel, itemSpecial, itemDescription)
#endregion

bot = commands.Bot(command_prefix = "~", help_command = None)

#region Commands
#region System Commands
# Desliga
@bot.command(name = "off")
async def Shutdown(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Off (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if ctx.message.author.id == admID:
            
            await ctx.send("```Até o outro dia```")

            print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
            ManageSettings("w")

            print("[{0}][Sistema]: Erros ({1}) = {2}".format(datetime.now(), errorCount, errorList))
            print("[{0}][Sistema]: Salvando e encerrando".format(datetime.now()))

            await bot.close()
        else:

            await ctx.send("```Tá querendo me desligar é?```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Repete a mensagem em um canal
@bot.command(name = "say")
async def Say(ctx, channelID, *msg):

    global errorCount
    global errorList

    print("[{0}][Comando]: Say (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if ctx.message.author.id == admID:
            
            channel = bot.get_channel(int(channelID))

            if channel != None:

                message = " ".join(msg)
                await channel.send(message)
            else:

                await ctx.send("```Canal não encontrado```")
        else:

            await ctx.send("```Você não tem permissão para usar este comando```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Informações
@bot.command(name = "info")
async def Info(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Info (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        await ctx.send("```GFBot {0} - Criado em 26/06/2020\nMarcando tempo = {1}\nInterações = {2}\nCanal principal (ID) = {3}\nTTS = {4}\nConectado pelo usuário = {5}\nErros = {6}```".format(version, markingTime, allowIndepentInteractions, mainBotChannelID, tts, connectedByUser, errorCount))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Cria um erro propositalmente
@bot.command(name = "error")
async def RaiseError(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: ERRO (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        await ctx.send("```Criando erro```")
        raise Exception("Este erro é proposital e pode ser ignorado")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)
#endregion

#region Utilities
# Ajuda
@bot.command(name = "ajuda")
async def CustomHelp(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Ajuda (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        with open("Text\\help.txt", "r", encoding = "utf-8") as helpFile:
            helpStr = helpFile.read()
        
        await ctx.send(helpStr)
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Mede o tempo
@bot.command(name = "tempo")
async def Time(ctx):

    global errorCount
    global errorList
    global markingTime
    global initialTime

    print("[{0}][Comando]: Tempo (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if markingTime:

            markingTime = False
            delta = datetime.now() - initialTime
            await ctx.send("```Tempo marcado: " + str(delta) + "```")
        else:

            markingTime = True
            initialTime = datetime.now()
            print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
            ManageSettings("w")
            await ctx.send("```Marcando o tempo```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)
    
# Switch de interação
@bot.command(name = "interação")
async def InteractionSwitch(ctx):

    global errorCount
    global errorList
    global allowIndepentInteractions

    try:

        if allowIndepentInteractions:

            print("[{0}][Comando]: Interação (desativação) (Autor: {1})".format(datetime.now(), ctx.message.author.name))
            allowIndepentInteractions = False
            print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
            ManageSettings("w")
            await ctx.send("```Interação: Desligada.```")
        else:

            print("[{0}][Comando]: Interação (desativação) (Autor: {1})".format(datetime.now(), ctx.message.author.name))
            allowIndepentInteractions = True
            print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
            ManageSettings("w")
            await ctx.send("```Interação: Ligada.```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Modificador de canal
@bot.command(name = "canal")
async def ChannelModifier(ctx, channelArg = None):

    global errorCount
    global errorList
    global mainBotChannelID

    print("[{0}][Comando]: Canal (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if channelArg != None:

            try:

                idInt = int(channelArg)
            except:

                idInt = -1

            if idInt != -1:

                foundChannel = False
                print("[{0}][Sistema]: Procurando canais pelo ID".format(datetime.now()))

                for c in bot.guilds[0].channels:

                    print("[{0}][Sistema]: Canal listado = {1}".format(datetime.now(), str(c.id)))

                    if c.id == idInt:

                        print("[{0}][Sistema]: Canal encontrado".format(datetime.now()))
                        mainBotChannelID = idInt
                        print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
                        ManageSettings("w")
                        foundChannel = True
                        break
                
                if foundChannel:

                    await ctx.send("```Canal atualizado```")
                else:

                    await ctx.send("```Canal não encontrado```")
            else:

                await ctx.send("```ID inválido```")
        else:

            await ctx.send("```Tá errado, uso correto: !canal [id]```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Switch do TTS
@bot.command(name = "tts")
async def TTSSwitch(ctx):

    global tts

    if tts:

        print("[{0}][Comando]: TTS (desativar) (Autor: {1})".format(datetime.now(), ctx.message.author.name))

        tts = False
        print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
        ManageSettings("w")
        await ctx.send("```TTS desativado```")
    else:

        print("[{0}][Comando]: TTS (ativar) (Autor: {1})".format(datetime.now(), ctx.message.author.name))

        tts = True
        print("[{0}][Sistema]: Escrevendo configurações".format(datetime.now()))
        ManageSettings("w")
        await ctx.send("```TTS ativado```")

# Utilidades do RPG
@bot.command(name = "rpg")
async def RPGUtilities(ctx, arg = None, typeArg = None, levelArg = None):

    print("[{0}][Comando]: RPG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if arg != None:

        if arg.startswith("d"):

            result = 0
            validCommand = False

            if arg == "d4":

                result = randint(1, 4)
                validCommand = True
            elif arg == "d6":

                result = randint(1, 6)
                validCommand = True
            elif arg == "d8":

                result = randint(1, 8)
                validCommand = True
            elif arg == "d10":

                result = randint(1, 10)
                validCommand = True
            elif arg == "d12":

                result = randint(1, 12)
                validCommand = True
            elif arg == "d20":

                result = randint(1, 20)
                validCommand = True
            elif arg == "d100":

                result = randint(1, 100)
                validCommand = True
                
            if validCommand:

                await ctx.send("```Você rolou um dado {0}, resultado: {1}```".format(arg, result))
            else:

                await ctx.send("```Comando inválido pora```")  
        elif arg == "item":

            if typeArg != None:

                if typeArg == "arma" or typeArg == "armadura" or typeArg == "objeto":

                    if levelArg != None:

                        try:

                            level = float(levelArg)
                        except:

                            await ctx.send("```Comando inválido pora```")
                            
                        if level >= 0.0 and level <= 30.0:

                            if typeArg == "arma":

                                await ctx.send(RPGItemGenerator("weapon", level))
                            elif typeArg == "armadura":

                                await ctx.send(RPGItemGenerator("armor", level))
                            else:

                                await ctx.send(RPGItemGenerator("object", level))
                        else:

                            return ctx.send("```Comando inválido pora```")
                    else:

                        await ctx.send("```Tá errado. Uso: ~rpg item {0} [nível (0 - 30)]```".format(typeArg))
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

    global errorCount
    global errorList
    global connectedByUser

    print("[{0}][Comando]: Conectar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if ctx.message.author.voice:

            if ctx.voice_client == None or not ctx.voice_client.is_connected():

                await ctx.send("```Entrando```")
                connectedByUser = True
                await ctx.author.voice.channel.connect()
            else:

                await ctx.send("```Já tô conectado```")
        else:

            await ctx.send("```Não tenho nenhum canal pra me conectar.```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Desconectar
@bot.command(name = "desconectar")
async def Leave(ctx):

    global connectedByUser

    print("[{0}][Comando]: Desconectar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client != None and ctx.voice_client.is_connected():

        await ctx.send("```Saindo```")
        connectedByUser = False
        await ctx.voice_client.disconnect()
    else:

        await ctx.send("```Não tô conectado```")

# Envia a resposta do Wolfram Alpha
@bot.command(name = "wolf")
async def Wolfram(ctx, *search):

    global errorCount
    global errorList

    print("[{0}][Comando]: Wolf (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:
        
        query = " ".join(search)
        url = "https://www.wolframalpha.com/input/?i=" + urllib.parse.quote(query)

        await ctx.send(url)
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Gera um número aleatório
@bot.command(name = "rng")
async def RandomNumber(ctx, minStr = None, maxStr = None):

    global errorCount
    global errorList

    print("[{0}][Comando]: RNG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:
        
        inputIsValid = False
        min = 0
        max = 0

        try:

            min = int(minStr)
            max = int(maxStr)

            if min <= max:
            
                inputIsValid = True
            else:

                raise ValueError
        except:

            await ctx.send("```Input inválido```")

        if inputIsValid:

            await ctx.send("```{0}```".format(randint(min, max)))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Gera um string aleatório
@bot.command(name = "rsg")
async def RandomString(ctx, sizeStr = None):

    global errorCount
    global errorList

    print("[{0}][Comando]: RSG (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:
        
        inputIsValid = False
        size = 0

        try:

            size = int(sizeStr)

            if size <= 1994:

                inputIsValid = True
            else:

                raise ValueError
        except:

            await ctx.send("```Input inválido```")

        if inputIsValid:

            await ctx.send("```{0}```".format(RandStr(size)))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Exibe os dados de um usuário
@bot.command(name = "usuário")
async def UserInfo(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Usuário (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        user: discord.user
        joinedAt = ""

        if len(ctx.message.mentions) == 0:

            user = ctx.message.author
            joinedAt = str(mainGuild.get_member(ctx.message.author.id).joined_at)
        else:

            user = bot.get_user(ctx.message.mentions[0].id)
            joinedAt = str(mainGuild.get_member(ctx.message.mentions[0].id).joined_at)

        if user != None:

            await ctx.send("```Estas são as informações para: {0}\nId: {1}\nDiscriminador: {2}\nBot: {3}\nSistema: {4}\nEntrou no servidor em: {5}```".format(user.name, user.id, user.discriminator, user.bot, user.system, joinedAt))
            await ctx.send(user.avatar_url)
        else:

            await ctx.send("```O usuário não foi encontrado```")

    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Transforma um string em emojis
@bot.command(name = "emoji")
async def Emojify(ctx, *str):

    global errorCount
    global errorList

    print("[{0}][Comando]: Emojificar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        message = " ".join(str).lower()
        emojifiedMessage = ""

        for c in message:

            if c == " ":

                emojifiedMessage += "   "
            elif c == "0":

                emojifiedMessage += " :zero:"
            elif c == "1":

                emojifiedMessage += " :one:"
            elif c == "2":

                emojifiedMessage += " :two:"
            elif c =="3":

                emojifiedMessage += " :three:"
            elif c == "4":

                emojifiedMessage += " :four:"
            elif c == "5":

                emojifiedMessage += " :five:"
            elif c == "6":

                emojifiedMessage += " :six:"
            elif c == "7":

                emojifiedMessage += " :seven:"
            elif c == "8":

                emojifiedMessage += " :seven:"
            elif c == "9":

                emojifiedMessage += " :seven:"
            elif c in ascii_lowercase:

                emojifiedMessage += " :regional_indicator_{0}:".format(c)
        
        if len(emojifiedMessage) <= 2000:

            await ctx.send(emojifiedMessage)
        else:

            await ctx.send("```A mensagem é muito grande!```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)
#endregion

#region Humor
# Medidor de corno
@bot.command(name = "crono")
async def CuckLevel(ctx):

    print("[{0}][Comando]: Crono (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if len(ctx.message.mentions) == 0:
        
        await ctx.send("{0} é {1}\\% crono".format(ctx.message.author.mention, randint(0, 100)), tts = tts)
    else:

        await ctx.send("{0} é {1}\\% crono".format(ctx.message.mentions[0].mention, randint(0, 100)), tts = tts)

# Medidor de corno fake
@bot.command(name = "corno")
async def FakeCuckLevel(ctx):

    print("[{0}][Comando]: Corno (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if len(ctx.message.mentions) == 0:
        
        await ctx.send("{0} é 100\\% corno".format(ctx.message.author.mention), tts = tts)
    else:

        await ctx.send("{0} é 100\\% corno".format(ctx.message.mentions[0].mention), tts = tts)

# Salva imagens
@bot.command(name = "salvar")
async def SaveImage(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Salvar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        if len(ctx.message.attachments) > 0:

            extension = ctx.message.attachments[0].filename[-3:]
            if extension == "png" or extension == "jpg" or extension == "gif":
                    
                await ctx.message.attachments[0].save("Images\\{0}.{1}".format(RandStr(8), extension))
            else:

                await ctx.send("```Formato não suportado```")
        else:

            await ctx.send("```Não há nenhum arquivo```")
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Enviar imagem
@bot.command(name = "imagem")
async def GetImage(ctx):

    global errorCount
    global errorList

    print("[{0}][Comando]: Imagem (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    try:

        await SendImage(ctx.channel)
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Análise da partida
@bot.command(name = "valorant")
async def ValorantAnalysis(ctx):

    print("[{0}][Comando]: Valorant (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    teamA = 0
    teamB = 0

    if randint(0, 1) == 0:

        teamA = 13
    else:

        teamB = 13

    if teamA == 13:

        teamB = randint(0, 12)
    else:

        teamA = randint(0, 12)
    
    await ctx.send("```Resultado: {0} a {1}```".format(teamA, teamB))

# Tocar
@bot.command(name = "tocar")
async def Play(ctx, audio = None):

    print("[{0}][Comando]: Tocar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client != None and ctx.voice_client.is_connected():

        if ctx.voice_client.is_playing():

            await ctx.send("```Procurando novo áudio...```")
            ctx.voice_client.stop()
            
        if audio != None:

            audioFiles = [i for i in listdir("Audio") if isfile(join("Audio", i))]

            fileWasFound = False
            for file in audioFiles:

                if audio == file[:-4]:

                    fileWasFound = True
                    ctx.voice_client.play(discord.FFmpegPCMAudio(source = "Audio\\{0}".format(file), executable = "C:\\Users\\ericf\\Documents\\Programas\\FFMpeg\\ffmpeg-4.3-win64-static\\bin\\ffmpeg.exe"))

                    await ctx.send("```Arquivo encontrado, tocando...```")

            if not fileWasFound:

                await ctx.send("```Arquivo não encontrado```")
        else:

            await ctx.send("```Tá errado. Uso correto: ~tocar [audio]```")
    else:

        await ctx.send("```Não tô conectado```")

# Parar
@bot.command(name = "parar")
async def Stop(ctx):

    print("[{0}][Comando]: Parar (Autor: {1})".format(datetime.now(), ctx.message.author.name))

    if ctx.voice_client != None and ctx.voice_client.is_connected():

        if ctx.voice_client.is_playing():

            await ctx.send("```Parando o áudio```")
            ctx.voice_client.stop()
        else:

            await ctx.send("```Não tem nada tocando```")
    else:

        await ctx.send("```Não tô conectado```")
#endregion
#endregion

#region Loops
# Loop do sistema
@loop(seconds = 1)
async def SystemControl():

    global mainChannel
    global errorCount
    global sentErrorCount

    try:

        # Atualiza o canal
        if mainChannel != None:

            if mainChannel.id != mainBotChannelID:

                print("[{0}][Sistema]: Mudança de canal detectada, atualizando...".format(datetime.now()))
                mainChannel = bot.get_channel(mainBotChannelID)
        else:

            print("[{0}][Aviso]: O canal principal é nulo, definindo o canal principal pelo ID padrão".format(datetime.now()))
            mainChannel = bot.get_channel(mainBotChannelID)

        # Checa estabilidade do sistema
        if errorCount > sentErrorCount:

            sentErrorCount += 1

            if mainChannel == None and (mainBotChannelID != None and mainBotChannelID != 0):

                mainChannel = bot.get_channel(mainBotChannelID)

            await mainChannel.send("```diff\n- Instabilidade detectada no sistema! Erros = {0}\n- Os seguintes erros aconteceram: {1}```".format(errorCount, errorList))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

@SystemControl.before_loop
async def SystemControlBefore():

    global mainGuild
    global errorCount
    global mainChannel
    global isReady

    try:

        print("[{0}][Inicialização]: Inicializando PyGR {1}".format(datetime.now(), version))
        print("[{0}][Inicialização]: Inicializando o RNG".format(datetime.now()))

        seed(datetime.now())

        print("[{0}][Inicialização]: Checando configurações".format(datetime.now()))
        if ManageSettings("c"):

            print("[{0}][Inicialização]: Lendo configurações".format(datetime.now()))
            ManageSettings("r")
        else:
            
            print("[{0}][Inicialização]: Escrevendo configurações".format(datetime.now()))
            ManageSettings("w")

        await bot.wait_until_ready()

        # server
        mainGuild = bot.guilds[0]

        # Canal de interação
        mainChannel = bot.get_channel(mainBotChannelID)

        isReady = True
        print("[{0}][Inicialização]: Sistema interno pronto".format(datetime.now()))
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Loop de consciência
@loop(seconds = 10)
async def Conscience():

    global mainChannel
    global errorCount
    global errorList
    global connectedByUser

    try:

        if isReady:
            
            # Atividades
            if allowIndepentInteractions:
                
                for voice_channel in mainGuild.voice_channels:

                    if len(voice_channel.members) == 1:

                        if bot.user not in voice_channel.members:

                            if randint(1, 1000) == 1000:

                                connectedByUser = False
                                await voice_channel.connect()
                        elif bot.user in voice_channel.members and not connectedByUser:
                            
                            for voiceClient in bot.voice_clients:

                                if voiceClient.channel == voice_channel:

                                    await voiceClient.disconnect()
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)
#endregion

#region Events
# Bot pronto
@bot.event
async def on_ready():

    global errorCount
    global errorList

    try:

        print("[{0}][Sistema]: GFBot {1} pronto para operar".format(datetime.now(), version))
        print("[{0}][Sistema]: Logado como {1}, no id: {2}".format(datetime.now(), bot.user.name, bot.user.id))
        print("[{0}][Sistema]: Servers conectados: {1}".format(datetime.now(), bot.guilds))

        await bot.change_presence(activity = discord.Game(name = "Palhoça: Alcides Simulator"))
    except Exception as error:
            
        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

# Mensagem recebida
@bot.event
async def on_message(message):

    global errorCount
    global errorList

    try:
        
        print("[{0}][Mensagem]: [{1}] de [{2}] no canal [{3}]".format(datetime.now(), message.content, message.author.name, message.channel))

        # Inibe leitura das próprias mensagens
        if message.author == bot.user:
            return
        
        # Comandos
        await bot.process_commands(message)

        if bot.user.mentioned_in(message):

            print("[{0}][Mensagem]: Bot Mencionado".format(datetime.now()))

            awnser = Interact(message)

            if awnser != None:

                await awnser
    except Exception as error:

        print("[{0}][Erro]: {1}".format(datetime.now(), error))
        errorCount += 1
        errorList.append(error)

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

# Algum usuário está escrevendo
@bot.event
async def on_typing(channel, user, when):

    print("[{0}][Sistema]: [{1}] escrevendo no canal [{2}]".format(datetime.now(), user.name, channel.name))
#endregion

# Execução do bot
SystemControl.start()
Conscience.start()
bot.run(TOKEN)