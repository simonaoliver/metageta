#!/bin/bash
export VERSION=2.0
export CURDIR=$(cd "$(dirname "$0")"; pwd)
export GDAL_DATA=$CURDIR/../gdal_data
export GEOTIFF_CSV=$GDAL_DATA
export PYTHONPATH=$CURDIR/lib:$PYTHONPATH
