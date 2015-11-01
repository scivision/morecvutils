#!/usr/bin/env python
"""
Michael Hirsch
Example calculations of optical flow, starting with Horn Schunk Optical Flow using OpenCV
"""
from __future__ import division,absolute_import
from cv2 import cv
from numpy import asarray,dstack,uint8

def optflowHornSchunk(new,ref,uv,smoothing=0.01):
    """
    http://docs.opencv.org/modules/legacy/doc/motion_analysis.html
    ***************************
    Note that smoothness parameter for cv.CalcOpticalFlowHS needs to be SMALLER than matlab
    to get similar result. Useless when smoothness was 1 in python, but it's 1 in Matlab!
    *****************************
    """
    cvref = cv.fromarray(ref)
    cvnew = cv.fromarray(new)
    #result is placed in u,v
    # matlab vision.OpticalFlow Horn-Shunck has default maxiter=10, terminate=eps, smoothness=1
    cv.CalcOpticalFlowHS(cvref, cvnew, False, uv[0], uv[1],
                         smoothing,
                         (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 8, 0.1))

    # reshape to numpy float32, xpix x ypix x 2
    return dstack((asarray(uv[0]), asarray(uv[1])))

def setupuv(rc):
    """
    Horn Schunck legacy OpenCV function requires we use these old-fashioned cv matrices, not numpy array
    """
    (r,c) = rc
    u = cv.CreateMat(r, c, cv.CV_32FC1)
    v = cv.CreateMat(r, c, cv.CV_32FC1)
    return (u, v)

def calcofhs(new,ref,smoothing):
    uv = setupuv(new.shape)
    return optflowHornSchunk(new,ref,uv,smoothing)
#%% demo
if __name__ == '__main__':
    from numpy.random import rand
    rc = (512,512)
    r,c=rc
    uv = setupuv(rc)
    old = (rand(r,c)*255).astype(uint8)

    for i in range(100):
        new = (rand(r,c)*255).astype(uint8)
        flow = optflowHornSchunk(new,old,uv,smoothing=0.01)
        old = new.copy()
