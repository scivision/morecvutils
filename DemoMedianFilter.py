#!/usr/bin/env python
import cv2
import numpy as np
from skimage.util import random_noise
from matplotlib.pyplot import figure, show
from typing import Tuple


def gen_patterns(x: int, y: int, dtype=np.uint8, noise: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:

    if dtype == np.uint8:
        V = 255
    elif dtype in (float, np.float32, np.float64):
        V = 1
    elif dtype in (int, np.uint16):
        V = 65535
    else:
        raise TypeError(dtype)

    im = np.zeros((y, x), dtype=dtype)

    im[18:29, 5] = V  # vert line
    im[15, 18:29] = V  # horiz line
    im[4:7, 4:6] = V
    im[4:6, 24:27] = V
    im[4:7, 14:17] = V

    im[4:6, 9:11] = V
    im[6, 10] = V

    im[20:25:2, 20:25:2] = V
    im[21:24:2, 21:24:2] = V

    if noise > 0:
        im = random_noise(im, 's&p', amount=noise).astype('uint8')*V

    im2 = np.zeros((y, x), dtype='uint8')
    im2[4:7, 4:7] = V
    im2[4, 8] = V

    return im, im2


def plot_panel(fg, im: np.ndarray):
    ax = fg.add_subplot(1, 4, 1)
    ax.imshow(im, cmap='gray_r', interpolation='none', origin='bottom')
    ax.set_title('original')

    imfilt = cv2.medianBlur(im, 3)

    ax = fg.add_subplot(1, 4, 2)
    ax.imshow(imfilt, cmap='gray_r', interpolation='none', origin='bottom')
    ax.set_title('median filtered')

    openrad = 3
    kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (openrad, openrad))

    ax = fg.add_subplot(1, 4, 3)
    ax.imshow(cv2.erode(im, kern), cmap='gray_r', interpolation='none', origin='bottom')
    ax.set_title('erosion')

    ax = fg.add_subplot(1, 4, 4)
    ax.imshow(cv2.erode(imfilt, kern), cmap='gray_r', interpolation='none', origin='bottom')
    ax.set_title('erosion median filtered')

    # for a in ax:
    #   a.set_xlim((0, im.shape[1]))


im1, im2 = gen_patterns(32, 32, np.uint8, 0.)

plot_panel(figure(), im1)
plot_panel(figure(), im2)

show()
