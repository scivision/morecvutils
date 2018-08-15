#!/usr/bin/env python
"""
Michael Hirsch
Example calculations of optical flow, starting with Horn Schunk Optical Flow using OpenCV
"""
try:
    from cv2 import cv  # necessary for Windows, "import cv" doesn't work
except ImportError:  # NOTE: openCV 3.0 has legacy code buried in opencv-extra
    cv = None
from numpy import asarray, dstack
#
from pyoptflow import HornSchunck


def optflowHornSchunk(new, ref, uv, smoothing=0.01):
    if cv is not None:
        """
        http://docs.opencv.org/modules/legacy/doc/motion_analysis.html
        Note that smoothness parameter for cv.CalcOpticalFlowHS needs to be SMALLER than matlab
        to get similar result. Useless when smoothness was 1 in OpenCV, but it's 1 in Matlab!
        """
        cvref = cv.fromarray(ref)
        cvnew = cv.fromarray(new)
        #result is placed in u,v
        # matlab vision.OpticalFlow Horn-Shunck has default maxiter=10, terminate=eps, smoothness=1
        cv.CalcOpticalFlowHS(cvref, cvnew, False, uv[0], uv[1],
                             smoothing,
                             (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 8, 0.1))

        # reshape to numpy float32, xpix x ypix x 2
        flow = dstack((asarray(uv[0]), asarray(uv[1])))
    else:  # use Python method
        u, v = HornSchunck(ref, new)
        flow = dstack((u, v))

    return flow


def setupuv(rc):
    """
    Horn Schunck legacy OpenCV function requires we use these old-fashioned cv matrices, not numpy array
    """
    if cv is not None:
        (r, c) = rc
        u = cv.CreateMat(r, c, cv.CV_32FC1)
        v = cv.CreateMat(r, c, cv.CV_32FC1)
        return (u, v)
    else:
        return [None]*2


def calcofhs(new, ref, smoothing):
    uv = setupuv(new.shape)
    return optflowHornSchunk(new, ref, uv, smoothing)
