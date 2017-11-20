#!/usr/bin/env python
req = ['nose','numpy']
# %%
import subprocess
from setuptools import setup,find_packages

setup(name='morecvutils',
      packages=find_packages(),
      description='Computer Vision utilities, Cohen-Sutherland line clipping, OpenCV plot helpers for Optical Flow and Blob Analysis, AVI codec helpers',
      version='0.9.1',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/morecvutils',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Visualization',
      'Programming Language :: Python :: 3',
      ],
      install_requires=req,
      extras_require={'cv2':['cv2']},
      python_requires='>=3.5',
	  )

try:
    subprocess.run(['cmake','..'],cwd='bin',timeout=10)
    subprocess.run(['make'],cwd='bin',timeout=10)
except Exception:
    pass
