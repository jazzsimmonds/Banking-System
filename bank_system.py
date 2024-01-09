from customer_account import CustomerAccount 
from accountTypes import Accounts
from admin import Admin 


accounts_list = []
admins_list = []

class BankSystem(object):
    #initialize attributes of BankSystem
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):
        
        # create customers
        cust_id = 1234
        acct_no = 1001
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], cust_id) #creates instance of class CusomerAccount
        acct1 = Accounts(acct_no, "Savings Account", 5000.00, 1000.00, 3) #creates instance of class Accounts
        self.accounts_list.append(customer_1) #adds customer 1 to accounts_list
        customer_1.open_account(acct1) #calls function open_account() with the parameter acct1
        
        cust_id+=1 #increases the value of cust_id by 1
        acct_no+=1 #increases the value of acct_no by 1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], cust_id) #creates instance of class CusomerAccount
        acct1 = Accounts(acct_no, "Business Account", 3200.00, 0.00, 5) #creates instance of class Accounts
        self.accounts_list.append(customer_2)  #adds customer 2 to accounts_list
        customer_2.open_account(acct1) #calls function open_account() with the parameter acct1
        acct_no+=1 #increases the value of acct_no by 1
        acct2 = Accounts(acct_no, "Savings Account", 1520.00, 1000.00, 3) #creates instance of class Accounts
        customer_2.open_account(acct2) #calls function open_account() with the parameter acct2

        cust_id+=1 #increases the value of cust_id by 1
        acct_no+=1 #increases the value of acct_no by 1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], cust_id) #creates instance of class CusomerAccount
        acct1 = Accounts(acct_no, "Student Account", -1000.60, 1500.00, 0) #creates instance of class Accounts
        self.accounts_list.append(customer_3)  #adds customer 3 to accounts_list
        customer_3.open_account(acct1) #calls function open_account() with the parameter acct1
        acct_no+=1 #increases the value of acct_no by 1
        acct2 = Accounts(acct_no, "Current Account", 900.00, 500.00, 4) #creates instance of class Accounts
        customer_3.open_account(acct2) #calls function open_account() with the parameter acct2
        acct_no+=1 #increases the value of acct_no by 1
        acct3 = Accounts(acct_no, "Savings Account", 89.00, 1000.00, 3) #creates instance of class Accounts
        customer_3.open_account(acct3) #calls function open_account() with the parameter acct3
        

        cust_id+=1 #increases the value of cust_id by 1
        acct_no+=1 #increases the value of acct_no by 1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], cust_id) #creates instance of class CusomerAccount
        acct1 = Accounts(acct_no, "Children's Account", 40.00, 0.00, 0) #creates instance of class Accounts
        self.accounts_list.append(customer_4)  #adds customer 4 to accounts_list
        customer_4.open_account(acct1) #calls function open_account() with the parameter acct1
        
        cust_id+=1 #increases the value of cust_id by 1
        acct_no+=1 #increases the value of acct_no by 1
        customer_5 = CustomerAccount("Jasmine", "Simmonds",["19", "Montreal Close", "Worcester", "WR2 4DZ"], cust_id) #creates instance of class CusomerAccount
        acct1 = Accounts(acct_no, "Student Account", 2.19, 1500.00, 0) #creates instance of class Accounts
        self.accounts_list.append(customer_5)  #adds customer 5 to accounts_list
        customer_5.open_account(acct1) #calls function open_account() with the parameter acct1
        acct_no+=1 #increases the value of acct_no by 1
        acct2 = Accounts(acct_no, "Savings Account", 650.00, 1000.00, 3) #creates instance of class Accounts
        customer_5.open_account(acct2) #calls function open_account() with the parameter acct2
        
        #write customers to Customer.txt
        self.write_customer_file() 
        #wrtie accounts to Accounts.txt
        self.write_accounts_file()
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True) #creates instance of class Admin
        self.admins_list.append(admin_1) #adds admin 1 to admins_list

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False) #creates instance of class Admin
        self.admins_list.append(admin_2) #adds admin 2 to admins_list
        
        #write admins to Admins.txt
        self.write_admin_file()
    
    #textfile functions
    def write_accounts_file(self):
        #writes all accounts details to Accounts.txt
        accfile = open("Accounts.txt","w") #opens Accounts.txt in write mode
        accfile.truncate(0) #deletes everyhthin in Accounts.txt
        accfile.close() #closes Accounts.txt
        cust = None #sets the value of cust to None
        for i in self.accounts_list: #searches through each item in the list
            cust = i.get_cust_id() #calls function get_cust_id() to get cust_id for account i
            i.accounts_file(cust) #calls fucntion accounts_file(). writes accounts to Accounts.txt
            
        
    def write_customer_file(self):
        #writes all customer details to Customers.txt
        num = 1
        custfile = open("Customers.txt","w") #opens Customers.txt in write mode
        for i in self.accounts_list: #searches through each item in the list
            i = '{}'.format(i) #turns i into a string so that it can be written to the text file
            x = '{}'.format(num) + "." #formats x so its a string
            custfile.write(x+i+"\n") #writes to Customers.txt
            num += 1 #increases the value of num by 1
        custfile.close() #closes text file
        
    def write_admin_file(self):
        #writes all admin details to Admis.txt
        num = 1
        adminfile = open("Admins.txt","w") #opens Admins.txt in write mode
        for i in self.admins_list: #searches through each item in the list
            i = '{}'.format(i) #turns i into a string so that it can be written to the text file
            x = '{}'.format(num) + "." #formats x so its a string
            adminfile.write(x+i+"\n") #writes to Admins.txt
            num += 1 #increases the value of num by 1
        adminfile.close() #closes text file
            
    def load_customer_file(self):
        #loads Customers.txt
        custfile = open("Customers.txt","r") #opens Customers.txt in read mode
        file = custfile.read() #reads text file, copies contents to the variable file
        custfile.close() #closes text file
        return file
    
    def load_admin_file(self):
        #loads Admins.txt
        adminfile = open("Admins.txt","r") #opends Admins.txt in read mode
        file = adminfile.read() #reads text file, copies contents to the variable file
        adminfile.close() #closes text file
        return file
    
    def load_accounts_file(self):
        #loads Accounts.txt
        accfile = open("Accounts.txt","r") #opends Accounts.txt in read mode
        file = accfile.read() #reads text file, copies contents to the variable file
        accfile.close() #closes text file
        return file
            
    #search functions
    def search_admins_by_name(self, admin_username):
        #search through admins_list[] to find admin
        found_admin = None #sets found_admin to None
        for ad in self.admins_list: #searches through each item in the list
            username = ad.get_username() #calls function get_username() to get username for admin i
            if username == admin_username: #if username is the same as admin_username
                found_admin = ad #changes the value of found_admin to ad
                break #breaks for loop
        if found_admin == None: #if found_admin is None
            print("\n The admin %s does not exist. Please try again"%admin_username)
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        #search through accounts_list[] to find customer
        found_customer = None  #sets found_customer to None
        for cust in self.accounts_list: #searches through each item in the list
            surname = cust.get_last_name() #calls function get_last_name() to get last name for customer i
            if surname == customer_lname: #if surname is the same as customer_lname
                found_customer = cust #changes the value of found_customer to cust
                break #breaks for loop
        if found_customer == None: #if found_customer is None
            print("\n The customer %s does not exist. Please try again."%customer_lname)
        return found_customer
    
    def search_customer_accounts(self,customer_obj, acct_no):
        #searches through accounts[] to find account
        found_account = customer_obj.search_for_account(acct_no) #calls search_for_account() with parameter acct_no to find the account of customer_obj
        msg = "\n Account not found" #sets value of msg
        if found_account != None: #if found_account is not equal to None
            msg = "\n Account %d Found."%found_account #sets value of msg
        return msg, found_account
    
    #login functions
    def admin_login(self, username, password):
        #STEP A.1
        found_admin = self.search_admins_by_name(username) #calls search_admins_by_name() function
        msg = "\n Login Unsuccesful" #sets value of msg
        if found_admin != None: #if found_admin is not equal to None
            if found_admin.get_password() == password: #calls function get_password() to find password for found_admin
                msg = "\n Login sucessful"    #checks if password is the same as the password returned from get_password()
        return msg, found_admin
    
    def customer_login(self, name, accountId):
        found_customer = self.search_customers_by_name(name) #calls search_customers_by_name() function
        msg = "\n Login Unsuccesful" #sets value of msg
        if found_customer != None: #if found_customer is not equal to None
            if found_customer.get_cust_id() == accountId: #calls function get_cust_id() to find cust_id for found_customer
                msg = "\n Login sucessful"    #checks if accountId is the same as the cust_id returned from get_cust_id()
        return msg, found_customer
    
    #account functions
    def transferMoney(self, sender_acc, receiver_lname, sender_account_no, receiver_account_no, amount):
        #transfers money between two accounts in accounts[]
        receiver_acc = self.search_customers_by_name(receiver_lname)
        if sender_acc != None and receiver_acc != None: #is sender_acc and receiver_acc are not equal to None
            msg, accounts_obj = self.search_customer_accounts(sender_acc, sender_account_no)
            msg1, receiver_obj = self.search_customer_accounts(receiver_acc, receiver_account_no)
            print(msg)
            print(msg1)
            if accounts_obj != None and receiver_obj != None: #if accounts_obj and receiver_obj are not equal to None
                if accounts_obj != receiver_obj: #if accounts_obj is not the same as receiver_obj
                    print("\nTransaction Pending...")
                    print("")
                    can_send = sender_acc.withdraw_money(accounts_obj, amount) #calls function withdraw_money() to withdraw money from accounts_obj
                    if can_send == True: #if can send is True. Checks accounts_obj had enough money in their account
                        receiver_acc.deposit_money(receiver_obj, amount) #calls functon deposit_money() to deposit money into receiver_obj
                    else: #if can_send is False. (accounts_obj had insuficient funds)
                        print("Error, insuficent funds in acccount %d"%accounts_obj)
                        print("Transfer unable to be completed. Please try again")
                else: #if accounts_obj and receiver_obj are the same. (cant transfer money to their own account)
                    print("\nError. Sender account and receiver account cant be the same. Please try again.")
            else: #accounts_obj and/or receiver_obj are None. (account was not found)
                print("\nError. The accout for %s cant be found. Please try again."%receiver_lname)
    
    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list: #searches through each item in the list
                i+=1 #increases the value of i by 1
                print('\n Customer %d: ' %i, end = ' ')
                print("\n---------------")
                c.print_details() #calls function print_details() to print accounts for customer c
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
    def totalCustomers(self):
        #calculates total customers in accounts_list[]
        total_customers = len(self.accounts_list) #finds number of items in list
        return total_customers
    
    def total_money_customers(self):
        total_money = 0
        for i in self.accounts_list: #searches through each item in the list
            money = i.total_money() #calls function total_money() to find the total money of all customer i's accounts
            total_money += money #adds the value of money to total_money
        return total_money
    
    def total_interest_customers(self):
        #calculates the total interest payable for 1 year from all customers in accounts_list[] 
        total_interest = 0
        for i in self.accounts_list: #searches through each item in the list
            interest = i.calc_total_interest() #calls function calc_total_interest() to find the total interest payable of all customer i's accounts
            total_interest += interest #adds the value of interest to total_interest
        return total_interest
    
    def total_overdraft_customers(self):
        #calculates the total overdraft amount being used by all customers in accounts_list[] 
        totalOverdraft = 0
        for i in self.accounts_list: #searches through each item in the list
            overdraft = i.cal_total_overdraft() #calls function cal_total_overdraft() to find the total interest being used by all customer i's accounts
            totalOverdraft += overdraft #adds the value of overdraft to totalOverdraft
        return totalOverdraft
        

    #main menu functions
    def main_menu(self):
        #prints the main menu
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Customer login")
        print ("3) Quit Python Bank System")
        print (" ")
        option = input ("Choose your option: ")
        return option


    def run_main_options(self):
        #run main menu options
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            try: #checks choice is an integer
                choice = int(choice)
            except: #prints error message if choice isnt an integer
                print("\nIncorrect input type entered. Please try again")
            if choice == 1: #if choice is 1
                #admin login
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password) #calls function admin_login() with the parameters username and password
                print(msg)
                if admin_obj != None: #if admin_obj is not equal to None
                    if msg == "\n Login sucessful":
                        self.run_admin_options(admin_obj) #calls function run_admin_options() with the parameter admin_obj
            elif choice == 2: #if choice is 2
                #customer login
                while True:
                    name = input("Customer Last name: ")
                    if name.isalpha(): #checks name is letters
                        name = name.capitalize() #capitalizes the first lettter in name
                        break #breaks while loop
                    else: #if name is not letters an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    accountId = input("Customer id: ")
                    try: #checks accountId is an integer
                        accountId = int(accountId)
                        break #breaks while loop
                    except: #if accountId isnt an integer an error message is printed
                       print("\nIncorrect input type entered. Please try again")
                msg, customer_obj = self.customer_login(name, accountId) #calls function customer_login() with the parameters name and accountId
                print(msg)
                if customer_obj != None: #if customer_obj is not equal to None
                    if msg == "\n Login sucessful":
                        self.run_customer_menu(customer_obj) #calls function run_customer_menu() with the parameter customer_obj
            elif choice == 3: #if choice is 3
                #close bank system
                loop = 0 #breaks while loop
            else: #if choice is not 1,2 or 3
                print("\nPlease enter a valid option.")
        print ("\n Thank-You for stopping by the bank!")
        
    #admin menu functions  
    def admin_menu(self, admin_obj):
        #print the options you have
         print ("")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations")
         print ("3) Customer Profile Settings")
         print ("4) Delete customer")
         print ("5) Print all customers detail")
         print ("6) Request managment report")
         print ("7) Admin account settings")
         print ("8) Sign out")
         print (" ")
         option = input ("Choose your option: ")
         return option

    def run_admin_options(self, admin_obj):
        #run admin options                          
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            try: #checks choice is an integer
                choice = int(choice)
            except: #if choice isnt an integer an error message is printed
                print("\nIncorrect input type entered. Please try again")
            if choice == 1:
                #transfer money between accounts
                while True:
                    sender_lname = input("\n Please input sender surname: ")
                    if sender_lname.isalpha(): #checks sendre_lname is letters only
                        sender_lname = sender_lname.capitalize() #capitalizes first letter of the string
                        break #ends while loop
                    else: #if sender_lname isnt letters only an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    sender_account_no = input("\n Please input sender account number: ")
                    try: #checks sender_acct_no is an integer
                        sender_account_no = int(sender_account_no)
                        break #breaks while loop
                    except: #if sender_account_no isnt an integer an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    amount = input("\n Please input the amount to be transferred: ")
                    try: #checks amount is a float. converts integer to float
                        amount = float(amount)
                        break #breaks while loop
                    except: #if amount isnt a float an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    receiver_lname = input("\n Please input receiver surname: ")
                    if receiver_lname.isalpha(): #checks receiver_lname is letters only
                        receiver_lname = receiver_lname.capitalize() #capitalizes first letter of the string
                        break #ebds while loop 
                    else: #if receiver_lname isnt letters only an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    receiver_account_no = input("\n Please input receiver account number: ")
                    try: #checks receiver_account_no is an integer
                        receiver_account_no = int(receiver_account_no)
                        break #ends while loop
                    except: #if receiver_account_no isnt an integer an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                sender_acc = self.search_customers_by_name(sender_lname) #calls function search_customers_by_name() with the parameter sender_lname
                if sender_lname != None: #if sender_lname is not equal to None
                    self.transferMoney(sender_acc, receiver_lname, sender_account_no, receiver_account_no, amount) #calls transfer_money() function with 5 parameters
                else: #if sender_lname is equal to None (customer cant be found)
                    print("\nError. The accout for %s cant be found. Please try again."%sender_lname)                    
            elif choice == 2: #if choice is 2
                #customer account operations
                while True:
                    customer_name = input("\n Please input customer surname: ")
                    if customer_name.isalpha(): #chekcs customer_name is letters only
                        customer_name = customer_name.capitalize() #capitalizes first letter of the string
                        break #breaks while loop
                    else: #if customer_name isnt letters only an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                customer_account = self.search_customers_by_name(customer_name) #calls function search_customers_by_name() with the parameter customer_name
                if customer_account != None: #if customer_account is not equal to None
                    while True:
                        acct_no = input("Please entre the customers account number: ")
                        try: #checks that the user inputted an integer
                            acct_no = int(acct_no)
                            break #breaks while loop
                        except: #runs if the user did not input an integer
                            print("\nIncorrect input type entered. Please try again")
                    msg, accounts_obj = self.search_customer_accounts(customer_account, acct_no) #calls function search_customer_accounts() with the parameters customer_account and acct_no
                    print(msg)
                    if accounts_obj != None: #if accounts_obj is not equal to None
                        customer_account.run_accounts_options(accounts_obj) #calls function run_accounts_options() with parameter accounts_obj
            elif choice == 3: #if choice is 3
                #customer profile settings
                while True:
                    customer_name = input("\n Please input customer surname: ")
                    if customer_name.isalpha(): #checks customer_name is letters only
                        customer_name = customer_name.capitalize() #capitalizes first letter of the string
                        break #breaks while loop
                    else: #if customer_name is not letters only an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                customer_account = self.search_customers_by_name(customer_name) #calls function search_customers_by_name() with the parameter customer_name
                if customer_account != None: #if customer_account is not equal to none
                    customer_account.run_account_options() #calls function run_account_options() for customer_account
            elif choice == 4: #if choice is 4 
                #delete a customer
                if admin_obj.has_full_admin_right() == True: #calls function has_full_admin_right() for aadmin_obj. if it returns True:
                    while True:
                        custName = input("Please enter the last name of the customer you would like to remove: ")
                        if custName.isalpha(): #checks custName is letters only
                            custName = custName.capitalize() #capitalizes first letter of the string
                            break #breaks while loop
                        else: #if custName isnt letters only an error message is printed
                            print("\nIncorrect input type entered. Please try again")
                    found_customer = self.search_customers_by_name(custName) #find account details linked to the last name 
                    if found_customer != None: #if found_customer if not equal to None
                        self.accounts_list.remove(found_customer) #removes customers account from accounts_list
                        print("\n %s has sucessfully been removed."%custName)
                        self.write_customer_file() #calls function write_customer_file()
                else: #if has_full_admin_rights() returns False
                    print("\nThis action is restricted as you do not have full admin rights")
            elif choice == 5: #if choice is 5
                #print ALL customers details
                self.print_all_accounts_details() #calls functions print_all_accounts_details()
            elif choice == 6: #if choice is 6
                #managment report
                total_cust = self.totalCustomers() #calls function totalCustomers()
                total_cust_money = self.total_money_customers() #calls function total_money_customers()
                total_intr = self.total_interest_customers() #calls function total_interest_customers()
                total_overdraft = self.total_overdraft_customers() #calls function total_overdraft_customers()
                print("\nManagment Report:")
                print ("~~~~~~~~~~~~~~~~~~~")
                print("Total customers: %s"%total_cust)
                print("Total sum of money in all customer accounts: £%.2f"%total_cust_money)
                print("The total interest payapble to accounts based on a monthly payment for one year is £%.2f"%total_intr)
                print("Total amount of overdrafts currently taken: £ %.2f"%total_overdraft)
            elif choice == 7: #if choice is 7
                admin_obj.run_admin_options() #calls function run_admin_options() for admin_obj
            elif choice == 8: #if choice is 8
                #sign out
                loop = 0 #breaks loop
        print ("\n Signing out...")

    #customer menu functions
    def customer_menu(self, customer_obj):
        #print customer menu
         print (" ")
         print ("Welcome %s %s : Your transaction options are:" %(customer_obj.get_first_name(), customer_obj.get_last_name()))
         print ("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
         print ("1) Transfer money")
         print ("2) Other account operations")
         print ("3) profile settings")
         print ("4) Sign out")
         print (" ")
         option = input ("Choose your option: ")
         return option
    
    def run_customer_menu(self, customer_obj):
        #run customer options
        loop = 1
        while loop == 1:
            choice = self.customer_menu(customer_obj)
            try: #checks choice is an integer 
                choice = int(choice)
            except: #if choice isnt integer an error message is printed
                print("\nIncorrect input type entered. Please try again")
            if choice == 1: #if choice is 1
                #transfer money
                while True:
                    acct_no = input("Please enter the senders account number: ")
                    try: #checks acct_no is an integer
                        acct_no = int(acct_no)
                        break #breaks while loop
                    except: #if acct_no isnt an integer an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    receiver_lname = input("Please enter the receivers last name: ")
                    if receiver_lname.isalpha(): #checks reciever_lname is letters only
                        receiver_lname = receiver_lname.capitalize() #capitalizes first letter of the string
                        break #breaks while loop
                    else: #if receiver_lname is not letters only an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    receiver_acc_no = input("Please enter the receivers account number: ")
                    try: #checks receiver_acc_no is an integer
                        receiver_acc_no = int(receiver_acc_no)
                        break #breaks while loop
                    except: #if reciever_acc_no isnt an integer an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    amount = input("Amount: £")
                    try: #checks amount is a float. turns integers into a floar
                        amount = float(amount)
                        break #breaks while loop
                    except: #if amount isnt a float an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                self.transferMoney(customer_obj, receiver_lname, acct_no, receiver_acc_no, amount) #calls function transferMoney() with 5 parameters
            elif choice == 2: #if choice is 2
                #account operations
                while True:
                    acct_no = input("Please entre your account number: ")
                    try: #checks that the user inputted an integer
                        acct_no = int(acct_no)
                        break #breaks while loop
                    except: #runs if the user did not input an integer
                        print("\nIncorrect input type entered. Please try again")
                msg, accounts_obj = self.search_customer_accounts(customer_obj, acct_no) #calls function search_customer_accounts() with parameters customer_obj and acct_no
                print(msg)
                if accounts_obj != None: #if accounts_obj is not equal to None
                    customer_obj.run_accounts_options(accounts_obj) #calls function run_accounts_options with parameter accounts_obj
            elif choice == 3: #if choice is 3
                #profile settings
                customer_obj.run_account_options() #calls function run_account_options() for customer_obj
            elif choice == 4: #if choice is 4
                #sign out
                loop = 0 #ends while loop
        print ("\n Signing out...")

app = BankSystem() 
app.run_main_options()
