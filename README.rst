.. image:: https://landscape.io/github/scienceopen/CVutils/master/landscape.svg?style=flat
   :target: https://landscape.io/github/scienceopen/CVutils/master
   :alt: Code Health

.. image:: https://coveralls.io/repos/scienceopen/CVutils/badge.svg?branch=master&service=github 
  :target: https://coveralls.io/github/scienceopen/CVutils?branch=master 

.. image:: https://codeclimate.com/github/scienceopen/CVutils/badges/gpa.svg
  :target: https://codeclimate.com/github/scienceopen/CVutils
  :alt: Code Climate

========
CVutils
========

:Author: Michael Hirsch
:License: MIT
:Prereq: `OpenCV 2.4 or 3.0 <https://scivision.co/category/opencv/>`_

.. contents::

Misc. algorithms useful for computer vision.

Install
=======

`Requires OpenCV 2.4 or 3.0 <https://scivision.co/category/opencv/>`_

::
   
   git clone --depth 1 https://github.com/scienceopen/CVutils/
   conda install --file requirements.txt
   python setup.py develop


Functions
=========

========================= ======================
function                  description
========================= ======================
lineClipping.py            Cohen-Sutherland line clipping algorithm for Python. Input scalars, output intersection length, or ``None`` if no intersection.

draw_flow()                given a 2-D complex Numpy array of optical flow ``flow``, draw flow vectors with arrows
draw_hsv()                 make a colored HSV image corresponding to flow direction and intensity at each point
  
connectedComponents.py     given a binary image ``morphed`` and the ``blobdet`` from ``setupblob()``, along with ``img``, do connected components analysis

calcOptFlow.py             using Horn-Schunck optical flow estimation with OpenCV in Python. Not so obvious from the docs, and with notes on how to make this `match Matlab's vision.opticalFlowHS method <https://scivision.co/opencv-cv-calcopticalflowhs-horn-schunck-smoothness-lambda-parameter/>`_.
========================= ======================
