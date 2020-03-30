import crawler
import app_temps as tmp

tk = tmp.tk
ttk = tmp.ttk

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
                label = tmp.ResultLabel(main, f'{cap}', val, {
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
root.title('Coronavirus Cases Check')
root.minsize(400, 400)

# top section - search
searchFrame = tk.Frame(root)
search = tmp.SearchInput(searchFrame)
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
