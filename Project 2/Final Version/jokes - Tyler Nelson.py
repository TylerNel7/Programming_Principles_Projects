# Name:  Tyler Nelson

# This file is provided to you as a starting point for the "jokes.py" program of Assignment 2
# of Programming Principles in Semester 1, 2020.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json

#set class name
class ProgramGUI:
    #create constructer 
    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of jokes.py" section of the assignment brief.  

        #create main window and set to 'self.main'. Assign title, geometry and resizeable conditions
        self.main = tkinter.Tk()
        self.main.title('Joke Catalogue')
        self.main.geometry('300x130')
        self.main.resizable(width=False, height=False)

        #Check file and load data
        try:
            f = open('data.txt', 'r')
            self.data = json.load(f)
            f.close()

        #Otherwise show error message and close program
        except:
            tkinter.messagebox.showerror('Error', 'Missing/Invalid file')
            self.main.destroy()
            return

        #Set current joke value
        self.current_joke = 0

        #Set GUI frames and assign appropirate conditions (and packing into window)
        self.text = tkinter.Frame(self.main, padx=8, pady=10)
        self.button = tkinter.Frame(self.main, padx=8, pady=15)
        self.text.pack()
        self.button.pack()

        #Set GUI labels and assign appropirate conditions (and packing into window)
        self.setup = tkinter.Label(self.text, text='')
        self.punchline = tkinter.Label(self.text, text='')
        self.setup.pack()
        self.punchline.pack()
       
        #Set GUI buttons and assign appropirate conditions (and packing into window)
        self.laugh_btn = tkinter.Button(self.button, padx='10', text='Laugh', command=lambda: self.rate_joke('laughs'))
        self.groan_btn = tkinter.Button(self.button, padx='10', text='Groan', command=lambda: self.rate_joke('groans'))
        self.laugh_btn.pack(side='left', padx='10')
        self.groan_btn.pack(side='right', padx='10')

        #Run function to set value of text in labels and start the mainloop
        self.show_joke()
        tkinter.mainloop()


    def show_joke(self):
        # This method is responsible for displaying the setup and punchline of the current joke in the GUI.
        # See Point 1 of the "Methods in the GUI class of jokes.py" section of the assignment brief

        #Set 'self.joke' to the active dictionary based on the variable 'self.current_joke' and update the label text respectively
        self.joke = self.data[self.current_joke]
        self.setup.configure(text=self.joke['setup'])
        self.punchline.configure(text=self.joke['punchline'])
        
        
    def rate_joke(self, rating):   
        # This method is responsible for recording the rating of the joke when a button is clicked.
        # See Point 2 of the "Methods in the GUI class of jokes.py" section of the assignment brief.

        #Add the integer 1 to the respective response (either 'laughs' or 'groans') in the respected dictionary 
        self.joke[rating] += 1

        #Save response to joke in data.txt file
        f = open('data.txt', 'w')
        json.dump(self.data, f, indent=4)
        f.close()

        #If the current joke displayed is the last, then display message and end program afterwards
        if self.joke == self.data[-1]:
            tkinter.messagebox.showinfo('Rating Recorded', 'Thank you for rating,\nThat was the last joke,\nThe program will now end')
            self.main.destroy()

        #Otherwise, add '1' to the self.current_joke variable, display appropirate message, then move on to next joke 
        else:
            self.current_joke = self.current_joke + 1
            tkinter.messagebox.showinfo('Rating Recorded', 'Thank you for rating,\nThe next joke will now appear.')
            self.show_joke()
            

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
