#Write a python code to compare two numbers
#if user give instructions 
print("Comapre two numbers")

number1=int(input("Enter number1"))
number2=int(input("Enter number2"))

if  number1<number2:
    print(number2, 'is greater')
elif   number1>number2:
       print(number1, 'is greater')
else:
    print('Both are equal')
