"""This module provides resources of variations for all program."""

from string import ascii_lowercase, ascii_uppercase
from os import getpid


class Vars():
    """This class stores vars for the The Shell.
    """
    variations = {
        "?": "0",
        "$": str(getpid()),
        "a": "hello",
        "_": ""
    }

    def get_var(key):
        """
        get_var(key)    ->  value.

        This module retrives value of variations.

        Required argument:
            key --  the key of value.
        """
        try:
            return str(Vars.variations[key])
        except KeyError:
            return ""


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


class CharAndNumber():
    """Just char and number."""
    char_and_number = list(ascii_lowercase + ascii_uppercase + '0123456789')
