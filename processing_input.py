"""This module handle user's input."""

from Stuffs import GlobalAliases
from Features import (expan_globbing_pattern, expan_parameter, expan_tilde,
                      assign_paramenter)


def handle_input(orchestra):
    """
    handle_input(orchestra) ->  command, arguments.

    This function divide user's input into command, arguments.

    Required argument:
        orchestra   --  input of user.
    """
    orchestra = orchestra.split(" ")
    while "" in orchestra:
        orchestra.remove("")
    orchestra = assign_paramenter(orchestra)
    orchestra = expan_parameter(orchestra)
    orchestra = expan_globbing_pattern(orchestra)
    orchestra = expan_tilde(orchestra)
    try:
        command = orchestra[0]
    except IndexError:
        return "", ""
    arguments = orchestra[1:]
    # check command alias
    temp_command = []
    if command in GlobalAliases.aliases.keys():
        temp_command = GlobalAliases.aliases[command].split(" ")
    if temp_command:
        command = temp_command[0]
        temp_command.remove(command)
        for element in temp_command[1::-1]:
            arguments.insert(0, element)
    # return values
    return command, arguments
