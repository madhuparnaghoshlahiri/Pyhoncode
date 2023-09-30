a=20
b=0
print(a+b)
try:
    print(a/b)
except ZeroDivisionError:
    print("Unable to Divide")
else:
    print("I am Else")
finally:
    print("I am Finally")

print(a*b)
print(a-b)
