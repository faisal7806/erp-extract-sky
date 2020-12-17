# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sky_custom/__init__.py
from sky_custom import __version__ as version

setup(
	name='sky_custom',
	version=version,
	description='Sky Custom App',
	author='The Hacker Boi',
	author_email='ajadhao86@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
