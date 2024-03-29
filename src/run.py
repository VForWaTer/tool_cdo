import os
from datetime import datetime as dt

from cdo import *
from cdolib import *
from lib import *
from json2args import get_parameter

# parse parameters
kwargs = get_parameter()

# check if a toolname was set in env, default tool: sellonlatbox
toolname = os.environ.get('TOOL_RUN', 'sellonlatbox').lower()

# switch the tool
if toolname == 'sellonlatbox':
    # get the parameters
    try:
        infile = kwargs['infile']
        min_lon, max_lon, min_lat, max_lat = kwargs['min_lon'], kwargs['max_lon'], kwargs['min_lat'], kwargs['max_lat']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the command
    sellonlatbox(min_lon, max_lon, min_lat, max_lat, infile)

elif toolname == 'seldate':
    # get the parameters
    try:
        infile = kwargs['infile']
        startdate, enddate = kwargs['startdate'], kwargs['enddate']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the command
    seldate(startdate, enddate, infile)

elif toolname == 'seldate_sellonlatbox':
    # get the parameters
    try:
        infile = kwargs['infile']
        startdate, enddate = kwargs['startdate'], kwargs['enddate']
        min_lon, max_lon, min_lat, max_lat = kwargs['min_lon'], kwargs['max_lon'], kwargs['min_lat'], kwargs['max_lat']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the command
    seldate_sellonlatbox(startdate, enddate, min_lon, max_lon, min_lat, max_lat, infile)

elif toolname == 'selregion':
    # get the parameters
    try:
        infile = kwargs['infile']
        shape_geojson = kwargs['shape_geojson']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the command
    selregion(shape_geojson, infile)

elif toolname == 'mergetime':
    # get the parameters
    try:
        nc_folder, startdate, enddate = kwargs['nc_folder'], kwargs['startdate'], kwargs['enddate']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the command
    mergetime(nc_folder, startdate, enddate)

elif toolname == 'aggregate_netcdf':
    # get the parameters
    try:
        nc_folder, shape_geojson = kwargs['nc_folder'], kwargs['shape_geojson']
        variable, startdate, enddate, mode = kwargs['variable'], kwargs['startdate'], kwargs['enddate'], kwargs['mode']
        # if mode='percentile', the percentile value has to be specified in kwargs
        if mode == 'percentile':
            try:
                percentile = kwargs['percentile']
            except:
                raise ValueError("With aggregation mode='percentile', the percentile value has to be given with parameter 'percentile'.")
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the tool
    aggregate_netcdf(nc_folder, variable, shape_geojson, startdate, enddate, mode)

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
