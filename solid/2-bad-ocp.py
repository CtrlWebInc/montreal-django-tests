for x in range(1, 46):
    if x % 3 == 0 and x % 5 == 0:
        print("Quack! *Flap*")
    elif x % 5 == 0:
        print("Quack!")
    elif x % 3 == 0:
        print("*Flap*")
    else:
        print(x)
