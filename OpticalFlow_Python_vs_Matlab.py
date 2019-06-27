#!/usr/bin/env python
from pathlib import Path
import imageio
from typing import Sequence
import numpy as np
from matplotlib.pyplot import figure, draw, pause, show
#
from morecvutils.calcOptFlow import setupuv, optflowHornSchunk


def plotflow(mag, matmag):
    fg = figure(figsize=(12, 5))
    ax = fg.subplots(1, 2)

    for i in range(I.shape[0]-1):
        if i == 0:
            hi = ax[0].imshow(mag[0, ...])
            ax[0].set_title('Python optical flow mag')
            fg.colorbar(hi, ax=ax[0])

            if matmag is not None:
                hm = ax[1].imshow(matmag[0, ...])
                ax[1].set_title('Matlab Optical flow mag')
                fg.colorbar(hm, ax=ax[1])

            hs = fg.suptitle('frame #')
        else:
            hi.set_data(mag[i, ...])
            if matmag is not None:
                hm.set_data(matmag[i, ...])

            hs.set_text('frame # {}'.format(i))

        draw()
        pause(0.001)


def matlab_flow(I):
    import matlab.engine
    eng = matlab.engine.start_matlab("-nojvm")

    matmag = eng.test_optflow(matlab.uint8(I.tolist()))
    matmag = np.asarray(matmag)

    eng.quit()

    return matmag


def py_flow(I, N, r, c):
    uv = setupuv((r, c))

    mag = np.empty((N, r, c))  # priming read

    for i in range(N):
        flow = optflowHornSchunk(I[i+1, ...], I[i, ...], uv, smoothing=0.001)
        mag[i, ...] = np.hypot(flow[..., 0], flow[..., 1])

    return mag


def setup(flist: Sequence[Path]):
    N = len(flist)-1
    r, c = imageio.imread(str(flist[0])).shape
    im = np.empty((N+1, r, c), dtype=np.uint8)

    for i, f in enumerate(flist):
        im[i, ...] = imageio.imread(str(f))

    return im, N, r, c


if __name__ == '__main__':

    flist = sorted(Path('tests/data').glob('*.png'))

    I, N, r, c = setup(flist)
    # %% python
    mag = py_flow(I, N, r, c)
    # %% Matlab
    try:
        matmag = matlab_flow(I)
    except ImportError:
        matmag = None
    # %%
    plotflow(mag, matmag)

    show()
