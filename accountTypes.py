class Accounts:
    #initialize attributes of Accounts
    def __init__(self, acct_id, accountName, balance, overdraftLimit, interest):
        self.acct_id = int(acct_id)
        self.acct_name = accountName
        self.balance = float(balance)
        self.overdraftLimit = float(overdraftLimit)
        self.interest = int(interest)
        
    #get functions 
    def get_acct_id(self):
        return self.acct_id
    
    def get_acct_name(self):
        return self.acct_name
    
    def get_balance(self):
        return self.balance
    
    def get_overdraft_limit(self):
        return self.overdraftLimit
    
    def get_interest(self):
        return self.interest
    
    #string representation of object
    def __str__(self):
        return f'{self.acct_id}, {self.acct_name}, £{self.balance}, £{self.overdraftLimit}, {self.interest}%'  
    
    #print functions
    def print_balance(self):
        print("\n The balance for Account %d is £%.2f"%(self.acct_id, self.balance))
        
    def print_account_info(self):
        return """Account ID: %d
    Account Name: %s
    Balance: £%.2f
    Overdraft Limit: £%.2f
    Interest: %d"""%(self.acct_id,self.acct_name,self.balance,self.overdraftLimit,self.interest)
     
    #textfile functions
    def updateBalance(self,oldBalance):
        #updates firstname and Customers.txt
        accfile = open("Accounts.txt","r+") #opens Accounts.txt in read and write mode
        file = accfile.read() #copies contents of Accounts.txt to file
        oldBalance = '{}'.format(oldBalance) #formats oldBalance so its a string
        y = '{}'.format(self.balance) #formats self.balance so its a string and stores it in variable y
        file = file.replace(oldBalance, y) #replaces any instances of oldBalance in Customers.txt with y
        file = '{}'.format(file) #formates file so its a string
        accfile.truncate(0) #deletes contents of Accounts.txt
        accfile.write(file) #writes contents of file to Accounts.txt
        accfile.close() #closes Accounts.txt
        
    #account functions     
    def check_overdraft(self,amount):
        overdraft = False #sets overdraft as False
        x = self.balance - amount #subracts amount from self.balance
        x = abs(x) #makes x a positive number
        if x <= self.overdraftLimit: #if x if smaler than or equal to self.overdraftLimit
            overdraft = True #sets overdraft as True
        return overdraft
    
    def deposit(self, amount):
        oldBalance = self.balance #copies self.balance to oldBalance
        self.balance+=amount #adds amount to self.balance
        print("Deposit complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
        self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance
        
    def withdraw(self, amount):
        if self.balance < amount: #if self.balance is smaller than amount
            if self.overdraftLimit != 0: #if self.overdraftLimit is not equal to 0
                overdraft = self.check_overdraft(amount) #calls function check_overdraft() with parameter amount
                if overdraft == True: #if overdraft is True
                    oldBalance = self.balance #copies self.balance to oldBalance
                    self.balance = self.balance - amount #subracts amount from self.balance
                    remainingOverdraft = self.overdraftLimit - abs(self.balance) #abs(self.balance) gives the positive version of self balance, which is then subracted from self.overdraftLimit
                    print("Withdrawal complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
                    print("Account %d remaining overdraft is: £%.2f"%(self.acct_id, remainingOverdraft))
                    self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance
                else: #if overdraft is False
                    while True:
                        print("Insuficcent funds avaliable")
                        print("Your balance is £%.2f"%self.balance)
                        print("Your overdraft limit is £%.2f"%self.overdraftLimit)
                        while True:
                            amount = input("Please select a different withdrawl amount: £")
                            try: #chekcs amount is an float. turns integers into floats
                                amount = float(amount)
                                break #breaks while loop
                            except: #if amount isnt an float an error message 
                                print("\nIncorrect input type entered. Please try again")
                        overdraft = self.check_overdraft(amount) #calls function check_overdraft() with parameter amount
                        if self.balance > amount: #if self.balance if bigger than amount
                            oldBalance = self.balance #copies self.balance to oldBalance
                            self.balance = self.balance - amount #subracts amount from self.balance
                            remainingOverdraft = self.overdraftLimit - abs(self.balance)  #abs(self.balance) gives the positive version of self balance, which is then subracted from self.overdraftLimit
                            print("Withdrawal complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
                            print("Account %d remaining overdraft is: £%.2f"%(self.acct_id, self.overdraftLimit))
                            self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance
                            break #breaks while loop
                        elif overdraft == True: #if overdraft is True
                            oldBalance = self.balance #copies self.balance to oldBalance
                            self.balance = self.balance - amount #subracts amount from self.balance
                            remainingOverdraft = self.overdraftLimit - abs(self.balance)  #abs(self.balance) gives the positive version of self balance, which is then subracted from self.overdraftLimit
                            print("Withdrawal complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
                            print("Account %d remaining overdraft is: £%.2f"%(self.acct_id, remainingOverdraft))
                            self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance
                            break #breaks while loop
            else: #if self.overdraftLimit is 0
                while True:
                    print("Insuficcent funds avaliable")
                    print("Your balance is £%.2f"%self.balance)
                    print("Your overdraft limit is £%.2f"%self.overdraftLimit)
                    while True:
                        amount = input("Please select a different withdrawl amount: £")
                        try: #chekcs amount is an float. turns integers into floats
                            amount = float(amount)
                            break #breaks while loop
                        except: #if amount isnt an float an error message 
                            print("\nIncorrect input type entered. Please try again")
                    if self.balance > amount: #if self.balance is bigger than amount
                        oldBalance = self.balance #copies self.balance to oldBalance
                        self.balance = self.balance - amount #subracts amount from self.balance
                        print("Withdrawal complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
                        self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance
                        break
        else: #if self.balance is bigger than amount
            oldBalance = self.balance #copies self.balance to oldBalance
            self.balance = self.balance - amount #subracts amount from self.balance
            print("Withdrawal complete. The new balance for Account %d is £%.2f"%(self.acct_id, self.balance))
            self.updateBalance(oldBalance) #calls function updateBalance() with the parameter oldBlance

            
        
        
