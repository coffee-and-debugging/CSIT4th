# Common calulation performer(simple calculator) code, with the help of AI or vibe coding, developed by Aamos Raut.

import math

class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '^': self.power,
            'sqrt': self.square_root,
            '%': self.percent
        }
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error: Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a, b=None):
        if a < 0:
            raise ValueError("Error: Cannot calculate square root of negative number!")
        return math.sqrt(a)
    
    def percent(self, a, b):
        return (a * b) / 100
    
    def calculate(self, num1, operator, num2=None):
        try:
            num1 = float(num1)
            
            if operator in ['sqrt']:
                result = self.operations[operator](num1)
            else:
                if num2 is None:
                    raise ValueError("Second number required for this operation")
                num2 = float(num2)
                result = self.operations[operator](num1, num2)
            
            # Round to avoid floating point errors
            result = round(result, 10)
            return result
            
        except ValueError as e:
            return str(e)
        except KeyError:
            return f"Error: Invalid operator '{operator}'"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

def main():
    calc = Calculator()
    
    print("=" * 40)
    print("  WELCOME TO PYTHON CALCULATOR  ")
    print("=" * 40)
    print("\nSupported operations:")
    print("  +  : Addition")
    print("  -  : Subtraction")
    print("  *  : Multiplication")
    print("  /  : Division")
    print("  ^  : Power (exponent)")
    print("  %  : Percentage (first% of second)")
    print("  sqrt: Square root (requires one number)")
    print("=" * 40)
    print("Type 'quit' to exit")
    print("=" * 40)
    
    while True:
        print("\n" + "-" * 40)
        
        # Get first number
        num1_input = input("Enter first number (or 'quit' to exit): ").strip()
        if num1_input.lower() == 'quit':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        # Validate first input
        try:
            float(num1_input)
        except ValueError:
            print("Error: Please enter a valid number!")
            continue
        
        # Get operator
        operator = input("Enter operator (+, -, *, /, ^, %, sqrt): ").strip()
        if operator.lower() == 'quit':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        # For sqrt, we don't need second number
        if operator == 'sqrt':
            result = calc.calculate(num1_input, operator)
            print(f"\n√{num1_input} = {result}")
            continue
        
        # Get second number for binary operations
        num2_input = input("Enter second number: ").strip()
        if num2_input.lower() == 'quit':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        # Validate second input
        try:
            float(num2_input)
        except ValueError:
            print("Error: Please enter a valid number!")
            continue
        
        # Calculate and display result
        result = calc.calculate(num1_input, operator, num2_input)
        
        if isinstance(result, str) and result.startswith("Error"):
            print(f"\n{result}")
        else:
            # Format the output nicely
            if operator == '%':
                print(f"\n{num1_input}% of {num2_input} = {result}")
            else:
                print(f"\n{num1_input} {operator} {num2_input} = {result}")

def quick_calculate():
    """Alternative mode: Single-line calculation"""
    calc = Calculator()
    
    print("\n" + "=" * 40)
    print("     QUICK CALCULATION MODE")
    print("=" * 40)
    print("Enter calculations like: 5 + 3 or 16 sqrt")
    print("Type 'quit' to exit\n")
    
    while True:
        expression = input(">>> ").strip()
        
        if expression.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not expression:
            continue
        
        parts = expression.split()
        
        if len(parts) == 2 and parts[1].lower() == 'sqrt':
            result = calc.calculate(parts[0], 'sqrt')
            print(f"= {result}")
        elif len(parts) == 3:
            result = calc.calculate(parts[0], parts[1], parts[2])
            print(f"= {result}")
        else:
            print("Error: Invalid format. Use: number operator number")
            print("Example: 5 + 3 or 16 sqrt")

if __name__ == "__main__":
    print("\nChoose mode:")
    print("1. Interactive Calculator")
    print("2. Quick Calculation Mode")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == '2':
        quick_calculate()
    else:
        main()