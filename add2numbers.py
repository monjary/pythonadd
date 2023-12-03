def add(arg1, arg2):
    arg1 = int(arg1) #stop error about strings by making strings numbers
    arg2 = int(arg2)

    args = (arg1, arg2)

    if args[0] < args[1]:
        arg2 = arg1 #swap vars to have make first arg higher
        arg1 = arg2

    if not args[1] > 0:
        return -(-args[0] + -args[1]) #deal with 2 negatives
    else: #don't need to check arg 0 because it is larger and has to be positive
        return args[0] + args[1]
        
print("would you like to add 2 number")

if input() == "yes":
    print(add(input("enter first"), input("enter 2nd")))
else:
    if input() == "no":
        print("ok")
    