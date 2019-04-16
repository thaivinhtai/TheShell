"""This module represent multiple filenames by using special characters called
wildcards with a single file name. A wildcard is essentially a symbol which may
be used to substitute for one or more characters.
"""

from glob import glob
from collections import Iterable
from six import string_types


def flatten_nested_list(nested_list):
    """
    flatten_nested_list(nested_list)    ->  convert nested list to 1D list.

    Required argument:
        nested_list --  any list.
    """
    for item in nested_list:
        if isinstance(item, Iterable) and not isinstance(item, string_types):
            for element in flatten_nested_list(item):
                yield element
        else:
            yield item


def expan_globbing_pattern(patterns):
    """
    expan_globbing_pattern(patterns) -> a list of pathname pattern expansion.

    This function  finds all the pathnames matching a specified pattern
    according to the rules used by the Unix shell, although results are
    returned in arbitrary order.

    Required argument:
        patterns     --  a list.
    """
    index = 0
    temp_expansion = []
    for element in patterns:
        if "[" in element or "?" in element or "*" in element:
            temp_expansion = glob(element, recursive=True)
            temp_expansion.sort()
        if temp_expansion:
            patterns[index] = temp_expansion
        index += 1
    orchestra = list(flatten_nested_list(patterns))
    return orchestra
