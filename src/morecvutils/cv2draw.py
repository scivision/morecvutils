import cv2

import numpy as np


def draw_flow(img, flow, step=16):
    """
    draws flow vectors on image
    this came from opencv/examples directory
    another way: http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
    """
    maxval = np.iinfo(img.dtype).max

    # scaleFact = 1. #arbitary factor to make flow visible
    canno = (0, maxval, 0)  # green color
    h, w = img.shape[:2]
    y, x = np.mgrid[step // 2 : h : step, step // 2 : w : step].reshape(2, -1)
    fx, fy = flow[y, x].T
    # create line endpoints
    lines = np.vstack([x, y, (x + fx), (y + fy)]).transpose.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    # create image
    if img.ndim == 2:  # assume gray
        vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:  # already RGB
        vis = img
    # draw line
    cv2.polylines(vis, lines, isClosed=False, color=canno, thickness=1, lineType=8)
    # draw filled green circles
    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(vis, center=(x1, y1), radius=1, color=canno, thickness=-1)
    return vis


def draw_hsv(mag, ang, dtype=np.uint8, fn: str | None = None):
    """
    mag must be uint8, uint16, uint32 and 2-D
    ang is in radians (float)
    """
    assert mag.shape == ang.shape
    assert mag.ndim == 2
    maxval = np.iinfo(dtype).max

    hsv = np.dstack(
        (
            (np.degrees(ang) / 2).astype(dtype),  # /2 to keep less than 255
            np.ones_like(mag) * maxval,  # maxval must be after in 1-D case
            cv2.normalize(mag, alpha=0, beta=maxval, norm_type=cv2.NORM_MINMAX),  # type: ignore[call-overload]
        )
    )
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    if fn is not None:
        print("writing " + fn)
        cv2.imwrite(fn, rgb)

    return rgb  # , hsv


def flow2magang(flow, dtype=np.uint8):
    """
    flow dimensions y,x,2  3-D.  flow[...,0] is magnitude, flow[...,1] is angle
    """
    fx, fy = flow[..., 0], flow[..., 1]
    return np.hypot(fx, fy).astype(dtype), np.arctan2(fy, fx) + np.pi


# %% selftest
if __name__ == "__main__":
    flow = np.array(
        [[[55, np.pi / 4], [128, 3 * np.pi / 2]], [[123, np.pi / 2], [48, np.pi]]]
    )

    mag, ang = flow2magang(flow, np.uint8)

    rgb = draw_hsv(mag, ang)

    assert rgb[1, 0, 2] == 239
