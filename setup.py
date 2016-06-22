#!/usr/bin/env python3
from setuptools import setup
import subprocess

try:
    proc = subprocess.Popen(['cmake','..'], cwd='bin')
    #proc.communicate makes first Popen wait till done before proceeding
    proc.communicate()

    subprocess.Popen(['make'], cwd='bin')
except OSError:
    print('skipped optional compile')

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    pass


setup(name='cvutils',
      packages=['cvutils'],
      description='OpenCV utilities for blob detection, optical flow plots, etc.',
      author='Michael Hirsch',
      url='https://github.com/scienceopen/cvutils',
	  )

