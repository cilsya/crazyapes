# Windows specific for dealing with the console
# https://www.programcreek.com/python/example/104587/win32api.GetStdHandle
#import win32api as api, win32process as proc
import ctypes
import os
import win32api
import win32gui

#-------------------------------------------------------------------------------

#https://github.com/theinternetftw/xyppy/blob/
#20d5efdee9b955519c2f76923b0adb9e71aa927f/xyppy/term.py/
# https://stackoverflow.com/questions/18775309/
#strange-inconsistencies-getting-default-console-colors-on-windows-with-python
class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
                ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [("dwSize", COORD),
                ("dwCursorPosition", COORD),
                ("wAttributes", ctypes.c_ushort),
                ("srWindow", SMALL_RECT),
                ("dwMaximumWindowSize", COORD)]



#windll.kernel32.GetConsoleScreenBufferInfo.argtypes
# = [wintypes.HANDLE, ctypes.POINTER(CONSOLE_SCREEN_BUFFER_INFO)]

# https://stackoverflow.com/questions/12549921/
#make-windows-console-cursor-invisible-with-python-ctypes-modules
class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [('dwSize', ctypes.c_int),
                ('bVisible', ctypes.c_int)]

#-------------------------------------------------------------------------------

def set_console_cursor_visibility(visibility):
        """
        https://stackoverflow.com/questions/12549921/
        make-windows-console-cursor-invisible-with-python-ctypes-modules
        """
        
        STD_OUTPUT_HANDLE = ctypes.c_ulong(-11)
        
        stdout_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        cursorInfo = CONSOLE_CURSOR_INFO()
        cursorInfo.dwSize = 1
        cursorInfo.bVisible = visibility
        ctypes.windll.kernel32.SetConsoleCursorInfo( stdout_handle,
                                                     ctypes.byref(cursorInfo))

def set_console_cursor_position(x, y):
        
        STD_OUTPUT_HANDLE = ctypes.c_ulong(-11)
        
        cbuf = CONSOLE_SCREEN_BUFFER_INFO()
        stdout_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(stdout_handle,
                                                          ctypes.byref(cbuf))

        cursor = cbuf.dwCursorPosition
        cursor.X = x
        cursor.Y = y
        ctypes.windll.kernel32.SetConsoleCursorPosition(stdout_handle,
                                                        cursor)

def clear_row(row=1):
    
    # https://www.geeksforgeeks.org/python-os-get_terminal_size-method/\
    # Get the size of the terminal
    #
    # I believe this is a tuple.
    # width: size_of_terminal[0]
    # height: size_of_terminal[1]
    size_of_terminal = os.get_terminal_size()
    
    # This is how many characters are across in the console
    #row_width = 80
    row_width = size_of_terminal[0]
    
    for i in range(0, row_width + 1 ):
       # Place the cursor at the first x position of the decided row
       set_console_cursor_position(i, row)
        
       # Clear that character
       # NOTE: Do NOT do a carriage return (go to newline). So sent
       #      end="" instead of end="\n" (for windows)
       #
       # NOTE2: Flush right away to dump what is in the bufffer as if it is 
       #        streaming flush=True (for python 3, it was sys.stdout.flush()
       #        in python 2)
       #
       print(" ",
             end="",
             flush=True)
       
def clear_row_range(row_range=[0, 5]):
    """
    NOTE: The first number in list is inclusive, the last number in list
          is exclusive
    """
    row_start = row_range[0]
    row_end = row_range[1]
    
    for i in range(row_start, row_end):
        clear_row(row=i)
    