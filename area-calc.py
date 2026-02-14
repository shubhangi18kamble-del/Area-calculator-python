print("**********AREA CALCULATOR**********")
while True:
    print("""    press 1 to get the area of square
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get the area of triangle
    press 5 for exit """)
    
    choice = int(input("enter a number batween 1 - 5: "))
    if choice == 1:
        
            side = float(input("enter the length of side: "))
            area = side**2
            print("the area of square:",area)
        
    
    elif choice == 2:

            len=float(input("Enter the length:"))
            wid=float(input("enter the width:"))
            area = len*wid
            print("the area of rectangle :",area)

    elif choice == 3:

            radius=float(input("enter the length of randius:"))
            area =3.14*(radius**2)
            print("the area of circle :",area)
            

    elif choice ==4:
            
            base=float(input("enter the base length:"))
            height=float(input("enter the height:"))
            area = 1/2*(base*height)
            print("the area of triangle:",area)
       
    elif choice== 5:
           print("Thank you for using area calculator.")
           break
    else:
        print("Invalid choice! Please try again.")
    