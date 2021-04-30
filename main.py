# -*- coding: utf-8 -*-

'''
Bot para Discord - 2020/06/26 - Eric Fernandes Evaristo
Projeto: Bot-Project
Bot: PyGR
'''

import sys
import asyncio

from bot_system import CustomBot
from admin_cog import AdminCog
from help_cog import HelpCog
from time_cog import TimeCog
from settings_cog import SettingsCog
from rpg_cog import RPGCog
from voice_cog import VoiceCog
from utilities_cog import UtilitiesCog
from humor_cog import HumorCog
from text_cog import TextCog
from event_cog import EventCog

# Token. Não compartilhe!
TOKEN = "NzI2MTM5MzYxMjQxODU4MTU5.XvY99A.Fh8e071wE-eqGo2tndUlAG3vuCU"

# Constantes
NAME = "PyGR"
VERSION = "4.0.3"
ADM_ID = 382542596196663296

# Corrige o erro de saída temporáriamente.
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = CustomBot(command_prefix = "~",
                help_command = None,
                name = NAME,
                version = VERSION)

# Execução do bot
bot.add_cog(AdminCog(bot, ADM_ID))
bot.add_cog(HelpCog(bot))
bot.add_cog(TimeCog(bot))
bot.add_cog(SettingsCog(bot))
bot.add_cog(RPGCog(bot))
bot.add_cog(VoiceCog(bot))
bot.add_cog(UtilitiesCog(bot))
bot.add_cog(HumorCog(bot))
bot.add_cog(TextCog(bot))
bot.add_cog(EventCog(bot))
bot.loop.create_task(bot.setup())
bot.run(TOKEN)
