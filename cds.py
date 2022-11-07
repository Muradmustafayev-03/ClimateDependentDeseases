# !/usr/bin/env python
import cdsapi

c = cdsapi.Client()

c.retrieve('reanalysis-era5-complete', {
    # Requests follow MARS syntax
    # Keywords 'expver' and 'class' can be dropped. They are obsolete
    # since their values are imposed by 'reanalysis-era5-complete'
    'date': '2013-01-01',  # The hyphens can be omitted
    'levelist': '1/10/100/137',  # 1 is top level, 137 the lowest model level in ERA5. Use '/' to separate values.
    'levtype': 'ml',
    'param': '130',  # Full information at https://apps.ecmwf.int/codes/grib/param-db/
    # The native representation for temperature is spherical harmonics
    'stream': 'oper',  # Denotes ERA5. Ensemble members are selected by 'enda'
    'time': '00/to/23/by/6',  # You can drop :00:00 and use MARS shorthand notation, instead of '00/06/12/18'
    'type': 'an',
}, 'output')  # Output file; in this example containing fields in grib format. Adapt as you wish.
