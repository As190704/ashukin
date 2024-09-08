import random
topofrange = input("Type a number: ")

if topofrange.isdigit():
    topofrange = int(topofrange)

    if topofrange <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
    else:
        print("Please type a number next time.")
        quit()
        
random_number = random.randint(0,topofrange)
guesses = 0

while True:
    guesses += 1
    userguess = input("Make a guess: ")
    if userguess.isdigit():
     userguess = int(userguess)

    else:
        print("Please type a number next time.")
        continue
        
if userguess == random_number:
    print("You guessed it!")
elif userguess > random_number:
        print("You were above the number!")
else:
        print("You were below the number!")
    
print("you guessed it in",guesses,"guesses")  
