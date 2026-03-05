"""Command line program for ERA5 data pre-processing.

Processes data from the following location at NCI:
/g/data/rt52/era5/{level_type}/reanalysis/{variable}/*/*.nc

Example:
python era5.py msl single-levels 12 test.nc

"""
import pdb
import glob
import argparse

import numpy as np
import xarray as xr


def get_output_encoding(ds, var):
    """Define the output file encoding."""

    encoding = {}
    ds_vars = list(ds.coords) + list(ds.keys())
    for ds_var in ds_vars:
        if ds_var == var:
            encoding[ds_var] = {'_FillValue': np.float32(1e20)}
            encoding[ds_var]['dtype'] = 'float32'
        else:
            encoding[ds_var] = {'_FillValue': None}
            encoding[ds_var]['dtype'] = 'float64'

    return encoding


def main(args):
    """Run the program."""

    inpaths = f'/g/data/rt52/era5/{args.level_type}/reanalysis/{args.variable}/*/*.nc'
    infiles = sorted(glob.glob(inpaths))
    if not infiles:
        raise OSError(f'No input files at {inpaths}')
    input_ds = xr.open_mfdataset(infiles)
    output_da = input_ds[args.variable]
    output_da = output_da.sel(time=output_da['time'].dt.hour == args.hour)
    if args.level:
        output_da = output_da.sel(level=args.level)
    pdb.set_trace()
    output_ds = output_da.to_dataset()
    output_ds.attrs = input_ds.attrs
    encoding = get_output_encoding(output_ds, args.variable)
    output_ds.to_netcdf(args.outpath, encoding=encoding)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    valid_hours = np.arange(0, 24)
    valid_levels = [
        1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 125, 150, 175, 200,
        225, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750,
        775, 800, 825, 850, 875, 900, 925, 950, 975, 1000
    ]
    parser.add_argument("variable", type=str, help="ERA5 variable selection")
    parser.add_argument("level_type", type=str, choices=('single-levels', 'pressure-levels'), help="ERA5 level type selection")
    parser.add_argument("hour", type=int, choices=valid_hours, help="ERA5 hour selection")
    parser.add_argument("outpath", type=str, help="output file path")
    parser.add_argument("--level", type=int, default=None, choices=valid_levels, help="ERA5 level selection")
    args = parser.parse_args()
    if args.level_type == 'pressure_levels':
        assert args.level, 'You must select a level using the --level option' 
    main(args)
