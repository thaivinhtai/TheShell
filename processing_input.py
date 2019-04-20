"""This module handle user's input."""

from Stuffs import GlobalAliases
from Features import expan_globbing_pattern, expan_parameter


def handle_input(orchestra):
    """
    handle_input(orchestra) ->  command, arguments.

    This function divide user's input into command, arguments.

    Required argument:
        orchestra   --  input of user.
    """
    # open_apostrophe = False
    # mark = ""
    # for char in orchestra:
    #     if char == "'":
    #         open_apostrophe == True
    #         mark = "'"
    # while count_apostrophe % 2 != 0:
    #     wait_apostrophe = input("> ")
    #     if wait_apostrophe == "'":
    #         break
    #
    orchestra = orchestra.split(" ")
    while "" in orchestra:
        orchestra.remove("")
    # check file globbing
    orchestra = expan_parameter(orchestra)
    orchestra = expan_globbing_pattern(orchestra)
    command = orchestra[0]
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
