"""This module shows history."""

from Stuffs import History


def print_history(argument):
    """
    print_history(argument) -> print history.
    """
    argument = ""
    i = 0
    for data in History.history_conten:
        i += 1
        print((5 - len(str(i)))*" " + str(i) + "  " + data)
    return 0, 0
