"""The ‘$’ character introduces parameter expansion, command substitution, or
arithmetic expansion. The parameter name or symbol to be expanded may be
enclosed in braces, which are optional but serve to protect the variable to be
expanded from characters immediately following it which could be interpreted as
part of the name.
"""

from string import ascii_lowercase, ascii_uppercase
from Stuffs import Vars


def handle_process_id(orchestra):
    """
    handel_process_id(orchestra) -> expand "$$".

    This function expand all "$$" in input.

    Reqired argument:
        orchestra   -- user's input
    """
    element_index = -1
    for element in orchestra:
        element_index += 1
        while "$$" in element:
            orchestra[element_index] =\
                orchestra[element_index].replace("$$", Vars.get_var("$"))
    return orchestra


def expan_all(orchestra):
    """
    expan_all(orchestra)    -> expand all parameter.

    This function expan all the parameters in user's input.

    Required argument:
        orchestra   --  user's input.
    """

    char_and_numb = list(ascii_lowercase + ascii_uppercase + '0123456789')
    element_index = -1

    def get_begin_and_end_replace_position(element):
        """
        This function return list of begin and end position to replace.

        Required argument:
            element     --  argument.
        """
        begin_index = []
        last_index = []
        temp_index = -1
        for char in list(element):
            temp_index += 1
            if char == "$":
                begin_index.append(temp_index)
            if char not in char_and_numb:
                last_index.append(temp_index)
        temp = []
        for element in last_index:
            print(element, "l")
            print(begin_index[0], "b")
            if element <= begin_index[0]:
                temp.append(element)
        for element in temp:
            last_index.remove(element)
        while len(last_index) > len(begin_index):
            last_index.remove(last_index[-1])
        return begin_index, last_index

    def get_replace_list(element, begin_index, last_index):
        """
        This functions returns the value will replaces.

        Required arguments:
            element     --  argument
            begin_index --  list of begin position
            last_index  --  list of end position
        """
        replace_list = []
        for index in range(len(last_index)):
            replace_list.append(element[begin_index[index]:last_index[index]])
        return replace_list

    def execute_replace(replace_list, element_index, orchestra):
        """
        This function expand the arguments by replace string.

        Required argument:
            replace_list    --  value will replace.
            element_index   --  index of orchestra.
            orchestra       --  user's input.
        """
        for data in replace_list:
            orchestra[element_index] = orchestra[element_index]\
                                        .replace(data, Vars.get_var(data[1:]))
        if ("$" in orchestra[element_index] and
                orchestra[element_index][-1] != "$"):
            orchestra[element_index] =\
                orchestra[element_index].\
                replace(orchestra[element_index][orchestra[element_index]
                        .index("$"):],
                        Vars
                        .get_var(orchestra[element_index]
                                 [orchestra[element_index]
                                 .index("$") + 1:]))

    def handle_one_by_one(element, orchestra):
        """
        This function handle one by one argument.

        Required arguments:
            element         --  argument
            orchestra       --  whole input of user.
        """
        nonlocal element_index
        nonlocal char_and_numb
        element_index += 1
        if "$" in element and (element[0] != "'" or element[-1] != "'"):
            begin_index, last_index =\
                get_begin_and_end_replace_position(element)
            replace_list = get_replace_list(element, begin_index, last_index)
            execute_replace(replace_list, element_index, orchestra)
        if "$" in element and element[0] == "'" and element[-1] == "'":
            orchestra[element_index] =\
                orchestra[element_index].\
                replace(orchestra[element_index][0], "")

    for element in orchestra:
        handle_one_by_one(element, orchestra)
    return orchestra


def expan_parameter(orchestra):
    """
    expan_parameter(orchestra)  ->  parameter expansion.

    This function expan all parameters.

    Required argument:
        orchestra   --  user's input
    """
    orchestra = handle_process_id(orchestra)
    orchestra = expan_all(orchestra)
    return orchestra
