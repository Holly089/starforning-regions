#Holly McClelland 26/09/17
#ASTR318 line ratios
#oxygen line ration


import cmath
import aplpy
import pylab as pl
import numpy as np
from astropy.io import fits

#get data.fits
OII_7320 = fits.open('OII7320_mom0_mosaic_dered.fits')
OII_7330 = fits.open('OII7330_mom0_mosaic_dered.fits')
OIII_4959 = fits.open('OIII4959_mom0_mosaic_dered.fits')
OIII_5007 = fits.open('OIII5007_mom0_mosaic_dered.fits')


hd = fits.getheader('OIII5007_mom0_mosaic_dered.fits')

OII_7320_data = OII_7320[0].data
OII_7330_data =OII_7330[0].data
OIII_4959_data = OIII_4959[0].data
OIII_5007_data = OIII_5007[0].data


#ave lines
OII_ave = (OII_7320_data + OII_7330_data )/ 2
OIII_ave = (OIII_4959_data + OIII_5007_data)/2

#line ratio
O_Ratio = OII_ave/OIII_ave


ff = fits.PrimaryHDU(data=O_Ratio, header=hd)
ff.writeto('O_Ratio.fits')

#figure
f = aplpy.FITSFigure('O_Ratio.fits')
f.show_colorscale(vmin=0, vmax=0.6)
f.add_colorbar()
f.colorbar.set_axis_label_text('[OII]/[OIII]')
f.save('O_line_map.png')

#plot
pl.imshow(O_Ratio, origin='lower', vmin=0, vmax = 1.5)      
pl.colorbar()                                 
pl.show() 

#pl.savefig('O_Ratio_Map.png')