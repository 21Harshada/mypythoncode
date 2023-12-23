num=45
#num1=int(input("Guess the number:"))
no_of_guesses=1
num1=0
while (no_of_guesses<=5):
    #no_of_guesses=no_of_guesses+1
    num1=int(input('Enter a number'))
    print(5-no_of_guesses,"Chances you have")
    if(num1>num):
        print('You have entered greater number!enter lesser number')
    elif(num1<num):
        print('You have entered lesser number!Enter greater number')
    else:
         print('You won!')
         break
    if(no_of_guesses>=5):
         print("you lose")
    no_of_guesses=no_of_guesses+1
