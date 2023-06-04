from tkinter import ttk
import sys

def configure_style():
    style = ttk.Style()
    style.configure('TFrame', background='#333333')
    style.configure('TLabel', background='#333333', foreground='#FFFFFF', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12), foreground='#000000', background='#555555')
    style.map('TButton', foreground=[('active', '#000000')], background=[('active', '#000000')])
    style.configure('TCombobox', background='#555555', fieldbackground='#555555', foreground='#FFFFFF'
                    , selectbackground='#000000')

    # 'Entry' might not work on OSX
    # change to 'TEntry'
    if sys.platform == "win32":
        # Windows-specific styles
        style.configure('Entry', fieldbackground='#555555', foreground='#FFFFFF')
    else:
        # macOS/Linux-specific styles
        style.configure('TEntry', fieldbackground='#555555', foreground='#FFFFFF')

    return style

    return style
