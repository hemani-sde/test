import random 
print("Welcome to the Guess the Number Game !")
print("Get a chance to win :")
print("1. brand new car")
print("2. Laptop")
print("3. Smartphone")
chance=5
print("You have total 5 chances to guess the number between 1 to 1000")
for i in range (0,5):
    user=int(input("Enter your guessed number: "))
    computer=random.randint(1,1000)
    if(user==computer):
        print("Congratulations ! You have won the game")
        gift=int(input("Choose your gift: 1. Car 2. Laptop 3. Smartphone : "))
        if(gift==1):
            print("You have won a brand new Car !")
        elif(gift==2):
            print("You have won a Laptop !")
        elif(gift==3):
            print("You have won a Smartphone !")
        break 
    else:
        if(i==4):
            print("Sorry ! you ahve used all ypur chances :(")
            break
        print(f"Wrong Guess ! Try again. ")
        