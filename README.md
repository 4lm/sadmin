# sadmin
Assignment in OOSS, THB, WS18 for creating a "Studierendenverwaltung" in Django

## Installation

[This installation manual was tested with a GNU/Linux operating system (Ubuntu 18.04) and might be adjusted for usage with other operating systems]

- First you need Git, Python (>= 3.6) with Virtualenv and Pip installed. If you are under Linux/Mac this should be a no-brainer, if you use Windows and you don't have a Git, Python, Virtualenv and Pip workflow yet, please read this [tutorial](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/) for Pip and Virtualenv installation/usage and visit this [link](https://git-scm.com/download/win) do download/install Git.
- If not already down Install Git, Python (>= 3.6), Pip (normally comes with Python) and Virtualenv
- Open the console (aka terminal, shell) on your computer
- Create a project directory in your terminal
- CD into your project directory (/path/to/project/)
- Download this Django project:
```
git clone https://github.com/4lm/sadmin.git
```
- CD into the downloaded git project folder (/path/to/project/sadmin/):
```
cd sadmin
```
- Create a virtualenv:
```
virtualenv venv --python=python3.6
```
- Activate virtualenv:
```
source venv/bin/activate
```
- Install project requirements via pip:
```
pip install -r requirements.txt
```
- CD into the django project folder (/path/to/project/sadmin/sadmin/):
```
cd sadmin
```
- Init project, also with some init data:
```
python manage.py migrate
python manage.py loaddata initial_data.json
```
- Start the development server:
```
python manage.py runserver
```
 