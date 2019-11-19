#!/usr/bin/env python
import cv2
import numpy as np
from skimage.util import random_noise

from morecvutils.connectedComponents import setupblob, doblob


def gen_patterns(x: int, y: int, dtype=np.uint8, add_noise: float = 0.0) -> np.ndarray:

    if dtype == np.uint8:
        V = 255
    elif dtype in (float, np.float32, np.float64):
        V = 1
    elif dtype in (int, np.uint16):
        V = 65535
    else:
        raise TypeError(dtype)

    im = np.zeros((y, x), dtype=dtype)

    im[18:55, 5] = V  # vert line
    im[15, 18:55] = V  # horiz line

    im[224:227, 224:226] = V
    im[224:226, 24:27] = V
    im[214:217, 14:17] = V

    im[4:6, 9:11] = V
    im[6, 10] = V

    im[40:140:1, 20:100:1] = V  # area 100*80

    im[190:220:1, 120:200:1] = V

    if add_noise > 0:
        im = random_noise(im, 's&p', amount=add_noise).astype('uint8') * V

    return im


def main():

    # image dimension (arbitrary)
    x = y = 256

    img_area = x * y
    print(f'area of the {x} x {y} image is {img_area} pixels')

    # set some arbitrary parameters
    max_blob = img_area // 4
    min_blob = img_area // 1000

    print(f'Minimum and maximum blob areas: {min_blob}, {max_blob}')

    im1 = gen_patterns(x, y, np.uint8, 0.0)

    blob = setupblob(min_blob, max_blob, 4)

    labeled_img, label_sizes = doblob(im1, blob)

    cv2.imshow('Labeled Image', labeled_img)
    print('press any key to exit')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
