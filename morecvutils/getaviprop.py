#!/usr/bin/env python
"""
gets basic info about AVI file using OpenCV

input: filename or cv2.Capture
"""
from pathlib import Path
from struct import pack
from typing import Dict, Any
import cv2


def getaviprop(fn: Path) -> Dict[str, Any]:
    if isinstance(fn, (str, Path)):  # assuming filename
        fn = Path(fn).expanduser()
        if not fn.is_file():
            raise FileNotFoundError(fn)
        v = cv2.VideoCapture(str(fn))
        if v is None:
            raise OSError(f'could not read {fn}')
    else:  # assuming cv2.VideoCapture object
        v = fn

    if not v.isOpened():
        raise OSError(f'cannot read {fn}  probable codec issue')

    vidparam = {
        'nframe': int(v.get(cv2.CAP_PROP_FRAME_COUNT)),
        'xy_pixel': (
            int(v.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(v.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        ),
        'fps': v.get(cv2.CAP_PROP_FPS),
        'codec': fourccint2ascii(int(v.get(cv2.CAP_PROP_FOURCC))),
    }

    if isinstance(fn, Path):
        v.release()

    return vidparam


def fourccint2ascii(fourcc_int: int) -> str:
    """
    convert fourcc 32-bit integer code to ASCII
    """
    assert isinstance(fourcc_int, int)

    return pack('<I', fourcc_int).decode('ascii')


if __name__ == '__main__':
    from argparse import ArgumentParser

    p = ArgumentParser(description='get parameters of AVI file')
    p.add_argument('avifn', help='avi filename')
    p = p.parse_args()

    vidparam = getaviprop(p.avifn)
    print(vidparam)
