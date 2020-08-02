#Holly McClelland 26/09/17
#ASTR318 line ratios
#S23 line ration


import cmath
import aplpy
import pylab as pl
import numpy as np
from astropy.io import fits

#get the data
SII6717 = fits.open('SII6717_mom0_mosaic_dered.fits')
SII6731 = fits.open('SII6731_mom0_mosaic_dered.fits')
SIII9068 = fits.open('SIII9068_mom0_mosaic_dered.fits')
HB = fits.open('Hb_mom0_mosaic_dered.fits')

hd = fits.getheader('SII6731_mom0_mosaic_dered.fits')

SII6717_data = SII6717[0].data
SII6731_data = SII6731[0].data
SIII9068_data = SIII9068[0].data
HB_data = HB[0].data


#line ratio
S_lines = SII6717_data +SII6731_data + SIII9068_data
S23 = S_lines/HB_data



ff = fits.PrimaryHDU(data=S23, header=hd)
ff.writeto('S23.fits')


#figure
f = aplpy.FITSFigure('O_Ratio.fits')
f.show_colorscale(vmin=0, vmax=4)
f.add_colorbar()
f.colorbar.set_axis_label_text('[SII + SIII]/[H Beta]')
f.save('S23_line_map.png')


#plot
pl.imshow(S23, origin='lower', vmin=0, vmax = 4 )      
pl.colorbar()                                 
pl.show() 

#pl.savefig('electron_temp_map.png')