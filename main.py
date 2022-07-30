# -*- coding: utf-8 -*-

'''
Bot para Discord - 2020-06-26 - Eric Fernandes Evaristo
Projeto: Bot-Project
Bot: OwOBot

 ██████╗ ██╗    ██╗ ██████╗
██╔═══██╗██║    ██║██╔═══██╗
██║   ██║██║ █╗ ██║██║   ██║
██║   ██║██║███╗██║██║   ██║
╚██████╔╝╚███╔███╔╝╚██████╔╝
 ╚═════╝  ╚══╝╚══╝  ╚═════╝
'''

import sys
import asyncio

from source.bot_system import CustomBot
from source.admin_cog import AdminCog
from source.help_cog import HelpCog
from source.time_cog import TimeCog
from source.settings_cog import SettingsCog
from source.rpg_cog import RPGCog
from source.voice_cog import VoiceCog
from source.utilities_cog import UtilitiesCog
from source.humour_cog import HumorCog
from source.text_cog import TextCog
from source.event_cog import EventCog

# Constantes
NAME = "OwOBot"
VERSION = "5.0-dev"

# Corrige o erro de saída temporáriamente.
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = CustomBot(command_prefix="~",
                help_command=None,
                name=NAME,
                version=VERSION)

# Execução do bot
bot.add_cog(AdminCog(bot))
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
bot.run(bot.token)
