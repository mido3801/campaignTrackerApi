from enum import Enum


class Classes(str, Enum):
    """
    Class names
    """
    ROGUE = 'rogue'
    PALADIN = 'paladin'
    FIGHTER = 'fighter'
    WARLOCK = 'warlock'
    DRUID = 'druid'
    SORCERER = 'sorcerer'
    WIZARD = 'wizard'
    RANGER = 'ranger'
    ARTIFICER = 'artificer'
    CLERIC = 'cleric'
    BLOOD_HUNTER = 'blood hunter'
    BARBARIAN = 'barbarian'


class Races(str, Enum):
    """
    Races
    """
    HUMAN = 'human'
    DWARF = 'dwarf'
    GNOME = 'gnome'
    ELF = 'elf'
    ORC = 'orc'
