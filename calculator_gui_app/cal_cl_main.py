#Command line calculator using if,elif,else statements and predefined functions!!!

def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

x = int(input('Enter the first number:-'))
y = int(input('Enter the second number:-'))

operation = input("Enter the operation you want to perform (add,subtract, multiply, divide) - ")

if operation.startswith('add'):
    print(sum(x,y))

elif operation.startswith('subtract'):
    print(diff(x,y))

elif operation.startswith('multiply'):
    print(mul(x,y))

elif operation.startswith('divide'):
    print(div(x,y))

else:
    print("Wrong choice of operation!!!!")
