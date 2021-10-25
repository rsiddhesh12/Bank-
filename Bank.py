alist=[]
import random
import string
class Account:
    def __init__(s,id=0,name='',email='',contact=0,amount=0,acNo='',password='',x=0,y=0):
        s.id=id
        s.name=name
        s.email=email
        s.contact=contact
        s.amount=amount
        s.acNo=acNo
        s.password=password
        s.x=x
        s.y=y

    def __str__(s):
        return '{} {} {} {} {} {} {} {} {}'.format(s.id,"",s.name," ",s.email," ",s.contact," ",s.amount," ",s.acNo," ",s.password," ",s.x," ",s.y)

    def reg(s):
        print('-------------Register Yourself to open bank Account-----------------')
        try:
            s.id=input("Enter Your ID:")
            s.name=input("Enter Your Name:")
            s.email=input("Enter Your Email:")
            s.contact=int(input("Enter You contact:"))
            s.amount=float(input("Enter Your Amount:"))
        except Exception as e:
            print("Enter Valid Input")
        else:
            print("Thank You For Registration")
            print("Note down your Account number and Password")
            print('-'*30)
            s.acNo=s.get_random_acNo()
            print(" Account Number:",s.acNo)
            s.password=s.get_random_password()
            print(" Password : ",s.password)
            print('-'*30)
            a=Account(s.id,s.name,s.email,s.contact,s.amount,s.acNo,s.password)
            alist.append(a)
        
    def login(s):
        print('--------------Welcome to Bank Login Interface-----------------------')
        try:
            acc=input("Enter Account Number :")
            passw=input("Enter Password :")
        except Exception as e:
            print("Enter Valid Input")
        else:
            for i in alist:
                if acc==i.acNo or passw==i.password:
                    print('Login Success \n',i.name,'\n',i.email)
                    s.transaction()
                else:
                    print("Login Fail")
                    
    def get_random_password(s):
        random_source = string.ascii_letters + string.digits
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        for i in range(6):
            password += random.choice(random_source)

        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password

    def get_random_acNo(s):
        random_source = string.digits
        aNo = random.choice(string.digits)
        aNo += random.choice(string.digits)
        aNo += random.choice(string.digits)
        for i in range(7):
            aNo += random.choice(random_source)

        password_list = list(aNo)
        random.SystemRandom().shuffle(password_list)
        aNo = ''.join(password_list)
        return aNo

    def view_detail(s):
        an=input("Enter Account Number:")
        for i in alist:
            if i.acNo==an:
                print("--------------------User Details------------------------")
                print("Name:",i.name,"\nEmail ID:",i.email,"\nContact Number:",i.contact,"\nAccount No:",i.acNo)
            else:
                print("Enter Valid Account Number")

    def Deposite(s):
        try:
            an=input("Enter Account Number:")
            s.x=float(input("Enter Amount to Deposite:"))
        except Exception as e:
            print("Enter valid Input")
        else:
            for i in alist:
                if i.acNo==an:
                    i.amount=i.amount+s.x
                    print("-----------------------SUCCESS--------------------------")
                else:
                    print("Enter Valid Account Number")
    
    def Withdraw(s):
        try:
            an=input("Enter Account Number:")
            s.y=float(input("Enter Amount to Withdraw:"))
        except Exception as e:
            print("Enter Vaid Input")
        else:
            for i in alist:
                if i.acNo==an:
                    i.amount=i.amount-s.y
                    print("---------------------------SUCCESS-----------------------")
                else:
                    print("Enter Valid Data")
                    
    def view_balance(s):
        an=input("Enter Account Number:")
        for i in alist:
            if i.acNo==an:
                print("Your Account Balance is:",i.amount)
            else:
                print("Enter Valid Account Number")
                

    def transaction(s):
        choice=0
        while (choice!=5):
             print("Enter 1 for View Details")
             print("      2 for Deposite")
             print("      3 for Withdraw")
             print("      4 for Check Balance")
             print("      5 for Exit")
             try:
                 choice=int(input())
             except Exception as e:
                 print("Enter Valid Choice")
             else:
                 if choice==1:
                     s.view_detail()
                 elif choice==2:
                     s.Deposite()
                 elif choice==3:
                     s.Withdraw()
                 elif choice==4:
                     s.view_balance()

def Operation():
    a=Account()
    choice=0
    while (choice!=3):
        print("Enter 1 Register")
        print("      2 Login")
        print("      3 exit")
        try:
            choice=int(input())
        except Exception as e:
            print("Enter Valid Choice")
        else:
            if choice==1:
                a.reg()
            elif choice==2:
                a.login()
Operation()
            
            
    
