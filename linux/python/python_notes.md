# Notes about python on linux system

## Where are packages installed ?
help('modules')

/lib/site-packages in your Python folder

import module_name
print(module_name.__file__)
import pygal
print(pygal.__file__)

>>> import os
>>> print(os.__file__)
/usr/lib/python3.8/os.py

>>> dir(math)
>>> help(math)
>>> help('_sha1')


## Python packages links
https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
https://www.tutorialsteacher.com/python/python-package
