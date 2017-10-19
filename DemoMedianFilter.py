#!/usr/bin/env python
import cv2
from numpy import zeros,count_nonzero
from skimage.util import random_noise
from matplotlib.pyplot import subplots,show

from time import time

Nx=Ny=32
V = 255 # opencv 0,255 for binary

im = zeros((Ny,Nx),dtype='uint8')
#im = random_noise(im,'s&p',amount=0.25).astype('uint8')*V
im[18:29,5] = V # vert line
im[15,18:29] = V # horiz line
im[4:7,4:6] = V
im[4:6,24:27] = V
im[4:7,14:17] = V

im[4:6,9:11] = V
im[6,10] = V

im[20:25:2,20:25:2] = V
im[21:24:2,21:24:2] = V

imfilt = cv2.medianBlur(im,3)
#%%
im2 = zeros((Ny,Nx),dtype='uint8')
im2[4:7,4:7] = V
im2[4,8] = V

tic = time()
im2filt = cv2.medianBlur(im2,3)
print('median filter time {:.3e} sec'.format(time()-tic))
#%% Erosion
openrad = 3
kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (openrad,openrad))

im3 = zeros((Ny,Nx),dtype='uint8')
im3[4:7,4:7] = V
im3[4,8] = V

tic = time()
im3filt = cv2.erode(im3,kern)
print('erosion time {:.3e} sec'.format(time()-tic))
#%%
fg,ax = subplots(2,4,num=1,sharex=True,sharey=True)

fg.suptitle('Median Filter vs. Morphological Erosion',fontsize='large')

ax[0,0].imshow(im,cmap='gray_r',interpolation='none',origin='bottom')
ax[0,0].set_title('original')

ax[0,1].imshow(imfilt,cmap='gray_r',interpolation='none',origin='bottom')
ax[0,1].set_title('median filtered')

ax[0,2].imshow(cv2.erode(im,kern),cmap='gray_r',interpolation='none',origin='bottom')
ax[0,2].set_title('erosion original')

ax[0,3].imshow(cv2.erode(imfilt,kern),cmap='gray_r',interpolation='none',origin='bottom')
ax[0,3].set_title('erosion median filtered')



ax[1,0].imshow(im2,cmap='gray_r',interpolation='none',origin='bottom')
ax[1,0].set_title('original')

ax[1,1].imshow(im2filt,cmap='gray_r',interpolation='none',origin='bottom')
ax[1,1].set_title('median filtered')

ax[1,2].imshow(cv2.erode(im2,kern),cmap='gray_r',interpolation='none',origin='bottom')
ax[1,2].set_title('erosion')

ax[1,3].imshow(cv2.erode(im2filt,kern),cmap='gray_r',interpolation='none',origin='bottom')
ax[1,3].set_title('erosion median filtered')

for a in ax.ravel():
    a.set_xlim((0,Nx))

#print('{} pixels remain'.format(count_nonzero(imfilt)))

show()