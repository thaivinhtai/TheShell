"""This module define or display aliases."""

from re import sub
from Stuffs import GlobalAliases


def execute_alias(arguments):
    """
    execute_alias(arguments)    -> usage: alias [name[=value]...].

    Without arguments, this function prints the list of aliases in the reusable
    form `alias NAME=VALUE' on standard output.

    Otherwise, an alias is defined for each NAME whose VALUE is given.
    A trailing space in VALUE causes the next word to be checked for
    alias substitution when the alias is expanded.

    Optional argument:
        :param arguments:     [name[=value]...]
    :return: list of aliases
    """
    if not arguments:
        return [print("alias " + key + "='", value, "'", sep="")
                for key, value in GlobalAliases.aliases.items()], 0
    for arg in arguments:
        if arg in GlobalAliases.aliases.keys():
            print("alias " + arg + "='", GlobalAliases.aliases[arg],
                  "'", sep="")
    temp_list = []
    for arg in arguments:
        if '=' in arg:
            temp_list.append(arg.split('=', 1))
    for element in temp_list:
        GlobalAliases.aliases[element[0]] = sub('["' + "']", '', element[1])
    return GlobalAliases.aliases, 0
