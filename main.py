def login(): #Function to take username and password ans input form user.
    username = input("Enter your username or email: ")
    password = input("Enter your password: ")
    return username, password

context = {} # to access or run all code and function in other python file

def checker(txt_username_value , txt_password_value, username, password, role_no): #Function which take argument from function which store username, password, txt_username_value , txt_password_value of specific role and check their username and password.
    for i in range (2,-1,-1):
        if username == txt_username_value and password == txt_password_value:
            if role_no == 1:
                exec(open("administrator.py").read(), context) #Run administrator.py
                break
            elif role_no == 2:
                # exec(open("manager.py").read())#Run manager.py
                print("Successfully Login! to manager.py")
                break
            elif role_no == 3:
                # exec(open("chef.py").read())#Run chef.py
                print("Successfully Login! to chef.py")
                break
            elif role_no == 4:
                # exec(open("coustomer.py").read())#Run customer.py
                print("Successfully Login! to customer.py")
                break
        else:
            if i > 0:
                print("\nInvalid Username or password. Please enter username and password again!")
                print(f"You have {i} attempts remaining\n")
                username, password = login()
            else:
                print("\nLimit exceed. Login Unsuccessful!\n")
                exit()

def admin_checker(role_no): #Function which read administator txt file and retrive username and password and send them to checker function
    username, password = login() 
    with open("Administrator.txt", "r") as admin:
        lines = admin.readlines()
        for i in range(len(lines)):
            if lines[i].strip().startswith(f"username:{username}"):
                txt_username_key, txt_username_value = lines[i].strip().split(":")
                txt_password_key, txt_password_value = lines[i+1].strip().split(":")
                checker(txt_username_value, txt_password_value, username, password, role_no)
        checker("", "", username, password, role_no)

def manager_checker(role_no): #Function which read manager txt file and retrive username and password and send them to checker function
    username, password = login()
    with open("manager.txt", "r") as manage:
        lines = manage.readlines()
        for i in range(len(lines)):
            if lines[i].strip().startswith(f"username:{username}"):
                txt_username_key, txt_username_value = lines[i].strip().split(":")
                txt_password_key, txt_password_value = lines[i+1].strip().split(":")
                checker(txt_username_value, txt_password_value, username, password, role_no)
        checker("", "", username, password, role_no)

def chef_checker(role_no):#Function which read chef txt file and retrive username and password and send them to checker function
    username, password = login()
    with open("chef.txt", "r") as chef:
        lines = chef.readlines()
        for i in range(len(lines)):
            if lines[i].strip().startswith(f"username:{username}"):
                txt_username_key, txt_username_value = lines[i].strip().split(":")
                txt_password_key, txt_password_value = lines[i+1].strip().split(":")
                checker(txt_username_value, txt_password_value, username, password, role_no)
        checker("", "", username, password, role_no)

def customer_checker(role_no): #Function which read customer txt file and retrive username and password and send them to checker function
    username, password = login()
    with open("customer.txt", "r") as custm:
        lines = custm.readlines()
        for i in range(len(lines)):
            if lines[i].strip().startswith(f"username:{username}"):
                txt_username_key, txt_username_value = lines[i].strip().split(":")
                txt_password_key, txt_password_value = lines[i+1].strip().split(":")
                checker(txt_username_value, txt_password_value, username, password, role_no)
        checker("", "", username, password, role_no)

def customer_register(role_no):
    username, password = login()
    with open("customer.txt", "r") as costm_r: #Opening customer.txt file to read all content and verify if usename and passwor is in content or not.
        content = costm_r.read()
        if username  in content and password in content:
            print("User already exit!")
            customer_register()
        else:
            with open("customer.txt", "a") as costm_w: #If user is not registered then add them to customer.txt
                cos_dict = {"username": username, "password": password}
                for key, value in cos_dict.items():
                    costm_w.write(f"\n{key}:{value}")

                print("User successfully registered!")
            login_navigation = input("\nType login to enter login page: ")
            print("")
            if login_navigation.lower() == "login": #ask user to goto login page or not
                customer_checker(role_no)
            else:
                print("You have entered something else, So.... Good Bye.\n")
                exit()

def roles(): #Function which ask user, their role of getting access.
    role_no = int(input('''Enter number according to your role:
                     1.Administrator
                     2.Manager
                     3.Chef
                     4.customer\n''')) #Taking 1 for administator, 2 for manager, 3 for chef, 4 for customer.
    if role_no == 1:
        admin_checker(role_no)
    elif role_no == 2:
        manager_checker(role_no)
    elif role_no == 3:
        chef_checker(role_no)
    elif role_no == 4:
        cos_login = int(input("Enter 1 for login and 2 for register:"))
        while True: #to let ask user value again and again if they do not enter value 1-2
            if cos_login == 1:
                customer_checker(role_no)
                break
            elif cos_login == 2:
                customer_register(role_no)
                break
            else:
                print("Invalid Number!")
                cos_login = int(input("Enter 1 for login and 2 for register:"))
    else:
        print("Invalid Number!")
        roles()

if __name__ == "__main__": #Doesnot repate twice if i run main.py directly
    roles()