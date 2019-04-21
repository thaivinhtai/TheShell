# import curses
# from curses.textpad import Textbox, rectangle
#
# import os
# rows, columns = os.popen('stty size', 'r').read().split()
# print(rows, columns)
#
# def main(stdscr):
#     # stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")
#
#     editwin = curses.newwin(5,int(columns), 2,1)
#     # rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
#     # stdscr.refresh()
#
#     # box = Textbox(editwin)
#
#     # Let the user edit until Ctrl-G is struck.
#     # box.edit()
#
#     # Get resulting contents
#     # message = box.gather()
#
#
# curses.wrapper(main)




# import curses
# import os
#
# def main(win):
#     win.nodelay(True)
#     key=""
#     win.clear()
#     win.addstr("Detected key:")
#     while 1:
#         try:
#            key = win.getkey()
#            win.clear()
#            win.addstr("Detected key:")
#            win.addstr(str(key))
#            if key == os.linesep:
#               break
#         except Exception as e:
#            # No input
#            pass
#
# curses.wrapper(main)




# from ctypes import *
# import windll
#
# STD_OUTPUT_HANDLE = -11
#
# class COORD(Structure):
#     pass
#
# COORD._fields_ = [("X", c_short), ("Y", c_short)]
#
# def print_at(r, c, s):
#     h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
#     windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
#
#     c = s.encode("windows-1252")
#     windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
#
# print_at(6, 3, "Hello")


# import readline
#
# defaultText = 'I am the default value'
# readline.set_startup_hook(lambda: readline.insert_text(defaultText))
# res = input('Edit this:')
# print(res)

import pwd
for p in pwd.getpwall():
    print(p[0])
