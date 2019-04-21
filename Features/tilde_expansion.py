"""If a word begins with an unquoted tilde character (‘~’), all of the
characters up to the first unquoted slash (or all characters, if there is no
unquoted slash) are considered a tilde-prefix. If none of the characters in the
tilde-prefix are quoted, the characters in the tilde-prefix following the tilde
are treated as a possible login name. If this login name is the null string,
the tilde is replaced with the value of the HOME shell variable. If HOME is
unset, the home directory of the user executing the shell is substituted
instead. Otherwise, the tilde-prefix is replaced with the home directory
associated with the specified login name.

If the tilde-prefix is ‘~+’, the value of the shell variable PWD replaces the
tilde-prefix. If the tilde-prefix is ‘~-’, the value of the shell variable
OLDPWD, if it is set, is substituted.

If the characters following the tilde in the tilde-prefix consist of a number
N, optionally prefixed by a ‘+’ or a ‘-’, the tilde-prefix is replaced with the
corresponding element from the directory stack, as it would be displayed by the
dirs builtin invoked with the characters following tilde in the tilde-prefix as
an argument (see The Directory Stack). If the tilde-prefix, sans the tilde,
consists of a number without a leading ‘+’ or ‘-’, ‘+’ is assumed.

If the login name is invalid, or the tilde expansion fails, the word is left
unchanged.

Each variable assignment is checked for unquoted tilde-prefixes immediately
following a ‘:’ or the first ‘=’. In these cases, tilde expansion is also
performed. Consequently, one may use filenames with tildes in assignments to
PATH, MAILPATH, and CDPATH, and the shell assigns the expanded value.
"""

from os import getcwd, environ
from os.path import expanduser
from pwd import getpwall


def expan_tilde(orchestra):
    """
    expand_tilde(orchestra) -> expan every argument.

    Required argument:
        orchestra   --  user input.
    """
    users = []
    for user in getpwall():
        users.append(user[0])
    index = -1
    for element in orchestra:
        index += 1
        if "/" not in element:
            continue
        if element.startswith("~/"):
            orchestra[index] = expanduser(element)
        elif element.startswith("~+/"):
            orchestra[index] = element.replace("~+", getcwd())
        elif element.startswith("~-/"):
            orchestra[index] = element.replace("~-", environ['OLDPWD'])
        elif element.startswith("~") and\
                element[1: element.index("/")] in users:
                orchestra[index] = element.replace("~", "/home/")
    return orchestra
