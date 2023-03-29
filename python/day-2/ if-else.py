x = int(input("enter your value: "))
print("your age is:", x)

if ( x >= 18 ):
    print("you can drive gear vehicle")

    if( x >= 20):
        print("your can drive commercial vehicles")
        
elif(x >= 16):
    print("you can drive non-gear vehicle")
else:
    print("you cant drive gear Vehicle")

