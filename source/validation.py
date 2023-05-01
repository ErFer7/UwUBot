# -*- coding: utf-8 -*-

'''
Módulo para a validação personalizada.
'''

import re
from enum import Enum

from discpybotframe.validation import Validator, ArgumentFormat, ArgumentType


class CustomArgumentType(Enum):

    '''
    Tipo de argumento personalizado.
    '''

    DICE = 1


class CustomArgumentFormat(ArgumentFormat):

    '''
    Formato de argumento personalizado.
    '''

    def validate(self, arg: str) -> bool:

        if self._type == CustomArgumentType.DICE:
            pattern = re.compile(r'^[0-9]*d(4|6|8|10|12|20|100)$', re.IGNORECASE)
            if not pattern.match(arg):
                return False

        return super().validate(arg)
