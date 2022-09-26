result = None
x = int(input("Number1:"))
y = int(input("Number2:"))
try:
    result = x/y
except ZeroDivisionError as e:
    print(type(e))
else:
    print("Inside else")
finally:
    print("Inside finally")
print("__NewLine__")
print("Result",result)
