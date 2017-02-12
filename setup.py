#!/usr/bin/env python
from setuptools import setup

req = ['nose','numpy']

setup(name='morecvutils',
      packages=['morecvutils'],
      description='Computer Vision utilities, Cohen-Sutherland line clipping, OpenCV plot helpers for Optical Flow and Blob Analysis, AVI codec helpers',
      version='0.9',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scienceopen/morecvutils',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Visualization',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req,
      extras_require={'cv2':['cv2']},
	  )

