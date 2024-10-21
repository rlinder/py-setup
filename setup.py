from setuptools import setup

setup(
   name='py_setup',
   version='1.0.0-1',
   description='Play with Python Setup',
   author='Ruben LINDER',
   author_email='ruben.linder@7asecond.com',
   packages=['py_setup'],  #same as name
   install_requires=['requests',  'sqlalchemy', 'trino[sqlalchemy]'], #external packages as dependencies
)