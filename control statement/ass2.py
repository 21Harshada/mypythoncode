#Largest of three numbers
num=int(input('Enter 1st No.:'))
num1=int(input('Enter 2nd No.:'))
num2=int(input('Enter 3rd No.:'))
if(num>num1) and (num>num2):
    print('1st number is graeter')
elif(num1>num) and (num1>num2):
    print('2nd Number is greater')
else:
    print('3rd number is greater')