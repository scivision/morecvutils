#!/usr/bin/env python
"""
Michael Hirsch
Example calculations of optical flow, starting with Horn Schunk Optical Flow using OpenCV
"""
import numpy as np
try:
    import cv2
except ImportError:  # NOTE: openCV 3 has legacy code buried in opencv-extra
    cv2 = None
from numpy import asarray, dstack
#
from pyoptflow import HornSchunck


def optflowHornSchunk(new: np.ndarray, ref: np.ndarray,
                      uv, smoothing=0.01) -> np.ndarray:
    if cv2 is not None:
        """
        http://docs.opencv.org/modules/legacy/doc/motion_analysis.html
        Note that smoothness parameter for cv.CalcOpticalFlowHS needs to be SMALLER than matlab
        to get similar result. Useless when smoothness was 1 in OpenCV, but it's 1 in Matlab!
        """
        cvref = cv2.fromarray(ref)
        cvnew = cv2.fromarray(new)
        # result is placed in u,v
        # matlab vision.OpticalFlow Horn-Shunck has default maxiter=10, terminate=eps, smoothness=1
        cv2.CalcOpticalFlowHS(cvref, cvnew, False, uv[0], uv[1],
                              smoothing,
                              (cv2.CV_TERMCRIT_ITER | cv2.CV_TERMCRIT_EPS, 8, 0.1))

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
    if cv2 is not None:
        (r, c) = rc
        u = cv2.CreateMat(r, c, cv2.CV_32FC1)
        v = cv2.CreateMat(r, c, cv2.CV_32FC1)
        return (u, v)
    else:
        return [None]*2


def calcofhs(new, ref, smoothing):
    uv = setupuv(new.shape)
    return optflowHornSchunk(new, ref, uv, smoothing)
