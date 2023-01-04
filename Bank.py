#Importing Modules
import mysql.connector as sql
import time
import sys
#SQL Connection
mydb=sql.connect(host='localhost',user='root',passwd='123',database='bank')
mc=mydb.cursor()

#Continue
def continuee():
    Continue_input=input("Do you want to continue?(Y/N)\n")
    if Continue_input=="Y" or Continue_input=="y":
        Menu()
    elif Continue_input=="N" or Continue_input=="n":
        print("Thank you for using Windsor ATM")
        sys.exit()
    else:
        print("Wrong Input")
        continuee()


#1. Withdraw
def withdraw():
    demand=int(input("How much money do you want to Withdraw(Rupees)\n"))
    print("Are you sure you want to withdraw",demand,"Rupees?")
    withdrawl_choice=int(input("Press 1 to Confirm\nPress 2 to go back to Withdrawl Screen\nPress 3 to go back to the Main Menu\n"))
    mc.execute("select balance from users where ID=(%s)"%(inputID))
    balance = mc.fetchone()
    balance = balance[0]
    if withdrawl_choice==1 and balance>=demand:
        print("Your transaction is being processed\nPlease Wait")
        newBalance=balance-demand
        mc.execute("update users set balance=(%s) where ID=(%s)"%(newBalance,inputID))
        time.sleep(2)
        mydb.commit()
        print("Please collect cash")
        print("Your new Balance is:")
        print(newBalance,"Rupees")
    elif withdrawl_choice==1 and balance<demand:
        print("Error:Not enough money in account to withdraw")
        withdraw()
    elif withdrawl_choice==2:
        withdraw()
    elif withdrawl_choice==3:
        Menu()
    else:
        print("Wrong Choice")
        withdraw()
    continuee()


#2.Deposit
def deposit():
    deposit_amount=int(input("Enter the amount of money you want to Deposit\n"))
    mc.execute("select balance from users where ID=(%s)"%(inputID))
    balance=mc.fetchone()
    balance = balance[0]
    print("Are you sure you want to deposit",deposit_amount,"Rupees?")
    deposit_choice=int(input("Press 1 to Confirm\nPress 2 to go back to Deposit Screen\nPress 3 to go back to the Main Menu\n"))
    if deposit_choice==1:
        newBalance=balance+deposit_amount
        print("Your transaction is being processed\nPlease Wait")
        newBalance=balance+deposit_amount
        mc.execute("update users set balance=(%s) where ID=(%s)"%(newBalance,inputID))
        time.sleep(2)
        mydb.commit()
        print("Transaction Successful")
        print("Your new balance is")
        print(newBalance,"Rupees")

    elif deposit_choice==2:
         deposit()
    elif deposit_choice==3:
        Menu()
    else:
        print("Wrong Choice")
        deposit()
    continuee()


#3. Show Account Details
def show():
    mc.execute("select ID,name,phone,balance from users where ID=(%s)"%(inputID))
    Details=mc.fetchall()
    for i in Details:
        print("[ID,Name,Phone,Balance")
        print(i)
    continuee()


#4. Transfer Funds
def transfer():
    transfer_account=int(input("Enter beneficiary account number\n"))
    transfer_amount=int(input("How much money do you want to transfer\n"))
    mc.execute("select balance from users where ID=(%s)"%(inputID))
    balance=mc.fetchone()
    balance = balance[0]
    mc.execute("select balance from users where ID=(%s)"%(transfer_account))
    check=mc.fetchall()
    if mc.rowcount==1:
        mc.execute("select balance from users where ID=(%s)"%(transfer_account))
        beneficiary_balance=mc.fetchone()
        beneficiary_balance=beneficiary_balance[0]
        print("Are you sure you want to transfer",transfer_amount,"Rupees to account number(",transfer_account,")")
        transfer_choice=int(input("Press 1 to Confirm\nPress 2 to go back to Transfer Funds Screen\nPress 3 to go back to the Main Menu\n"))
        if transfer_choice==1 and transfer_account==inputID:
            print("Error:You cannot transfer money to your own account!")
            transfer()
        elif transfer_choice==1 and balance>=transfer_amount and transfer_account!=inputID:
            print("Your transaction is being processed\nPlease Wait")
            newBalance=balance-transfer_amount
            beneficiary_balance=beneficiary_balance+transfer_amount
            mc.execute("update users set balance=(%s) where ID=(%s)"%(beneficiary_balance,transfer_account))
            mc.execute("update users set balance=(%s) where ID=(%s)"%(newBalance,inputID))
            time.sleep(2)
            mydb.commit()
            print("Transaction Successful")
            print("Your new balance is")
            print(newBalance,"Rupees")
        elif transfer_choice==1 and balance<transfer_amount:
            print("Error:Not enough money in account to transfer")
            transfer()
        elif transfer_choice==2:
            transfer()
        elif transfer_choice==3:
            Menu()
        continuee()
    elif mc.rowcount==0:
        print("Account Not Found")
        Menu()


#5. Change PIN
def changePIN():
    newPIN1=int(input("Enter New 4-digit PIN\n"))
    newPinString=newPIN1
    if len(str(newPinString))==4:
        newPIN2=int(input("Re-Enter New 4-digit PIN\n"))
        if newPIN1==newPIN2:
            print("Are you sure you want to change your PIN? ")
            changePIN_choice=int(input("Press 1 to Confirm\nPress 2 to go back to Change PIN Screen\nPress 3 to go back to the Main Menu\n"))
            if changePIN_choice==1:
                mc.execute("update users set PINCODE=(%s) where ID=(%s)"%(newPIN1,inputID))
                print("Please Wait")
                time.sleep(2)
                mydb.commit()
                print("Transaction successfull")
            elif changePIN_choice==2:
                changePIN()
            elif changePIN_choice==3:
                Menu()
        elif newPIN1!=newPIN2:
            print("PIN does match") 
            changePIN()
    else:
        print("Your PIN must be of 4 digits")
        changePIN()
    continuee()


#Menu
def Menu():
    print("What would you like to do? ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Show Account Details")
    print("4. Transfer Funds")
    print("5. Change PIN")
    print("6. Exit")
    menu_input=int(input("Enter your choice:\n"))
    if menu_input==1:
        withdraw()
    elif menu_input==2:
        deposit()
    elif menu_input==3:
        show()
    elif menu_input==4:
        transfer()
    elif menu_input==5:
        changePIN()
    elif menu_input==6:
        print("Thank you for using Windsor ATM")
        sys.exit()
    else:
        print("Wrong choice")
        Menu()

#Main Function
print("Welcome to the Windsor ATM")
startup=int(input("Press 1. To Register New User\nPress 2. To Login\n"))
if startup==2:
    inputID=int(input("Please enter your ID\n"))
    mc.execute("Select * from users where ID=%s"%(inputID))
    row=mc.fetchall()
    if mc.rowcount==1:
        inputPIN=int(input("Please enter your 4-digit PIN\n"))
        mc.execute("select from users where PINCODE = %s and ID = %s"%(inputPIN, inputID))
        row=mc.fetchall()
        if mc.rowcount==1:
            Menu()
        elif mc.rowcount==0:
            print("Wrong PIN")  
    else:
        print("ID not found")
elif startup==1:
    name=input("Enter you Name\n")
    PIN=int(input("Enter a 4-Digit Pin\n"))
    newPinString=PIN
    if len(str(newPinString))==4:
        Phone=int(input("Enter your Phone Number\n"))
        Balance=int(input("How much money do you want to desposit to this account?\n"))
        mc.execute("insert into users(pincode,name,phone,balance) values(%s,'%s',%s,%s)"%(PIN,name,Phone,Balance))
        print("Creating Account\nPlease Wait")
        time.sleep(2)
        mydb.commit()
        print("Account Successfully Created")
        mc.execute("select id from users where pincode=(%s) and name=('%s') and Phone=(%s)"%(PIN,name,Phone))
        Details=mc.fetchone()
        for i in Details:
            print("Your New Account ID is:",i)
            inputID=i
        Menu()
    else:
        print("Your PIN must be of 4 digits!")
