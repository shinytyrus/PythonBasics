# Overview
This is a repository used to store basis, intermediate or advanced examples of python code uses, that can be used on
different projects. I keep forgetting these skills when I go back and forth from coding, so I've finally thought about 
storing them in one place to hopefully remember quicker over time. I'll also store a simple setup using my go-to IDE,
which in this case is PyCharm, and I'll also add some testing examples too using 'pytest'.

## Setting up PyCharm
Before I start any coding, the first part I usually set up involves selecting an IDE. There are many IDE's available
by most people I feel switch between PyCharm or VSCode. There's also other useful text editors others like Sublime Text,
Atom or simply Notepad++ which are also great and simple, but I liked the additional features available in PyCharm.

You can download PyCharm from here - https://www.jetbrains.com/pycharm/download/#section=mac
I usually download the Community edition since it has all the features I need, but you can try out the Professional 
Edition if the additional features is what you need.

Once you've downloaded and installed it, follow the basic setup steps that it gives you. I prefer setting it into Dark
mode and skipping all the other setup steps. If you haven't used PyCharm before, doing the learning guide is quite
helpful with all the shortcuts that they make available to you. You won't remember them all straight away, but you'll
start to learn them over time. 

### Plugins
Once I've done that, I like to set up some useful plugins. There's a range of plugins that are installed by default, I 
won't go through these, but I will go through the additional ones. Below are a list of the additional plugins I like to
install:

* Requirements - https://plugins.jetbrains.com/plugin/10837-requirements - requirements file syntax
* .ignore - https://plugins.jetbrains.com/plugin/7495--ignore - .ignore file syntax
* Rainbow Brackets - https://plugins.jetbrains.com/plugin/10080-rainbow-brackets - Useful when you're dealing with multiple brackets
* Nyan Progress Bar - https://plugins.jetbrains.com/plugin/8575-nyan-progress-bar - This is just fun haha
* Material Theme UI - https://plugins.jetbrains.com/plugin/8006-material-theme-ui - Custom Themes
* Makefile Language - https://plugins.jetbrains.com/plugin/9333-makefile-language - Makefile syntax help
* GitToolBox - https://plugins.jetbrains.com/plugin/7499-gittoolbox - Additional git features that are helpful
* AWS ToolKit - https://plugins.jetbrains.com/plugin/11349-aws-toolkit - I tend to use this when working with AWS Lambda remotely

Of course, all of these are suggestions, you don't have to install them all at the start, you can install them when 
required. For example, I don't use the AWS ToolKit when I'm not working with AWS Lambdas, so then I don't need it.

Once you've set up the plugins and configured them to your liking, you're ready to go!

### Create a New Project in PyCharm
Before you start to use Python, you need to setup a new Project in PyCharm. You can do this by opening PyCharm and clicking 
Create New Project. From this you can easily setup a new Python project or just follow the instructions 
here -> https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html

Once you've done that you'll see a new Project window pop-up with all the default files.

## Setting up Python & Your Virtual Environment
Now that you've got PyCharm setup, you can now start playing around with Python. First, double check which Python 
version your running by either looking down the bottom right of the PyCharm window or in PyCharm, 
go to -> Settings -> Project (Your Project Name) -> Python Interpreter, and it should tell you which version your 
running. If you didn't manually install it, the Python version will be the most up-to-date version packaged with the 
PyCharm installer. Currently, I'm running version 3.9 for which feature updates can be found 
here - https://www.python.org/downloads/release/python-390/

### Set up your virtual environment
If you've created a new project in PyCharm, it's possible that you've already got a virtual environment setup. If you 
imported a project or didn't create a new one with a virtual environment, we'll go through how to set one up.

Let's first go through what a virtual environment is. A Python Virtual environment is a local folder structure of Python
packages that are related only to the project the virtual environment is linked to. It allows you to create separate
virtual environments for each project to reduce un-wanted packages for different projects, reduce dependency package
issues and reduce the amount of packages installed in your global System environment. For example, some projects may use
different versions of packages, and you can't install both of these at the same time globally, so you need two locations 
for them. Then you have to point your project to tell it where the correct version of the package is etc. and this
becomes tedious over time. Creating a virtual environment means that you know exactly what packages a project is using,
and you can manage it better over time. 

You can create a virtual environment in two ways. The first is using PyCharm. In Pycharm, go to -> Settings ->
Project (project name) -> Python Interpreter -> Add Interpreter (Add Local Interpreter) -> Virtualenv Environment ->
New -> Choose the location to save the virtual environment and the base python interpreter and click OK.

In case the above instructions don't work, check the PyCharm 
Documentation - https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env

The second way to create a virtual environment is using the Terminal and this guide from Real Python covers all the 
steps required - https://realpython.com/python-virtual-environments-a-primer/#how-can-you-work-with-a-python-virtual-environment

Once you've done that, you're ready to go and get hands on into code! 

## Playing around with Python, the simple steps!







