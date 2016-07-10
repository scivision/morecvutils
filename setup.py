#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.call(['cmake','..'], cwd='bin')

    subprocess.call(['make'], cwd='bin')
except OSError:
    print('skipped optional compile')

try:
    subprocess.call(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    pass


setup(name='cvutils',
      packages=['cvutils'],
      description='OpenCV utilities for blob detection, optical flow plots, etc.',
      author='Michael Hirsch',
      url='https://github.com/scienceopen/cvutils',
	  )

