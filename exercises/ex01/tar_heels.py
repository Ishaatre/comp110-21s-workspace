"""An exercise in remainders and boolean logic."""

__author__ = "730393785"


# Begin your solution here...
user_input: int = int(input("Enter an int:"))
if (user_input % 2 == 0 and user_input % 7 == 0): 
    print("TAR HEELS")
else:
    if user_input % 2 == 0: 
        print ("TAR")  
    else:
        if user_input % 7 == 0: 
            print ("HEELS")  
        else: 
            print("CAROLINA")   