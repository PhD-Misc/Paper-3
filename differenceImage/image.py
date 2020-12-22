from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from astropy.wcs import WCS
from datetime import datetime, timedelta

hdu1 = fits.open("cleaned1-image.fits")
hdu2 = fits.open("cleaned2-image.fits")
time1 = datetime.strptime(hdu1[0].header['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
time2 = datetime.strptime(hdu2[0].header['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
wcs = WCS(hdu1[0].header, naxis=2)



img1 = hdu1[0].data[0,0,:,:]
img2 = hdu2[0].data[0,0,:,:]

plt.figure().add_subplot(1,1,1, projection=wcs)
plt.imshow(img1[450:1200, 600:1500], origin="lower",vmax=50,vmin=-10)
plt.grid()
plt.xlabel("RA (hours)")
plt.ylabel("DEC (Degrees)")
plt.show()
