from main import login, roles
print("\nWelcome! to Administrator panel")
print("")
#---------------------------------------------------------------------------------------------------------------------------

def add_manager():
    username, password = login()
    with open("manager.txt", "a") as manag_a: #open administrator.txt and add user to it.
        cos_dict = {"username": username, "password": password}
        for key, value in cos_dict.items():
            manag_a.write(f"\n{key}:{value}")
        print("\nUser successfully added!\n\n")
    what_you_want()

def edit_manager():
    username, password = login()
    with open("manager.txt", "r") as manag_e_r:
        lines = manag_e_r.readlines()
    updated_lines = []
    found = False
    skip_next = False
    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        if lines[i].strip() == f"username:{username}" and lines[i + 1].strip() == f"password:{password}":
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            updated_lines.append(f"username:{new_username}\n")
            updated_lines.append(f"password:{new_password}\n")
            found = True
            skip_next = True # Skip password Line
            continue
        else:
            updated_lines.append(lines[i])  
    if found:
        with open("manager.txt", "w") as manag_d_w:
            manag_d_w.writelines(updated_lines) # Rewrite the whole text and remove matched username and password
            print("\nManager updated successfully.")
        what_you_want()
    else:
        print("\nNo matching manager account found.\n")
        what_you_want()
    
def delete_manager():
    username, password = login()
    with open("manager.txt", "r") as manag_d_r:
        lines = manag_d_r.readlines()
    update_lines = []
    found = False
    skip_next = False
    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        if lines[i].strip() == f"username:{username}" and lines[i + 1].strip() == f"password:{password}":
            found = True
            skip_next = True # Skip password Line
            continue
        update_lines.append(lines[i]) 
    if found:
        with open("manager.txt", "w") as manag_d_w:
            manag_d_w.writelines(update_lines) # Rewrite the whole text and remove matched username and password
            print("\nChef account deleted successfully.") 
        what_you_want()
    else:
        print("\nNo matching manager account found.")
        what_you_want()


def manage_manager():
    n = int(input("\nEnter '1' for add, '2' for edit, '3' for delete: "))
    if n==1:
        add_manager()
    elif n==2:
        edit_manager()
    elif n==3:
        delete_manager()
    else:
        print("Please! Input number between 1-3.")
        manage_manager()

#---------------------------------------------------------------------------------------------------------------------------

def add_chef():
    username, password = login()
    with open("chef.txt", "a") as manag_a: #open chef.txt and add user to it.
        cos_dict = {"username": username, "password": password}
        for key, value in cos_dict.items():
            manag_a.write(f"\n{key}:{value}")
        print("\nUser successfully added!\n\n")
    what_you_want()

def edit_chef():
    username, password = login()
    with open("Chef.txt", "r") as chef_e_r:
        lines = chef_e_r.readlines()
    updated_lines = []
    found = False
    skip_next = False
    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        if lines[i].strip() == f"username:{username}" and lines[i + 1].strip() == f"password:{password}":
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            updated_lines.append(f"username:{new_username}\n")
            updated_lines.append(f"password:{new_password}\n")
            found = True
            skip_next = True # Skip password Line
            continue
        else:
            updated_lines.append(lines[i])  
    if found:
        with open("Chef.txt", "w") as chef_d_w:
            chef_d_w.writelines(updated_lines) # Rewrite the whole text and remove matched username and password
            print("\nChef updated successfully.")
        what_you_want()
    else:
        print("\nNo matching Chef account found.\n")
        what_you_want()
    
def delete_chef():
    username, password = login()
    with open("chef.txt", "r") as chef_d_r:
        lines = chef_d_r.readlines()
    update_lines = []
    found = False
    skip_next = False
    for i in range(len(lines)):
        if skip_next:
            skip_next = False
            continue
        if lines[i].strip() == f"username:{username}" and lines[i + 1].strip() == f"password:{password}":
            found = True
            skip_next = True # Skip password Line
            continue
        update_lines.append(lines[i]) 
    if found:
        with open("chef.txt", "w") as chef_d_w:
            chef_d_w.writelines(update_lines) # Rewrite the whole text and remove matched username and password
            print("\nChef account deleted successfully.") 
        what_you_want()
    else:
        print("\nNo matching chef account found.")
        what_you_want()

def manage_chef():
    n = int(input("\nEnter '1' for add, '2' for edit, '3' for delete: "))
    if n==1:
        add_chef()
    elif n==2:
        edit_chef()
    elif n==3:
        delete_chef()
    else:
        print("Please! Input number between 1-3.")
        manage_chef()

#---------------------------------------------------------------------------------------------------------------------------

def view_sales_report():
    # with open("sales.txt", "r") as sales:
    #     asked_month = int(input("Enter the month: "))
    #     content = sales.read()
    #     if asked_month in content:
    #         pass
    #     else:
    #         print("Entered date do not have any report.")
    print("Successfully came to view sales report function.")
    what_you_want()

def view_feedback():
    # with open("feedback.txt", "r") as feedback:
    #     content = feedback.read()
    #     if user in content:
    #         pass
    #     else:
    #         print("User not found")
    print("Successfully came to view feedback function.")
    what_you_want()

def update_own_profile():
    username, password = login()
    with open("Administrator.txt", "w") as admin:
        adm_dict = {"username": username, "password": password}
        for key, value in adm_dict.items():
           admin.write(f"\n{key}:{value}")
        print("\nAdministrator User Successfully Updated!")
    
def what_you_want():
    print("\nWhat You Want to Do\n")
    to_do = int(input("Enter '1' to manage staff,\nEnter '2' to View sales report based on month,\nEnter '3' to View feedback sent by customers,\nEnter '4' to Update own profile,\nEnter '5' to exit from code.\n\n"))
    if to_do == 1:
        staff_to_do = int(input("\nEnter '1' to manage Manager, Enter '2' to manage Chef: "))
        while True:
            if staff_to_do == 1:
                manage_manager()
                break
            elif staff_to_do == 2:
                manage_chef()
                break
            else:
                print("\nPlease! enter number 1-2.")
                staff_to_do = int(input("\nEnter '1' to manage Manager,\tEnter '2' to manage Chef"))
    elif to_do == 2:
        view_sales_report()
    elif to_do == 3:
        view_feedback()
    elif to_do == 4:
        update_own_profile()
    elif to_do == 5:
        exit("Successful to exit")
    else:
        print("Please! enter number 1-4:")
        what_you_want()

what_you_want()