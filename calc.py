print("number 1")
number1 = input()
print("number 2")
number2 = input()
number1 = int(number1)
number2 = int(number2)

def multiply(number1, number2):
    return number1 * number2

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1 / number2

def power(number1, number2):
    return number1 ** number2

print("add, subtract, multiply, power, divide")
choice = input()

if choice == "add":
    result1 = add(number1, number2)
    print(result1)

elif choice == "subtract":
    result2 = subtract(number1, number2)
    print(result2)
elif choice == "multiply":
    result3 = multiply(number1, number2)
    print(result3)
elif choice == "divide":
    result4 = divide(number1, number2)
    print(result4)
else:
    choice == "power"
    result5 = power(number1, number2)
    print(result5)
