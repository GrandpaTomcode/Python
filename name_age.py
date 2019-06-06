#using the input tag to ask for the users first name and what their age is, if less or 6 it will 'reject' them 
#or if they are older than 7 it will welcome them
#Made 5/6/19
f_name = input("What is your first name?   ")
#l_name = input("what's your last name?   ")
if f_name == "Harry":
    print(f_name, "is learning Python")
elif f_name == "Tom":
    print(f_name, "Is bad at manageing money")
else:
    #asks them their age in case they are too young
    age = int(input("how old are you?  "))
    if age <=6:
        print("wow you're {} Maybe you shouldn't start just yet... maybe when you're older than".format(age))
    else:
        #If older than 6
        print("welcome to Python even tho you are {}".format(age))

