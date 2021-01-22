# -*- coding: utf-8 -*-

import discord
from utility_functions import FindWholeWord
from random import randint

'''
Código não utilizado
'''

def Interact(message: discord.message):

    if FindWholeWord("tu é")(message.content.lower()):

        if FindWholeWord("gay")(message.content.lower()):

            return message.channel.send("Não. Sou apenas uma máquina. UMA MÁQUINA DE SEXO.")
        elif FindWholeWord("corno")(message.content.lower()):

            return message.channel.send("Um bot sem chifre é um bot indefeso.")
        elif FindWholeWord("comunista")(message.content.lower()):

            return message.channel.send("Obviamente que sim.")
        else:
            rng = randint(0, 3)

            if rng == 0:

                return message.channel.send("Teu pai aquele arrombado.")
            elif rng == 1:

                return message.channel.send("Sim.")
            elif rng == 2:

                return message.channel.send("Não.")
            else:

                return message.channel.send("Não, mas tu é.")
    elif FindWholeWord("quem é")(message.content.lower()):

        rng = randint(0, 3)

        if rng == 0:

            return message.channel.send("É uma grande pessoa")
        elif rng == 1:

            return message.channel.send("É o maior boiola de todos os tempos")
        elif rng == 2:

            return message.channel.send("É um grande amigo meu.")
        else:

            return message.channel.send("Olha, se eu visse esse cara na rua eu deitava no soco.")
    elif FindWholeWord("concorda")(message.content.lower()):

        rng = randint(0, 4)

        if rng == 0:

            return message.channel.send("Concordo muito.")
        elif rng == 1:

            return message.channel.send("Concordo.")
        elif rng == 2:

            return message.channel.send("Não sei bem na verdade.")
        elif rng == 3:

            return message.channel.send("Discordo.")
        else:

            return message.channel.send("Discordo muito.")