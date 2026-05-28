### ALOK SHRESTHA


import math
class CalculatorLogic:
    def __init__(self):
        self.first_num=None
        self.second_num=None
        self.math=None
        # self.fact = 1.0
    
    def get_first_val_and_operator(self,first_num,operator):# suru ko value liney ani operator store garney just that much
        self.first_value = float(first_num)
        self.operation = operator

    def get_second_val_and_calculate(self,second_num):
        self.second_value = float(second_num)
        if(self.operation=="add"):
            return self.first_value+self.second_value
        
        if(self.operation=="subtract"):
            return self.first_value-self.second_value
        
        if(self.operation=="multiplication"):
            return self.first_value*self.second_value
        
        if(self.operation=="division"):
            self.value = None
            try:
                return self.first_value / self.second_value
            except ZeroDivisionError:
                return "Error: Cannot divide by zero"
        
        if(self.operation=="power"):
            return self.first_value**self.second_value
        
        
    def get_val_and_square(self,first_num):
        self.first_value = float(first_num)*float(first_num)
        return self.first_value
    
    def get_val_and_square_root(self,first_num):
        self.calculated_value = float(first_num)**(1/2)  # 5^(1/2)= rootunder(5)
        return self.calculated_value

    def get_val_and_find_sin(self,first_num):
        self.value = math.sin(first_num)
        return self.value
    def get_val_and_find_cos(self,first_num):
        self.value = math.cos(first_num)
        return self.value
    def get_val_and_find_tan(self,first_num):
        self.value = math.tan(first_num)
        return self.value
    def get_val_and_find_e(self,first_num):
        self.value = math.exp(first_num)
        return self.value
    def get_val_and_find_log(self,first_num):
        self.value = math.log10(first_num)
        return self.value
    def get_val_and_find_ln(self,first_num):
        self.value = math.log(first_num)
        return self.value
    def get_val_and_find_fact(self,first_num):# factorial integer rw non negative number ko lagi matra ho so be ready for error
        self.fact=1
        for i in range(1,int(first_num)+1):
            self.fact = self.fact*i
        return self.fact 

    