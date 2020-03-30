import crawler
import tkinter as tk
from tkinter import ttk


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
    

result_labels = {}

def filter_result(res):
    pass

def clear_screen():
    for child in main.pack_slaves():
        child.pack_forget()

def display_results(e=None):
    result = crawler.searchCountry(search.get())
    clear_screen()
    if result != search.placeholder_text:
        for res in result:
            cap, val = res, result[res]
            if cap and val:
                val = val.strip('\n')
                label = ResultLabel(main, f'{cap}', val, {
                    'font':('Avenir', 10, 'bold'), 'padx': 7,
                    'relief':'flat', 'anchor':'w', 'width':27
                }, {
                    'font':('Roboto', 10), 'anchor':'w', 'relief':'flat',
                    'fg':'royalblue'
                })
                label.pack(side='top', fill='x')

                result_labels[cap] = label

        del label, cap, val



# root (app) settings
root = tk.Tk()
root.title('Coronavirus (COVID19) Cases Check')
root.minsize(400, 400)

# top section - search
searchFrame = tk.Frame(root)
search = SearchInput(searchFrame)
search_button = ttk.Button(
    searchFrame, text='Search', command=display_results, width=15
)
search.pack(
    side='left', fill='x', expand=1, padx=7, pady=5, ipady=3, ipadx=6
)
search_button.pack(
    side='right', fill='x', padx=7, pady=5, ipady=2
)
searchFrame.pack(side='top', fill='x')

# main section - body
main = tk.Frame(root)
main.pack(side='top', fill='both', padx=7)


root.mainloop()
