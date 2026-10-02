def isNegative(float):
    if float < 0:
        return True
    else:
        return False

x = float(input("Enter a negative number: "))
y = isNegative(x)
print (f"That's {y}!")