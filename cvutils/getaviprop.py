#!/usr/bin/env python
"""
gets basic info about AVI file using OpenCV

input: filename or cv2.Capture
"""
from . import Path
import cv2
try:
    from cv2 import cv
except:
    pass #OpenCV 3
from six import string_types,integer_types
from struct import pack


def getaviprop(f):
    if isinstance(f,(string_types,Path)): #assuming filename
        f = Path(f).expanduser()
        v = cv2.VideoCapture(str(f))
        if v is None:
            raise RuntimeError('could not read {}'.format(f))
    else: #assuming cv2.VideoCapture object
        v=f

    if not v.isOpened():
        raise RuntimeError('cannot read {}  probable codec issue'.format(f))

#%% note the subtle different CV_ prefix to property name, thus this verbose technique
    try: #opencv 2.X
        vidparam = {'nframe': int(v.get(cv.CV_CAP_PROP_FRAME_COUNT)),
                    'xpix'  : int(v.get(cv.CV_CAP_PROP_FRAME_WIDTH)),
                    'ypix'  : int(v.get(cv.CV_CAP_PROP_FRAME_HEIGHT)),
                    'fps'   : v.get(cv.CV_CAP_PROP_FPS),
                    'codec' : fourccint2ascii(int(v.get(cv.CV_CAP_PROP_FOURCC)))
                    }
    except NameError: #opencv 3.0
        vidparam = {'nframe': int(v.get(cv2.CAP_PROP_FRAME_COUNT)),
                    'xpix'  : int(v.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    'ypix'  : int(v.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                    'fps'   : v.get(cv2.CAP_PROP_FPS),
                    'codec' : fourccint2ascii(int(v.get(cv2.CAP_PROP_FOURCC)))
                    }
    if isinstance(f,Path): #not if it was fed a capture!
        v.release()

    return vidparam

def fourccint2ascii(fourcc_int):
    """
    useful for converting fourcc in integer form (32-bit int) to ASCII
    """
    assert isinstance(fourcc_int,integer_types)
    return pack('<I',fourcc_int)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p=ArgumentParser(description='get parameters of AVI file')
    p.add_argument('avifn',help='avi filename')
    p=p.parse_args()

    vidparam = getaviprop(p.avifn)
    print(vidparam)