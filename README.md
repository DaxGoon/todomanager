**ToDo Manager for Developers.**

In progress.

I will update the readme when it's (almost) complete.

*How to add a todo on your project*

Tasks are assigned on files inside your project folder. 
If you want to add a todo on a file just add:

`# todo: whatever todo you want to add ---file_name@line_number_for_reference`

for example, if I am working on a main.py file and want to add a reminder todo to check
for error at line 157, I would write the following line somewhere in main.py file:

`# todo: check for error --- main.py@157`

`# todo:` is case sensitive and only in the lowercase is recognised by the application.
There must be only one space between `#` and `todo:`


__ROADMAP for the application:__

The following are not implemented yet, I will edit this file when these features are implemented:
1. Automatic Project Creation
2. Viewing todos by projects
3. Database integration
4. GUI integration
