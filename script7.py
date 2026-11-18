def sum(num1, num2):
    return num1+num2
def minus(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2
a = int(input("ingrese un numero:"))
b = int(input("ingrese otro numero:"))
operation = input("ingrese un operador:")
if not operation in ["+", "-", "*", "/"]:
    raise ValueError
total = 0
if operation == "+":
    total = sum(a, b)
elif operation == "-":
    total = minus(a, b)
elif operation == "*":
    total = multiply(a, b)
elif operation == "/":
    total = divide(a, b)

print(total)



