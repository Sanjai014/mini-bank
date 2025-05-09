with open ("Admin.txt","w") as file:
    file.write("Admin123,pass123\n")

def Admin_view():
    print("\n---Banking Menu (Admin)---\n")        
    print("1.create_account")
    print("2.deposit")
    print("3.withdraw")
    print("4.check_balance")
    print("5.show_transaction_histry")
    print("6.exit")



def User_view():
    print("\n====Banking Menu====\n")
    print("1.deposit")
    print("2.withdraw")
    print("3.check_balance")
    print("4.show_transaction_histry")
    print("5.exit")





def Create_Account():
    print("\n=====Create_Account=====\n")
    
    Account_Holder_Name = input(f"\n{'Enter Account Holder Name' :<25} :")
    User_Name = input(f"{'Enter User Name' :<25} :")
    User_Password = input(f"{'Enter User Password' :<25} :")
    balance = float(input(f"{'Enter Initial Balance' :<25} :"))
    Phone_number = input(f"{'Enter phone number' :<25} :")
    Address=input(f"{'Enter the Address' :<25} :")
    
    try:
        with open("Acc_No.txt", 'r') as file:
            last = file.read().strip()
            new = int(last[3:]) + 1
    except FileNotFoundError:
        new = 1

    Account_Number = "ACC" + str(new).zfill(3)
    user_ID = "U_ID" + str(new).zfill(4)

    
    with open("Acc_No.txt", 'w') as file:
        file.write(Account_Number)

    
    with open("ACC_Details.txt", "a") as file:
        file.write(f"{Account_Number},{User_Password},{User_Name},{balance}\n")


    with open("User_Details.txt", "a") as file:
        file.write(f"{user_ID},{User_Name},{User_Password},\n")

    

    print("\nAccount Created Successfully")
    print(f"\nAccount_number : {Account_Number}")
    print(f"user_ID : {user_ID}")
    print(f"Account_Holder_Name : {Account_Holder_Name}")
    print(f"User_Name : {User_Name}")
    print(f"User_Password : {User_Password}")
    print(f"Balance : {balance}")
    print(f"Phone_number : {Phone_number}")
    print(f"Address : {Address}")

    from datetime import datetime
    date_time_now = datetime.now()

    with open("Transaction_Details.txt", "a") as file:
        file.write(f"{date_time_now},{Account_Number} ,withdraw,{balance},{balance},\n")

# Create_Account()




def deposit():
    print("\n===== Deposit =====\n")
    Account_Number = input("Enter the Account Number: ")
    with open ("ACC_Details.txt",'r') as file :
        ACC1 = file.readlines()
        for ACC2 in ACC1:
            ACC3 =ACC2.strip().split(',')
        if Account_Number == ACC3[0]:
            amount = float(input("Enter the Amount to Deposit: Rs."))
            if amount > 0:
                ACC3[3]=float(ACC3[3])+amount
                print("You have deposited successfully.")
                from datetime import datetime
                date_time_now = datetime.now()


                with open("Transaction_Details.txt", "a") as file:
                    file.write(f"{date_time_now},{Account_Number} ,deposit,{amount},{ACC3[3]}\n")
            else:
                print("Amount must be positive.")

        else:
            print("Account not in Accounts.")
# deposit()


def withdraw():
    print("\n===== Withdraw =====\n")
    Account_Number = input("Enter the Account Number: ")
    with open ("ACC_Details.txt",'r') as file :
         ACC1 = file.readlines()
         for ACC2 in ACC1:
            ACC3 =ACC2.strip().split(',')
         if Account_Number == ACC3[0]:
            amount = float(input("Enter the Amount to Deposit: Rs."))
            if amount > 0 and amount < float(ACC3[3]):
               
                    ACC3[3]=float(ACC3[3])-amount
                    print("Withdrawal successful.")
                    from datetime import datetime
                    date_time_now = datetime.now()
                    
                    with open("Transaction_Details.txt", "a") as file:
                        file.write(f"{date_time_now},{Account_Number} ,deposit,{amount},{ACC3[3]},\n")
            else:
                    print("Insufficient balance.")
         else:
            print("Incorrect  Account Number.")
   
# withdraw()

def check_balance():
    print("\n=====check_balance=====\n ")
    Account_Number = input("Enter the Account Number: ")
    with open ("ACC_Details.txt",'r') as file :
         ACC1 = file.readlines()
         for ACC2 in ACC1:
            ACC3 =ACC2.strip().split(',')
         if Account_Number == ACC3[0]:
   
              print(f"Your balance is: Rs.{ACC3[3]}")
         else:
              print("Account not found.")
# check_balance()


# def show_transaction_histry():
#     print("\n===== Transaction History =====\n")
#     Account_Number = input("Enter the Account Number: ")
#     with open("Transaction_Details.txt", "r") as file:
#         lines=file.readline()
#         for i in range(len(lines)):
#           list=lines[i].split(",") 
#           if Account_Number==list[1]:
#              print(f"-{list[1]},{list[2]}")
#           else:
#               print("error")
#             # found = False
#             # for line in file:
#             #     if Account_Number in line:
#             #         print(line.strip())
#             #         found = True
#             # if not found:
#             #     print("No transactions found for this account.")
   
# show_transaction_histry()
def Admin_function():
    User_Name = input(f"{'Enter User Name' :<25} :")
    User_Password = input(f"{'Enter User Password' :<25} :")
   







def main_menu():
    while True:
        print("\n==== Welcome to the Bank ====")
        print("1. Admin Login")
        print("2. User Login")
    
        choice = input("Choose an option: ")
        if choice == '1':
                User_Name = input(f"{'Enter User Name' :<25} :")
                User_Password = input(f"{'Enter User Password' :<25} :")
                if User_Name=="Admin123" and User_Password=="pass123":
                  while True:  
                    print("\n===Admin_view===\n")
                    print("\n---Banking Menu (Admin)---\n")        
                    print("1.create_account")
                    print("2.deposit")
                    print("3.withdraw")
                    print("4.check_balance")
                    print("5.show_transaction_histry")
                    print("6.exit")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        Create_Account()                      
                    elif choice == '2':
                        deposit()
                    elif choice == "3":
                            print("\n===withdraw===\n")
                            withdraw()
                    elif choice == "4":
                            print("\n===check_balance===\n")
                            check_balance() 

                # elif choice == "5":
                #        print("\n===show_transaction_histry===\n")
                #         show_transaction_histry()
                          
                    elif choice ==  "6":
                        print("Thanks for using this app.")
                        exit()
                    else:
                        print("Invalid choice.")
    

        elif choice == '2':
            User_Name = input(f"{'Enter User Name' :<25} :")
            User_Password = input(f"{'Enter User Password' :<25} :")

            with open("ACC_Details.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[2] == User_Name and data[1] == User_Password:
                            while True: 

           
                                    print("\n====Banking Menu====\n")
                                    print("1.deposit")
                                    print("2.withdraw")
                                    print("3.check_balance")
                                    print("4.show_transaction_histry")
                                    print("5.exit")
                        

                                    choice = input("Choose an option: ")
                                    if choice == '1':
                                        print("\n===deposit===\n")
                                        deposit()
                                    elif choice == "2":
                                        print("\n===withdraw===\n")
                                        withdraw()
                                    elif choice == "3":
                                        print("\n===check_balance===\n")
                                        check_balance()
                                    # elif choice == "4":
                                        #print("\n===show_transaction_histry===\n")
                                    #      show_transaction_histry()
                                    elif choice ==  "5":
                                        print("Thanks for using this app.")
                                        exit()
        
                              
                            
              

main_menu()
