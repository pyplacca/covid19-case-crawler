from tkinter import ttk
import tkinter as tk


class SearchInput(tk.Entry):

    def __init__(self, master=None, **kws):
        self.entry_var = tk.StringVar()
        tk.Entry.__init__(
            self, master, textvariable=self.entry_var, **kws
        )
        # 
        self.typing = False
        self.placeholder_text = 'Enter a country (eg: USA)..'
        self.entry_var.set(self.placeholder_text)
        self._focusout('')
        self.focus_set()
        # event bindings
        self.bind('<FocusIn>', self._focusin)
        self.bind('<FocusOut>', self._focusout)
        self.bind('<Key>', self._clear_placeholder)

    def _clear_placeholder(self, event):
        if event.keysym == 'BackSpace':
            self._focusout('')
        if self.typing:
            return
        else:
            self.entry_var.set('')
            self._switch_color('#272727')
            self.typing = True

    def _focusin(self, event):
        # internal use only
        if self._placeholder_present:
            self._switch_color('#c4c4c4')
            self.typing = False
            self.icursor(0)
        else:
            self.icursor('end')

    def _focusout(self, event):
        # internal use only
        if not self.entry_var.get():
            self.entry_var.set(self.placeholder_text)
        if self._placeholder_present:
            self._switch_color('#8b8b8b')
            self.typing = False

    @property
    def _placeholder_present(self):
        return self.entry_var.get() == self.placeholder_text

    def _switch_color(self, color):
        # internal use only
        self.config(fg=color)
    

class ResultLabel(tk.LabelFrame):

    def __init__(
        self, master=None, caption='', value='', caption_opts={}, label_opts={}
    ):
        tk.LabelFrame.__init__(self, master, relief='flat')
        top = tk.LabelFrame(self, relief='flat')
        self.caption = tk.Label(top, text=caption, **caption_opts)
        self.label = tk.Label(top, text=value, **label_opts)
        top.pack(side='top', fill='x')
        self.caption.pack(side='left')
        self.label.pack(side='left')
        ttk.Separator(self, orient='horizontal').pack(
            side='top', fill='x', expand=1
        )
 