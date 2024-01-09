
class Admin:
    #initialize attributes of Admin
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
        
    #get functions
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
    
    def get_address(self):
        return self.address
    
    def get_username(self):
        return self.user_name
        
    def get_password(self):
        return self.password
    
    def has_full_admin_right(self):
        return self.full_admin_rights
    
    def display_address(self):
        num = self.address[0] #sets num to the first value in the list self.address
        street = self.address[1] #sets street to the second value in the list self.address
        city = self.address[2] #sets city to the third value in the list self.address
        postcode = self.address[3] #sets postcode to the fourth value in the list self.address
        num = '{}'.format(num) #turns num into a string
        a = num + " " + street + ", " + city + ", " + postcode #adds spaces and commas between elements in self.address
        return a
    
    #update functions
    def update_first_name(self, fname):
        #updates firstname and and Admins.txt
        oldName = self.fname #copies self.fname to oldName
        self.fname = fname #changes value of self.fname to fname
        adminfile = open("Admins.txt","r+") #opens Admins.txt in read and write mode
        file = adminfile.read() #copies contents of Admins.txt to file
        oldName = '{}'.format(oldName) #formats oldName so its a string
        y = '{}'.format(self.fname) #formats self.fname so its a string and stores it in variable y
        file = file.replace(oldName, y) #replaces any instances of oldName in Admins.txt with y
        file = '{}'.format(file) #formates file so its a string
        adminfile.truncate(0) #deletes contents of Admins.txt
        adminfile.write(file) #writes contents of file to Admins.txt
        adminfile.close() #closes Admins.txt
    
    def update_last_name(self, lname):
        #updates lastname and Admins.txt
        oldName = self.lname #copies self.lname to oldName
        self.lname = lname #changes value of self.lname to lname
        adminfile = open("Admins.txt","r+") #opens Admins.txt in read and write mode
        file = adminfile.read() #copies contents of Admins.txt to file
        oldName = '{}'.format(oldName) #formats oldName so its a string
        y = '{}'.format(self.lname) #formats self.lname so its a string and stores it in variable y
        file = file.replace(oldName, y) #replaces any instances of oldName in Admins.txt with y
        file = '{}'.format(file) #formates file so its a string
        adminfile.truncate(0) #deletes contents of Admins.txt
        adminfile.write(file) #writes contents of file to Admins.txt
        adminfile.close() #closes Admins.txt
                
        
    def update_address(self, houseNo, streetName, townCity, postcode):
        #updates address and Admins.txt
        oldAddr = self.address #copies self.address to oldAddr
        addr = [houseNo, streetName, townCity, postcode] #sets values of list addr 
        self.address = addr #changes value of self.address to addr
        print("\n Address updated")
        adminfile = open("Admins.txt","r+") #opens Admins.txt in read and write mode
        file = adminfile.read() #copies contents of Admins.txt to file
        oldAddr = '{}'.format(oldAddr) #formats oldAddr so its a string
        y = '{}'.format(self.address) #formats self.address so its a string and stores it in variable y
        file = file.replace(oldAddr, y) #replaces any instances of oldAddr in Admins.txt with y
        file = '{}'.format(file) #formates file so its a string
        adminfile.truncate(0) #deletes contents of Admins.txt
        adminfile.write(file) #writes contents of file to Admins.txt
        adminfile.close() #closes Admins.txt
    
    def set_username(self, uname):
        #updates username and Admins.txt
        oldUser = self.user_name #copies self.user_name to oldUser
        self.user_name = uname #changes value of self.user_name to uname
        print("\n Username updated")
        adminfile = open("Admins.txt","r+") #opens Admins.txt in read and write mode
        file = adminfile.read() #copies contents of Admins.txt to file
        oldUser = '{}'.format(oldUser) #formats oldUser so its a string
        y = '{}'.format(self.user_name) #formats self.user_name so its a string and stores it in variable y
        file = file.replace(oldUser, y)  #replaces any instances of oldUser in Admins.txt with y
        file = '{}'.format(file) #formates file so its a string
        adminfile.truncate(0) #deletes contents of Admins.txt
        adminfile.write(file) #writes contents of file to Admins.txt
        adminfile.close() #closes Admins.txt
        
    
    def update_password(self, password):
        #updates password and Admins.txt
        oldPassword = self.password #copies self.password to oldPassword
        self.password = password #changes value of self.password to password
        print("\n Password updated")
        adminfile = open("Admins.txt","r+") #opens Admins.txt in read and write mode
        file = adminfile.read() #copies contents of Admins.txt to file
        oldPassword = '{}'.format(oldPassword) #formats oldPassword so its a string
        y = '{}'.format(self.password) #formats self.password so its a string and stores it in variable y
        file = file.replace(oldPassword, y)  #replaces any instances of oldPassword in Admins.txt with y
        file = '{}'.format(file) #formates file so its a string
        adminfile.truncate(0) #deletes contents of Admins.txt
        adminfile.write(file) #writes contents of file to Admins.txt
        adminfile.close() #closes Admins.txt
    
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right
        
    #account functions
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

    #print functions
    def print_details(self):
        print("""\n Name: %s %s
 Address: %s
 Username: %s
 Password: %s
 Full rights: %s """%(self.fname, self.lname, self.display_address(), self.user_name, self.password, self.full_admin_rights))
    
    #string representation of object
    def __str__(self):
        return f'{self.fname} {self.lname}, ({self.address[0]} {self.address[1]}, {self.address[2]}, {self.address[3]}), {self.user_name}, {self.password}, {self.full_admin_rights}'

    #admin functions
    def admin_account_menu(self):
        #print admin account menu
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your admin options are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Update name")
        print("2) Update address")
        print("3) Update Username")
        print("4) Update password")
        print("5) Show Admin details")
        print("6) Back")
        print(" ")
        option = input("Choose your option: ")
        return option
    
    def run_admin_options(self):
        loop = 1
        while loop == 1:
            choice = self.admin_account_menu()
            try: #checks choice is an integer
                choice = int(choice)
            except: #if choice isnt an integer an error message is printed
                print("\nIncorrect input type entered. Please try again")
            if choice == 1: 
                #Update name
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
            elif choice == 3:
                #update username
                while True:
                    uname = input("Please enter the new username: ")
                    try: #check uname is a string
                        uname = str(uname)
                        self.set_username(uname) #calls functon set_username() with parameter uname
                        break
                    except: #if uname isnt a string an error message is printed
                        print("\nIncorrect input type entered. Please try again")
            elif choice == 4:
                y = 3 #y is set to 3. used as a counter
                while y >= 0: #while y is bigger than or equal to 0
                    current_pass = input("Please enter your current password: ")
                    found_pass = self.get_password() #calls function get_password()
                    if found_pass == current_pass: #if found_pass is the same as current_pass
                        new_pass = input("Please enter your new password: ")
                        new_pass = str(new_pass) #makes new_pass a string
                        self.update_password(new_pass) #ccalls functiom update_password() with parameter new_pass
                        break #break while loop
                    else:
                        y -= 1 #-1 from the value of y
                        print("What you entered does not match your current password: ")
                        print("You have %d attempts left"%y)
            elif choice == 5: #if choice is 5
                #print admin details
                self.print_details() #calls function print_details()
            elif choice == 6:
                #back
                break #breaks loop
                
