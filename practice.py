import sys

def add (num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    su = num1 - num2
    return su

def mul(num1, num2):
    mu = num1 * num2
    return mu

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)