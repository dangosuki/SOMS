# Student Offense Management System

# How to run this build

Note that this project was all created and tested on Windows 11 machines

## Pre-requisites

Install virtual env on your computer using the command below:

```bash
pip install virtualenv
```

## Setting up a virtual environment

Run the command below to create a virtual environment with python 3.10 installed

```bash
py -3.10 -m venv sample-venv
```

A folder will be created with the name *sample-venv*. Go inside sample-venv using the command below:

```bash
cd sample-venv
```

Now that you are inside *sample-venv*, to activate the virtual environment, run the command below:

```bash
Scripts\activate.bat
```

You will see that there is a *(sample-venv)* on the left side of your command prompt. It looks like this:

```bash
(sample-venv) C:\...\sample-venv
```

Now that you are inside the virutal environment, you must first install the dependencies of the project.

You can download the text file named *requirements.txt* from the assets dropdown on the project's releases and place it inside the *sample-venv* folder or you can create a text file named *requirements.txt* inside the *sample-venv* folder. Open the said text file using any text editor app and paste the lines below and save the file.

```
asgiref==3.8.1
defusedxml==0.7.1
diff-match-patch==20230430
Django==5.0.4
django-filter==24.2
django-import-export==3.3.8
et-xmlfile==1.1.0
gunicorn==22.0.0
MarkupPy==1.14
odfpy==1.4.1
openpyxl==3.1.2
packaging==24.0
pillow==10.3.0
psycopg2==2.9.9
PyYAML==6.0.1
sqlparse==0.5.0
tablib==3.5.0
typing_extensions==4.11.0
tzdata==2024.1
whitenoise==6.6.0
xlrd==2.0.1
xlwt==1.3.0
```

Then, install these dependencies using the command below (assuming you are inside the *sample-venv* folder and the virtual environment is activated)

```bash
pip install -r requirements.txt
```

If you want to deactivate the virtual environment, just run the command below:

```bash
Scripts\deactivate.bat
```

## Building the project

Note that you can obtain the project's files either by cloning the repo

### Cloning the project from the repository

Note that you must clone the repository inside the *sample-venv* folder.

```bash
cd sample-venv
```

Make sure that you are inside the *sample-venv* folder before proceeding to clone the repository.

The link to the project's repository is this: [SOMS (github.com)](https://github.com/dangosuki/SOMS)

In order to clone this git repo to your machine, run the command below:

```git
git clone https://github.com/dangosuki/SOMS.git
```

A folder with the name SOMS will be created. Inside it are the contents of the repository.

Activate the virtual environment first using the command below (Assuming you are inside *sample-venv* folder).

```bash
Scripts\activate.bat
```

## Running the web application

At this step, it i is assumed that you have already activated the virtual environment and you are inside the *sample-venv* folder. You must see this below in your command prompt:

```bash
(sample-venv) C:\...\sample-venv
```

Next, we need to start the development server using the commands below:

```bash
python SOMS\manage.py migrate
```

```bash
python SOMS\manage.py runserver
```

You will see in your a line saying

```bash
Starting development server at http://127.0.0.1:8000/
```

Paste the url into your browser and then you should be seeing the home page of the application now

# Requirements

The dependencies included in requirements.txt are listed below plus other libraries that we used not installed through pip

- Python libraries
  
  - Django - https://www.djangoproject.com/
  
  - Numpy - https://numpy.org/ 
  
  - Scipy - https://scipy.org/

- Chart.js - https://www.chartjs.org/

- Ionicons - https://ionic.io/ionicons

# References

- no author. [Django documentation](https://docs.djangoproject.com/en/4.0/?fbclid=IwAR2dqnYI2Q_iRjttWoAFagmqd_ke_HnjRE7PHrCd-nApRYyxHAKQjhqGDks). Last accessed: March 15, 2022
