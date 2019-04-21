"""This module unsets values and attributes of shell variables and functions.
"""

from Stuffs import Vars


def unset(arguments):
    """
    unset(arguments)    ->  For each NAME, remove the corresponding variable.

    Required argument:
        arguments   --  list of argument
    """
    if not arguments:
        return 0, 0
    for element in arguments:
        if element in Vars.variations:
            Vars.variations.pop(element)
    return 0, 0
