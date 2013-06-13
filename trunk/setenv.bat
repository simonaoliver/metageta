@ECHO OFF 
SETLOCAL ENABLEDELAYEDEXPANSION
PUSHD %~DP0
SET CURDIR=%CD%
PUSHD ..
SET TOPDIR=%CD%
POPD
POPD

SET GDAL_ROOT=%TOPDIR%\bin\gdal
SET GDAL_API_PROXY=ecw,sid,jp2,j2k,ntf
rem SET GDAL_API_PROXY_CONN_POOL=NO
rem SET GDAL_PAM_PROXY_DIR=%TEMP%
SET GDAL_DATA=%GDAL_ROOT%\share\gdal-data
SET GEOTIFF_CSV=%GDAL_DATA%
SET PROJ_LIB=%GDAL_ROOT%\share\proj
SET GDAL_DRIVER_PATH=%GDAL_ROOT%\bin\plugins

SET PYTHONHOME=%TOPDIR%\bin\Python27
SET PYTHONPATH=%PYTHONHOME%\Lib\lib-tk
SET PYTHONPATH=%PYTHONHOME%\Lib\site-packages\pywin32_system32;%PYTHONHOME%\Lib\site-packages\win32;%PYTHONHOME%\Lib\site-packages\win32\lib;%PYTHONHOME%\Lib\site-packages\pythonwin;%PYTHONPATH%
SET PYTHONPATH=%GDAL_ROOT%\bin;%GDAL_ROOT%\lib;%PYTHONPATH%
SET PYTHONPATH=%CURDIR%;%PYTHONPATH%

SET path=
SET path=%WINDIR%;%WINDIR%\system32
PATH=%GDAL_ROOT%\bin;%PATH%
PATH=;%GDAL_ROOT%\lib\osgeo;%PATH%
PATH=%GDAL_DRIVER_PATH%;%PATH%
PATH=%PYTHONPATH%;%PATH%
PATH=%PYTHONHOME%;%PATH%
PATH=%CURDIR%;%PATH%

SET GDAL_SKIP=
SET _GDAL_SKIP=JP2MrSID JP2OpenJPEG
for /f "tokens=1" %%D IN ('gdalinfo  --formats^|findstr /r "%_GDAL_SKIP%"') DO SET GDAL_SKIP=!GDAL_SKIP! %%D

