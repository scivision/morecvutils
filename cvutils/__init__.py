from . import (lineClipping)

try:
    from . import (connectedComponents,cv2draw,getaviprop)
except ImportError as e:
    from warnings import warn
    warn('Possible not working OpenCV:   '.format(e))

#%% OpenCV 2 (legacy function)
try:
    from . import calcOptFlow
except:
    print('you may be running OpenCV 3, maybe these functions are in opencv-legacy')
