#Welcome 
input("\nWELCOME, press enter to start...")

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

#wait for user to exit
    call = input("\nTask complete! type exit to quit or enter to continue : ")
    if call == "exit":
        break 
