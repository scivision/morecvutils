#!/usr/bin/env python3
from setuptools import setup
import subprocess

proc = subprocess.Popen(['cmake','..'], cwd='bin')
#proc.communicate makes first Popen wait till done before proceeding
proc.communicate()

subprocess.Popen(['make'], cwd='bin')


try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    pass


with open('README.rst','r') as f:
	long_description = f.read()

setup(name='cvutils',
      packages=['cvutils'],
      description='OpenCV utilities for blob detection, optical flow plots, etc.',
      long_description=long_description,
      author='Michael Hirsch',
      url='https://github.com/scienceopen/cvutils',
	  )

