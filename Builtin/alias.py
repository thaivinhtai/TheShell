"""This module define or display aliases."""


def execute_alias(**kwargs):
    """
    execute_alias(key=value, [key=value, ...])

    Without arguments, this function prints the list of aliases in the reusable
    form `alias NAME=VALUE' on standard output.

    Otherwise, an alias is defined for each NAME whose VALUE is given.
    A trailing space in VALUE causes the next word to be checked for
    alias substitution when the alias is expanded.

    Optional argument:
        :param kwargs:     key='value'
    :return: list of aliases
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
    if not kwargs:
        return [print("alias " + key + "='", value, "'", sep="") for key, value in aliases.items()]
    for key, value in kwargs.items():
        aliases[key] = [element for element in value if element != ""]
    return aliases