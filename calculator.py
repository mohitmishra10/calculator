
n1=1 
while n1 == 1: 
    print("\n This is calculator  program")
    print("1. Addition")
    print("2.Subtraction")
    print("3.Multiplication") 
    print("4.Division") 

    num=int(input("Enter your choice: ")) 

    if num == 1: 
        x=float(input("Enter first no:")) 
        y=float(input("Enter second no:")) 
        print("Add is : ",(x+y)) 

    elif num==2: 
        x=float(input("Enter first no :")) 
        y=float(input("Enter second no :")) 
        print("Sub is : ",(x-y)) 

    elif num==3 : 
        x=float(input("Enter first no :")) 
        y=float(input("Enter second no :")) 
        print("Mul is : ",(x*y)) 

    elif num==4: 
        x=float(input("Enter first no :")) 
        y=float(input("Enter second no :")) 
        print("Div is : ",(x/y)) 

    else: 
        print("Wrong choice") 
    n=input("If you want to continue enter 1 \n otherwise Enter any key ") 
    
    if n!="1": 
        exit()
    n1=int(n)