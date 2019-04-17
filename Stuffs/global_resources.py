"""This module provides resources of variations for all program."""


class Var():
    """This class stores vars for the The Shell.
    """
    variations = {}


class GlobalAliases():
    """This defines global aliases dictionary.
    """
    aliases = {
        'egrep': 'egrep --color=auto',
        'fgrep': 'fgrep --color=auto',
        'grep': 'grep --color=auto',
        'l': 'ls -CF',
        'la': 'ls -A',
        'll': 'ls alF',
        'ls': 'ls --color=auto'
    }
