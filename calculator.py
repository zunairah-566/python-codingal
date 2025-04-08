def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("a. addition")
print("b. subtraction")
print("c. division")
print("d. multiplication")

ch = input("please enter your choice")

num1 = int(input("enter first number \n"))
num2 = int(input("enter second number \n"))

if ch=='a':
    print(num1, "+" , num2 , "=", add(num1,num2))

elif ch == 'b':
    print(num1, "-", num2 , "=", sub(num1,num2))