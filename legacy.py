# -*- coding: utf-8 -*-

'''
Código que precisa ser descartado
'''

from random import randint

from bot_functions import find_word


def interact(string: str):
    '''
    Interage. Esta função precisa ser retrabalhada.
    '''

    if find_word("tu é", string):

        if find_word("gay", string):

            return "Não. Sou apenas uma máquina. UMA MÁQUINA DE SEXO."
        elif find_word("corno", string):

            return "Um bot sem chifre é um bot indefeso."
        elif find_word("comunista", string):

            return "Obviamente que sim."
        else:
            rng = randint(0, 3)

            if rng == 0:

                return "Teu pai aquele arrombado."
            elif rng == 1:

                return "Sim."
            elif rng == 2:

                return "Não."
            else:

                return "Não, mas tu é."
    elif find_word("quem é", string):

        rng = randint(0, 3)

        if rng == 0:

            return "É uma grande pessoa"
        elif rng == 1:

            return "É o maior boiola de todos os tempos"
        elif rng == 2:

            return "É um grande amigo meu."
        else:

            return "Olha, se eu visse esse cara na rua eu deitava no soco."
    elif find_word("concorda", string):

        rng = randint(0, 4)

        if rng == 0:

            return "Concordo muito."
        elif rng == 1:

            return "Concordo."
        elif rng == 2:

            return "Não sei bem na verdade."
        elif rng == 3:

            return "Discordo."
        else:

            return "Discordo muito."
