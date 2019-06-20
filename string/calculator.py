actions = ["+","-","*","/"]

arg1 = input("print number>>> ")
arg2 = input("print second number>>> ")
action = input("action>>> ")

try:
    if "." in arg1:
        arg1 = float(arg1)
    else:
        arg1 = int(arg1)
except ValueError:
    print("Error arg1")
    exit(1)

try:
    if "." in arg2:
        arg2 = float(arg2)
    else:
        arg2 = int(arg2)
except ValueError:
    print("Error arg2")
    exit(1)

if isinstance (arg1, str) or isinstance (arg2, str):
    print("Error arg")
    exit()

if "." in arg1:
    arg1 = float(arg1)
else:
    arg1 = int(arg1)

if "." in arg2:
    arg2 = float(arg2)
else:
    arg2 = int(arg2)

if action not in actions:
    print("Error")
    exit()

if action == "+":
    print(arg1+arg2)
elif action == "-":
    print(arg1-arg2)
elif action == "*":
    print(arg1*arg2)
elif action == "/":
    print(arg1/arg2)
