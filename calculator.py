operation=input("Select operation((+,-,*,%,/,//,^): ")
print("Your Opertaion: ",operation)
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
if operation=="+":
    print(num1,"+",num2)
    print(num1+num2)
elif operation=="-":
    print(num1,"-",num2)
    print(num1-num2)
elif operation=="*":
    print(num1,"*",num2)
    print(num1*num2)
elif operation=="**":
    print(num1,"**",num2)
    print(num1**num2)
elif operation=="/":
    print(num1,"/",num2)
    print(num1/num2)
elif operation=="//":
    print(num1,"//",num2)
    print(num1//num2)
elif operation=="%":
    print(num1,"%",num2)
    print(num1%num2)
else:
    print("Invalid operator,Please enter valid operator")
