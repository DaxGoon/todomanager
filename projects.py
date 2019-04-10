"""
project class and related methods.
"""


# 1. ProjectList class
class ProjectList:
    """
    collection of project objects.
    """
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """
        adds a project to a projects list
        :param project: project to be added
        :return: None
        """
        self.projects.append(project)

    def remove_project(self, num):
        """
        removes a project from the projects list
        :param num: project number as shown by show_projects() to remove the related project
        :return: None
        """
        self.projects.remove(self.projects[num-1])

    def show_projects(self):
        """
        show the available projects
        :return: None
        """
        for num, project in enumerate(self.projects):
            print(num+1, ". ", project)


# 2. Project class
class Project:
    """
    blueprint for Project objects.
    """
    def __init__(self):
        self.files = []

    def add_file(self, file):
        """
        adds a file to a project
        :param file: filename
        :return: None
        """
        self.files.append(file)

    def remove_file(self, file):
        """
        removes a file from projects
        :param file: filename
        :return:None
        """
        self.files.remove(file)

    def show_project_contents(self):
        """
        shows the files in the project
        :return: None
        """
        print(self.files)
