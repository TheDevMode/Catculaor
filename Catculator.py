#Input here
num_1 = float(input("First number: "))
num_2 = float(input("Second number: "))

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
           
    
#Logic output
print(f"{num_1}{operator}{num_2} = {result}",)

