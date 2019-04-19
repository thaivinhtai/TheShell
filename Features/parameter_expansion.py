"""The ‘$’ character introduces parameter expansion, command substitution, or
arithmetic expansion. The parameter name or symbol to be expanded may be
enclosed in braces, which are optional but serve to protect the variable to be
expanded from characters immediately following it which could be interpreted as
part of the name.
"""


def expan_parameter(orchestra):
    temp = [element for element in orchestra if "$" in element]
    print(temp)
