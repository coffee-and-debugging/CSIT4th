#### Alok Shrestha


from tkinter import *
from Logic import CalculatorLogic

##### asm bhyayena so nothing to connect to 
##### asm nabahyesi python shifter ko point bhayena so not done
##### same reason for auto chooser
##### paranthesis aayena k garney logic nai |||| might do it later while completing asm part
##### history pani sakena
class CalculatorUI:

    def __init__(self):
        self.root = Tk()

        # Display part of the calc here 
        self.e = Entry(self.root,width=80,borderwidth=8)
        self.e.grid(row=0,column=0,columnspan=5)

        #call the function
        self.create_buttons()

        ## INITIALIZE HERE SO THAT LATER PYTHON KNOWS EXACTLY WHAT THIS VALUE ARE SINCE THEY ARE INITIALIZED HERE
        self.first_num=None
        self.second_num=None
        self.math=None

        self.Logic = CalculatorLogic()

        self.resetter = 0 #chat ko concept ho hai yo chahi, yesley chahi k garxa bhanda like mero answer ayo tara aba maile new value lekhda tei append hunxa normally but after this concept i get new buffer to write on
        
    def button_add(self):
        self.first_val = self.e.get()
        self.Logic.get_first_val_and_operator(self.first_val,"add")
        self.e.delete(0,END)
        self.resetter = 1

    def button_divide(self):
        self.first_val = float(self.e.get())
        self.Logic.get_first_val_and_operator(self.first_val,"division")
        self.e.delete(0,END)
        self.resetter = 1
    
    def button_multiply(self):
        self.first_val = float(self.e.get())
        self.Logic.get_first_val_and_operator(self.first_val,"multiplication")
        self.e.delete(0,END)
        self.resetter = 1
    
    def button_subtract(self):
        self.first_val = float(self.e.get())
        self.Logic.get_first_val_and_operator(self.first_val,"subtract")
        self.e.delete(0,END)
        self.resetter = 1


    #class haru use garyo bhandai ma yo chahi falnu bhayena !! THIS IS WHAT DISPLAYS VALUE IN THE CALCULATOR || USER KO VALUE DEKHAUXA
    def button_click(self,number):

        if self.resetter == 1:
            self.e.delete(0,END)
            self.resetter = 0

        self.current = self.e.get()
        self.e.delete(0,END)
        self.e.insert(0,str(self.current)+str(number))
    # DEL RW CLEAR UI KO PART HO SO LEAVE IT IN UI
    def button_del(self):

        self.e.delete(len(self.e.get())-1,END)   # This line is copied from Chatgpt Couldnot understand how to skip the index and get the second last value Note;;;;; have to search for another method
    
    def button_clear(self):
        self.e.delete(0,END)
    
    


    def button_sqrt(self):
        self.current = float(self.e.get())
        self.e.delete(0,END)
        self.rooted = self.Logic.get_val_and_square_root(self.current)
        self.e.insert(0,self.rooted)
        self.resetter = 1


    def button_square(self):
        self.current = float(self.e.get())
        self.e.delete(0,END)
        self.squared_val=self.Logic.get_val_and_square(self.current)
        self.e.insert(0,self.squared_val)
        self.resetter = 1
    
    def button_equals(self):
        self.second_val=float(self.e.get())
        self.e.delete(0,END)
        self.e.insert(0,self.Logic.get_second_val_and_calculate(self.second_val))
        self.resetter = 1

    
    def button_power(self):
        self.first_val = self.e.get()
        self.Logic.get_first_val_and_operator(self.first_val,"power")
        self.e.delete(0,END)
        self.resetter = 1
    
    def button_dot(self):
        return
    
    def button_pie(self):
        self.val = self.e.get()
        self.e.delete(0,END)
        self.e.insert(END,str(3.1415926))
    
    def button_exp(self):
        self.val = float(self.e.get())
        self.e.delete(0,END)
        self.exp = self.Logic.get_val_and_find_e(self.val)
        self.e.insert(0,self.exp)
        self.resetter = 1

    
    def button_ans(self):
        self.second_val=float(self.e.get())
        self.e.delete(0,END)
        self.e.insert(0,self.Logic.get_second_val_and_calculate(self.second_val)) 
        self.resetter = 1
     
    def button_sin(self):
        self.current = float(self.e.get())
        self.e.delete(0,END)
        self.sin_val=self.Logic.get_val_and_find_sin(self.current)
        self.e.insert(END,self.sin_val)
        self.resetter = 1
    def button_cos(self):
        self.current = float(self.e.get())
        self.e.delete(0,END)
        self.cos_val=self.Logic.get_val_and_find_cos(self.current)
        self.e.insert(END,self.cos_val)
        self.resetter = 1
    def button_tan(self):
        self.current = float(self.e.get())
        self.e.delete(0,END)
        self.tan_val=self.Logic.get_val_and_find_tan(self.current)
        self.e.insert(END,self.tan_val)
        self.resetter = 1
    def button_log(self):
        self.value = float(self.e.get())
        self.e.delete(0,END)
        self.e.insert(0,self.Logic.get_val_and_find_log(self.value))
        self.resetter = 1

    def button_ln(self):
        self.value = float(self.e.get())
        self.e.delete(0,END)
        self.e.insert(0,self.Logic.get_val_and_find_ln(self.value))
        self.resetter = 1
    
    def button_factorial(self): # factorial integer rw non negative number ko lagi matra ho so be ready for error
        self.value = float(self.e.get())
        self.e.delete(0,END)
        self.e.insert(0,self.Logic.get_val_and_find_fact(self.value))
        self.resetter = 1
    

    
    def button_python(self):
        return
    
    def button_asm(self):
        return
    
    def button_auto(self):
        return
    
    def button_history(self):
        return
    

    def button_Paranthesis(self):
        return

    def create_buttons(self):

        # defining the button 
        self.Button_1 = Button(self.root,text="1",padx=20,pady=5,width=5,command=lambda: self.button_click(1))
        self.Button_2 = Button(self.root,text="2",padx=20,pady=5,width=5,command=lambda: self.button_click(2))
        self.Button_3 = Button(self.root,text="3",padx=20,pady=5,width=5,command=lambda: self.button_click(3))
        self.Button_4 = Button(self.root,text="4",padx=20,pady=5,width=5,command=lambda: self.button_click(4))
        self.Button_5 = Button(self.root,text="5",padx=20,pady=5,width=5,command=lambda: self.button_click(5))
        self.Button_6 = Button(self.root,text="6",padx=20,pady=5,width=5,command=lambda: self.button_click(6))
        self.Button_7 = Button(self.root,text="7",padx=20,pady=5,width=5,command=lambda: self.button_click(7))
        self.Button_8 = Button(self.root,text="8",padx=20,pady=5,width=5,command=lambda: self.button_click(8))
        self.Button_9 = Button(self.root,text="9",padx=20,pady=5,width=5,command=lambda: self.button_click(9))
        self.Button_0 = Button(self.root,text="0",padx=20,pady=5,width=5,command=lambda: self.button_click(0))
        self.Button_del = Button(self.root,text="del",padx=20,pady=5,width=5,command=self.button_del)
        self.Button_clear = Button(self.root,text="C",padx=20,pady=5,width=5,command=self.button_clear)
        self.Button_paranthesis = Button(self.root,text="(   )",padx=20,pady=5,width=5,command=self.button_Paranthesis)
        self.Button_divide = Button(self.root,text="/",padx=20,pady=5,width=5,command=self.button_divide)
        self.Button_multiply = Button(self.root,text="*",padx=20,pady=5,width=5,command=self.button_multiply)
        self.Button_subtract = Button(self.root,text="-",padx=20,pady=5,width=5,command=self.button_subtract)
        self.Button_sqrt = Button(self.root,text="sqrt",padx=20,pady=5,width=5,command=self.button_sqrt)
        self.Button_add = Button(self.root,text="+",padx=20,pady=5,width=5,command=self.button_add)
        self.Button_square = Button(self.root,text="x²",padx=20,pady=5,width=5,command=self.button_square)
        self.Button_equals = Button(self.root,text="=",padx=20,pady=5,width=5,command=self.button_equals)
        self.Button_power = Button(self.root,text="^",padx=20,pady=5,width=5,command=self.button_power)
        self.Button_dot = Button(self.root,text=".",padx=20,pady=5,width=5,command=self.button_dot)
        self.Button_pie = Button(self.root,text="π",padx=20,pady=5,width=5,command=self.button_pie)
        self.Button_exp = Button(self.root,text="e",padx=20,pady=5,width=5,command=self.button_exp)
        self.Button_ans = Button(self.root,text="Ans",padx=20,pady=5,width=5,command=self.button_ans)
        self.Button_log = Button(self.root,text="log",padx=20,pady=5,width=5,command=self.button_log)
        self.Button_ln = Button(self.root,text="ln",padx=20,pady=5,width=5,command=self.button_ln)
        self.Button_sin = Button(self.root,text="Sin",padx=20,pady=5,width=5,command=self.button_sin)
        self.Button_cos = Button(self.root,text="Cos",padx=20,pady=5,width=5,command=self.button_cos)
        self.Button_tan = Button(self.root,text="Tan",padx=20,pady=5,width=5,command=self.button_tan)
        self.Button_python = Button(self.root,text="Python",padx=20,pady=5,width=5,command=self.button_python)
        self.Button_asm = Button(self.root,text="ASM",padx=20,pady=5,width=5,command=self.button_asm)
        self.Button_auto = Button(self.root,text="Auto",padx=20,pady=5,width=5,command=self.button_auto)
        self.Button_history = Button(self.root,text="History",padx=20,pady=5,width=5,command=self.button_history)
        self.Button_factorial = Button(self.root,text="Factorial",padx=20,pady=5,width=5,command=self.button_factorial)

        #getting the button on the root 
        self.Button_7.grid(row=2,column=0,padx=5,pady=5)
        self.Button_8.grid(row=2,column=1,padx=5,pady=5)
        self.Button_9.grid(row=2,column=2,padx=5,pady=5)

        self.Button_4.grid(row=3,column=0,padx=5,pady=5)
        self.Button_5.grid(row=3,column=1,padx=5,pady=5)
        self.Button_6.grid(row=3,column=2,padx=5,pady=5)

        self.Button_1.grid(row=4,column=0,padx=5,pady=5)
        self.Button_2.grid(row=4,column=1,padx=5,pady=5)
        self.Button_3.grid(row=4,column=2,padx=5,pady=5)

        self.Button_0.grid(row=5,column=0,padx=5,pady=5)

        self.Button_clear.grid(row=1,column=0,padx=5,pady=5)
        self.Button_del.grid(row=1,column=1,columnspan=1,padx=5,pady=5)
        self.Button_paranthesis.grid(row=1,column=2,padx=5,pady=5)
        self.Button_divide.grid(row=1,column=3,padx=5,pady=5)
        self.Button_multiply.grid(row=1,column=4,padx=5,pady=5)
        self.Button_subtract.grid(row=2,column=3,padx=5,pady=5)
        self.Button_sqrt.grid(row=2,column=4,padx=5,pady=5)
        self.Button_add.grid(row=3,column=3,padx=5,pady=5)
        self.Button_square.grid(row=3,column=4,padx=5,pady=5)
        self.Button_equals.grid(row=4,column=3,padx=5,pady=5)
        self.Button_power.grid(row=4,column=4,padx=5,pady=5)
        self.Button_dot.grid(row=5,column=1,padx=5,pady=5)
        self.Button_pie.grid(row=5,column=2,padx=5,pady=5)
        self.Button_exp.grid(row=5,column=3,padx=5,pady=5)
        self.Button_ans.grid(row=5,column=4,padx=5,pady=5)

        self.Button_log.grid(row=6,column=0,padx=5,pady=5)
        self.Button_ln.grid(row=6,column=1,padx=5,pady=5)
        self.Button_sin.grid(row=6,column=2,padx=5,pady=5)
        self.Button_cos.grid(row=6,column=3,padx=5,pady=5)
        self.Button_tan.grid(row=6,column=4,padx=5,pady=5)

        self.Button_python.grid(row=7,column=0,padx=5,pady=5)
        self.Button_asm.grid(row=7,column=1,padx=5,pady=5)
        self.Button_auto.grid(row=7,column=2,padx=5,pady=5)
        self.Button_history.grid(row=7,column=3,padx=5,pady=5)
        self.Button_factorial.grid(row=7,column=4,padx=5,pady=5)


app = CalculatorUI()
app.root.mainloop()