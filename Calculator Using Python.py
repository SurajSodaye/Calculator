def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error: Divison by zero"
    return x/y

print("=== Simple Calculator ===")
print("Choose operation:")
print("1. Add(+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divison (/)")

op = input("Enter Your Choice (+,-,*,/):")
a= float(input("Enter First Number: "))
b= float(input("Enter Second Number: "))

if op == '+':
    result = add(a, b)
elif op =='-':
    result = subtract(a,b)
elif op =='*':
    result = multiply(a,b)
elif op =='/':
    result = divide(a,b)
else:
    result = "Invalid operator"

print("Result: ", result)

