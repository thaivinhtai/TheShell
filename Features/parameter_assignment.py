"""A parameter is an entity that stores values. It can be a name, a number, or
one of the special characters listed below. A variable is a parameter denoted
by a name. A variable has a value and zero or more attributes. Attributes are
assigned using the declare builtin command (see the description of the declare
builtin in Bash Builtins).

A parameter is set if it has been assigned a value. The null string is a valid
value. Once a variable is set, it may be unset only by using the unset builtin
command.
"""

from Stuffs import Vars


def assign_paramenter(orchestra):
    """
    assign_paramenter(orchestra) -> assign paramenters.

    Required argument:
        orchestra   --  user's input.
    """

    def assign(element):
        """
        assign(element) -> assign value to parameter.

        required argument:
            element --  single argument.
        """
        nonlocal orchestra
        nonlocal temp
        position = element.index("=")
        if "'" in element or '"' in element[:position]:
            return element
        temp.append(element)
        if "'" not in element and '"' not in element:
            Vars.variations[element[:position]] = element[position + 1:]
            return element
        element = element[position + 1:].replace("'", "")
        parse = element[position + 1:].replace('"', "")
        Vars.variations[element[:position]] = parse
        return element

    temp = []
    for element in orchestra:
        if "=" in element:
            # position = element.index("=")
            # if "'" in element or '"' in elemnt[:position]:
            #     continue
            # temp.append(element)
            # if "'" not in element and '"' not in elemnt:
            #     Vars.variations[element[:position]] = element[position + 1:]
            #     continue
            # element = element[position + 1:].replace("'", "")
            # parse = element[position + 1:].replace('"', "")
            # Vars.variations[element[:position]] = parse
            assign(element)
    for element in temp:
        orchestra.remove(element)
    return orchestra
