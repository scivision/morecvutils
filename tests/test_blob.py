#!/usr/bin/env python
import pytest
import numpy as np
from pytest import approx
from pathlib import Path

import morecvutils.connectedComponents as mb

R = Path(__file__).parent


def test_blob():

    im_good = np.zeros((32, 32), dtype=np.uint8)
    im_good[10:20, 10:20] = 255

    im_bad = np.zeros((32, 32), dtype=np.uint8)
    im_bad[10:12, 10:12] = 255

    blob = mb.setupblob(10, 200, 4)

    labeled_img, label_sizes = mb.doblob(im_good, blob)

    assert labeled_img.shape == (32, 32, 3)
    assert len(label_sizes) == 1

    labeled_img, label_sizes = mb.doblob(im_bad, blob)

    assert len(label_sizes) == 0


def test_avi():
    pytest.importorskip('cv2')
    from morecvutils.getaviprop import getaviprop

    finf = getaviprop(R / 'data/bunny.avi')

    assert finf['fps'] == approx(24.0)
    assert finf['xy_pixel'] == (426, 240)
    assert finf['nframe'] == 168
    assert finf['codec'] == 'H264'


if __name__ == '__main__':
    pytest.main([__file__])
