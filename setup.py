#!/usr/bin/env python3

from setuptools import setup 

with open('README.rst') as f:
	long_description = f.read()
	
setup(name='CVutils',
      version='0.1',
	  description='OpenCV utilites for blob detection, optical flow plots, etc.',
	  long_description=long_description,
	  author='Michael Hirsch',
	  author_email='hirsch617@gmail.com',
	  url='https://github.com/scienceopen/CVutils',
	  install_requires=['numba','numpy','enum34'],
      packages=['CVutils'],
	  )
