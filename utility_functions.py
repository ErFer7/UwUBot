# -*- coding: utf-8 -*-

'''
Funções para utilidades
'''

from re import compile, IGNORECASE # (!) Checar a redefinição de compile
from string import ascii_lowercase
from random import randint, choice

def FindWholeWord(word):

    """ Encontra o string caso ele seja uma palavra entre espaços
    """

    return compile(r'\b({0})\b'.format(word), flags = IGNORECASE).search

def RandStr(length: int):

    """ Gera um string aleatório dentro do comprimento definido
    """

    letters = ascii_lowercase
    return "".join(choice(letters) for i in range(length))

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