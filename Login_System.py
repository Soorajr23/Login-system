# Importing Regular expressions re for email & password validation
import re

user_id = 0
pass_id = 0

# Function for Login
def login():

    global count
    count = 0
    username = input("\nEnter your Registered Username/Mail ID: ")
    password = input("\nEnter your Registered Password: ")

    f = open("Login_database")

    line = f.readlines()

    l = len(line)

# Loop to Check if the Username and password are registered or not/Forget Password Option
    for i in range(0,l,2):

        if (username in line[i]) and (password in line[i+1]):
            print("\nLog-in is Successful")
            count = 1
            break

        elif (username in line[i]) and (password not in line[i+1]):
            option = input("""\nThe entered password is wrong 
            
            Please Enter your Registered password again!
            
            Press '1' if you want to access forget password to change your password:
            
            """)

            if option == "1":

                new_password = input("\nPlease Enter your new password to be registered")

                password_condition = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&]).{5,16}$"

                if re.search(password_condition, new_password):
                    print("\nThe Entered Password is Valid")

                else:
                    print("\nThe Entered password is Not Valid")


                line[i+1] = new_password+"\n"

                f = open("Login_database", "w")
                f.writelines(line)
                count = 1
                print("\nThe password is successfully registered, Please Login Again!")

            else:
                print("\nPlease login again with your registered password correctly! ")
                return 0


    if count != 1:
        print(f"\nThe Entered Username: {username} is not registered")

    f.close()

# Registering the Username & Password after verification into the file

def registration():

    reg_user = input("\nEnter the Username to be registered: ")
    reg_password = input("\nEnter the Password to be registered: ")

    # Conditions to be taken note of:
    # start with a-z
    # has numbers 0-9
    # should have one "." & "_"
    # "@" once
    # "." should be followed by min 2 or 3 letters eg .com or .in

    f = open("Login_database")

    if reg_user in f.read():
        print("\nThe Username/Email is already Registered, Please choose Login to access")
        return 0

    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    password_condition = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&]).{5,16}$"

    # Checking the email using re.search() Function using if else loop

    if re.search(email_condition, reg_user):
        print("\nThe Entered Username/Mail-ID is Valid")
        user_id = 1
    else:
        print("\nThe Entered Username/Mail-ID is not Valid!")
        user_id = 0

    if re.search(password_condition, reg_password):
        print("\nThe Entered Password is Valid")
        pass_id = 1
    else:
        print("\nThe Entered Password is not Valid!")
        pass_id = 0

    # Loop to register the username & password
    if user_id == 1 and pass_id == 1:

       f = open("Login_database", "a")

       f.writelines(reg_user)
       f.write("\n")
       f.writelines(reg_password)
       f.write("\n")

       print("\nThe User ID & Password are Valid and are registered successfully")

    elif user_id == 0 and pass_id == 1:
        print(f"\nEntered {user_id} is mot a Valid User ID, please enter a Valid one")

    else:
        print("""\nThe Entered Password is not Valid. Please Enter a valid password!"

                NOTE:     
                Password should have:

                At-least One Upper Case
                At-least One Lower Case
                At-least One Number & Special Character

                Total Length should be more than 5 and Less than 16

                """)

# Creating a File to access the Email ID and password for login system:

file = input("\n Enter 1 to Create a new file else to access the created file: ")

#Creating a Login Database File

if file == "1":
    f = open("Login_database", "x")
else:
    f = open("Login_database", "r")

f = open("Login_database", "r")

# Getting Input for Login & Registration Choice
choice = input("""\nEnter the Choice
          1 - Login 
          2 - Registration\n""")

if choice == "1":
    log = login()
elif choice == "2":
    reg = registration()
else:
    print("\nEnter a Valid Choice")

f.close()

