# Overview
This is a repository used to store basis, intermediate or advanced examples of python code uses, that can be used on
different projects. I keep forgetting these skills when I go back and forth from coding, so I've finally thought about 
storing them in one place to hopefully remember quicker over time. I'll also store a simple setup using my go-to IDE,
which in this case is PyCharm, and I'll also add some testing examples too using 'pytest'.

# Setting up PyCharm
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

## Plugins
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

## Fonts
This is a more pedantic section that I wanted to add which was fonts. Everyone has their favourite fonts and some more
than others. I preferred the default 'JetBrains Monospaced' font or the 'Fira Code' monospaced font because you can use 
font ligatures. I found this from a friend and since I've started using it, I've liked it because it's just that little
bit fancy when using arrows for example ->. You can find out more about font ligatures here -> https://en.wikipedia.org/wiki/Ligature_(writing)

## Create a New Project in PyCharm
Before you start to use Python, you need to setup a new Project in PyCharm. You can do this by opening PyCharm and clicking 
Create New Project. From this you can easily setup a new Python project or just follow the instructions 
here -> https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html

Once you've done that you'll see a new Project window pop-up with all the default files.

# Setting up Python & Your Virtual Environment
Now that you've got PyCharm setup, you can now start playing around with Python. First, double check which Python 
version your running by either looking down the bottom right of the PyCharm window or in PyCharm, 
go to -> Settings -> Project (Your Project Name) -> Python Interpreter, and it should tell you which version your 
running. If you didn't manually install it, the Python version will be the most up-to-date version packaged with the 
PyCharm installer. Currently, I'm running version 3.9 for which feature updates can be found 
here - https://www.python.org/downloads/release/python-390/

## Set up your virtual environment
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

# Playing around with Python, the simple steps!
## Folder Structure
An important part of getting started with Python is setting up a folder structure. You may not need to do this right
away, especially if your project is only a few small files. However, if your project starts to span out to multiple
files, it's better to have it setup from the start, rather than moving modules around later. 

A good example of a folder structure for a Python project is in the Hitchhiker's Guide to Python -> https://docs.python-guide.org/writing/structure/#structure-of-the-repository
It goes through a simple example of setting up your project, even if you want to save it as a module or a package later
on. My suggestion of a basic setup is as follows:

-> ROOT
    -> README.md
    -> Module_A/
        -> sample_a.py
    -> tests/
        -> test_sample_a.py

The 'README.md' file stores information about the project, just like this file you're reading. The 'Module_A' folder 
stores the functional code that is written and is related to Module_A. You may have other Module folders to split up the
related files. Finally, there's a 'tests' folder which holds all the test code for each module. Within this folder, you
can add sub-folders for each module to test, or you can use a specific naming convention like 
'test_module_a_<test_name>'.


# Testing 
An important part about Python that you need to keep in mind is testing. It's important to always test the code we write
so that we know it's meeting the defined requirements/parameters. There are a few frameworks that can be used to test in
Python, but the one I prefer is 'pytest' because of how easy it is to use and adapt
-> https://docs.pytest.org/en/7.1.x/index.html

## PyTest -> Installation and Set Up
Setting up Pytest is quite straight forward. First, open up a terminal and change directory to your project. Then make 
sure that your in your Python Virtual Environment. You could install this globally but if you decide to test out other 
testing frameworks it may cause issues. Once you've activated your Virtual Environment, use pip to install the framework
-> 'pip install pytest'.

### Using PyTest in PyCharm
Using PyTest within PyCharm has its benefits as it can make the testing process a bit easier and more fluid to run.
With PyCharm, you need to set up a test configuration. A test configuration defines the parameters for the test. In this
case, we can set up one test configuration or multiple. To start of we'll create a single test configuration by going to
-> Configurations -> Edit Configurations -> Add New Configurations -> pytest.

In here, you'll need to set the following:

* Target -> Script Path
* Target Location -> <The PATH to your project directory>
* Environment -> Working Directory -> <The PATH to your project directory>

Once you've done that save it.

Then create a sample file within the tests folder called sample.py with the following code:

    def func(x):
        return x + 1
    
    
    def test_answer():
        assert func(3) == 5

Run the configuration, and you should see that it runs one test and it passed!

Once you've verified it works, you can add more test files and also run those. 

### Using Pytest in the Terminal
In some cases you may not have access to PyCharm but you can still run tests using the terminal. Simply open up a
terminal/console and change directory to the root folder of the project. Once in there you can create the same sample
file as noted in the previous section for PyCharm. When that's run, you can run the following command to run the test
using pytest: `python3 -m pytest`

This will output the same information as if you'd run it using the sample PyCharm test configuration as the section
above. 

## Code Coverage
Code coverage is additional step you can add into your testing as it checks how much of your code you've actually
tested. You can write as many tests as you want but if you don't test all of your code, then it's possible that you may
run into edge cases where your code will break. Code Coverage helps to verify that you've tested all your code and not
missed any parts. For example, it helps to check if you've tested all the functions or if you've tested all the branches
in your code as well (known as branch coverage).

Setting up code coverage is quite simple and since we're already using pytest as our testing framework, we can use 
'pytest-cov' as our code coverage tool. To do this, similar to installing 'pytest', first open up a terminal and change
directory to your projects folder. Then, make sure that your in your Python Virtual Environment and it's activated. Then
use pip to install the framework -> 'pip install pytest-cov'.

Once that successfully installs, you should be able to run it.

### Code Coverage using PyCharm
To enable code coverage in PyCharm can be done through the Run Configuration setup earlier. Edit the pytest run
configuration and in the 'Additional Arguments' section add the following parameters 
`--cov-branch --cov=Module_A --cov-report=html`. 

`--cov-branch` enables branch coverage and lets you know if you've covered all possible branches within the code. An
example of a branch is an if-statement, where there could be multiple possibilities. 

`--cov=Module_A` enables coverage on all files within that source or module. In this case we've enabled coverage for the
'Module_A' module and all it's files underneath. If your module is named differently, you can just change the name or if
you have multiple modules that you want to run coverage over, just add more values for that parameter. 

`--cov-report=html` this stores the results of the coverage into a report and in this case saves it out as a HTML file.
This comes in useful as you can open up the HTML file within a browser of your choice and see which lines have been
covered and which haven't across all the files that were tested. 

Run the configuration and you should see a new folder stored within the project called 'htmlcov'. Within this folder
will be a file called 'index.html', open that in a browser and you'll see the total coverage for all your files. Remember
coverage doesn't show you what tests fail and pass, it only shows you what part of your code that you've tested and 
haven't tested. 

### Code Coverage using Terminal
To enable code coverage using the Terminal, simply open up a terminal/console and change directory to the root folder of
the project. Once in there, you can run the following command to run the test and code coverage using pytest:
`python3 -m pytest --cov-branch --cov=Module_A --cov-report=html`.

This will output the same information as if you'd run it using the sample PyCharm test configuration as the section
above. You can then open up the 'index.html' file to see the results of the coverage.

# Python Packages
There are a whole range of python packages like the ones we've already discussed above. Each package is stored on
Python's Package Index called PyPI. You can install, uninstall, upgrade any packages you want but this doesn't mean that
you should install all the packages. It's good practice to only install the packages you need as many packages have
other packages they are dependant on which can get quite confusing. Especially when you want to install two different
packages but they require the same dependant package but different versions of it.

When you're starting off there's only a small selection of Python Packages I'd suggest you install and these are:

* virtualenv - To create your virtual environments
* pytest - For testing your code (do this within a virtual environment)
* pytest-cov - For checking code coverage (do this within a virtual environment)
* black - To format your code (do this within a virtual environment)

For a basic Python project where you're writing simple functions and don't need to access parts of the internet or
do some fancy stuff, these packages will be all you really need. However, when you start to build your project up more,
you may want to use configuration files, dealing with HTTP response codes or checking against security vulnerabilities 
in your code, there will be other packages you may want to look into. These packages are as follows:

* json - Used for parsing JSON content
* pyyaml - Used for parsing YAML content
* jinja2 - Used for templating parts of your code
* requests - Used for making HTTP requests
* boto3 - The AWS SDK
* datetime - Useful for when you are dealing with dates/times or timezone values
* argparse - Useful for parsing input arguments from a python executable
* sqlalchemy - Useful when communicating with a Database via SQL
* pipdeptree - See all the install packages and their dependencies
* pip-autoremove - Remove a package and all it's dependencies (may not work)