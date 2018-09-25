import Factorial
import Power
import Fibonacci

repeat = True

while(repeat):
    user_selection = input("Select number of operation you'd like to perform:\n1\n2\n3\n")

    veracity = False

    while(not veracity):
        n_selection = input("Please input the value of n: ")
        if(int(n_selection) > 20):
            print("Error: Please input a value less than or equal to 20")
        else:
            veracity = True

    veracity = False
    
    while(not veracity):
        if(int(user_selection) == 1):
            print(Power.powerOfTwo(int(n_selection)))
            veracity = True

        elif(int(user_selection) == 2):
            veracity = True
            print(Factorial.factorial(int(n_selection)))

        elif(int(user_selection) == 3):
            print(Fibonacci.Fibonacci(int(n_selection)))
            veracity = True

        else:
            print("Invalid input please try again.\n")

    do_repeat = input("Would you like to try again(y/n)? ")
    if(do_repeat == "yes" or do_repeat == "y" or do_repeat == "Y" or do_repeat == "Yes"):
        repeat = True
    else:
        repeat = False
