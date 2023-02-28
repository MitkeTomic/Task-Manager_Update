# Task-Manager_Update
This is an update of the Task-Manager Program that is using functions and lists to make this program more readable, modular and efficient

This is a Python program that presents a menu to the user with several options. The program starts an infinite loop using the "while True" statement. The user can select from the following options:

  Register a user ('r'): If the user is an administrator, they can register a new user by calling the "reg_user()" function.
  
  Add a task ('a'): The user can add a new task by calling the "add_task()" function.
  
  View all tasks ('va'): The user can view all tasks by calling the "view_all()" function.
  
  View my tasks ('vm'): The user can view all the tasks assigned to them by calling the "view_mine()" function.
  
  Generate reports ('gr'): If the user is an administrator, they can generate reports in taskoverview.txt and user_overview.txt files by calling the         "gen_files()" function.
  
  Display statistics ('ds'): If the user is an administrator, they can display reports within taskoverview.txt and user_overview.txt files by calling the     "display_data()" function.
  
  Exit the program ('e'): The user can exit the program by typing 'e' at the menu.
  
  If the user enters an invalid option or is not authorized to use a particular option, the program displays an error message and prompts the user to try     again.

This program can be used as a basic task management system that allows users to add tasks and administrators to generate and display reports.
