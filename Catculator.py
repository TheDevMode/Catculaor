#Import libraries
import math
import sys

#Welcome 
input("\nWELCOME, press enter to start...")

#Loading logics
def standard_calculator():
        while True:
#Input here
            try:
                num_1 = float(input("First number: "))
                num_2 = float(input("Second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input("Press Enter to try again...")
                continue

        #Input operation
            operator = input("Input one ( + , - , x or * , / ): ")

            result = None

        #Operation logic
            if operator == "+":
                result = num_1 + num_2
            elif operator == "-":
                result = num_1 - num_2
            elif operator == "*" or operator == "x":
                result = num_1 * num_2
            elif operator == "/":
                result = num_1 / num_2
            else:
                result = print("Invalid operation")
    
        #Easter Egg          
            if result is not None:
                if result == 63 or result == 63.0:
                    print("Chosen random number!")
        
        #Logic output
            print(f"{num_1}{operator}{num_2} = {result}",)
            
            
def advanced_calculator():
    #Input here
    while True:
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            input("Press Enter to try again...")
            continue
        
       #input operation
        operator = input("Input one ( sqrt , log , sin , cos , tan ): ")

        result = None
        #Logic
        if operator == "sqrt":
            result = math.sqrt(num)
        elif operator == "log":
            result = math.log(num)
        elif operator == "sin":
            result = math.sin(num)
        elif operator == "cos":
            result = math.cos(num)
        elif operator == "tan":
            result = math.tan(num)
        else:
            print("Invalid operation")

        if result is not None:
            print(f"{operator}({num}) = {result}")

def exit():
    print("Exiting the calculator. Goodbye!")
    sys.exit(0)#recommended to use sys.exit() for exiting the program instead of exit() for better control over the exit status.
    


#user modes 
print("1) Standard operations")
print("2) Advanced operations")
print("3) Exit")

#mode selection
mode = input("Choose 1 or 2 or 3: ")

while True:
    if mode == "1":
        standard_calculator()
    elif mode == "2":
        advanced_calculator()
    elif mode == "3":
        exit()
        

    else:
        print("[!] Invalid selection. Please choose 1 or 2 or 3.")
        input("Press Enter to try again...")
