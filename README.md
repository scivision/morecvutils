[![image](https://zenodo.org/badge/19711552.svg)](https://zenodo.org/badge/latestdoi/19711552)

[![Build Status](https://travis-ci.com/scivision/morecvutils.svg?branch=master)](https://travis-ci.com/scivision/morecvutils)
[![Python versions (PyPI)](https://img.shields.io/pypi/pyversions/morecvutils.svg)](https://pypi.python.org/pypi/morecvutils)
[![Downloads](https://pepy.tech/badge/morecvutils)](https://pepy.tech/project/morecvutils)

# CVutils

Uses Python with
[OpenCV](https://scivision.co/category/opencv/)
in miscellaneous demos of algorithms useful for computer vision.

Note: Line clipping was [moved to its own repo](https://github.com/scivision/lineclipping-python-fortran).

## Install

```sh
python -m pip install -e .
```

## Functions

* draw_flow()  given a 2-D complex Numpy array of optical flow `flow`, draw flow vectors with arrows
* draw_hsv() make a colored HSV image corresponding to flow direction and intensity at each point
* connectedComponents.py  given a binary image `morphed` and the `blobdet` from `setupblob()`, along with `img`, do connected components analysis
* OpticalFlow_Matlab_vs_Python.py   using Horn-Schunck optical flow estimation with OpenCV in Python. Not so obvious from the docs, and with notes on how to make this [match Matlab's vision.opticalFlowHS method](https://scivision.co/opencv-cv-calcopticalflowhs-horn-schunck-smoothness-lambda-parameter/). [Install Matlab Engine for Python](https://scivision.co/matlab-engine-callable-from-python-how-to-install-and-setup/)
