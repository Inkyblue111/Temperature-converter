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
    '''Sets up the GUI'''
    
    def __init__(self, root):
        
        self.converter = TemperatureConverter()
        
        # Main window
        self.root = root
        self.root.geometry("400x150")
        
        # Container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Dictionary to hold frames
        # Key is the frame name and value is the method that creates the frame