# virtualenv environments (and optionally doesn’t access the globally installed dependencies either). You can even configure what version of Python you want to use for each individual environment. It's very much recommended to use virtualenv when dealing with Python applications.
# $ pip3 install virtualenv
# $ cd my-project/
# $ virtualenv venv
# If you want your virtualenv to also inherit globally installed packages run:
# $ virtualenv venv --system-site-packages
# hese commands create a venv/ directory in your project where all dependencies are installed. You need to activate it first though (in every terminal instance where you are working on your project):
# $ source venv/bin/activate
# To leave the virtual environment run:
# $ deactivate
# To make it easier to work on multiple projects that has separate environments you can install virtualenvwrapper. It's an extension to virtualenv and makes it easier to create and delete virtual environments without creating dependency conflicts.
# Note: virtualenvwrapper keeps all the virtual environments in ~/.virtualenv while virtualenv




