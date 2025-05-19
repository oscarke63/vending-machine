n=10
try:
    res=n/0
except ZeroDivisionError:
    print("You can't divide by zero")