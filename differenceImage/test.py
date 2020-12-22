from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

for f in range(24):
    print(f)
    hdu1 = fits.open("test1-" + str(f).zfill(4) + "-dirty.fits")
    hdu2 = fits.open("test2-" + str(f).zfill(4) + "-dirty.fits")
    diff = hdu2[0].data[0,0,:,:] - hdu1[0].data[0,0,:,:]
    plt.clf()
    plt.imshow(diff, origin="lower")
    plt.colorbar()
    plt.show()
