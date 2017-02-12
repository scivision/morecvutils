#!/usr/bin/env python
from pathlib import Path
from scipy.ndimage import imread
from numpy import uint8,asfortranarray,hypot,empty,asarray,float32
from matplotlib.pyplot import subplots,draw,pause
#
from morecvutils.calcOptFlow import setupuv, optflowHornSchunk

def plotflow(mag,matmag):
    fg,ax = subplots(1,2,figsize=(12,5))

    for i in range(I.shape[0]-1):
        if i==0:
            hi = ax[0].imshow(mag[0,...])
            ax[0].set_title('Python optical flow mag')
            fg.colorbar(hi,ax=ax[0])
            hm = ax[1].imshow(matmag[0,...])
            ax[1].set_title('Matlab Optical flow mag')
            fg.colorbar(hm,ax=ax[1])
            hs = fg.suptitle('frame #')
        else:
            hi.set_data(mag[i,...])
            hm.set_data(matmag[i,...])
            hs.set_text('frame # {}'.format(i))
        draw(); pause(0.001)

def matlab_flow(I):
    import matlab.engine
    eng = matlab.engine.start_matlab("-nojvm")

    matmag = eng.test_optflow(matlab.uint8(I.tolist()))
    matmag = asarray(matmag)

    eng.quit()

    return matmag

def py_flow(I,N,r,c):
    uv = setupuv((r,c))

    mag = empty((N,r,c)) #priming read

    for i in range(N):
        flow = optflowHornSchunk(I[i+1,...], I[i,...], uv,smoothing=0.001)
        mag[i,...] = hypot(flow[...,0],flow[...,1])

    return mag

def setup(flist):
    N = len(flist)-1
    r,c = imread(str(flist[0])).shape
    I = empty((N+1,r,c),dtype=uint8)

    for i,f in enumerate(flist):
        I[i,...] = imread(str(f))

    return I,N,r,c
#%% demo
try:
    plotflow(mag,matmag)
except NameError:
    flist = sorted(Path('tests/data').glob('*.png'))

    I,N,r,c = setup(flist)
    #%% python
    mag = py_flow(I,N,r,c)
    #%% Matlab
    matmag = matlab_flow(I)
    #%%
    plotflow(mag,matmag)
