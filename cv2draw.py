from __future__ import division
import cv2
from numpy import dstack,degrees,pi,array,ones_like,uint8,arctan2,hypot

def draw_hsv(mag,ang,fn=None):   
    """
    mag must be uint8, uint16, uint32 and 2-D
    ang is in radians (float)
    """
    dtype = mag.dtype
    assert mag.shape == ang.shape
    assert mag.ndim == 2
    
    hsv = dstack(((degrees(ang)/2).astype(dtype), 
                  ones_like(mag)*255,  #255 must be after in 1-D case
                  cv2.normalize(mag, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)))
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)

    if fn is not None:
        print('writing ' + fn)
        cv2.imwrite(fn,rgb)
    
    return rgb, hsv
    
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