#Holly McClelland 19/09/17

#ASTR381
#temp calculation

import cmath
import aplpy
import pylab as pl
import numpy as np
from astropy.io import fits


#get data
NII_6548 = fits.open('NII6548_mom0_mosaic_dered.fits')
NII_6584 = fits.open('NII6584_mom0_mosaic_dered.fits')
NII_5755 = fits.open('NII5755_mom0_mosaic_dered.fits')

hd = fits.getheader('NII5755_mom0_mosaic_dered.fits')


NII_6548_data = NII_6548[0].data
NII_6584_data = NII_6584[0].data
NII_5755_data = NII_5755[0].data

#ratio calc
R = (NII_6548_data+NII_6584_data)/NII_5755_data

#calc temp
T_e = 2.5*10**4/(np.log(R))

#fits file
ff = fits.PrimaryHDU(data=T_e, header=hd)
ff.writeto('Te.fits')

#figure
f = aplpy.FITSFigure('Te.fits')
f.show_colorscale(vmin=0, vmax=25000)
f.add_colorbar()
f.colorbar.set_axis_label_text('K')
f.save('Te_map.png')


#plot
#pl.imshow(T_e, origin='lower', vmin=0, vmax=25000)      
#pl.colorbar()                                 
#pl.show() 



#to save the map
#pl.savefig('electron_temp_map.png')