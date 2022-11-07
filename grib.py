import pygrib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import numpy as np

plt.figure(figsize=(12, 8))

grib = 'cams_aod.grib'  # Set the file name of your input GRIB file
grbs = pygrib.open(grib)

print(grib)
