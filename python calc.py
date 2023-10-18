#def final_outcome(first_number, operation, second_number):
#    result = 0
#    if operation == "+":
#        result = first_number+second_number
#    elif operation =="-":
#        result = first_number-second_number
#    elif operation =="*":
#        result = first_number*second_number    
#    elif operation == "/":
#        result = first_number/second_number
#    return result
#
#first_number = int(input("What's the first number?: "))
#operation = input("+\n-\n*\n/\n Pick an operation: ")
#second_number = int(input("What's the next number: "))
#result = final_outcome(first_number=first_number, operation=operation, second_number=second_number)
#print (f"{first_number} {operation} {second_number} = {result}")
#flag=True
#while flag: 
#    userinput = input (f"Press 'y' to continue operations with number {result} or press 'n' to start a new calculation. Press any other key to exit")
#    if userinput == "y":
#        first_number = result
#        operation = input("+\n-\n*\n/\n Pick an operation: ")
#        second_number = int(input("What's the next number: "))
#        result = final_outcome(first_number=first_number, operation=operation, second_number=second_number)
#        print (f"{first_number} {operation} {second_number} = {result}")
 
#Calculator

#Add
def add(n1, n2):
    return n1+n2 
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print (symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n to start a new calculation: ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
            
calculator()