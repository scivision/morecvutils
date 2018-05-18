.. image:: https://zenodo.org/badge/19711552.svg
   :target: https://zenodo.org/badge/latestdoi/19711552



========
CVutils
========

:Author: Michael Hirsch
:License: MIT
:Prereq: `OpenCV 2 or OpenCV 3 <https://scivision.co/category/opencv/>`_

.. contents::

Misc. algorithms useful for computer vision.
 
Note: Line clipping was `moved to its own repo <https://github.com/scivision/lineclipping-python-fortran>`_.

Install
=======
::
   
   python -m pip install -e .



Functions
=========

================================= ======================
function                          description
================================= ======================
draw_flow()                       given a 2-D complex Numpy array of optical flow ``flow``, draw flow vectors with arrows
draw_hsv()                        make a colored HSV image corresponding to flow direction and intensity at each point
  
connectedComponents.py            given a binary image ``morphed`` and the ``blobdet`` from ``setupblob()``, along with ``img``, do connected components analysis

OpticalFlow_Matlab_vs_Python.py   using Horn-Schunck optical flow estimation with OpenCV in Python. Not so obvious from the docs, and with notes on how to make this `match Matlab's vision.opticalFlowHS method <https://scivision.co/opencv-cv-calcopticalflowhs-horn-schunck-smoothness-lambda-parameter/>`_. `Install Matlab Engine for Python <https://scivision.co/matlab-engine-callable-from-python-how-to-install-and-setup/>`_
================================= ======================
