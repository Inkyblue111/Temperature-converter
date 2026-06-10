from tkinter import *

FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

ABS_ZERO_FAHRENHEIT = -459.67
ABS_ZERO_CELSIUS = -273.15

class TemperatureConverter:
    ''' Handles the temperature conversion and input validation '''
    
    def calculate_to_c(self, temp):
        ''' Validates and converts enry to degrees in centigrade '''
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_FAHRENHEIT:
                result = (float(temp)-32) * 5 / 9
                return f'{result:.1f} degrees celsius'
            else:
                return "Temperature to low"
        except ValueError:
            return "Put in a number"
    
    def calculate_to_f(self, temp):
        ''' Validates and converts enry to degrees in fahrenheit '''
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_CELSIUS:
                result = (float(temp)* 9 / 5) + 32
                return f'{result:.1f} fahrenheit'
            else:
                return "Temperature to low"
        except ValueError:
            return "Put in a number"    

class ConverterGUI:
    ''' Sets up the GUI '''
    
    def __init__(self, root):
        
        self.converter = TemperatureConverter()
        
        # Main window
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x150")
        
        # Container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Dictionary to hold frames
        # Key is the frame name and value is the method that creates the frame
        self.frames = {}
        
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_c_frame()
        self.frames["to_fFrame"] = self.create_f_frame()
        
        # Show the inital frame
        self.show("MainFrame")
    
    def show_frame(self, name):
        ''' Displays the required fram from the dictionary '''
        frame = self.frames[name]
        frame.tkraise() # Move the frame to the top of the stack
    
    def create_main_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        # When working with stacked frames, it is better to use .grid than .pack sticky stretches the frame to fill up the window space
        # so the other frames can be covered, especially the ones that are larger than the current frame
        
        # Main heading
        Label(frame, font=FONT_MAIN_TITLE, text="Temperature Converter").grid(row=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Buttons: to Centigrade and to Fahrenheit
        Button(frame, text="to Centigrade", bg="yellow", font=FONT_HEADING, command=lambda: 
               self.show_frame("to_cFrame")).grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        Button(frame, text="to Fahrenheit", bg="pink", font=FONT_HEADING, command=lambda: 
               self.show_frame("to_fFrame")).grid(row=1, column=1, padx=10, pady=10, sticky="nsew")    
        return frame
    
    def create_c_frame(self):
        ''' Create the fahrenheit to centigrade screen '''
        pass
    
    def to_centigrade(self):
        ''' Calls the TempConverter object and displays the result in the app '''
        result = self.convert.calulate_to_c(self.temp_entry_c.get())
        self.result_c_label.configure(text=result)
    
    def create_f_frame(self):
        ''' Create the centigrade to fahrenheit screen '''
        pass
    
    def to_fahrenheit(self):
        ''' Calls the TempConverter object and displays the result in the app '''
        result = self.convert.calulate_to_f(self.temp_entry_f.get())
        self.result_f_label.configure(text=result)
    
    def reset(self, entry, label):
        ''' reset entry box and result label to blank '''
        entry.delete(0,END)
        Label.configure(text="")

