def calc(no1,no2,choice):
    no1 = int(no1)
    no2 = int(no2)
    choice = int(choice)	
    if choice == 1:
        return int(no1 + no2)
    elif choice == 2:
        return int(no1 - no2)
    elif choice == 3:
        return int(no1 * no2)
    elif choice == 4:
        return int(no1 / no2)
    elif choice == 5:
        return int(no1 % no2)
    else:
        return "Please enter proper choice for calculation!!!"

no1 = input("Enter number1 for calculation:->")
no2 = input("Enter number2 for calculation:->")
choice = input("Enter your choice for calculation \n 1 Addition \n 2 Subtraction \n 3 Multiplication \n 4 Division \n 5 Modulo \n :->")
print("Output:", calc(no1,no2,choice))
