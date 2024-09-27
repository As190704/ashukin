pwd = input("What is your master password? ")

def view():
   with open('password.txt',"r")as f:
       for line in f.readlines():
           data = line.rstrip()
    
def add():
 name = input('Account name: ')
 pwd = input("Password : ")  
   
with open('password.txt',"a") as f:
       f.write(name + ":" + pwd + "\n") 
       
while True:
   mode = input("add password or view existng one(view,add),press q for quit ?  ")
   
   if mode == "view":
       pass
   elif mode == "add":
       pass
   else:
       print("Invalid mode!")
       continue