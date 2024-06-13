def add(num1, num2):
    ad = num1 + num2
    return ad

def sub(num1, num2):
    su import sys

def add(num1, num2):
    ad = num1 + num2
    return ad

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
= num1 - num2
    return su

def mul(num1, num2):
    mu = num1 * num2
    return mu

print(add(13, 10))
print(sub(13, 10))
print(mul(13, 10))