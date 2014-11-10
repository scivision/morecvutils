# forked from https://bitbucket.org/marcusva/py-sdl2 (which has public-domain license)
# The MIT License (MIT)
# Copyright (c) 2014 Michael Hirsch
# reference: http://en.wikipedia.org/wiki/Cohen%E2%80%93Sutherland_algorithm
# I have corrected errors in the cohensutherland code and compared cohensutherland with Matlab polyxpoly() results.

def cohensutherland(xmin, ymax, xmax, ymin, x1, y1, x2, y2,dbglvl=0):
    """Clips a line to a rectangular area.

    This implements the Cohen-Sutherland line clipping algorithm.  xmin,
    ymax, xmax and ymin denote the clipping area, into which the line
    defined by x1, y1 (start point) and x2, y2 (end point) will be
    clipped.

    If the line does not intersect with the rectangular clipping area,
    four None values will be returned as tuple. Otherwise a tuple of the
    clipped line points will be returned in the form (cx1, cy1, cx2, cy2).
    """
    INSIDE,LEFT, RIGHT, LOWER, UPPER = 0,1, 2, 4, 8

    def _getclip(xa, ya,dbglvl=0):
        if dbglvl>1: print('point: '),; print(xa,ya)
        p = INSIDE  #default is inside

        # consider x
        if xa < xmin:
            p |= LEFT
        elif xa > xmax:
            p |= RIGHT

        # consider y
        if ya < ymin:
            p |= LOWER # bitwise OR
        elif ya > ymax:
            p |= UPPER #bitwise OR
        return p

# check for trivially outside lines
    k1 = _getclip(x1, y1,dbglvl)
    k2 = _getclip(x2, y2,dbglvl)

# examine non-trivially outside points
    while (k1 | k2) != 0: # if both points are inside box (0000) , ACCEPT trivial whole line in box

        # if line trivially outside window, REJECT
        if (k1 & k2) != 0:
            if dbglvl>1: print('  REJECT trivially outside box')
            return None, None, None, None

        #non-trivial case, at least one point outside window
        opt = k1 or k2 # take first non-zero point, short circuit logic
        if opt & UPPER:
            x = x1 + (x2 - x1) * (1.0 * (ymax - y1)) / (y2 - y1) #1.0 forces float in divide
            y = ymax
        elif opt & LOWER:
            x = x1 + (x2 - x1) * (1.0 * (ymin - y1)) / (y2 - y1)
            y = ymin
        elif opt & RIGHT:
            y = y1 + (y2 - y1) * (1.0 * (xmax - x1)) / (x2 - x1)
            x = xmax
        elif opt & LEFT:
            y = y1 + (y2 - y1) * (1.0 * (xmin - x1)) / (x2 - x1)
            x = xmin
        else: raise RuntimeError('Undefined clipping state')

        if opt == k1:
            x1, y1 = x, y
            k1 = _getclip(x1, y1,dbglvl)
            if dbglvl>1: print('checking k1: ' + str(x) + ',' + str(y) + '    ' + str(k1))
        elif opt == k2:
            if dbglvl>1: print('checking k2: ' + str(x) + ',' + str(y) + '    ' + str(k2))
            x2, y2 = x, y
            k2 = _getclip(x2, y2,dbglvl)
    return x1, y1, x2, y2

if __name__ == '__main__': #test case
    from numpy.testing import assert_array_almost_equal
    '''
    make box with corners LL/UR (1,3) (4,5)
    and line segment with ends (0,0) (4,6)
    '''
    x1, y1, x2, y2 = cohensutherland(1,   5, 4, 3,
                                     0,   0, 4, 6)

    assert_array_almost_equal([x1,y1,x2,y2],[2,3,3.3333333333333,5])
    exit(0)
