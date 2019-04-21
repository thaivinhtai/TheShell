"""This module provides some aliases that will be used many times in the "Mini
-shell" program.

Functions in this module:
 - get_full_path(file) -> return full path of file.
 - get_file_type(file) -> return type of file.
 - get_path_environ()  -> get the value of $PATH in Operating System as list.
 - get_input_display() -> display of current working directory of the shell.
 - add_content_file(name, content)  -> add content to a file.
 - open_file(file) ->  open a file for reading and writing.
 - read_file(file) ->  get content of a file.
"""

from os import (path, environ, getcwd, open, O_RDWR, O_CREAT, write, open,
                close, fdopen)
from io import RawIOBase, BufferedIOBase


def get_full_path(file):
    """
    get_full_path(file) -> return full path of file.

    This function figures out exactly the path of file on system.

    Required argument:
        file    --  a string-type file name.
    """
    if file[0] == '~':
        file = path.expanduser(file)
    else:
        file = path.realpath(file)
    return file


def get_file_type(file):
    """
    get_file_type(file) -> return type of file.

    This function check if a file is a directory, file and return its type via
    a string. If the file is not exist, return None.

    Required argument:
        file    -- a string-type file name.
    """
    try:
        file = get_full_path(file)
        if isinstance(file, (RawIOBase, BufferedIOBase)):
            return "bin"
        if path.isfile(file):
            return "file"
        if path.isdir(file):
            return "directory"
        return 0
    except FileNotFoundError:
        return None


def get_path_environ():
    """
    get_path_environ()  -> get the value of $PATH in Operating System as list.

    This Function splits all the value in the $PATH and return a list of path.
    """
    return environ['PATH'].split(":")


def get_input_display():
    """
    This funtion return the display of current working directory of the shell.
    """
    current_dir = getcwd()
    home_dir = get_full_path("~")
    current_dir = current_dir.replace(home_dir, "~")
    return ("\033[92m\033[1m" + "intek-sh" + "\033[0m" +
            ":" + "\033[94m\033[1m" + current_dir + "\033[0m$ ")


def add_content_file(name, content=""):
    """
    add_content_file(name, content)  -> add content to a file.
    This function add content to a file, if it's not exist, create it.
    Required arguments:
        name        -- name of file.
        content     -- content add to file.
    """
    name = get_full_path(name)
    file_descriptor = open(name, O_RDWR | O_CREAT, 0o644)
    byte_object = str.encode(content)
    write(file_descriptor, byte_object)
    return close(file_descriptor)


def open_file(file):
    """
    open_file(file) ->  open a file for reading and writing.
    This function returns a file object.
    Required argument:
        file    --  file' name.
    """
    try:
        file = get_full_path(file)
        file = open(file, O_RDWR)
        file = fdopen(file)
        return file
    except PermissionError:
        return None


def read_file(file):
    """
    read_file(file)     ->  get content of a file.
    Required argument:
        file    --  name or path of file.
    """
    try:
        file = open_file(file)
        content = file.read()
        file.close()
        return content
    except (UnicodeDecodeError, PermissionError, AttributeError) as errors:
        del errors
        return ""
