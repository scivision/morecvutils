.. image:: https://zenodo.org/badge/19711552.svg
   :target: https://zenodo.org/badge/latestdoi/19711552

.. image:: https://travis-ci.org/scivision/morecvutils.svg?branch=master
    :target: https://travis-ci.org/scivision/morecvutils

.. image:: https://coveralls.io/repos/scivision/morecvutils/badge.svg?branch=master&service=github 
  :target: https://coveralls.io/github/scivision/morecvutils?branch=master 


========
CVutils
========

:Author: Michael Hirsch
:License: MIT
:Prereq: `OpenCV 2 or OpenCV 3 <https://scivision.co/category/opencv/>`_

.. contents::

Misc. algorithms useful for computer vision.

Install
=======
::
   
   python setup.py develop

Fortran Build (optional)
------------------------
If you want to use the Fortran Cohen-Sutherland line clipping modules directly (optional)::

    cd bin
    cmake ..
    make
    

Usage
=====
The main difference with textbook implementations is that I return a sentinel value (NaN, None, nothing) if there's no intersection of line with box.

Python
------

.. code:: python

    import morecvutils.lineclipping as lc
    
    x3,y3,x4,y4 = lc.cohensutherland((xmin, ymax, xmax, ymin, x1, y1, x2, y2)
    
If no intersection, `(None, None, None, None)` is returned.

Fortran
-------
`lineclipping.f90` has two subroutines.
Pick `Ccohensutherland` if you're calling from C/C++/Python, which cannot tolerate assummed-shape arrays. 
It's a slim wrapper to `cohensutherland` which is elemental (can handle scalar or any rank array).

Fortran programs will simply use

.. code:: fortran

    use lineclipping
    call cohensutherland(xmin,ymax,xmax,ymin,x1,y1,x2,y2)


The arguments are::

    INPUTS
    ------
    xmin,ymax,xmax,ymin:  upper left and lower right corners of box (pixel coordinates)

    INOUT
    -----
    x1,y1,x2,y2: 
    in - endpoints of line
    out - intersection points with box. If no intersection, all NaN


Julia
-----
Simliar to Python, except `nothing` is returned if no intersection found.

.. code:: julia

    cohensutherland(xmin, ymax, xmax, ymin, x1, y1, x2, y2)
    
 

Functions
=========

================================= ======================
function                          description
================================= ======================
lineClipping.jl                    Cohen-Sutherland line clipping algorithm for Julia. Input scalars, output intersection length, or ``None`` if no intersection.

lineclipping.f90                   Cohen-Sutherland line clipping algorithm for Fortran. Input scalars or arrays, output intersections.

lineClipping.py                     Cohen-Sutherland line clipping algorithm for Python. Input scalars, output intersection length, or ``None`` if no intersection.

draw_flow()                         given a 2-D complex Numpy array of optical flow ``flow``, draw flow vectors with arrows
draw_hsv()                           make a colored HSV image corresponding to flow direction and intensity at each point
  
connectedComponents.py              given a binary image ``morphed`` and the ``blobdet`` from ``setupblob()``, along with ``img``, do connected components analysis

OpticalFlow_Matlab_vs_Python.py     using Horn-Schunck optical flow estimation with OpenCV in Python. Not so obvious from the docs, and with notes on how to make this `match Matlab's vision.opticalFlowHS method <https://scivision.co/opencv-cv-calcopticalflowhs-horn-schunck-smoothness-lambda-parameter/>`_. `Install Matlab Engine for Python <https://scivision.co/matlab-engine-callable-from-python-how-to-install-and-setup/>`_
================================= ======================
