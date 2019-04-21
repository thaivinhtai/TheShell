"""This module provides resources of variations for all program."""

import sys
from string import ascii_lowercase, ascii_uppercase
from os import getpid, environ, path
from Stuffs import read_file


class Vars():
    """This class stores vars for the The Shell.
    """
    special_vars = {
        "?": "0",
        "$": str(getpid()),
        "_": ""
    }
    variations = dict(environ)
    variations.update(special_vars)

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


class History():
    """Call and store history."""
    path_dir = path.dirname(sys.argv[0])
    history_local = path_dir + "/Stuffs/Data/history"
    history_conten = read_file(history_local).split("\n")
