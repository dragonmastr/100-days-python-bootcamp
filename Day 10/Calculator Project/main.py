import art
print(art.logo +"\n")
def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def subtract(n1,n2):
    return n1 - n2

def calculator():
    flag = True
    result = 0
    while flag :
        n1 = int(input("What is the first number?:"))
        print("+\n-\n*\n/\n")
        operator = input("Pick an operation:")
        n2 = int(input("What is the second number?:"))
        match operator:
            case "+":
                result = add(n1,n2)
            case "-":
                result = subtract(n1, n2)
            case "*":
                result = multiply(n1,n2)
            case "/":
                result = divide(n1,n2)
            case _:
                print("wrong operator")
                return
        return result

print(calculator())
