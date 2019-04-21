"""This module is an exit of the program."""

from Stuffs import History, add_content_file


def exit_intek_shell(argument):
    """
    exit_intek_shell(argument) -> return "exit" and exit status.

    Optional argument:
        -   argument    --  exit status.
    """
    argument = list(argument)
    content = ""
    while "" in History.history_conten:
        History.history_conten.remove("")
    for line in History.history_conten:
        content += line + "\n"
    if not argument:
        print("exit")
        add_content_file(History.history_local, content)
        return "exit", 0
    try:
        int(argument[0])
        print("exit")
        add_content_file(History.history_local, content)
        return "exit", argument[0]
    except ValueError:
        print("exit")
        print("intek-sh: exit:", str(argument[0]))
        add_content_file(History.history_local, content)
        return "exit", 2
