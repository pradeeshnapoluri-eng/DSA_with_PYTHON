def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def into(a,b):
    return a*b
def div(a,b):
    return a/b
element_1=int(input("give your number: "))

operations={

    '+': add,
    '-': sub,
    '*': into,
    '/': div
}

for i in operations:
    print("operations are", i)
next_step = True
while next_step:
    operator = input('choose ur operator: ')
    element_2 = int(input("give your next number: "))
    calculation = operations[operator]  ##it gets what operator we selected and then it will call the function of that operator
    ####print(calculation)
    result = calculation(element_1,element_2)  ##with that opertion it do calculation withthose elements
    print(f"{element_1} {operator} {element_2} = {result}")
##chatgpt added 
    if operator not in operations:
        print("Invalid operator")
        continue

    if operator == '/' and element_2 == 0:
        print("Cannot divide by zero")
        continue

    ##for continution
    
    should_continue = input(f"do you want to continue with {result} or start new calculation? type 'y' for continue and 'n' for new calculation: ")
    if should_continue == 'y':
        element_1 = result
    else:
        next_step = False
        print("THANKYOU FOR USING MY MINI CALCULATOR")