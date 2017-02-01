#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.call(['cmake','..'], cwd='bin')

    subprocess.call(['make'], cwd='bin')
except OSError as e:
    print(e)
    print('skipped optional compile')

try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)


setup(name='cvutils',
      packages=['cvutils'],
	  )

