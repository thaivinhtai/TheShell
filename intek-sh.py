#!/usr/bin/env python3

"""This program is called The Shell, that simulates the Bash Shell."""

from Builtin import (execute_program, change_dir, exit_intek_shell,
                     print_env, export, unset, execute_alias, GlobalAliases)
from Features import expan_globbing_pattern
from Stuffs import get_input_display


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
    # check file globbing
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


def run_command(command, arguments):
    """
    switch_command(command) ->  choose a command.

    This is a manual swithcer for select function quickly.

    Required arguments:
        command     --  a string-type, which is name of command.
        arguments    --  argument of command.
    """
    switcher = {
        'cd': change_dir,
        'exit': exit_intek_shell,
        'printenv': print_env,
        'export': export,
        'unset': unset,
        'alias': execute_alias
    }
    try:
        func = switcher.get(command)
        return func(arguments)
    except TypeError:
        return execute_program(command, arguments)


def main():
    """
    This is the core of the program, get input and execute.
    """
    while True:
        try:
            orchestra = input(get_input_display())
            if orchestra == "":
                continue
            command, arguments = handle_input(orchestra)
            result, status = run_command(command, arguments)
            if result == "exit":
                return status
        except EOFError:
            return 1
        except KeyboardInterrupt:
            print("")
            continue


if __name__ == "__main__":
    main()
