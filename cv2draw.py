from __future__ import division
import cv2
from numpy import (dstack,degrees,pi,array,ones_like,arctan2,hypot,mgrid,vstack,
                    uint8,int32,iinfo)

def draw_flow(img, flow, step=16,dtype=uint8):
    """
    draws flow vectors on image
    this came from opencv/examples directory
    another way: http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
    """
    maxval=iinfo(img.dtype).max

    #scaleFact = 1. #arbitary factor to make flow visible
    canno = (0, maxval, 0)  # green color
    h, w = img.shape[:2]
    y, x = mgrid[step//2:h:step, step//2:w:step].reshape(2,-1)
    fx, fy =  flow[y,x].T
    #create line endpoints
    lines = vstack([x, y, (x+fx), (y+fy)]).T.reshape(-1, 2, 2)
    lines = int32(lines + 0.5)
    #create image and draw line
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, isClosed=False, color=canno, thickness=1, lineType=8)
    #draw filled green circles
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, center=(x1, y1), radius=1, color=canno, thickness=-1)
    return vis

def draw_hsv(mag,ang,dtype=uint8,fn=None):
    """
    mag must be uint8, uint16, uint32 and 2-D
    ang is in radians (float)
    """
    assert mag.shape == ang.shape
    assert mag.ndim == 2
    maxval=iinfo(dtype).max

    hsv = dstack(((degrees(ang)/2).astype(dtype), #/2 to keep less than 255
                  ones_like(mag)*maxval,  #maxval must be after in 1-D case
                  cv2.normalize(mag, alpha=0, beta=maxval, norm_type=cv2.NORM_MINMAX)))
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)

    if fn is not None:
        print('writing ' + fn)
        cv2.imwrite(fn,rgb)

    return rgb#, hsv

def flow2magang(flow,dtype=uint8):
    """
    flow dimensions y,x,2  3-D.  flow[...,0] is real, flow[...,1] is imag
    """
    fx,fy = flow[...,0], flow[...,1]
    return hypot(fx,fy).astype(dtype), arctan2(fy, fx) + pi

#%% selftest
if __name__ == '__main__':
    flow = array([[[55,pi/4],
                  [128,3*pi/2]],
                  [[123,pi/2],
                  [48,pi]]])

    mag, ang = flow2magang(flow,uint8)

    rgb,hsv=draw_hsv(mag, ang)
    assert hsv[0,0,2] == 22
    assert rgb[1,0,2] == 239