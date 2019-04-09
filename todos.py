"""
todo class and related methods.
"""


# 1. ToDoList class
class ToDoList:
    """
    blueprint for list of todo objects.
    """
    def __init__(self):
        self.todos = []

    def add_todo(self, todoobj):
        """
        add a todo as a dictionary.
        :param todoobj: todo object.
        :return: None
        """
        self.todos.append(todoobj)

    def remove_todo(self, num):
        """
        remove a todo's index on ToDoList.
        :param num: todo objects' list index number from ToDoList
        :return: None
        """
        self.todos.remove(self.todos[num-1])

    def show_todos(self):
        """
        shows the available todos in the list.
        :return: value from the todo list.
        """
        for num, todo_items in enumerate(self.todos):
            #print(num+1, ". ", todo_items["task"], "\nDue: ", todo_items["due"], "\nImportance: ", todo_items["importance"], "\n")
            print(num+1, ". ", todo_items.task, "\nDue: ", todo_items.due, "\nImportance: ", todo_items.importance, "\n")


# 2. ToDo class
class ToDo:
    """
    single todo object blueprint.
    """
    def __init__(self):
        self.task = ""
        self.importance = ""
        self.due = ""

    # print the various attributes of the ToDo object
    def show_task(self):
        print(self.__dict__["task"])

    def show_importance(self):
        print(self.__dict__["importance"])

    def show_due(self):
        print(self.__dict__["due"])

    def add_task(self, todo_item):
        self.task = todo_item  # ! THIS IS POTENTIALLY OVERWRITING, WE HAVE TO FIND .append like method


# test it out - ToDoList test successful
# test_todopr = ToDoList()
# test_todopr.add_todo(
#     {
#         "task": "do something",
#         "importance": "1",
#         "due": "tomorrow"
#     }
# )
# test_todopr.show_todos()
# test_todopr.remove_todo(1)
# test_todopr.show_todos()

# a_todo = ToDo()
# a_todo.show_importance()
# a_todo.importance = 4
# a_todo.show_importance()
