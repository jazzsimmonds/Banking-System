
class CustomerAccount:
    #initialize attributes of CustomerAccoung
    def __init__(self, fname, lname, address, cust_id):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.cust_id = int(cust_id)
        self.accounts = [] 
    
    #add account
    def open_account(self, acct):
        self.accounts.append(acct) #adds acct to accounts list
    
    #get functions
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
    
    def get_address(self):
        return self.address
    
    def get_cust_id(self):
        return self.cust_id
    
    def display_address(self):
        num = self.address[0] #sets num to the first value in the list self.address
        street = self.address[1] #sets street to the second value in the list self.address
        city = self.address[2] #sets city to the third value in the list self.address
        postcode = self.address[3] #sets postcode to the fourth value in the list self.address
        num = '{}'.format(num) #turns num into a string
        a = num + " " + street + ", " + city + ", " + postcode #adds spaces and commas between elements in self.address
        return a
    
    #textfile functions
    def accounts_file(self, cust):
        #writes each account to Accounts.txt
        num = 1
        x = cust
        cust = "Customer " + '{}'.format(cust) + ": \n" 
        accfile = open("Accounts.txt","a+") #opens Accounts.txt in append mode
        accfile.write(cust) #writes cust to Accounts.txt
        for i in self.accounts: #searches through each item in the list
            i = '{}'.format(i) #turns i into a string so that it can be written to the text file
            x = '{}'.format(num) + "." #formats x so its a string
            accfile.write(x+i+"\n") #writes to Accounts.txt
            num += 1 #increases the value of num by 1
        accfile.close() #closes text file
        
    #update functions
    def update_first_name(self, fname):
        #updates firstname and Customers.txt
        oldName = self.fname #copies self.fname to oldName
        self.fname = fname #changes value of self.fname to fname
        custfile = open("Customers.txt","r+") #opens Customers.txt in read and write mode
        file = custfile.read() #copies contents of Customers.txt to file
        oldName = '{}'.format(oldName) #formats oldName so its a string
        y = '{}'.format(self.fname) #formats self.fname so its a string and stores it in variable y
        file = file.replace(oldName, y) #replaces any instances of oldName in Customers.txt with y
        file = '{}'.format(file) #formates file so its a string
        custfile.truncate(0) #deletes contents of Customers.txt
        custfile.write(file) #writes contents of file to Customers.txt
        custfile.close() #closes Customers.txt
    
    def update_last_name(self, lname):
        #updates lastname and Customers.txt
        oldName = self.lname #copies self.lname to oldName
        self.lname = lname #changes value of self.lname to lname
        custfile = open("Customers.txt","r+") #opens Customers.txt in read and write mode
        file = custfile.read() #copies contents of Customers.txt to file
        oldName = '{}'.format(oldName) #formats oldName so its a string
        y = '{}'.format(self.lname) #formats self.lname so its a string and stores it in variable y
        file = file.replace(oldName, y) #replaces any instances of oldName in Customers.txt with y
        file = '{}'.format(file) #formates file so its a string
        custfile.truncate(0) #deletes contents of Customers.txt
        custfile.write(file) #writes contents of file to Customers.txt
        custfile.close() #closes Customers.txt
                 
    def update_address(self, houseNo, streetName, town, postcode):
        #updates address and Customers.txt
        oldAddr = self.address #copies self.address to oldAddr
        addr = [houseNo, streetName, town, postcode] #sets values of list addr 
        self.address = addr #changes value of self.address to addr
        print("\n Address updated")
        custfile = open("Customers.txt","r+") #opens Customers.txt in read and write mode
        file = custfile.read() #copies contents of Customers.txt to file
        oldAddr = '{}'.format(oldAddr) #formats oldAddr so its a string
        y = '{}'.format(self.address) #formats self.address so its a string and stores it in variable y
        file = file.replace(oldAddr, y) #replaces any instances of oldAddr in Customers.txt with y
        file = '{}'.format(file) #formates file so its a string
        custfile.truncate(0) #deletes contents of Customers.txt
        custfile.write(file) #writes contents of file to Customers.txt
        custfile.close() #closes Customers.txt
        
    #print functions 
    def print_address(self):
        print("Address: %s"%self.address) #prints self.address
    
    def print_details(self):
        #STEP A.4.3
        print(""" Name: %s %s
 Address: %s
 Account Number: %d"""%(self.fname, self.lname, self.display_address(), self.cust_id))
        print("\nCustomer's Accounts:")
        print("-------------------")
        i = 0
        for c in self.accounts: #searches through each item in the list
            i+=1 #increases value of i by 1
            x = "%"
            print("%d . %s%s"%(i,c.print_account_info(),x))
    
    
    def search_for_account(self, acct_no):
        found_account = None #sets found_account to None (empty)
        for i in self.accounts: #searches through each item in the list
            account = i.get_acct_id() #calls function to get account id for account i
            if account == acct_no: #if contents of account are the same as acct_no
                found_account = account #copies account to found_account
                break #breaks for loop
        if found_account == None: #if found_account is None
            print("\n The Account %s does not exist. Please try again."%acct_no)
        return found_account
    
    #account operations
    def check_balance(self, acct_no):
        for i in self.accounts: #searches through each item in the list
            if i.get_acct_id() == acct_no: #if acct_num is the same as the account id for i
                balance = i.get_balance() # calls function to get balance for account i
                print("\nBalance: £%.2f"%balance) #prints balance

    def deposit_money(self, acct_no, dep):
        for i in self.accounts: #searches through each item in the list
            if i.get_acct_id() == acct_no: #if acct_num is the same as the account id for i
                i.deposit(dep)#call deposit function for i with the parameter dep

    def withdraw_money(self, acct_no, wd):
        can_withdraw = False #sets can_withdraw as False
        for i in self.accounts: #searches through each item in the list
            if i.get_acct_id() == acct_no: #if acct_num is the same as the account id for i
                overdraft_limit = i.get_overdraft_limit() #calls function get_overdraft_limit() to check overdraft for account i
                bal = i.get_balance() #calls function get_balance() to get balance for account i
                if overdraft_limit == 0: #if overdraft limit is equal to 0 (doesn't have an overdraft)
                    if bal > wd: #if balance is bigger than wd
                        i.withdraw(wd) #calls function withdraw(). withdraws wd from account i
                        can_withdraw = True #sets can_withdraw to True
                        break #breaks for loop
                else: #if overdraft_limit doesnt equal 0
                    if bal > 0: #if bal is bigger than 0 
                        if bal > wd: #if balance is bigger than wd
                            i.withdraw(wd) #calls function withdraw(). withdraws wd from account i
                            can_withdraw = True #sets can_withdraw to True
                            break #breaks for loop
                    else: #if balance is smaller than 0
                        can_withdraw = i.check_overdraft(wd)
                        if can_withdraw == True: #if can_withdraw is True
                            i.withdraw(wd) #calls function withdraw(). withdraws wd from account i
                            break #breaks for loop
        return can_withdraw
                
    def total_money(self):
        money = 0
        for i in self.accounts: #searches through each item in the list
            m = i.get_balance() #calls on the get balance function for account i
            money += m #adds m to money
        return money
    
    def calc_total_interest(self):
        #calcutes the total interest payable to ALL accounts for 1 year
        #based off each accounts current balance and interest rates
        interest = 0 
        for i in self.accounts: #searches through each item in the list
            year_payable_interest = 0
            bal = i.get_balance() #calls function get_balance() to get balance for account i
            ir = i.get_interest() #calls function get_interest() to get interest rate for account i
            if ir != 0: #makes sure interest rate isnt 0%
                year_payable_interest = self.calc_interest(bal, ir) #calls function cal_interest() with the parameters bal and ir
            interest += year_payable_interest #increased the value of interest by year_payable_interest
        return interest
    
    def calc_interest(self, bal, rate): 
        #calculate an accounts total interest payable for 1 year
        year_payable_interest = bal * (rate/100) #multiplies balance by (rate divied by 100)
        return year_payable_interest
    
    def cal_total_overdraft(self):
        #calculates total overdrafts being used by ALL customers
        overdraft = 0
        for i in self.accounts: #searches through contents of the list
            used_overdraft = 0
            limit = i.get_overdraft_limit() #calls function get_overdraft_limit() to get overdraft limit for account i 
            bal = i.get_balance() #calls function get_balance() to get balance for account i
            if limit != 0: #runs if limit is not equal to 0
                used_overdraft = self.calc_overdraft(limit, bal)
            overdraft += used_overdraft #adds the total of used_overdraft to overdraft
        return overdraft
    
    def calc_overdraft(self,limit, bal):
        #calculates how far a customer is into their overdraft
        used_overdraft = 0
        if bal < 0: #runs if balance is smaller than 0
            used_overdraft = abs(bal)#converts contents of bal to a positive number
        return used_overdraft
    
    def check_postcode(self,pc):
        #checks user entered a valid input type
        #6 formarts for UK postcodes:
            #(9=number, A=letter)
            #A9 9AA
            #A9A 9AA, A99 9AA, AA9 9AA
            #AA99 9AA, AA9A 9AA
        msg = "no"
        postcode_length = len(pc) #finds the number of characters in pc
        if postcode_length == 5: #runs if postcode has 5 characters
            a = pc[0] #stores character 1 as a
            b = pc[1] #stores character 2 as b
            c = pc[2] #stores character 3 as c
            d = pc[3] #stores character 4 as d
            e = pc[4] #stores character 5 as e
            if a.isalpha(): #checks if its a letter
                if b.isdigit(): #checks if its a number
                    if c.isdigit(): #checks if its a number
                        if d.isalpha(): #checks if its a letter
                            if e.isalpha(): #checks if its a letter
                                msg = "yes"
                                pc = pc[0]+pc[1]+" "+pc[2]+pc[3]+pc[4]
                                pc = pc.upper() #makes enter contents of pc capital letters
                                #A9 9AA
        elif postcode_length == 6: #runs if postcode has 6 characters
            a = pc[0] #stores character 1 as a
            b = pc[1] #stores character 2 as b
            c = pc[2] #stores character 3 as c
            d = pc[3] #stores character 4 as d
            e = pc[4] #stores character 5 as e
            f = pc[5] #stores character 6 as f
            if a.isalpha(): #checks if its a letter
                if b.isdigit(): #checks if its a number
                    if c.isalpha(): #checks if its a letter
                        if d.isdigit(): #checks if its a number
                            if e.isalpha(): #checks if its a letter
                                if f.isalpha(): #checks if its a letter
                                    msg = "yes"
                                    pc = pc[0]+pc[1]+pc[2]+" "+pc[3]+pc[4]+pc[5]
                                    pc = pc.upper() #makes enter contents of pc capital letters
                                    #A9A 9AA
                    else: #runs if c is not a letter
                        if c.isdigit(): #checks if its a number
                            if d.isdigit(): #checks if its a number
                                if e.isalpha(): #checks if its a letter
                                    if f.isalpha(): #checks if its a letter
                                        msg = "yes"
                                        pc = pc[0]+pc[1]+pc[2]+" "+pc[3]+pc[4]+pc[5]
                                        pc = pc.upper() #makes enter contents of pc capital letters
                                        #A99 9AA
                else: #runs if b in not a number
                    if b.isalpha(): #checks if its a letter
                        if c.isdigit(): #checks if its a number
                            if d.isdigit(): #checks if its a number
                                if e.isalpha(): #checks if its a letter
                                    if f.isalpha(): #checks if its a letter
                                        msg = "yes"
                                        pc = pc[0]+pc[1]+pc[2]+" "+pc[3]+pc[4]+pc[5]
                                        pc = pc.upper() #makes enter contents of pc capital letters
                                        #AA9 9AA
        elif postcode_length == 7: #runs if postcode has 7 characters
            a = pc[0] #stores character 1 as a
            b = pc[1] #stores character 2 as b
            c = pc[2] #stores character 3 as c
            d = pc[3] #stores character 4 as d
            e = pc[4] #stores character 5 as e
            f = pc[5] #stores character 6 as f
            g = pc[6] #stores character 7 as g
            if a.isalpha(): #checks if its a letter
                if b.isalpha(): #checks if its a letter
                    if c.isdigit(): #checks if its a number
                        if d.isalpha(): #checks if its a letter
                            if e.isdigit(): #checks if its a number
                                if f.isalpha(): #checks if its a letter
                                    if g.isalpha(): #checks if its a letter
                                        msg = "yes"
                                        pc = pc[0]+pc[1]+pc[2]+pc[3]+" "+pc[4]+pc[5]+pc[6]
                                        pc = pc.upper() #makes enter contents of pc capital letters
                                        #AA9A 9AA 
                        else: #runs if d is not a letter
                            if d.isdigit(): #checks if its a number
                                if e.isdigit(): #checks if its a number
                                    if f.isalpha(): #checks if its a letter
                                        if g.isalpha(): #checks if its a letter
                                            msg = "yes"
                                            pc = pc[0]+pc[1]+pc[2]+pc[3]+" "+pc[4]+pc[5]+pc[6]
                                            pc = pc.upper() #makes enter contents of pc capital letters
                                            #AA99 9AA 
        return msg, pc     
    
    #string representation of object
    def __str__(self):
        return f'{self.fname} {self.lname}, ({self.address[0]} {self.address[1]}, {self.address[2]}, {self.address[3]}), {self.cust_id}'
    
    #Account menu
    def account_menu(self):
        #prints profile settins menu
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Update customer name")
        print ("2) Update customer address")
        print ("3) Show customer details")
        print ("4) Back")
        print (" ")
        option = input ("Choose your option: ")
        return option
    
    def run_account_options(self):
        #runs profile settings options based on user input
        loop = 1
        while loop == 1: 
            choice = self.account_menu() #calls funtion account_menu(). stores users input as choice
            try: #checks if choice is an integer
                choice = int(choice)
            except: #prints error message if choice isnt an integer
                print("\nIncorrect input type entered. Please try again")
            if choice == 1: #if choice is 1 
                #update customer name
                xloop = 1
                while xloop == 1: 
                    x = input("Would you like to change the forename, surname or both?: ")
                    x = x.lower() #makes contents of x lowercase
                    if x == "forename": #if x is forename
                        while True:
                            fName = input("Please enter the new forename: ")
                            if fName.isalpha(): #checks fName is only letters
                                fName = str(fName)
                                fName = fName.capitalize() #capitalizes first letter of the string
                                self.update_first_name(fName) #calls function update_first_name() with the parameter fName
                                break #breaks while loop
                            else: #if fName isnt only letters an error message is printed
                                print("\nIncorrect input type entered. Please try again")
                        xloop = 0 #breaks while loop
                    elif x == "surname":
                        while True:
                            sName = input("Please enter the new surname: ")
                            if sName.isalpha(): #checks sName is only letters
                                sName = str(sName)
                                sName = sName.capitalize() #capitalizes first letter of the string
                                self.update_last_name(sName) #calls function update_last_name() with the parameter sName
                                break #breaks while loop
                            else: #if sName isnt only letters an error message is printed
                                print("\nIncorrect input type entered. Please try again")
                        xloop = 0 #breaks while loop
                    elif x == "both":
                        while True:
                            fName = input("Please enter the new forname: ")
                            if fName.isalpha(): #checks fName is only letters
                                fName = str(fName)
                                fName = fName.capitalize() #capitalizes first letter of the string
                                break #breaks while loop
                            else: #if fName isnt only letters an error message is printed
                                print("\nIncorrect input type entered. Please try again")
                        while True:
                            sName = input("Please enter the new surname: ")
                            if sName.isalpha(): #checks sName is only letters
                                sName = str(sName)
                                sName = sName.capitalize() #capitalizes first letter of the string
                                break #breaks while loop
                            else: #if sName isnt only letters an error message is printed
                                print("\nIncorrect input type entered. Please try again")
                                
                        self.update_first_name(fName) #calls function update_first_name() with the parameter fName
                        self.update_last_name(sName) #calls function update_last_name() with the parameter sName
                        xloop = 0 #breaks while loop
                    else:
                        print("Error, incorrect value entered. Please try again.")
                print("\n The updated customer name is %s %s" %(self.fname, self.lname))
            elif choice == 2:
                #update address
                while True:
                    house_no = input("Please enter the new house number: ")
                    try: #chekcs house_no is an integer
                        house_no = int(house_no)
                        break #breaks while loop
                    except: #prints error message is house_no isnt an integer
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    street_name = input("Please entre the new street name: ")
                    x = street_name.replace(" ", "") #removes whitespaces
                    if x.isalpha(): #checks only letters are inputted
                        street_name = street_name.title()#capitalizes first letter of each word
                        break #breaks while loop
                    else: #prints error message if x isnt only letters
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    town_city = input("Please entre the new Town/City: ")
                    if town_city.isalpha(): #checks only letters are inputted
                        town_city = town_city.capitalize() #capitalizes first letter of the string
                        break #breaks while loop
                    else: #prints error message if town_city isnt only letters
                        print("\nIncorrect input type entered. Please try again")
                while True:
                    postcode = input("Please entre the new postcode: ")
                    postcode = postcode.replace(" ", "") #removes whitespaces
                    msg, postcode = self.check_postcode(postcode)
                    if msg == "yes": #if msg is "yes". (if postcode is the correct format)
                        self.update_address(house_no, street_name, town_city, postcode)
                        break #breaks while loop
                    else: #prints error message if invalid postcode format is entered
                        print("Error, invalid postcode type entered. Please try again")
            elif choice == 3: #if choice is 3
                print("")
                self.print_details() #calss function print_details()
            elif choice == 4: #if choice is 4
                #return
                loop = 0 #ends while loop
        print ("\n Exit account operations")
        
    #Accounts menu
    def accounts_menu(self, accounts_obj):
        #prints account operations menu
        print("")
        print("Account Number: %d "%accounts_obj)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your transaction options are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit ")
        print("2) Withdraw")
        print("3) Check balance")
        print("4) Return")
        print(" ")
        option = input("Choose your option: ")
        return option
    
    def run_accounts_options(self, accounts_obj):
        #run account operations options
        loop = 1
        while loop == 1:
            choice = self.accounts_menu(accounts_obj) #calls funtion accounts_menu(). stores users input as choice
            try: #checks if choice is an integer
                choice = int(choice)
            except: #if choice isnt an integer an error message is printed
                print("\nIncorrect input type entered. Please try again")
            if choice == 1: #if choice is 1
                #deposit
                while True:
                    dep = input("Enter the amount you would like to deposit: ")
                    try: #checks dep is a float. also turns integers into a float
                        dep = float(dep)
                        break #breaks while loop
                    except: #if dep isnt a float an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                self.deposit_money(accounts_obj, dep) #calls function deposit_money() with the parameters accounts_obj and dep
            elif choice == 2: #if choice is 2
                #withdraw
                while True:
                    wd = input("Enter the amount you would like to withdraw: ")
                    try: #checks wd is a float. changed integers to a float
                        wd = float(wd)
                        break #breaks while loop
                    except: #if wd isnt a float an error message is printed
                        print("\nIncorrect input type entered. Please try again")
                self.withdraw_money(accounts_obj, wd) #calls function withdraw_money() with the parameters accounts_obj and wd
            elif choice == 3: #if choice is 3
                #check balance
                self.check_balance(accounts_obj) #calls function check_balance() with the parameter accounts_obj
            elif choice == 4:
                #return
                loop = 0 #ends while loop
        
        
            
                