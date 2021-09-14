# practice!!
import winsound, time, tkinter
import tkinter.messagebox

class MyInfo():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the buttons in the bottom frame
        self.showInfo = tkinter.Button(self.bottom_frame,
            text='Show Info', command=self.display_info)
        self.quit = tkinter.Button(self.bottom_frame,
            text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.showInfo.pack(side='left')
        self.quit.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enetr the loop
        tkinter.mainloop()

    # the display_info is the callback function
    def display_info(self):
        # create the label widget in top frame
        self.label_1 = tkinter.Label(self.top_frame,
            text='Steven Marcus')
        self.label_2 = tkinter.Label(self.top_frame,
            text='274 Baily Drive')
        self.label_3 = tkinter.Label(self.top_frame,
            text='Waynesville, NC 27999')
        
        # pack the widgets
        self.label_1.pack(side='top')
        self.label_2.pack(side='top')
        self.label_3.pack(side='top')

# cc = MyInfo()

import tkinter.font


class display():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the frame
        self.top_frame = tkinter.Frame(self.main_window)
        #self.bottom_frame = tkinter.Frame(self.main_window)

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.top_frame, width=200,height=200)
        
        # draw a rectangle
        self.canvas.create_rectangle(20,20,180,180)

        # make a text of your name
        self.canvas.create_text(100,100,text='ELLa')

        # pack the widget
        self.canvas.pack()

        # pack the frame
        self.top_frame.pack()

        # start the mainloop
        tkinter.mainloop()

# cc = display()

class dd():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create frame
        self.text = tkinter.Label(self.main_window,text='FFFF',
            bg='pink',fg='white',anchor=tkinter.E)
        
        self.text.pack()
        tkinter.mainloop()

# x = dd()


class latinTranslator():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create a frame for the buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the buttons
        self.b1 = tkinter.Button(self.top_frame,text='sinister',command=self.b1_descr_label)
        self.b2 = tkinter.Button(self.mid_frame,text='dexter',command=self.b2_descr_label)
        self.b3 = tkinter.Button(self.bottom_frame,text='medium',command=self.b3_descr_label)


        self.b1.pack(side='top')
        self.b2.pack(side='top')
        self.b3.pack(side='top')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def b1_descr_label(self):
        self.b1_translate = tkinter.Label(self.top_frame,text='sinister means')
        self.value = tkinter.StringVar()
        self.b1_translated = tkinter.Label(self.top_frame,textvariable=self.value)
        self.value.set('left')
        self.b1_translate.pack(side='left')
        self.b1_translated.pack(side='left')

    def b2_descr_label(self):
        self.b2_translate = tkinter.Label(self.mid_frame,text='dexter means')
        self.value = tkinter.StringVar()
        self.b2_translated = tkinter.Label(self.mid_frame,textvariable=self.value)
        self.value.set('right')
        self.b2_translate.pack(side='left')
        self.b2_translated.pack(side='left')

    def b3_descr_label(self):
        self.b3_translate = tkinter.Label(self.bottom_frame,text='medium means')
        self.value = tkinter.StringVar()
        self.b3_translated = tkinter.Label(self.bottom_frame,textvariable=self.value)
        self.value.set('center')
        self.b3_translate.pack(side='left')
        self.b3_translated.pack(side='left')

# vv = latinTranslator()

class MilesPerGallon():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create three frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.mid_1_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the widgets in top frame
        self.label_1 = tkinter.Label(self.top_frame,text='Enter the number of gallons:')
        self.label_1_entry = tkinter.Entry(self.top_frame, width=10)

        # create widget in mid frame
        self.label_2 = tkinter.Label(self.mid_frame,text='Enter the number of miles:')
        self.label_2_entry = tkinter.Entry(self.mid_frame, width=10)

        # create widget in mid_1 frame
        self.mpg = tkinter.Label(self.mid_1_frame,text='MPG:')
        # stringvar object
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid_1_frame,textvariable=self.value)

        # create the buttons in the bottom frame
        self.button_1 = tkinter.Button(self.bottom_frame,
            text='Calculate MPG',command=self.calc_mpg)
        self.button_2 = tkinter.Button(self.bottom_frame,
            text='Quit',command=self.main_window.destroy)
        
        # pack the widgets
        self.label_1.pack(side='left')
        self.label_1_entry.pack(side='left')
        self.label_2.pack(side='left')
        self.label_2_entry.pack(side='left')
        self.mpg.pack(side='left')
        self.mpg_label.pack(side='left')

        # pack the buttons
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid_1_frame.pack()
        self.bottom_frame.pack()

        # enter the mainloop
        tkinter.mainloop()

    def calc_mpg(self):
        self.car_mpg = round((float(self.label_1_entry.get()) / float(self.label_2_entry.get())),2)
        self.value.set(self.car_mpg)

# ll = MilesPerGallon()

import tkinter.font
import tkinter.messagebox

class dd():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('420x420')
        self.main_window.resizable(width=False,height=False)
        #self.main_window['bg'] = 'purple'
        # self.main_window.configure(bg='blue')
        self.main_window['background']='#856ff8'

        self.top_frame = tkinter.Frame(self.main_window)
        
        # create font
        myFont = tkinter.font.Font(family='Times New Roman', size=21)
        # create a button
        self.button = tkinter.Button(self.top_frame,text='Convert',command=self.convert,
            bg='black',fg='white',width=6,height=1,font=myFont)
        
        # pack the button
        self.button.pack()

        # pack the frame
        self.top_frame.pack()

        # enter the mainloop
        tkinter.mainloop()

    def convert(self):
        tkinter.messagebox.showinfo('DISPLAY','HEYYYY!!')
        # create three frames

        """
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,bg='blue',
            width=200,height=200)
        self.myFont = tkinter.font.Font(family='Arial', size=14)
        self.canvas.create_text(100,100,
            text='Celcius To Fahrenheit Converter',anchor=tkinter.NW)

        # create the widget in top frame


        # pack the widget
        self.canvas.pack()

        # pack the frames 
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()"""

        

# converter = dd()


class TemperatureConverter():
    def __init__(self):
        # create root window
        self.main_window = tkinter.Tk()

        # add root window title and dimension 
        self.main_window.title('Celcius To Fahrenheit Converter')

        # set the geometry(widthxheight) 
        self.main_window.geometry('500x250')
        
        # not resizable
        self.main_window.resizable(width=False,height=False)

        # set background color
        #self.main_window.configure(bg='blue')

        # create three frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create font to be used in label widget
        myFont = tkinter.font.Font(family='Arial', size=13, slant='italic')

        # create label widget in top frame
        self.label = tkinter.Label(self.top_frame,text='Enter the temperature in Celcius')
        # create the entry widget in the top frame
        self.label_entry = tkinter.Entry(self.top_frame,width=10)
        # create the widgets in the middle frame
        self.label_2 = tkinter.Label(self.mid_frame,text='Temperature in Fahrenheit:')
        # create the stringvar object
        self.label_2_var = tkinter.StringVar()
        # ...
        self.temp_label_2 = tkinter.Label(self.mid_frame,textvariable=self.label_2_var)

        # create the buttons
        self.button_1 = tkinter.Button(self.bottom_frame,text='Convert',
            command=self.convert_temp,bg='red',fg='yellow')
        self.button_2 = tkinter.Button(self.bottom_frame,text='Quit',font=myFont,
            command = self.main_window.destroy,fg='purple',bg='white')

        # pack the widgets
        self.label.pack(side='left')
        self.label_entry.pack(side='left')
        self.label_2.pack(side='left')
        self.temp_label_2.pack(side='left')

        # pack the buttons
        self.button_1.pack(side='left')
        self.button_2.pack(side='right')

        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
    
    # the callback function
    def convert_temp(self):
        self.temp_in_fahr = round((((9 / 5) * float(self.label_entry.get())) + 32),2)
        self.label_2_var.set(self.temp_in_fahr)

# cc = TemperatureConverter()


class CountdownTimer:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # set the geometry
        self.main_window.geometry('500x250')
        self.main_window.resizable(width=False,height=False)

        # make frames
        self.top_frame = tkinter.Frame(self.main_window).pack()
        self.mid_frame = tkinter.Frame(self.main_window).pack()
        self.bottom_frame = tkinter.Frame(self.main_window).pack()

        # make widget in top frame
        self.get_secs = tkinter.Label(self.top_frame,
            text='Number of seconds')
        self.get_secs.place(x=110,y=15)
        self.get_secs_entry = tkinter.Entry(self.top_frame, width=10)
        self.get_secs_entry.place(x=225,y=15)

        # widget in mid frame
        self.timer= tkinter.Label(self.mid_frame,text='00:00:00',
           font=('Arial', 59))
        self.timer.place(x=99,y=60)

        # button in bottom frame
        self.start_button = tkinter.Button(self.bottom_frame,text='Start',
            command=self.start)
        self.start_button.place(x=125,y=170)
        self.pause_button = tkinter.Button(self.bottom_frame,
            text='Pause', command = self.pause)
        self.pause_button.place(x=164,y=170)
        self.reset_button = tkinter.Button(self.bottom_frame,
            text='Reset', command = self.reset)
        self.reset_button.place(x=240,y=170)
        self.quit_button = tkinter.Button(self.bottom_frame,
            text='Quit', command = self.main_window.destroy)
        self.quit_button.place(x=356,y=170)

        # enter loop
        tkinter.mainloop()

    def start(self):
        self.state = True
        self.begin_timer()
    
    def pause(self):
        self.state = False
    
    def reset(self):
        self.state = False
        self.timer.config(text='00:00:00',font=('Arial', 59))
   
    def begin_timer(self):
        # get the number of seconds 
        no_of_secs = int(self.get_secs_entry.get())
        while no_of_secs  >-1:
            if self.state == True:
                if no_of_secs < 60:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = no_of_secs // 60
                    secs = no_of_secs % 60
                    # format the hours, minutes
                    # and seconds to be displayed
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                    no_of_secs -= 1
                    # decrement the number of seconds by one
                elif 60 <= no_of_secs < 3600:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = no_of_secs // 60
                    secs = no_of_secs % 60
                    # format the hours, minutes
                    # and seconds to be displayed
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                    no_of_secs -= 1
                    # decrement the number of seconds by one
                elif 3600 <= no_of_secs <= 86400:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = (no_of_secs % 3600) // 60
                    secs = (no_of_secs % 3600) % 60
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                    no_of_secs -= 1
                
    
yy = CountdownTimer()




def begin_timer(self):
        # get the number of seconds 
        secs = int(self.get_secs_entry.get())
        for no_of_secs in range(secs,-1,-1):
            if self.state == True:
                if no_of_secs < 60:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = no_of_secs // 60
                    secs = no_of_secs % 60
                    # format the hours, minutes
                    # and seconds to be displayed
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                    # decrement the number of seconds by one
                elif 60 <= no_of_secs < 3600:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = no_of_secs // 60
                    secs = no_of_secs % 60
                    # format the hours, minutes
                    # and seconds to be displayed
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                    # decrement the number of seconds by one
                elif 3600 <= no_of_secs <= 86400:
                    # calculate the number of hours, minutes and seconds
                    hrs = no_of_secs // 3600
                    mins = (no_of_secs % 3600) // 60
                    secs = (no_of_secs % 3600) % 60
                    display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                    self.timer.config(text=display_format)
                    # update the mid frame after 
                    # decrementing the number of seconds
                    self.timer.update()
                    time.sleep(1)
                
    
yy = CountdownTimer()
