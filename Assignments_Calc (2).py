
print("Enter inputs and Operation !!!!")
a = int(input("Enter first Number.."))
b = int(input("Enter second Number.."))
op = input("Select operation +-*/...")


match op:
    case '+': 
        print(f"{a} + {b} = {a+b}")
    case '-': 
        print(f"{a} - {b} = {a-b}")
    case '*': 
        print(f"{a} * {b} = {a*b}")
    case '/': 
        print(f"{a} / {b} = {a/b}")
    case _:  
        print("Invalid operation")
    