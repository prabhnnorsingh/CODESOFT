import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
num = "0123456789"
symbol = "[]{}#()*;._-"

length = int(input("Enter the length of password:- "))
complexity = input("Enter your preferred complexity of the password(easy,medium,hard) - ")

if complexity.startswith('easy'):
    ans = lower_case + upper_case
    password = "".join(random.sample(ans,length))
    print(password)

elif complexity.startswith('medium'):
    ans = lower_case + upper_case + num
    password = "".join(random.sample(ans,length))
    print(password)


elif complexity.startswith('hard'):
    ans = lower_case + upper_case + num + symbol
    password = "".join(random.sample(ans,length))
    print(password)


else:
    print("Undefined complexity entered!!!!")