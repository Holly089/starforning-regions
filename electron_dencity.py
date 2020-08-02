#Holly McClelland 18/09/17
#ASTR 381 

#calculating electron dencity with line ratios SII



import cmath
import aplpy
import pylab as pl
import numpy as np
from astropy.io import fits


#import data
SII_6717 = fits.open('SII6717_mom0_mosaic_dered.fits')
SII_6731 = fits.open('SII6731_mom0_mosaic_dered.fits')

hd = fits.getheader('SII6731_mom0_mosaic_dered.fits')

SII_6717_data = SII_6717[0].data
SII_6731_data = SII_6731[0].data


#calculating R_SII ratio
R_SII = SII_6717_data/SII_6731_data


#calc electron temp
N_e = (R_SII - 1.49)/(5.6713 - 12.8 * R_SII) * 10**4

ff = fits.PrimaryHDU(data=N_e, header=hd)
ff.writeto('Ne.fits')


#figure
f = aplpy.FITSFigure('Ne.fits')
f.show_colorscale(vmin=0, vmax=25000)
f.add_colorbar()
f.colorbar.set_axis_label_text('electron dencity (cm^-3)')
f.save('Ne_map.png')


#plot
#pl.imshow(N_e, origin='lower',vmin=0,vmax=1000)      
#pl.colorbar()                                 
#pl.show() 

#to save the map
#pl.savefig('electron_dencity_map.png')

