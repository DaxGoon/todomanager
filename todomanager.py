"""
main logic, file/directory reading and writing, cli options etc.
"""


# standard imports
import os
import glob
from projects import Project, ProjectList
from todos import ToDo, ToDoList


# Menu
def start():
    """
    starts the ToDo manager menu.
    :return: user_command (str)
    """
    print("Welcome to Todo Manager.", end="")
    print("""
    _______________________________
    C O M M A N D S
    -------------------------------
    v View all todos.
    d Delete a todo.
    a Add a project directory.
    r Remove a project directory.
    -------------------------------
    """, end="")
    print("What would you like to do?")
    # take user input
    user_command = ""
    while not user_command:
        user_command = input(" Enter a valid command: ")
        if user_command.isalpha() and user_command.lower() in ["v", "d", "a", "r"]:
            user_command = user_command.lower()
            return user_command
        else:
            user_command = ""
            continue


# Process the command returned from the menu
def operation(user_command):
    """
    perform operation based on user_command
    :param user_command: users' input (user_command) returned by start() function
    :return: None
    """
    # view todos
    if user_command == "v":
        if default_todo_list.todos:
            default_todo_list.show_todos()
        else:
            print("Sorry, no todos found!")
        print("Press ENTER to continue")  # continue the loop
        input()
        user_command = start()
        operation(user_command)
    # delete todos
    elif user_command == "d":
        if default_todo_list.todos:
            for idx, todo in enumerate(default_todo_list.todos):
                print(idx + 1, ". ", todo.task)
            num = int(input("Which todo you want to delete? enter number: "))
            default_todo_list.remove_todo(num)
            print("Todo deleted")
        else:
            print("Sorry, no todos found!")
        print("Press ENTER to continue")  # continue the loop
        input()
        user_command = start()
        operation(user_command)
    # add a project
    elif user_command == "a":
        project = input("Give a name to your project: ")
        default_project_list.add_project(project)
        print("Project added")
        print("Press ENTER to continue")  # continue the loop
        input()
        user_command = start()
        operation(user_command)
    # remove a project
    elif user_command == "r":
        if default_project_list.projects:
            for idx, project in enumerate(default_project_list.projects):
                print(idx + 1, ". ", project)
            project_num_to_delete = int(input("Which project you wanna delete? Enter a number: ")) - 1
            default_project_list.remove_project(project_num_to_delete)
            print("Project deleted")
        else:
            print("Sorry, no projects found")
        print("Press ENTER to continue")  # continue the loop
        input()
        user_command = start()
        operation(user_command)


# ask for a project directory
def acquire_dir():
    """
    Asks user to input the project directory name
    :return: directory_name
    """
    while True:
        directory_name = input("Enter the Project directory address to scan for Todos."
                               "\n(Hint: /Users/username/ProjectDirectory)\nPress ENTER for current directory: ")
        directory_name = os.path.join(os.getcwd(), directory_name)
        if os.path.isdir(directory_name):
            return directory_name
        else:
            print(directory_name, " does not exist. Provide a valid directory name!")


# read directory and return a list of files
def files_in_dir(directory_name, file_spec="*.py"):
    """
    scan the directory and return a list of files.
    :param directory_name: valid directory name retrived from acquire_dir() function
    :param file_spec: type of files to include (str of extensions)
    :return: list of files
    """
    return glob.glob(os.path.join(directory_name, file_spec))


# generator function for finding todos
def file_match(files_list):
    """
    read files in the list for "# todo:" tag
    :param files_list: list containing file names with valid address
    :return: list_of_extracted_todos
    """
    list_of_extracted_todos = []
    for ind_file in files_list:
        with open(ind_file, "r") as read_content:
            for todo_line in read_content.read().splitlines():
                if "# todo:" in todo_line:
                    list_of_extracted_todos.append(todo_line)
    return list_of_extracted_todos


def main():
    user_command = start()
    operation(user_command)


if __name__ == "__main__":
    # create a ProjectList Obj
    default_project_list = ProjectList()

    # create a Project Obj
    default_project = Project()

    # create a ToDoList Obj
    default_todo_list = ToDoList()

    # create a ToDo Obj
    default_todo = ToDo()

    # get the project directory
    directory_name = acquire_dir()

    # create a list of files by scanning the directory (if we jusy want python files, we'd replace *.* with *.py
    files_list = files_in_dir(directory_name, file_spec="*.*")

    # create a list of extracted todos
    todo_repo = file_match(files_list)

    # create ToDo objs from todo_repo
    todo_obj_list = [ToDo(task) for task in todo_repo]

    # add the newly created ToDo obj in ToDoList obj
    for ind_todo_obj in todo_obj_list:
        default_todo_list.add_todo(ind_todo_obj)

    # execute the main function
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
