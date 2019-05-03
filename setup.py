import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-polls',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='MIT License',
	description='A simple Django app to construct Web-based polls.',
	long_description=README,
	url='https://www.example.com',
	author='Valentin Ivanov',
	author_email='Valyo95@abv.bg',
	classifiers=[
		'Enviroment :: Web Enviroment',
		'Framework :: Django',
		'Framework :: Django :: 2.2',
		'Intended Audience :: Developers',
		'Licence :: MIT Licence',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)