#  https://www.youtube.com/watch?v=QZPv1y2znZo&t=2356s
import tkinter as tk

#colors
light_gray="#F5F5F5"
label_color="#141414" #25265E
white="#FFFFFF"
off_white="#F8FAFF"
light_blue="#CCEDFF"

#fonts
default_font_style= ("Arial",20)
small_font_style=("Arial",16)
large_font_style=("Arial",40,"bold")
medium_font_style=("Arial",30)
digits_font_style=("Arial",24,"bold")
class Calculator:  # All the initializations will be here
    def __init__(self): 
        self.window=tk.Tk() #main window of calculator
        self.window.geometry("375x667") #specifying width and height of this window  
        self.window.resizable(0,0) #Disable resizing of window  
        self.window.title("Super Calculator & Converter")  # title bar for app name  #another method to start calculator
        
        
        self.total_expression="" #the display will have two dispaly: current expression and total total_expression
        self.current_expression=""
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        self.digit={
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.create_digit_buttons()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #this dictionary maps the arithmetic operation in python to the operator symbols
        self.create_operator_buttons()
        self.create_special_button()
        self.total_expression,self.label=self.create_display_label()
        
        #to expand row and columns:
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range (1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
    def create_special_button(self):   
        self.create_clear_button()
        self.create_equals_button()
    def create_display_label(self):
        total_label=tk.Label(self.display_frame, text=self.total_expression,
                             anchor=tk.E,bg=light_gray,fg=label_color,padx=24,font=small_font_style) #anchor=tk.E means east of display (other N(north),S(sout),NE etc.) , padx:  give it padding horizontal direction  
        total_label.pack(expand=True,fill="both")
        
        label=tk.Label(self.display_frame, text=self.current_expression,anchor=tk.E,bg=light_gray,fg=label_color,padx=24,font=large_font_style) #anchor=tk.E means east of display (other N(north),S(sout),NE etc.) , padx:  give it padding horizontal direction  
        label.pack(expand=True,fill="both")
        return total_label,label
    
    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=light_gray)
        frame.pack(expand=True,fill="both") #these argument will allow our frame to expand and fill any empty space around the
        return frame
    
    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()
        
    def create_digit_buttons(self):
        for self.digit,grid_value in self.digit.items():
            button=tk.Button(self.buttons_frame,text=str(self.digit),bg=white,font=digits_font_style,
                             borderwidth=0,command=lambda x=self.digit: self.add_to_expression(x)) 
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    
    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()
        
    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            button =tk.Button(self.buttons_frame,text=symbol,bg=off_white,fg=label_color,font=medium_font_style, borderwidth=0,command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4,sticky=tk.NSEW)
            i+=1
    
    def create_clear_button(self):
        button=tk.Button(self.buttons_frame,text="C",bg=off_white, fg=label_color,font=default_font_style,borderwidth=0)      
        button.grid(row=0,column=1,columnspan=3,sticky=tk.NSEW)    
    
    def create_equals_button(self):
        button=tk.Button(self.buttons_frame,text="=",bg=light_blue, fg=label_color,font=medium_font_style,borderwidth=0)      
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW) 
    
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both") #these argument will allow button ...
        return frame
    
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression)
    
    
    
    def run(self):
        self.window.mainloop()
        
if __name__=="__main__":   #these lines of code will run only when calculate.py is run as a script from the terminal
    calc=Calculator()
    calc.run()