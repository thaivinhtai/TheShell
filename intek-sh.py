#!/usr/bin/env python3

"""This program is called The Shell, that simulates the Bash Shell."""

from Builtin import (execute_program, change_dir, exit_intek_shell,
                     print_env, export, unset, execute_alias)
from Stuffs import get_input_display, GlobalAliases, Vars
from processing_input import handle_input


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
            if command == "":
                continue
            result, Vars.variations['?'] = run_command(command, arguments)
            if result == "exit":
                return Vars.variations['?']
        except EOFError:
            return 1
        except KeyboardInterrupt:
            print("")
            continue


if __name__ == "__main__":
    main()
