# Windows specific for dealing with the console
# https://www.programcreek.com/python/example/104587/win32api.GetStdHandle
#import win32api as api, win32process as proc
import ctypes
import win32api
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