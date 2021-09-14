import tkinter
import tkinter.messagebox

# Using The Tkinter Module

def main():
    """Display an empty window"""
    mainWindow = tkinter.Tk()
    tkinter.mainloop()

#main()

class MYGUI():
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # create two Label widgets 
        self.label_1 = tkinter.Label(self.main_window, 
            text='Hello World!')
        self.label_2 = tkinter.Label(self.main_window, 
            text='This Is My GUI Program')
        
        # call both label widgets' pack method
        # side='left' argument used to change 
        # the layout widgets
        self.label_1.pack(side='left')
        self.label_2.pack(sid='left')

        # enter the tkinter loop
        tkinter.mainloop()

# object of class 
# my_gui = MYGUI()


class Gui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames, one for the top of the 
        # window, and one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three Label widgtes for the top frame
        self.label_1 = tkinter.Label(self.top_frame, text='Winken')
        self.label_2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label_3 = tkinter.Label(self.top_frame, text='Nod')

        # pack the labels in the top frame
        # use side='top' argument to stack them 
        # one on top of the other
        self.label_1.pack(side='top')
        self.label_2.pack(side='top')
        self.label_3.pack(side='top')

        # create three Label widgets for the bottom frame
        self.label_4 = tkinter.Label(self.bottom_frame, text='Winken')
        self.label_5 = tkinter.Label(self.bottom_frame, text='Blinken')
        self.label_6 = tkinter.Label(self.bottom_frame, text='Nod')

        # pack the labels in the bottom frame
        # use side='top' argument to stack them 
        # one on top of the other
        self.label_4.pack(side='left')
        self.label_5.pack(side='left')
        self.label_6.pack(side='left')

        # Yes, we have to pack the frame too!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

# my_guii = Gui()

class MyGui():
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button.
        # The do_something method should be executed when the 
        # user clicks the Button
        self.my_button = tkinter.Button(self.main_window,
            text='Click Me!!',command=self.do_something)
        
        # create a Quit button
        self.quit_button = tkinter.Button(self.main_window,
            text='Quit',command=self.main_window.destroy)

        # pack the Buttons
        self.my_button.pack()
        self.quit_button.pack()

        # enter the tkinter main loop
        tkinter.mainloop()
    
    # the do_something method is a callback function for the Button widget

    def do_something(self):
        # Display a info dialog box
        tkinter.messagebox.showinfo('Response',
            'Thanks for clicking the button')

# a_gui = MyGui()

# top = tkinter.Tk()

# B1 = tkinter.Button(top, text ="error", bitmap="error")
# B2 = tkinter.Button(top, text ="hourglass", bitmap="hourglass")
# B3 = tkinter.Button(top, text ="info", bitmap="info")
# B4 = tkinter.Button(top, text ="question", bitmap="question")
# B5 = tkinter.Button(top, text ="warning", bitmap="warning")
# B1.pack()
# B2.pack()
# B3.pack()
# B4.pack()
# B5.pack()
# top.mainloop()

# we use the label widget to display text in a window
# the pack method determines where a widget should be positioned and makes
# the widget visible when the main window is displayed 

# you call the pack method for each widget in a window

# a frame is a container that can hold other widgets 
# frames are used to organixe and arrange grouping of widgets in a window

# you use the Button widget to create a standard button in a window
# when the user clicks a button, a specified function or method is called

# an info dialog box is a simple window that displays a message to the 
# user, and has an OK button that dismisses the dialog box
# you can use the tkinter.messagebox module's showinfo function to display an info dialog box

# a callback function is a function or method that executes when the user clicks the button
# a callback function is also known as an event handler, 'cause it handles 
# the event that occurs when the user clicks the button

# GUI progrmas usually have a Quit button.. to make one
# you create a Button widget that calls the root widegt's destroy method
# a callback function

# an entry widget is a rectangular area that the user can type into
# you use the entry widget's get method to retrieve the data 
# that has ben typed into the widget, the get method returns a string
# so, it'll  have to be converted to the appropriate data type 

class KiloConverterGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames to group the widgets
        self.top_frame  = tkinter.Frame(self.main_window)
        self.bottom_frame  = tkinter.Frame(self.main_window)

        # create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
           text='Enter a disctance in kilometers:')
        #self.prompt_label = tkinter.Label(self.top_frame, 
            # text='2 * 4 =')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # create the button widgets for the button frame
        self.calc_button = tkinter.Button(self.bottom_frame,
        text='Convert',command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
            text='Quit',command=self.main_window.destroy)
        
        # pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # the convert button is a callback function 
    # for the Calculate button

    def convert(self):
        # get the value entered by user 
        # into the kilo widget
        kilo = float(self.kilo_entry.get())
        # answer = int(self.kilo_entry.get())
        # if answer == 8:
            # message = 'Got it!'
        # else: message = 'Wrong!'
        # convert kilometers to miles
        miles = kilo * 0.6214
        # display the result in an info dialog box
        tkinter.messagebox.showinfo('Results',
            '{} kilometers is equal to {}'.format(kilo, format(miles,'.2f')))
        # tkinter.messagebox.showinfo('Results', message)

# kilo_conv = KiloConverterGUI()

# stringVar can be used along with a Label widget to display data

class kiloConverter_2():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
            text='Enter a distance in kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # create widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame,
            text='Converted to miles:')
        
        # stringVar object

        self.value = tkinter.StringVar()
        
        # create a label and associate it with stringVar object
        # any value stored in the stringVar object will automatically be displayed

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        
        # pack the middle frame's widgets
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # create the button widgtes for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, 
            text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',
            command=self.main_window.destroy)
        
        # pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214, 2)

        # convert miles to a string and store it in the stringVar
        # this will automatically update the miles_label widget
        self.value.set(miles)

my_converter = kiloConverter_2()

class TestAvg():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create frames
        self.test_1_frame = tkinter.Frame(self.main_window)
        self.test_2_frame = tkinter.Frame(self.main_window)
        self.test_3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create widgets in test_1_frame
        self.prompt_label_1 = tkinter.Label(self.test_1_frame,
            text='Enter the score for Test 1:')
        self.test_1_entry = tkinter.Entry(self.test_1_frame, width=10)

        # pack widgets
        self.prompt_label_1.pack(side='left')
        self.test_1_entry.pack(side='left')

        # create widgets in test_2_frame
        self.prompt_label_2 = tkinter.Label(self.test_2_frame,
            text='Enter the score for Test 2:')
        self.test_2_entry = tkinter.Entry(self.test_2_frame, width=10)

        # pack widgets
        self.prompt_label_2.pack(side='left')
        self.test_2_entry.pack(side='left')

        # create widgets in test_3_frame
        self.prompt_label_3 = tkinter.Label(self.test_3_frame,
            text='Enter the score for Test 3:')
        self.test_3_entry = tkinter.Entry(self.test_3_frame, width=10)

        # pack widgets
        self.prompt_label_3.pack(side='left')
        self.test_3_entry.pack(side='left')

        # create widgets in avg_frame
        self.avg_prompt_label= tkinter.Label(self.avg_frame,
            text='Average:')
        
        self.studentAverage = tkinter.StringVar()

        self.average_label = tkinter.Label(self.avg_frame, 
            textvariable=self.studentAverage)

        # pack widgets
        self.avg_prompt_label.pack(side='left')
        self.average_label.pack(side='left')

        # create buttons in button_frame
        self.button_1 = tkinter.Button(self.button_frame, 
            text='Calculate Average', command=self.calculateAverage)
        self.button_2 = tkinter.Button(self.button_frame, 
            text='Quit', command=self.main_window.destroy)
        
        # pack buttons
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')

        # pack frames
        self.test_1_frame.pack()
        self.test_2_frame.pack()
        self.test_3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    def calculateAverage(self):
        # get each test score and compute the average
        try:
            test_1_score = float(self.test_1_entry.get())
            test_2_score = float(self.test_2_entry.get())
            test_3_score = float(self.test_3_entry.get())
        except ValueError:
            tkinter.messagebox.showinfo('Output', 'Invalid Input!')
        else:
            AVERAGE = (test_1_score + test_2_score + test_3_score) / 3
            self.studentAverage.set(format(AVERAGE, '.2f'))

student_avg = TestAvg()

# radio buttons normally appear in groups of two or more, and allows 
# the user to select one of several possible options
# you use the IntVar alongside the radio buttons

# check buttons which may appear alone or in groups, allows the user
# to make yes/no or on/off selections


class myGui():
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        # create two frames, one for the radio buttons
        # and another for the regular button widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create an IntVar object to use with the radio buttons
        self.radio_var = tkinter.IntVar()

        # set the intVar object to 0
        self.radio_var.set(0)

        # create the radio buttons widgets
        # in the top_frame
        self.rb1 = tkinter.Radiobutton(self.top_frame,
            text='Option 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
            text='Option 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
            text='Option 3', variable=self.radio_var, value=3)
        
        # pack the butons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # create an OK button and a Quit button
        self.ok_button = tkinter.Button(self.bottom_frame,
            text='OK',command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
            text='QUIT',command=self.main_window.destroy)
        
        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # start the main loop
        tkinter.mainloop()

    # the show_choce method is the callback for 
    # the OK button

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You selected Option ' +
            str(self.radio_var.get()))

myGUI = myGui()

class MiniQuiz:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.score = 0

        # make the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # make the label widget in top frame
        self.question = tkinter.Label(self.top_frame,
            text='7 * 9 = ')
        
        # pack the label widget
        self.question.pack(side='left')
        
        # make the intVar object for the
        # radio buttons
        self.radio_var = tkinter.IntVar()

        # set the intVar object to 1
        self.radio_var.set(1)

        # create the radio buttons
        self.rb1 = tkinter.Radiobutton(self.mid_frame,
            text='65', variable=self.radio_var, value=65)
        self.rb2 = tkinter.Radiobutton(self.mid_frame,
            text='56', variable=self.radio_var, value=56)
        self.rb3 = tkinter.Radiobutton(self.mid_frame,
            text='63', variable=self.radio_var, value=63)
        self.rb4 = tkinter.Radiobutton(self.mid_frame,
            text='61', variable=self.radio_var, value=61)
        
        # pack the buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()

        # create the other buttons in the 
        # bottom frame
        self.submit = tkinter.Button(self.bottom_frame,
            text='Submit', command=self.verify_answer)
        self.check_score = tkinter.Button(self.bottom_frame,
            text='Check Score', command=self.check_my_score)
        self.quit = tkinter.Button(self.bottom_frame,
            text='Quit', command=self.main_window.destroy)
        
        # pack buttons
        self.submit.pack(side='left')
        self.check_score.pack(side='left')
        self.quit.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # start the main loop
        tkinter.mainloop()

    # make a method to verify each answer
    # and display a message after
    def verify_answer(self):
        if int(self.radio_var.get()) != 63:
            message = 'Wrong!'
        else: 
            message = 'Bravo!'
            self.score += 2
        tkinter.messagebox.showinfo('Output', message)

    # the check_my_score method is a callback function
    # for the Check My Score button
    def check_my_score(self):
        tkinter.messagebox.showinfo('Result', 'Your score is ' +
            str(self.score))

# start_quiz = MiniQuiz()

class Gui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three IntVar objects to
        # use with the check buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # set the intVar objects to 0
        """self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)"""

        # create the check button widgets in top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame,
            text='Option 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
            text='Option 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
            text='Option 3', variable=self.cb_var3)
        
        # pack the buttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # create an Ok and Quit button
        self.ok_button = tkinter.Button(self.bottom_frame,
            text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
            text='Quit', command=self.main_window.destroy)
        
        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # start the main loop
        tkinter.mainloop()

    # the shpow choice is the callback function for the Ok button
    def show_choice(self):
        self.message = 'You selected:\n'

        # determine which checkbuttons were selected
        if self.cb_var1.get() == 1:
            self.message += '1\n'
        if self.cb_var2.get() == 1:
            self.message += '2\n'
        if self.cb_var3.get() == 1:
            self.message += '3\n'
        
        # display the message in an info dialog box
        tkinter.messagebox.showinfo('Selection', self.message)

guuuii = Gui()

# we use the canvas widget's screen coordinate system
# to specify the location of your graphics, to identify the position
# of each piel in an application's window

# coordinate system written as (X,Y)

# images that are displayed on a computer screen are made up of tiny dots caleld pixels

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw two lines
        self.canvas.create_line(0,0,199,199)
        self.canvas.create_line(199,0,0,199)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw a line connecting multiple points
        self.canvas.create_line(10,10,189,10,100,189,10,10,
            dash=(5,2),arrow=tkinter. BOTH,fill='blue',smooth=True,width=1.5)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_ = MyGui()


class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw a line connecting multiple points
        self.canvas.create_rectangle(20,20,180,180)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_gii = MyGui()

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw a line connecting multiple points
        self.canvas.create_oval(20,20,70,70)
        self.canvas.create_oval(100,100,180,130)

        # to create a circle, make all the length equal
        # self.canvas.create_oval(100,100,100,100)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_gii = MyGui()

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw an arc
        self.canvas.create_arc(10,10,190,190,start=45,extent=30)
        
        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_gii = MyGui()

# the point where two line segments are connected is called a vertex

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        
        # draw a line connecting multiple points
        self.canvas.create_polygon(60,20,100,20,140,60,140,100,
            100,140,60,140,20,100,20,60)
       
        # to create a circle, make all the length equal
        # self.canvas.create_oval(100,100,100,100)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_gii = MyGui()

import tkinter.font

class MyGui():
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,
            width=200, height=200)
        myFont = tkinter.font.Font(family='Helvetica', size=12)

        # draw a line connecting multiple points
        self.canvas.create_text(100,100, text='Hello Ella!!', 
            font=myFont,fill='blue',anchor=tkinter.NE)
        
        # to create a circle, make all the length equal
        # self.canvas.create_oval(100,100,100,100)

        # pack the canvas
        self.canvas.pack()

        tkinter.mainloop()

# a_gii = MyGui()