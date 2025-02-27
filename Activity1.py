age = int(input("enter age:"))
if age >= 18:
    print("you are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are not a senoir citizen")   
else:
    print("You are a minor.")