#!/usr/bin/env python
import pytest
import numpy as np

import morecvutils.connectedComponents as mb


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


if __name__ == '__main__':
    pytest.main([__file__])
