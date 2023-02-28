#=====importing libraries===========
'''This is the section where you will import libraries'''
import math
from datetime import datetime
#====== End of importing ============

# we are openning text files for reading and writing:
user_tasks = open("tasks.txt","r",encoding="utf-8")

user_credentials = open("user.txt","r",encoding="utf-8")

# Reading tasks.txt file:
user_task_read = user_tasks.readlines()


# reading user.txt file
user_credential_read = user_credentials.readlines()
# current date assigned to variable today that we will use as a global variable
today = datetime.today().strftime('%Y-%m-%d') 

username_list = []

password_list = []

#====Login Section====#
print("In order to login you will need to enter your credentials:\n\n")



# Checking if username and password entered are matching one in our database(user.txt file)
# For each line in user.txt file separating username and password in two separate elements in the list so we can use them in our program

# Iteratinh through the usernames and passwords and appending them to 2 separate lists
for name in user_credential_read:
    user_split = name.strip("\n").split(", ")
    username_list.append(user_split[0])
    password_list.append(user_split[1])
    


# Counting number of tasks so we can display them later
for count, line in enumerate(user_task_read):
    pass
number_of_tasks = (count + 1)

# Using while loop to validate username and password if we can find them in username_list and password_list
while True:
    username = input("Please enter your username:\n\n")

    password = input("Please enter your password:\n\n")

    if username not in username_list or password not in password_list:
        print("You entered incorrect username and/or password")
    elif username in username_list and password in password_list:
        print("You logged in sucessfully")
        break

user_tasks.close()
user_credentials.close
   
#=====End of Login Section====#
# function that registers new user:
def reg_user():
            # Making sure only admin can register users:

            while True:
                # Requesting new username from the user
                new_username = input("Please enter your new username:\n\n")
                #checking if new username is already taken and if it is asking user to enter one that is not taken:
                if new_username in username_list:
                    print("This username has already been taken by another user,please try diferent username.")
                    continue
                # Requesting new password from the user
                new_password = input("Please enter your new password\n\n")
           
                #confirming the password
                confirm_password = input("Please confirm your password\n\n")

                # Checking if user confirmed password they entered correctly and writing it to our data file if True
                # We are doing error handling and outputing error message if new password doesn't match
                
                if new_password != confirm_password:
                    print("You entered the wrong password,Please confirm new user's details again")
                    continue
                else:
                    print("You sucessfully registered new user")
                    user_list = open("user.txt","a+",encoding="utf-8")
                    user_list.write(f"\n{new_username}, {new_password}")
                    user_list.close
                break

   
            
 #================== start of add_task function================#
# function that is adding new tasks
def add_task():
        
    # Asking user for the username of the person task is assigned to:
    while True:
        task_username = input("What is the username of the person that will be assigned with this task?\n\n")
        if not task_username in username_list:
            print("You entered invalid username, please try again:")
            continue
        else:
            break

    # Asking for task title
    task_title = input("Please enter the task title:\n\n")

    # Asking for description of the task
    task_description = input("Please describe the task:\n\n")

    #Assigning due date to the task
    while True:
        due_date = input("Please assign due date in the format YYYY-MM-DD :\n\n")
        # In case user doesn't enter date in the correct format we are handling an error
        try:
            converted_date = datetime.strptime(due_date,"%Y-%m-%d").date()
        except:
            print("Please enter the date in the correct format:\n")
            continue
        # Getting current date:
        current_date = today
        break
    # Including completion indicator for the new task which is NO by defaulkt when task is being created:
    completion_indicator = "No"

    # Writing new task to the tasks.txt file
    task_write = open("tasks.txt","a+",encoding="utf-8")
    task_write.write(f"\n{task_username}, {task_title}, {task_description}, {converted_date}, {current_date}, {completion_indicator}")
    task_write.close()
#================== end of add_task function================#
# function that lists all tasks in tasks.txt file:

 #================== start of view_all function================#
def view_all():
    # Reading a line from the tasks.txt file and separating lines into elements in the list
    for pos, line in enumerate(user_task_read,1):
        split_line = line.split(", ")
        
        
        # Printing formatted task to the console
        output  = f"------------[{pos}]---------------\n"
        output += f"Assigned to:\t\t{split_line[0]}\n"
        output += f"Task:\t\t\t{split_line[1]}\n"
        output += f"Description:\t\t{split_line[2]}\n"
        output += f"Assigned Date:\t\t{split_line[3]}\n"
        output += f"Due Date:\t\t{split_line[4]}\n"
        output += f"Is completed\t\t{split_line[5]}\n"
        output += "n"
        output += "------------------------------------"
        
        print(output)
    while True:
        # asking user which task they want to modify and sabtracting 1 because our program is starting from index 0
        task_choice = int(input("Please select number of the task you want to modify or enter -1 to go back to the main menu.\n\n")) 
        #If user entered -1 we are returning themm to the main menu:
        if task_choice == -1:
            return
        # error handling - checking if user chose correct task number and if not warning them and returning back to chose again
        elif task_choice <= 0 or task_choice > len(user_task_read):
            print("You have selected an invalid option, please try again")
            continue
        else:
             # getting a line in our tasks.txt file that we want to modify/task that we want to modify
             edit_data = user_task_read[task_choice - 1]
             break
       
       
    while True:
        split_lines = edit_data.strip("\n").split(", ")
        # checking if the task has been completed and if True we are getting user back to the main menu
        if split_lines[-1] == "Yes":
            print("This task has been completed and you are not allowed to modify it anymore")
            break
        #printing the options for the user to edit task or to mark it as complete:
        output = f"------------[SELECT AN OPTION]------------\n"
        output += "1 - Edit file\n"
        output += "2 - Mark as complete\n"
        output += "_______________________\n\n"
        # asking user to choose option 1 or 2
        choice = int(input(output))
        # error handling, making sure user chose option 1 or option 2 and if not returning them back to chose again
        if choice <= 0 or choice >= 3:
            print("You have selected invalid option,please try again")
            continue
        # If user chose to edit file we are giving them 3 options:
        #======================= Start of edit file==================#
        if choice == 1:
           
            split_lines = edit_data.strip("\n").split(", ")
            
           
            output = f"------------[SELECT AN OPTION]------------\n"
            output += "1 - change username\n"
            output += "2 - change due date\n"
            output += "3 - change username and due date\n"
            output += "____________________________________________\n\n"
            # asking user to choose one option
            user_choice = int(input(output))
            # making sure user will choose valid options and if not warning them and returning back to choose again
            if user_choice <= 0 or user_choice >= 4:
                print("You have selected invalid option,please try again")
                continue
            # If user chose to change username only:
            #================== Start of change usename================#
            if user_choice == 1:
                change_username = input("Please enter username of the person you wanto to reassign this task to\n")
                # checking if username is assigned to one of the registered users and if not asking them to enter it again:
                if change_username not in username_list:
                    print("Please enter valid username")
                    continue
                # if username is in the username list:
                else:
                    #changing username with user input change_username
                    split_lines[0] = change_username
                    #joining a task together to a single line string
                    new_data = ", ".join(split_lines)
                    # swopping original line with new line that is including changed username
                    user_task_read[task_choice -1] = new_data
                    #TODO - need to make function that will automate this task
                    # writing the new line to the tasks.txt file
                    task_write = open("tasks.txt","w",encoding="utf-8")
                    for line in user_task_read:
                        task_write.write(line)
                break
            #===================== end of change username===================#

            #================== start of change due date================#
            # if user chose to change a date only:
            elif user_choice == 2:
                # new date input
                change_date = input("Please change the due date for this task\n")
                # changing original date
                split_lines[3] = change_date
                #joining task in the single line
                new_data = ", ".join(split_lines)
                # changing orignal line with the new line that contains new due date
                user_task_read[task_choice -1] = new_data
                #TODO - need to make function that will automate this task
                # writing new line to the tasks.txt
                task_write = open("tasks.txt","w",encoding="utf-8")
                for line in user_task_read:
                    task_write.write(line)
                task_write.close()
                break
             #================== end of change due date================#

             #================== start of change due date and username================#
            # if user chose to change both username of the person whom the task has been assigned and due date
            elif user_choice == 3:
                # new username
                change_username = input("Please enter username of the person you wanto to reassign this task to\n")
                #new due date
                change_date = input("Please change the due date for this task\n")
                # changing username and date
                split_lines[0] = change_username
                split_lines[3] = change_date
                # joining new line
                new_data = ", ".join(split_lines)
                #TODO - need to make function that will automate this task
                # assigning new line to our tasks.txt file
                user_task_read[task_choice -1] = new_data
                # writing new text line that contains new username and due date
                task_write = open("tasks.txt","w",encoding="utf-8")
                for line in user_task_read:
                    task_write.write(line)
                task_write.close()
            break
            #================== end of change due date and username================#

        #================== end of edit file option================#
            
            
        #================== start of mark as complete================#
        # marking task as complete
        elif choice == 2:
            #spliting text line for the task we chose
            split_data = edit_data.strip("\n").split(", ") 
            #finding last element in the list and changing it to "yes"
            split_data[-1] = "Yes\n"
            #joining the string again:
            new_data = ", ".join(split_data)
            #assigning changed text line to the corresponding line in our tasks.txt file
            user_task_read[task_choice -1] = new_data
            print(new_data)
        # writing new line to tasks.txt
        task_write = open("tasks.txt","w",encoding="utf-8")
        for line in user_task_read:
            task_write.write(line)
        task_write.close()
        break
        #================== end of mark as complete================#

#================== end of view_all function================#

#================== start of view_mine function================#
# function that lists tasks for the user that is logged in:
def view_mine():
        # Reading a line from the tasks.txt file and separating lines into elements in the list
    for pos, line in enumerate(user_task_read,1):
        split_line = line.split(", ")
        # Checking if username of the person logged in is the same as the username we read from the file 
        if username == split_line[0]:
            # Printing formatted task to the console
            output  = f"------------[{pos}]---------------\n"
            output += f"Assigned to:\t\t{split_line[0]}\n"
            output += f"Task:\t\t\t{split_line[1]}\n"
            output += f"Description:\t\t{split_line[2]}\n"
            output += f"Assigned Date:\t\t{split_line[3]}\n"
            output += f"Due Date:\t\t{split_line[4]}\n"
            output += f"Is completed\t\t{split_line[5]}\n"
            output += "\n"
            output += "------------------------------------"

            print(output)
#================== end of view_mine function================#

#================== start of gen_files function================#

def gen_files():
    #openning files for reading
    generate_task = open("task_overview.txt", "w+")
    generate_user = open("user_overview.txt","w+")
    #completed tasks counter
    completed_tasks = 0
    # uncompleted tasks counter
    uncompleted_tasks = 0
    # uncmpleted and overdue
    uncompleted_overdue = 0
    # assigned to user
    assigned_to_user = 0
    # assigned to user and completed
    assigned_to_user_completed = 0
    # assigned to user and uncompleted
    assigned_to_user_uncompleted = 0
    # assigned to user uncompleted and overdue
    assigned_uncompleted_overdue = 0

   
    # iterating through the tasks.txt file
    for  line in user_task_read:
        split_line = line.strip("\n").split(", ")


        # Checking if task is complete and adding 1 to completed_tasks if True
        if split_line[-1] == "Yes":
            completed_tasks = completed_tasks + 1

        # checking if task is not complete and adding 1 to uncompleted_tasks if True
        if split_line[-1] == "No":
            uncompleted_tasks += 1

        # checking if task is uncompleted and overdue and adding 1 to uncompleted_overdue if true
        if split_line[-1] == "No" and split_line[3] < today:
            uncompleted_overdue = uncompleted_overdue + 1

        # checking if task is assigned to the user that is currently logged in and adding 1 to assigned_to_user if True
        if username == split_line[0]:
            assigned_to_user = assigned_to_user + 1

        # checking if task is assigned to the logged in user and completed
        if username == split_line[0] and split_line[-1] == "Yes":
            assigned_to_user_completed = assigned_to_user_completed + 1

        # checking if task is assigned to the logged in user, and uncompleted
        if username == split_line[0] and split_line[-1] == "No":
            assigned_to_user_uncompleted = assigned_to_user_uncompleted + 1

        # checking if task is assigned to the logged in user,uncompleted and overdue 
        if username == split_line[0] and split_line[-1] == "No" and split_line[3] < today:
            assigned_uncompleted_overdue = assigned_uncompleted_overdue + 1
        
    # printing task report in user-friendly manner
    output  = f"------------[TASK REPORT]-------------------------------------------------------\n"
    output += f"The total number of tasks:\t\t\t\t\t{number_of_tasks}\n"
    output += f"The total number of completed tasks:\t\t{completed_tasks}\n"
    output += f"The total number of uncompleted tasks:\t\t{uncompleted_tasks}\n"
    output += f"The total number of tasks that haven't been completed and are overdue:\t{uncompleted_overdue}\n"
    output += f"The percentage of tasks that are incomplete:\t{(uncompleted_tasks/number_of_tasks).__round__(2)*100}%\n"
    output += f"The percentage of tasks that are overdue\t\t{(uncompleted_overdue/number_of_tasks).__round__(2)* 100}%\n"
    output += "\n"
    output += "---------------------------------------------------------------------------------"
    generate_task.write(output)
    # printing user-report in user-friendly manner
    output_task = f"------------[USER REPORT]-----------------------------------------------------------------------\n"
    output_task += f"The total number of registered users:\t\t{len(username_list)}\n"
    output_task += f"The total number of tasks:\t\t{number_of_tasks}\n"
    output_task += f"The total number of tasks assigned to {username} is:\t\t{assigned_to_user}\n"
    output_task += f"The percentage of the total number of tasks assigned to {username}:\t\t\t{(assigned_to_user/number_of_tasks).__round__(2)*100}%\n"
    output_task += f"The percentage of tasks assigned to {username} that have been completed:\t\t{(assigned_to_user_completed/assigned_to_user).__round__(2)*100}%\n"
    output_task += f"The percentage of tasks assigned to {username} that haven't been completed \t{(assigned_to_user_uncompleted/assigned_to_user).__round__(2)*100}%\n"
    output_task += f"The percentage of tasks assigned to {username} that haven't been completed and are overdue \t{(assigned_uncompleted_overdue).__round__(2)}%\n"
    output_task += "\n"
    output_task += "--------------------------------------------------------------------------------------------------"
    generate_user.write(output_task)
    # closing task_overview.txt and user_overview.txt files
    generate_user.close()
    generate_task.close()

def display_data():
# calling function to generate task.overview.txt and user_overview.txt if they don't exist 
        gen_files()
        # openning files for reading 
        generate_task = open("task_overview.txt", "r")
        generate_user = open("user_overview.txt","r")
    
        # printing content of the task_overview.txt
        for line in generate_task:
            print(line)
        print("\n\n\n\n")
        # printing content of the user_overview.txt
        for line in generate_user:
            print(line)
        # closing task.overview.txt and user_overview.txt
        generate_task.close()
        generate_user.close()

    #================== end of gen_files function================#

while True:
     #presenting the menu to the user and once we are logged in
    # making sure that the user input is coneverted to lower case
    menu = input('''Select one of the following Options below:

        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - Display statistics
        e - Exit
        : \n''').lower()
    #======= Option r =======#
    # If user chose r calling function that registers new user
    if menu == 'r' and username == "admin":
        reg_user()
        
    #========= End of option r ======#

    #========= Option a ==========#
    # If user chose a calling function that adds new task
    elif menu == 'a':
        add_task()
        

    #========== End of option a ===========#

    #========== Option va =============#
    # if user chose va calling a funtion that prints all tasks 
    elif menu == 'va':
        view_all()
           
    #=========== End of option va ========#

    #=========== Option vm =============#
    # if user chose option vm printing tasks that are assigned to the specific user
    elif menu == 'vm':
        view_mine()
        
    #================== End of option vm=======#

    #================== option gr =============#
    # if user choice is gr we generate reports in taskoverview.txt and user overview.txt files and present them to the user
    elif menu == "gr":
        gen_files()
        

    #================== end of option gr =============#

    #==================Option ds ===============#
    # if user choice is ds we will display reports that are within task.overview.txt and user_overview.txt
    elif menu == "ds" and username == "admin":
        display_data()
       
    #================= End of option ds =========#

    #================= Exit menu ================#
    # if user chose option e we are exiting a program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    #================= End of exit menu =========#
    else:
        print("You have made a wrong choice,or you need to be administrator in order to use this option.Please Try again")
    




