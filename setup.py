#!/usr/bin/env python3

from setuptools import setup
import subprocess

with open('README.rst','r') as f:
	long_description = f.read()

setup(name='cvutils',
      version='0.1',
	  description='OpenCV utilities for blob detection, optical flow plots, etc.',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/cvutils',
           packages=['cvutils'],
	  )

try:
    subprocess.call(['conda','install','--yes','--quiet','--file','requirements.txt'],shell=False) #don't use os.environ
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))
