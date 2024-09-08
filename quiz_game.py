print("Welcome to this quiz you should dare to answer!!")

playing=input("play? ")

if playing.lower() != "yes":
    quit()
    
print("okay let's play :)")
score=0

answer =input("What CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")  
    
answer =input("What GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer =input("What RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer =input("What PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer =input("What IPU stand for? ")
if answer.lower() == "indraprastha university":
    print("Correct!")
    score += 1
else:
    print("Incorrect")   
    
print("You got " + str(score)+ " questions correct!")
print("You got " + str((score/5)*100) + " %.")