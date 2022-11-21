def main(z=None):
    if z is None:
        x = float(input("What's x? "))
    else:
        x = z
    var = input("Enter One \"+, -, / ,* , %, ^\"? ")
    y = float(input("What's y? "))
    list = ["+","-","/","*","%","^"]
    while var in list:
        x = argument(var,x,y)
        var = input("Enter One \"+, -, / ,* , %, ^\"? ")
        y = float(input("What's y? "))
        main(x)
    z = x
    return print(f"{z:.2f}")
        

def argument(var,x,y):
    if var.strip() == "+":
        z = addition(x,y)
    elif var.strip() == "-":
        z = subtraction(x,y)
    elif var.strip() == "/":
        z = division(x,y)
    elif var.strip() == "*":
        z = multiplication(x,y)
    elif var.strip() == "%":
        z = modulos(x,y)
    elif var.strip() == "^":
        z = power(x,y)
    return z


def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def division(x,y):
    return x / y

def multiplication(x,y):
    return x * y

def modulos(x,y):
    return x % y

def power(x,y):
    return pow(x, y)


main()