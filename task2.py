#Header file

import random

#Defining question()

def question():

   #Generating two random number

   num1=random.randint(1,10)

   num2=random.randint(1,10)

   #Printing statement

   print("How much is",num1,"times",num2,"?")

   #Returning the multipication value of num1 and num1

   return num1*num2

#Comment() function

def comment(comment):

  #Checking comment

  if(comment==1):

    #If comment is 1 then print the below statement

    print("\ndone")

  else:

    #If comment is not equal to 1 then print the below statement

    print("Please try again")

 

#Defining main()

def main():

  #Declaring variable

  value=0

  #While loop

  while True:

    #Calling the question() function

    correctanswer=question()

    while True:     

       #Getting input from user for answer

       answer=input("\nYour answer:")

       #Computing the value

       if(int(answer)==int(correctanswer)):

        comment(int(value)+1)

        break    

       else:

        comment(int(value))

        break

       #Checking answer

       if(int(answer)!=int(correctanswer)):

        break

    #Getting user choice

    choice=input("\nTry another question?[y/n]")

    if(choice=='n'):

       break

#Calling main()

main()
