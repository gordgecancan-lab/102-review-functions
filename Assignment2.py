def isHappy(val):
    try:
        if int(val) > 0:
            print(f"{val} is a positive integer good job!")
        else:
            print(f"{val} is not positive integer, it's negative.")
    except:
        try:
            float(val)
            print(f"{val} isn't even an integer.")
        except:
            print(f"You suck at this")

x = input("Input a positive integer:  ")
isHappy(x)