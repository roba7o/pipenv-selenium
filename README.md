This project requires Python 3.8 or higher. You can download the latest Python version from Python.org.

This course also requires pipenv. To install pipenv, run pip install pipenv from the command line or use homebrew.

You should also have a Python editor/IDE of your choice. Good choices include PyCharm and Visual Studio Code.

You will also need to set latest chromedriver (this can be found in chrome settings) to your PATH (i used homebrew for this but there is multiple methods for windows and mac/zsh.). To verify correct setup on any operating system, simply try to run them from the terminal:
$ ChromeDriver

Project Setup
Clone this repository.
1. Run cd pipenv-selenium to enter the project.
2. Run pipenv install to install the dependencies.
3. Run pipenv shell to launch env
4. Run pipenv run python -m pytest to verify that the framework can run tests.

