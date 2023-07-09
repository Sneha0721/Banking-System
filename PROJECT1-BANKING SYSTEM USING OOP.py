#PARENT CLASS
class User:

#holds details about the user------------!!!

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

#function to shoe user details-------------!!!

    def show_details(self):
        print("User Personal details")
        print("")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

#CHILD CLASS
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Account balance has been updated: ",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("Insufficient balance!! Balance available:  ",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated :",self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance :",self.balance)

print("Enter your Name,Age and Gender")
name=input(print("Enter your name: "))
age=int(input(print("Enter your age: ")))
gender=input(print("Enter your gender: "))

#user=User(name,age,gender)
bank=Bank(name,age,gender)
v='Y'
print("Press\n1.To view personal details\n2.To deposit\n3.To withdraw\n4.To view account details")
while v=='Y':
    i=int(input())

    if i==1:
        bank.show_details()
    elif i==2:
        amount=int(input("How much money you want to deposit: "))
        bank.deposit(amount)
    elif i==3:
        amount=int(input("How much money you want to withdraw: "))
        bank.withdraw(amount)
    elif i==4:
        bank.view_balance()
    print("Do you want to do another operation: if yes the press Y")
    v=input()
    if(v=='N'):
        print("Thank You")














