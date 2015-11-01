#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	long_description = f.read()

setup(name='cvutils',
      version='0.1',
	  description='OpenCV utilites for blob detection, optical flow plots, etc.',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/cvutils',
	  install_requires=['numpy'],
           packages=['cvutils'],
	  )
