import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, date
import pytz


timezones = [i.replace('/',', ') for i in pytz.common_timezones]
selected_timezones = []


class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Clock')
        self.resizable(0,0)
        self.geometry('350x340')
        self['bg'] = 'black'
        self.frame_1 = tk.Frame(self,bg='black')
        self.frame_2 = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.frame_2, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame_2, 
            bg='black', fg='white',font=('Courier', 11),
            width= 33, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
       
        self.listbox.pack(side=tk.LEFT,expand='YES',fill=tk.X)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.time_label = tk.Label(self.frame_1, text=datetime.now().strftime('%H:%M:%S'),
            bg='black', fg='white',font=('Courier', 21))
        self.time_label.pack(padx=2,pady=2)
        self.date_label = tk.Label(self.frame_1,text=self.current_date(),
            bg='black', fg='white',font=('Courier', 16))
        self.date_label.pack(padx=2,pady=2)
        self.frame_1.pack(padx=4,pady=25)
        self.frame_2.place(x=15,y=149)

        # schedule a time update every second
        self.time_label.after(1000, self.update_time)

        self.timezone_button = ttk.Button(self.frame_1, text='Select a timezone',
            command=self.on_click)
        self.timezone_button.pack(padx=2,pady=16)

    def current_time(self):
        time = datetime.now().strftime('%H:%M:%S')
        return time
    
    def current_date(self):
        # get today's date and weekday
        today_date, weekday = date.today(), datetime.today().weekday()
        date_display = today_date.strftime('%B %d, %Y')
        weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
            'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        for i, j in weekdays.items():
            if weekday == j:
                return  f'{i} {date_display}'
    
    def update_time(self):
        '''update the time every second'''
        self.time_label.configure(text=self.current_time())

        # schedule another time update
        self.time_label.after(1000, self.update_time)
    
    def on_click(self):
        result = DisplayTimezones(self).returnValue()
        print('result', result)
        self.listbox.insert(0, *[result])


class DisplayTimezones(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('My Clock')
        self['bg'] = 'black'
        self.geometry('300x246')
        self.resizable(0,0)
        self.frame = tk.Frame(self, bg='black')
        self.label = tk.Label(self.frame, text='Select a timezone',
            bg='black', fg='white',font=('Times', 14))
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame,selectmode='single', 
            bg='black', fg='white', font=('Helvetica', 11),
            width= 33, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        # remove underscores from each timezone
        zones = [i.replace('_',' ') for i in timezones]
        self.listbox.insert(0, *zones)
        self.pick_btn = ttk.Button(self, text="OK", command=self.destroy)
    
        self.frame.pack()
        self.label.pack()
        self.listbox.pack(side=tk.LEFT,expand='YES',fill=tk.X)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.pick_btn.place(x=40,y=217)
        
        # add binding
        self.listbox.bind('<<ListboxSelect>>', self.getSelection)

    # function associated with binding
    def getSelection(self, event):
        widget = event.widget
        timezones = [i.replace('/',', ') for i in pytz.common_timezones]
        selection = widget.curselection()
        timezone_index = timezones[int(''.join(map(str,selection)))]
        
        # get timezone current time
        timezone_current_time = datetime.now(pytz.timezone(timezone_index.replace(', ', '/')))
        display_format = timezone_current_time.strftime("%H:%M")
        self.selected_timezones= [*[self.listbox.get(i) for i in selection], display_format]
        print(f'The time in {self.selected_timezones[0]}, is {self.selected_timezones[1]}')
        print('SELECTED TIMEZONES:', self.selected_timezones)
        

    # separate function for wait_window and the return of the selection
    def returnValue(self):
        tk.Toplevel.wait_window(self)
        return self.selected_timezones
    

if __name__ == '__main__':
    app = Clock()
    app.mainloop()

