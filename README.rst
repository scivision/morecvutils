.. image:: https://landscape.io/github/scienceopen/CVutils/master/landscape.svg?style=flat
   :target: https://landscape.io/github/scienceopen/CVutils/master
   :alt: Code Health
.. image:: https://travis-ci.org/scienceopen/CVutils.svg?branch=master
  :target: https://travis-ci.org/scienceopen/CVutils
.. image:: https://coveralls.io/repos/scienceopen/CVutils/badge.svg?branch=master&service=github 
  :target: https://coveralls.io/github/scienceopen/CVutils?branch=master 
.. image:: https://codeclimate.com/github/scienceopen/CVutils/badges/gpa.svg
  :target: https://codeclimate.com/github/scienceopen/CVutils
  :alt: Code Climate

========
CVutils
========

Misc. algorithms useful for computer vision

``lineClipping.py``  Cohen-Sutherland line clipping algorithm for Python. Input scalars, output intersection length, or ``None`` if no intersection.

``cv2draw.py``  
 ``draw_flow()`` given a 2-D complex Numpy array of optical flow ``flow``, draw flow vectors with arrows
 
 ``draw_hsv()`` make a colored HSV image corresponding to flow direction and intensity at each point
  
``connectedComponents.py`` given a binary image ``morphed`` and the ``blobdet`` from ``setupblob()``, along with ``img``, do connected components analysis

``calcOptFlow.py`` using Horn-Schunck optical flow estimation with OpenCV in Python. Not so obvious from the docs, and with notes on how to make this `match Matlab's vision.opticalFlowHS method <https://scivision.co/opencv-cv-calcopticalflowhs-horn-schunck-smoothness-lambda-parameter/>`_.
