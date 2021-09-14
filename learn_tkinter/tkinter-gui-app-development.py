import tkinter as tk
import csv, time, threading, json, random, urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler
import tkinter.messagebox as messagebox


"""root = Tk()
btn = Button(root, text='Click me!')
btn.config(command=print('Hello world!'))
btn.pack(padx=120, pady=30)
root.title('My tkinter app')
root.mainloop()"""


# buttons begining

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self,text='Click me!',
            command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print('Hello Tkinter!')

"""if __name__ == '__main__':
    app = App()
    app.title('My Tkinter App')
    app.mainloop()
"""

# Working with buttons

RELIEFS = [tk.SUNKEN, tk.RAISED,  tk.GROOVE, tk.RIDGE, tk.FLAT]

class ButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(file=r'C:\Users\Training\Documents\CODES\GUI\T148.gif')
        self.btn = tk.Button(self, text='Button with image',image=self.img,
            compound=tk.LEFT,command=self.disable_btn)
        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()
        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=tk.LEFT)
    
    def create_btn(self, relief):
        return tk.Button(self, text=relief, relief=relief)
    
    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)

"""if __name__ == '__main__':
    app = ButtonsApp()
    app.mainloop()
"""

# Creating text entries
# Use of placeholders
# start of bind and unbind functions

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.Entry(self)
        self.username.insert(0,'Enter your username')
        self.username.configure(state=tk.DISABLED)
        self.password = tk.Entry(self)
        # self.password = tk.Entry(self, show='*')
        self.password.insert(0,'Enter your password')
        self.password.configure(state=tk.DISABLED)
        self.login_btn = tk.Button(self, text='Login',
            command=self.store_login_details)
        self.clear_btn = tk.Button(self, text='Clear', command=self.clear_form)

        self.username.pack()
        self.password.pack()
        self.login_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def username_on_click(self, event):
        self.username.configure(state=tk.NORMAL)
        self.username.delete(0,tk.END)
        # make the callback only work once
        self.username.unbind('<Button-1>')

    def password_on_click(self,event):
        self.password.configure(state=tk.NORMAL)
        self.password.delete(0,tk.END)
        # make the callback only work once
        self.password.unbind('<Button-1>')

    def store_login_details(self):
        self.filename = 'details.csv'
        self.fields = ['Username', 'Password']
        _ , self.rows = [], []
        with open(self.filename, 'a',newline='') as csvFile:
            if self.username.get().lower() not in 'details.csv' and \
                self.password.get() not in 'details.csv':
                _.append(self.username.get().lower())
                _.append(self.password.get())
                self.rows.append(_)

                csvwriter = csv.writer(csvFile)
                csvwriter.writerow(self.fields)
                csvwriter.writerows(self.rows)    

            else: messagebox.showinfo('Error',
                'Login details has been taken!')             
            print(f'Username: {self.username.get()}')
            print(f'Password: {self.password.get()}')

    def clear_form(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()

        self.username.insert(0,'Enter your username')
        self.username.configure(state=tk.DISABLED)
        self.password.insert(0,'Enter your password')
        self.password.configure(state=tk.DISABLED)

        self.username.bind('<Button-1>', self.username_on_click)
        self.password.bind('<Button-1>', self.password_on_click)

"""if __name__ == '__main__':
    app = LoginApp()
    app.username.bind('<Button-1>', app.username_on_click)
    app.password.bind('<Button-1>', app.password_on_click)
    app.mainloop()
"""
# Tracing text changes
# use of StringVar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace('w', self.show_message)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(self, text='clear',
            command=lambda: self.var.set(''))
        
        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()
    
    def show_message(self, *args):
        # When invoked, the callback function receives three arguments: 
        # the internal variable name, an empty string (it is used in other types of Tk variables),
        # and the mode that triggered the operation. 
        # By declaring the method with *args, we make these arguments optional, 
        # because we are not using any of these values within the callback.

        value = self.var.get()
        text = 'Hello, {}!'.format(value) if value else ''
        self.label.config(text=text)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Validating a text entry

import re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self, text="Enter your username")
        vcmd = (self.register(self.validate_username), "%i", "%P")
        self.entry = tk.Entry(self, validate="key",
        validatecommand=vcmd,
        invalidcommand=self.print_error)
        self.label.pack()
        self.entry.pack(anchor=tk.W, padx=10, pady=10)
    def validate_username(self, index, username):
        print("Modification at index " + index)
        return self.pattern.match(username) is not None
    def print_error(self):
        print("Invalid username character")

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# validating entry input (my own way)

class trial():
    def __init__(self):
        self.main_window = tk.Tk()
        self.frame = tk.Frame(self.main_window)
        self.label = tk.Label(self.frame, text='Enter your name')
        self.entry = tk.Entry(self.frame, width=10)
        self.button = tk.Button(self.frame, text='validate', 
            relief= tk.SUNKEN, command=self.validate_func)
        reg = self.main_window.register(self.validate_func)
        #self.entry.config(validate="key", validatecommand=(reg, '%P'))
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.frame.pack()
        
        tk.mainloop()

    def validate_func(self):
        if self.entry.get() == 'emma':
            print('True')
            #return True
            messagebox.showinfo('Success', 'Valid!')
        else: 
            print('False')
            #return False 
            messagebox.showinfo('Error', 'Invalid!')


# trial()


# Selecting numerical values
# use case for the Spinbox and Scale classes

# spinbox returns the value as a string
# scale returns the value as an integer or float

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.spinbox = tk.Spinbox(self, from_=0, to=15)
        self.scale = tk.Scale(self, from_=0, to=10,
            orient=tk.HORIZONTAL)
        self.btn = tk.Button(self, text='Print values',
            command= self.print_values)
        
        self.spinbox.pack()
        self.scale.pack()
        self.btn.pack()
    
    def print_values(self):
        print(f'SPINBOX: {self.spinbox.get()}')
        print(f'SCLAEs: {self.scale.get()}')

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# trial using spinbox

# by default the orientation of scale is vertical
# but can be altered using `orient=tk.VERTICAL`


class GetAge(tk.Tk):
    def __init__(self):
        super().__init__()
        self.age = tk.Label(self, text='Age')
        self.spinbox = tk.Spinbox(self, from_=0, to=100)
        self.scale = tk.Scale(self, from_=0, to=100,resolution=0.5)
        self.age.pack()
        self.spinbox.pack()
        self.scale.pack()

"""
Ge = GetAge()
Ge.mainloop()
"""

# Creating selections with radio buttons

# Clicking a Radiobutton selects it and automatically 
# deselects any other Radiobutton in the same container, because
# only one Radiobutton in a container can be selected at any
# given time, they are said to be mutually exclusive.

COLORS = [('Red','red'), ('Green', 'green'), ('Blue', 'blue')]

class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set('red')
        # Remember to try to not repeat yourself whenever possible
        self.buttons = [self.create_radio(c) for c in COLORS]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)
    
    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self, text=text, value=value,
            command=self.print_option, variable=self.var)
    
    def print_option(self):
        print(self.var.get())

"""
if __name__ == '__main__':
    app = ChoiceApp()
    app.mainloop()
"""

# flexing my own radiobuttons (^_^)

COLORS = [('Red',1), ('Green', 2), ('Blue', 3)]

class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.var.set(0)
        self.btn = [self.create_btn(d) for d in COLORS]
        for i in self.btn:
            i.pack()
    
    def create_btn(self,f):
        text, value = f
        return tk.Radiobutton(self, text=text, value=value,
            command=self.display_options, variable=self.var)
    
    def display_options(self):
        print(self.var.get())

"""
if __name__ == '__main__':
    app = ChoiceApp()
    app.mainloop()
"""

# Implementing switches with checkboxes

class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.cb = tk.Checkbutton(self, text='Active?',
            command=self.print_value, variable=self.var)
        self.cb.pack()
    
    def print_value(self):
        print(self.var.get())

# doesn't work!
# make the checkbuttons individually

DECISIONS = ['Active', 'Inactive', 'Undefined']

class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.btns = [self.make_btns(o) for o in DECISIONS]
        for j in self.btns:
            j.pack()
    
    def make_btns(self,k):
        return tk.Checkbutton(self, text=k,
            command=self.print_value, variable=self.var)
    
    def print_value(self):
        print(self.var.get())

"""
if __name__ == '__main__':
    app = SwitchApp()
    app.mainloop()
"""

# Displaying a list of items

DAYS = ['Monday','Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday', 'January', 'February',
        'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']
MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]

class ListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.scroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.list = tk.Listbox(self.frame, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.list.yview)
        self.list.insert(0, *DAYS)
        self.print_btn = tk.Button(self, text='Print selection',
            command=self.print_selection)
        
        self.btns = [self.create_btn(m) for m in MODES]
        self.frame.pack()
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.print_btn.pack(fill=tk.BOTH)
        for btn in self.btns:
            btn.pack(side=tk.LEFT)

    def create_btn(self, mode):
        cmd = lambda: self.list.config(selectmode=mode)
        return tk.Button(self, command=cmd,
            text=mode.capitalize())
    
    def print_selection(self):
        selection = self.list.curselection()
        print('selection>>>', selection)
        print(*[self.list.get(i) for i in selection])

"""

if __name__ == '__main__':
    app = ListApp()
    app.mainloop()
"""

# Handling mouse and keyboard events

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        frame = tk.Frame(self, bg='green',
            height=100, width=100)
        frame.bind('<Button-1>', self.print_event)
        frame.bind('<Double-Button-1>', self.print_event)
        frame.bind('<ButtonRelease-1>', self.print_event)
        frame.bind('<B1-Motion>', self.print_event)
        frame.bind('<Enter>', self.print_event)
        frame.bind('<Leave>', self.print_event)
        frame.pack(padx=50, pady=50)
    
    def print_event(self, event):
        position = '(x={}, y={})'.format(event.x, event.y)
        print(event.type, 'event', position)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

class Binding(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200+10+10')
        self.title('My App')
        self.name = tk.Entry(self)
        self.name.insert(0, 'Enter your name')
        self.name.configure(state=tk.DISABLED)
        self.password = tk.Entry(self)
        self.password.insert(0, 'Enter your password')
        self.password.configure(state=tk.DISABLED)
        self.name.pack(fill=tk.BOTH)
        self.password.pack(fill=tk.BOTH )
    
    def name_click(self,event):
        self.name.configure(state=tk.NORMAL)
        self.name.delete(0, tk.END)
        self.name.unbind('<Button-1>')
    
    def password_click(self,event):
        self.password.configure(state=tk.NORMAL)
        self.password.delete(0, tk.END)
        self.password.unbind('<Button-1>')

"""
if __name__ == '__main__':
    app = Binding()
    app.name.bind('<Button-1>', app.name_click)
    app.password.bind('<Button-1>', app.password_click)
    app.mainloop()

"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        entry = tk.Entry(self)
        entry.bind('<FocusIn>', self.print_type)
        entry.bind('<Key>', self.print_key)
        entry.pack(padx=20, pady=20)
    
    def print_type(self, event):
        print(event.type)
    
    def print_key(self, event):
        args = event.keysym, event.keycode, event.char
        print('Symbol: {}, Code: {}, Char: {}'.format(*args))

# Setting the main window's icon, title, and size

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Tkinter App')
        # self.iconbitmap('python.ico')
        self.geometry('400x200+10+10')

# Grouping widgets with frames

class ListFrame(tk.Frame):
    def __init__(self, master, items=[]):
        super().__init__(master)
        self.list = tk.Listbox(self)
        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL,
            command=self.list.yview)
        self.list.config(yscrollcommand=self.scroll.set)
        self.list.insert(0, *items)
        self.list.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
    
    def pop_selection(self):
        index = self.list.curselection()
        print('INDEX>>>', index)
        if index:
            value = self.list.get(index)
            print('VALUE>>>', value)
            self.list.delete(index)
            return value
    
    def insert_item(self, item):
        self.list.insert(tk.END, item)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        months = ['January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December']
        self.frame_a = ListFrame(self, months)
        self.frame_b = ListFrame(self)
        self.btn_right = tk.Button(self, text='>',
            command=self.move_right)
        self.btn_left = tk.Button(self, text='<',
            command=self.move_left)
        
        self.frame_a.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_b.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_right.pack(expand=True, ipadx=5)
        self.btn_left.pack(expand=True, ipadx=5)
    
    def move_right(self):
        self.move(self.frame_a, self.frame_b)
    
    def move_left(self):
        self.move(self.frame_b, self.frame_a)
    
    def move(self, frame_from, frame_to):
        value = frame_from.pop_selection()
        if value:
            frame_to.insert_item(value)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Using the Pack geometry manager

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self, text='Label A', bg='yellow')
        label_b = tk.Label(self, text='Label B', bg='orange')
        label_c = tk.Label(self, text='Label C', bg='red')
        label_d = tk.Label(self, text='Label D', bg='green')
        label_e = tk.Label(self, text='Label E', bg='blue')

        opts = {'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH}
        label_a.pack(side=tk.TOP, **opts)
        label_b.pack(side=tk.TOP, **opts)
        label_c.pack(side=tk.LEFT, **opts)
        label_d.pack(side=tk.LEFT, **opts)
        label_e.pack(side=tk.LEFT, **opts)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Using the Grid geometry manager

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self, text="Label A", bg="yellow")
        label_b = tk.Label(self, text="Label B", bg="orange")
        label_c = tk.Label(self, text="Label C", bg="red")
        label_d = tk.Label(self, text="Label D", bg="green")
        label_e = tk.Label(self, text="Label E", bg="blue")
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        label_a.grid(row=0, column=0, **opts)
        label_b.grid(row=1, column=0, **opts)
        label_c.grid(row=0, column=1, rowspan=2, **opts)
        label_d.grid(row=0, column=2, rowspan=2, **opts)
        label_e.grid(row=2, column=0, columnspan=3, **opts)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""
# Using the Place geometry manager

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self, text="Label A", bg="yellow")
        label_b = tk.Label(self, text="Label B", bg="orange")
        label_c = tk.Label(self, text="Label C", bg="red")
        label_d = tk.Label(self, text="Label D", bg="green")
        label_e = tk.Label(self, text="Label E", bg="blue")
        label_a.place(relwidth=0.25, relheight=0.25)
        label_b.place(x=100, anchor=tk.N,
        width=100, height=50)
        label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER,
        relwidth=0.5, relheight=0.5)
        label_d.place(in_=label_c, anchor=tk.N + tk.W,
        x=2, y=2, relx=0.5, rely=0.5,
        relwidth=0.5, relheight=0.5)
        label_e.place(x=200, y=200, anchor=tk.S + tk.E,
        relwidth=0.25, relheight=0.25)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Grouping inputs with the LabelFrame widget

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        group_1 = tk.LabelFrame(self, padx=15, pady=10,
            text='Personal Information')
        group_1.pack(padx=10, pady=5)

        tk.Label(group_1, text='First Name').grid(row=0)
        tk.Label(group_1, text='Last Name').grid(row=1)
        tk.Entry(group_1).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(group_1).grid(row=1, column=1, sticky=tk.W)

        group_2 = tk.LabelFrame(self, padx=15, pady=10,
            text='Address')
        group_2.pack(padx=10, pady=5)

        tk.Label(group_2, text='Street').grid(row=0)
        tk.Label(group_2, text='City').grid(row=1)
        tk.Label(group_2, text='ZIP Code').grid(row=2)
        tk.Entry(group_2).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(group_2).grid(row=1, column=1, sticky=tk.W)
        tk.Entry(group_2, width=8).grid(row=2, column=1, 
            sticky=tk.W)

        self.btn_submit = tk.Button(self, text='Submit')
        self.btn_submit.pack(padx=10, pady=10, side=tk.RIGHT)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Dynamically laying out widgets

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        fields = ['First name', 'Last name', 'Phone', 'Email']
        labels = [tk.Label(self, text=f) for f in fields]
        entries = [tk.Entry(self) for _ in fields]
        self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text='Print info',
            command=self.print_info)
        
        for i, (label, entry) in enumerate(self.widgets):
            label.grid(row=i, column=0, padx=10, sticky=tk.W)
            entry.grid(row=i, column=1, padx=10, pady=5)
        self.submit.grid(row=len(fields), column=1, sticky=tk.E,
            padx=10, pady=10)
    
    def print_info(self):
        for label, entry in self.widgets:
            # there's a comma here..
            print('{} = {}'.format(label.cget('text'), '=', entry.get()))

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Creating horizontal and vertical scrollbars

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.scroll_x = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.scroll_y = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.canvas = tk.Canvas(self, width=300, height=100,
        xscrollcommand=self.scroll_x.set,
        yscrollcommand=self.scroll_y.set)
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)
        self.btn = tk.Button(self.frame, text="Load image",
        command=self.load_image)
        self.btn.pack()
        self.canvas.create_window((0, 0), window=self.frame,
        anchor=tk.NW)
        self.canvas.grid(row=0, column=0, sticky="nswe")
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self.resize)
        self.update_idletasks()
        self.minsize(self.winfo_width(), self.winfo_height())
    def resize(self, event):
        region = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=region)
    def load_image(self):
        self.btn.destroy()
        self.image = tk.PhotoImage(file=r'C:\Users\Training\Documents\CODES\GUI\T148.gif')
        tk.Label(self.frame, image=self.image).pack()

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Working with colors

from functools import partial
from tkinter.colorchooser import askcolor

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Colors demo')
        text = 'The quick brown fox jumps over the lazy dog'
        self.label = tk.Label(self, text=text)
        self.fg_btn = tk.Button(self, text='Set foreground color',
            command=partial(self.set_color, 'fg'))
        self.bg_btn = tk.Button(self, text='Set background color',
            command=partial(self.set_color, 'bg'))
        
        self.label.pack(padx=20, pady=20)
        self.fg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.bg_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def set_color(self, option):
        color = askcolor()[1]
        print('Chosen color:', color)
        self.label.config(**{option: color})   # same as (fg=color) or (bg=color)

""" 
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Setting widget fonts

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Fonts demo')
        text = 'The quick brown fox jumps over the lazy dog'
        self.label = tk.Label(self, text=text)

        self.family = tk.StringVar()
        self.family.trace('w', self.set_font)
        families = ('Times', 'Courier', 'Helvetica')
        self.option = tk.OptionMenu(self, self.family, *families)

        self.size = tk.StringVar()
        self.size.trace('w', self.set_font)
        self.spinbox = tk.Spinbox(self, from_=8, to=18,
            textvariable=self.size)
        
        self.family.set(families[0])
        self.size.set('10')
        self.label.pack(padx=20, pady=20)
        self.option.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.spinbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def set_font(self, *args):
        # get full families list
        # tk.font.families()
        family = self.family.get()
        size = self.size.get()
        self.label.config(font=(family,size))

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Using the options database

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Options demo')
        self.option_add('*font', 'helvetica 10')
        self.option_add('*header.font', 'helvetica 18 bold')
        self.option_add('*subtitle.font', 'helvetica 14 italic')
        self.option_add('*Button.foreground', 'blue')
        self.option_add('*Button.background', 'white')
        self.option_add('*Button.activeBackground', 'gray')
        self.option_add('*Button.activeForeground', 'black')
    
        self.create_label(name='header', text='This is the header')
        self.create_label(name='subtitle', text='This is the header')
        self.create_label(text='This is a paragraph')
        self.create_label(text='This is another paragraph')
        self.create_button(text='See more')
    
    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
    
    def create_button(self, **options):
        tk.Button(self, **options).pack(padx=5, pady=5, anchor=tk.E)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Changing the cursor icon

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cursors demo')
        self.resizable(0, 0)
        self.label = tk.Label(self, text='Click the button to start')
        self.btn_launch = tk.Button(self, text='Start!',
            command=self.perform_action)
        self.btn_help = tk.Button(self, text='Help',
            cursor='question_arrow')
        btn_opts = {'side': tk.LEFT, 'expand': True, 'fill': tk.X,
            'ipadx': 30, 'padx': 20, 'pady':5}
        self.label.pack(pady=10)
        self.btn_launch.pack(**btn_opts)
        self.btn_help.pack(**btn_opts)
    
    def perform_action(self):
        self.config(cursor='watch')
        self.btn_launch.config(state=tk.DISABLED)
        self.btn_launch.config(state=tk.DISABLED)
        self.label.config(text='Working...')
        self.after(3000, self.end_action)
    
    def end_action(self):
        self.config(cursor='arrow')
        self.btn_launch.config(state=tk.NORMAL)
        self.btn_launch.config(state=tk.NORMAL)
        self.label.config(text='Done!')

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""    

# Introducing the Text widget

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text demo")
        self.resizable(0, 0)
        self.text = tk.Text(self, width=50, height=10)
        self.btn_clear = tk.Button(self, text="Clear text",
        command=self.clear_text)
        self.btn_insert = tk.Button(self, text="Insert text",
        command=self.insert_text)
        self.btn_print = tk.Button(self, text="Print selection",
        command=self.print_selection)
        self.text.pack()
        self.btn_clear.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_insert.pack(side=tk.LEFT, expand=True, pady=10)
        self.btn_print.pack(side=tk.LEFT, expand=True, pady=10)

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def insert_text(self):
        self.text.insert(tk.INSERT, "Hello, world")

    def print_selection(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            content = self.text.get(*selection)
            print(content)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Adding tags to the Text widget

import webbrowser

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text tags demo")
        self.text = tk.Text(self, width=50, height=10)
        self.btn_link = tk.Button(self, text="Add hyperlink",
        command=self.add_hyperlink)
        self.text.tag_config("link", foreground="blue", underline=1)
        self.text.tag_bind("link", "<Button-1>", self.open_link)
        self.text.tag_bind("link", "<Enter>",
        lambda _: self.text.config(cursor="hand2"))
        self.text.tag_bind("link", "<Leave>",
        lambda e: self.text.config(cursor=""))
        self.text.pack()
        self.btn_link.pack(expand=True)

    def add_hyperlink(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.text.tag_add("link", *selection)

    def open_link(self, event):
        position = "@{},{} + 1c".format(event.x, event.y)
        index = self.text.index(position)
        prevrange = self.text.tag_prevrange("link", index)
        url = self.text.get(*prevrange)
        webbrowser.open(url)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""


## Dialogs and Menus


# Showing alert dialogs

import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_info = tk.Button(self, text='Show Info',
            command=self.show_info)
        btn_warn = tk.Button(self, text='Show Warning',
            command=self.show_warning)
        btn_error = tk.Button(self, text='Show Error',
            command=self.show_error)
        
        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_info.pack(**opts)
        btn_warn.pack(**opts)
        btn_error.pack(**opts)
    
    def show_info(self):
        msg = 'Your user preferences have been saved'
        mb.showinfo('Information', msg)
    
    def show_warning(self):
        msg = 'Temporary files have not been correctly removed'
        mb.showwarning('Warning', msg)
    
    def show_error(self):
        msg = 'The application has encountered an unknown error'
        mb.showerror('Error', msg)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Asking for user confirmation

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_button(mb.askyesno, 'Ask Yes/No', 'Returns True or False')
        self.create_button(mb.askquestion, 'Ask a question', 'Returns \'Yes\' or \'No\'')
        self.create_button(mb.askokcancel, 'Ask Ok/Cancel', 'Returns True or False')
        self.create_button(mb.askretrycancel, 'Ask Retry/Cancel', 'Returns True or False')
        self.create_button(mb.askyesnocancel, 'Ask Yes/No/Cancel', 'Returns True, False or None')

    def create_button(self, dialog, title, message):
        command = lambda: print(dialog(title, message))
        btn = tk.Button(self, text=title, command=command)
        btn.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Choosing files and directories

import tkinter.filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text='Choose file',
            command=self.choose_file)
        btn_dir = tk.Button(self, text='Choose directory',
            command=self.choose_directory)
        btn_file.pack(padx=60, pady=10)
        btn_dir.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("Plain text files", "*.txt"),('Comma seperated values', '.*csv'))
        my_file = fd.askopenfile(title="Open file", filetypes=filetypes)
        # check whether the dialog hasn't been 
        # dismissed before calling the file methods
        if my_file:
            print(my_file.readlines())
            my_file.close()
        """filetypes = (('Plain text files', '*.txt'), ('Python files', '*.py'),
            ('Images', '*.jpg *.gif *.png'), ('All files', '*'))
        filename = fd.askopenfilename(title='Open file', initialdir='/',
            filetypes=filetypes, multiple=True)
        if filename: print(filename)"""
    
    def choose_directory(self):
        directory = fd.askdirectory(title='Open directory', initialdir='/')
        if directory: print(directory)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Saving data into a file

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = tk.Text(self, height=10, width=50)
        self.btn_save = tk.Button(self, text='Save', command=self.save_file)

        self.text.pack()
        self.btn_save.pack(pady=10, ipadx=5)
    
    def save_file(self):
        contents = self.text.get(1.0, tk.END)
        new_file = fd.asksaveasfile(title='Save file',
            defaultextension='.txt', filetypes=(('Text files', '*.txt'),))
        
        if new_file:
            new_file.write(contents)
            new_file.close()

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Creating a menu bar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label='New file')
        file_menu.add_command(label='Open')
        file_menu.add_separator()
        file_menu.add_command(label='Save')
        file_menu.add_command(label='Save as...')
        
        menu.add_cascade(label='File', menu=file_menu)
        menu.add_command(label='About')
        menu.add_command(label='Quit', command=self.destroy)
        # we attach the menu to the top-level window by calling
        self.config(menu=menu)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Using variables in menus

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.checked = tk.BooleanVar()
        self.checked.trace('w', self.mark_checked)
        self.radio = tk.StringVar()
        self.radio.set('1')
        self.radio.trace('w', self.mark_radio)

        menu = tk.Menu(self)
        submenu = tk.Menu(menu, tearoff=0)
        
        submenu.add_checkbutton(label='Checkbutton', onvalue=True,
            offvalue=False, variable=self.checked)
        submenu.add_separator()
        submenu.add_radiobutton(label='Radio 1', value='1',
            variable=self.radio)
        submenu.add_radiobutton(label='Radio 2', value='2',
            variable=self.radio)
        submenu.add_radiobutton(label='Radio 3', value='3',
            variable=self.radio)
        
        menu.add_cascade(label='Options', menu=submenu)
        menu.add_command(label='Quit', command=self.destroy)
        self.config(menu=menu)
    
    def mark_checked(self, *args):
        print(self.checked.get())

    def mark_radio(self, *args):
        print(self.radio.get())

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# Displaying context menus

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Cut", command=self.cut_text)
        self.menu.add_command(label="Copy", command=self.copy_text)
        self.menu.add_command(label="Paste", command=self.paste_text)
        self.menu.add_command(label="Delete", command=self.delete_text)
        self.text = tk.Text(self, height=10, width=50)
        self.text.bind("<Button-3>", self.show_popup)
        self.text.pack()

    def show_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def cut_text(self):
        self.copy_text()
        self.delete_text()

    def copy_text(self):
        # this function gets the current selection
        # and adds it to the clipboard
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.clipboard_clear()
            self.clipboard_append(self.text.get(*selection))
            
    def paste_text(self):
        # the function inserts the clipboard contents into the 
        # insertion cursor position, defined by the INSERT index

        # wrap in try except block, incase the clipboard is empty
        try:
            self.text.insert(tk.INSERT, self.clipboard_get())
        except tk.TclError:
            pass

    def delete_text(self):
        # doesn't interact with the clipboard, but removes
        # the contents of the current selection
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.text.delete(*selection)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Opening a secondary window

# The root Tk instance represents the main window of our GUI—when it is
# destroyed, the application quits and the event mainloop finishes.
# However, there is another Tkinter class to create additional top-level
# windows in our application, called Toplevel. You can use this class to display
# any kind of window, from custom dialogs to wizard forms

# the Toplevel widget creates a new top-level window, which acts as a
# parent container like th Tk instance does.
# Unlike the Tk class, you can instantiate as many top-level windows as you like

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text='This is another window')
        self.button = tk.Button(self, text='Close', command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text='Open new window', command=self.open_window)
        self.btn.pack(padx=50, pady=20)
    
    def open_window(self):
        window = Window(self)
        # the grab_set method prevents users from interacting with 
        # the main window until this one is closed
        window.grab_set()

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Handling window deletion

import tkinter.messagebox as mb

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # In Tkinter, we can detect when a window is about to be closed by registering
        # a handler function for the WM_DELETE_WINDOW protocol. This can be triggered
        # by clicking on the X button of the title bar on most desktop environments
        self.protocol("WM_DELETE_WINDOW", self.confirm_delete)
        self.label = tk.Label(self, text="This is another window")
        self.button = tk.Button(self, text="Close",
        command=self.destroy)
        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

    def confirm_delete(self):
        message = "Are you sure you want to close this window?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text='Open new window', command=self.open_window)
        self.btn.pack(padx=50, pady=20)
    
    def open_window(self):
        window = Window(self)
        # the grab_set method prevents users from interacting with 
        # the main window until this one (top level window) is closed
        window.grab_set()

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Passing variables between windows

# Two different windows may need to share information during program
# execution. While this data might be saved to disk and read from the window
# that consumes it, in some circumstances it is more straightforward to handle
# it in memory and simply pass this information as variables.

from collections import namedtuple

User = namedtuple('User', ['username', 'password', 'user_type'])

class UserForm(tk.Toplevel):
    def __init__(self, parent, user_type):
        super().__init__(parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.user_type = user_type

        label = tk.Label(self, text="Create " + user_type.lower() + \
            '\'s account')
        entry_name = tk.Entry(self, textvariable=self.username)
        entry_pass = tk.Entry(self, textvariable=self.password,
        show="*")
        btn = tk.Button(self, text="Submit", command=self.destroy)
        label.grid(row=0, columnspan=2)
        tk.Label(self, text="Username:").grid(row=1, column=0)
        tk.Label(self, text="Password:").grid(row=2, column=0)
        entry_name.grid(row=1, column=1)
        entry_pass.grid(row=2, column=1)
        btn.grid(row=3, columnspan=2)

    def open(self):
        self.grab_set()
        # the wait_window() method is what actually stops the execution and prevents
        # us from returning the data before the form has been modified
        self.wait_window()
        username = self.username.get()
        password = self.password.get()
        return User(username, password, self.user_type)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        user_types = ("Administrator", "Supervisor", "Regular user")
        self.user_type = tk.StringVar()
        self.user_type.set(user_types[0])

        label = tk.Label(self, text="Please, select the type of user")
        radios = [tk.Radiobutton(self, text=t, value=t, \
        variable=self.user_type) for t in user_types]
        btn = tk.Button(self, text="Create user",
        command=self.open_window)

        label.pack(padx=10, pady=10)
        for radio in radios:
            radio.pack(padx=10, anchor=tk.W)
        btn.pack(pady=10)

    def open_window(self):
        window = UserForm(self, self.user_type.get())
        user = window.open()
        print(user)


if __name__ == '__main__':
    app = App()
    app.mainloop()



# Object-Oriented Programming and MVC (Model-View-Controller) pattern. 

# In short, this pattern proposes three components into which we can divide our GUI: a model that holds the
# application data, a view that displays this data, and a controller that
# handles user events and connects the view with the model.


# Structuring our data with a class

# --snip--


# Asynchronous Programming

# scheduling actions


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
            text='Wait 5 seconds')
        self.button.pack(padx=20, pady=20)
    
    def start_action(self):
        self.button.config(state=tk.DISABLED)
        time.sleep(5)
        self.button.config(state=tk.NORMAL)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
            text='Wait 5 seconds')
        self.button.pack(padx=20, pady=20)
    
    def start_action(self):
        self.button.config(state=tk.DISABLED)
        self.after(5000, lambda : self.button.config(state=tk.NORMAL))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
        text="Wait 5 seconds")
        self.button.pack(padx=50, pady=20)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.run_action)
        print(threading.main_thread().name)
        print(thread.name)
        thread.start()
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)

    def run_action(self):
        print("Starting long running action...")
        time.sleep(5)
        print("Long running action finished!")

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

class RandomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simulate latency
        time.sleep(3)
        # Write response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Write response body
        body = json.dumps({'random': random.random()})
        self.wfile.write(bytes(body, "utf8"))

def main():
    """Starts the HTTP server on port 8080"""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RandomRequestHandler)
    httpd.serve_forever()

"""
if __name__ == "__main__":
    main()
"""

import json
import threading
import urllib.request
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HTTP request example")
        self.label = tk.Label(self, text="Click 'Start' to get a random value")
        self.button = tk.Button(self, text="Start",
        command=self.start_action)
        self.label.pack(padx=60, pady=10)
        self.button.pack(pady=10)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction()
        thread.start()
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            text = "Random value: {}".format(thread.result)
            self.label.config(text=text)
            self.button.config(state=tk.NORMAL)

class AsyncAction(threading.Thread):
    def run(self):
        self.result = None
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        url = "http://localhost:8080"
        with urllib2.Request.opener.open(url) as f:
            obj = json.loads(f.read().decode("utf-8"))
            self.result = obj["random"]

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""


import time
import queue
import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Progressbar example")
        self.queue = queue.Queue()
        self.progressbar = ttk.Progressbar(self, length=300,
        orient=tk.HORIZONTAL)
        self.button = tk.Button(self, text="Start",
        command=self.start_action)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction(self.queue, 20)
        thread.start()
        self.poll_thread(thread)

    def poll_thread(self, thread):
        self.check_queue()
        if thread.is_alive():
            self.after(100, lambda: self.poll_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)
            mb.showinfo("Done!", "Async action completed")

    def check_queue(self):
        while self.queue.qsize():
            try:
                step = self.queue.get(0)
                self.progressbar.step(step * 100)
            except queue.Empty: pass

class AsyncAction(threading.Thread):
    def __init__(self, queue, steps):
        super().__init__()
        self.queue = queue
        self.steps = steps
    def run(self):
        for _ in range(self.steps):
            time.sleep(1)
            self.queue.put(1 / self.steps)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

# Cancelling scheduled actions

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action, text='Wait 5 seconds')
        self.cancel = tk.Button(self, command=self.cancel_action,
            text='Stop', state=tk.DISABLED)
        self.button.pack(padx=30, pady=20, side=tk.LEFT)
        self.cancel.pack(padx=30, pady=20, side=tk.LEFT)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        self.cancel.config(state=tk.NORMAL)
        self.scheduled_id = self.after(5000, self.init_buttons)
    
    def init_buttons(self):
        self.button.config(state=tk.NORMAL)
        self.cancel.config(state=tk.DISABLED)
    
    def cancel_action(self):
        print('Canceling scheduled', self.scheduled_id)
        self.after_cancel(self.scheduled_id)
        self.init_buttons()

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()

"""

# Handling idle tasks

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self, command=self.start_action,
            text='Wait 1 seconds')
        self.button.pack(padx=30, pady=20)
    
    def start_action(self):
        self.button.config(state=tk.DISABLED)
        self.update_idletasks()
        time.sleep(1)
        self.button.config(state=tk.NORMAL)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

import subprocess, threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Ping!",
        command=self.do_ping)
        self.output = tk.Text(self, width=80, height=15)
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        self.button.grid(row=0, column=1, padx=5, pady=5)
        self.output.grid(row=1, column=0, columnspan=2,
        padx=5, pady=5)

    def do_ping(self):
        self.button.config(state=tk.DISABLED)
        thread = AsyncAction(self.entry.get())
        thread.start()
        self.poll_thread(thread)

    def poll_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.poll_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)
            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, thread.result)

class AsyncAction(threading.Thread):
    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def run(self):
        self.result = subprocess.run(["ping", self.ip], shell=True,
            stdout=subprocess.PIPE).stdout

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""


# Canvas and Graphics


# understanding the coordinate system

# To draw graphic items on a canvas, we will need to specify 
# their position using a coordinate system


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Basic canvas')

        self.canvas = tk.Canvas(self, bg='pink')
        self.label = tk.Label(self)
        self.canvas.bind('<Motion>', self.mouse_motion)

        self.canvas.pack()
        self.label.pack()
    
    def mouse_motion(self, event):
        x, y = event.x, event.y
        text= 'Mouse position: ({}, {})'.format(x,y)
        self.label.config(text=text)

# drawing lines and arrows

# --snip--


# Writing text on a canvas


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Canvas text items')
        self.geometry('300x100')

        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.canvas = tk.Canvas(self, bg='white')

        self.entry.pack(pady=5)
        self.canvas.pack()
        self.update()

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        options = {'font': 'courier', 'fill': 'blue', 'activefill': 'red'}
        self.text_id = self.canvas.create_text((w/2, h/2), **options)
        self.var.trace('w', self.write_text)
    
    def write_text(self, *args):
        self.canvas.itemconfig(self.text_id, text=self.var.get())

# Placing the text bt its upper-left corner

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Canvas text items')
        self.geometry('300x100')

        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.canvas = tk.Canvas(self, bg='white')

        self.entry.pack(pady=5)
        self.canvas.pack()
        self.update()

        options = {'font': 'courier', 'fill': 'blue', 
            'anchor' : tk.NW, 'activefill': 'red'}
        self.text_id = self.canvas.create_text((0,0), **options)
        self.var.trace('w', self.write_text)
    
    def write_text(self, *args):
        self.canvas.itemconfig(self.text_id, text=self.var.get())


# setiing line wrapping

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Canvas text items')
        self.geometry('300x100')

        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.canvas = tk.Canvas(self, bg='white')

        self.entry.pack(pady=5)
        self.canvas.pack()
        self.update()

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        options = {'font': 'courier', 'fill': 'blue', 'width': 70}
        self.text_id = self.canvas.create_text((w/2, h/2), **options)
        self.var.trace('w', self.write_text)
    
    def write_text(self, *args):
        self.canvas.itemconfig(self.text_id, text=self.var.get())

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()
"""

# adding shapes to the canvas

# --snip--

# Finding items by their position

# --snip--



# Themed Widgets

# replacing basic widget classes

import tkinter.ttk as ttk

class App(tk.Tk):
    greetings = ('Hello', 'Ciao', 'Hola')

    def __init__(self):
        super().__init__()
        self.title('Tk Themed widgets')

        var = tk.StringVar()
        var.set(self.greetings[0])
        label_frame = ttk.LabelFrame(self, text='Choose a greeting')
        for greeting in self.greetings:
            radio = ttk.Radiobutton(label_frame, text=greeting,
                variable=var, value=greeting)
            
            radio.pack()
        
        frame = ttk.Frame(self)
        label = ttk.Label(frame, text='Enter your name')
        entry = ttk.Entry(frame)

        command = lambda: print('{}, {}!'.format(var.get(), entry.get()))
        button = ttk.Button(frame, text='Greet', command=command)

        label.grid(row=0, column=0, padx=5, pady=5)
        entry.grid(row=0, column=1, pady=5)
        button.grid(row=1, column=0, columnspan=2, pady=5)

        label_frame.pack(side=tk.LEFT, padx=10, pady=10)
        frame.pack(side=tk.LEFT, padx=10, pady=10)


# creating an editable drop-down with combobox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tk Combobox')
        colors = ('Purple', 'Yellow', 'Red', 'Blue')

        self.label = ttk.Label(self, text='Please select a color')
        self.combo = ttk.Combobox(self, values=colors)
        btn_submit = ttk.Button(self, text='Submit', 
            command=self.display_color)
        btn_clear = ttk.Button(self, text='Clear',
            command=self.clear_color)
        
        self.combo.bind('<<ComboboxSelected>>', self.display_color)

        self.label.pack(pady=10)
        self.combo.pack(side=tk.LEFT, padx=10, pady=5)
        btn_submit.pack(side=tk.TOP, padx=10, pady=5)
        btn_clear.pack(padx=10, pady=5)

    def display_color(self, *args):
        color = self.combo.get()
        print(f'You selected {color}')
    
    def clear_color(self):
        self.combo.set('')

# Using the Treeview widget

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ttk Treeview')

        columns = ('#1', '#2', '#3')
        self.tree = ttk.Treeview(self, show='headings', columns=columns)
        self.tree.heading('#1', text='Last name')
        self.tree.heading('#2', text='First name')
        self.tree.heading('#3', text='Email')
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL,
            command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        with open(r'C:\Users\Training\Documents\CODES\GUI\contacts.csv', newline='') as f:
            for contact in csv.reader(f):
                self.tree.insert('', tk.END, values=contact)
        self.tree.bind('<<TreeviewSelect>>', self.print_selection)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
    
    def print_selection(self, event):
        # print(self.tree.selection)
        for selection in self.tree.selection():
            # print(selection)
            item = self.tree.item(selection)
            print('itemm:', item)
            last_name, first_name, email = item['values'][0:3]
            text = 'Selection: {}, {} <{}>'
            print(text.format(last_name, first_name, email))

# Displaying tabbable panes with Notebook

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ttk Treeview')

        todos = { 
            'Home': ['Do the laundry', 'Go grocery shopping'],
            'Work': ['Install Python', 'Learn Tkinter', 'Reply emails'],
            'Vacations': ['Relax']
        }

        self.notebook = ttk.Notebook(self, width=250, height=100)
        self.label = ttk.Label(self)
        for key, value in todos.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=key, underline=0,
                sticky=tk.NE + tk.SW)
            
            for text in value:
                ttk.Label(frame, text=text).pack(anchor=tk.W)
        
        self.notebook.pack()
        self.label.pack(anchor=tk.W)
        self.notebook.enable_traversal()
        self.notebook.bind('<<NotebookTabChanged>>', self.select_tab)
    
    def select_tab(self, event):
        tab_id = self.notebook.select()
        print(f'Tab Id: {tab_id}')
        frame = self.nametowidget(tab_id)
        print(f'Frame: {frame}')
        tab_name = self.notebook.tab(tab_id, 'text')
        text = 'Your current selection is: {}'.format(tab_name)
        self.label.config(text=text)

"""
if __name__ == '__main__':
    app = App()
    app.mainloop()

"""


# Applying Ttk Styling

# --snip--

# creating a datepicker

# --snip--









































































































































