'''
Dictionary of field names and data types
========================================
'''

fields={'abstract'        :'no fieldtype required as this is not included in the shapefile...',
        'bands'           :('string',50),
        'cellx'           :'float',
        'celly'           :'float',
        'units'           :('string',25),
        'cloudcover'      :('string',50),
        'cols'            :'int',
        'compressionratio':'int',
        'compressiontype' :('string',50),
        'datatype'        :('string',50),
        'datecreated'     :('string',25),
        'datemodified'    :('string',25),
        'demcorrection'   :('string',50),
        'epsg'            :('string',4),
        'filelist'        :('string',255),
        'filename'        :('string',50),
        'filepath'        :('string',255),
        'filesize'        :'int',
        'filetype'        :('string',50),
        'guid'            :('string',36),
        'imgdate'         :('string',25),
        'lineage'         :'no fieldtype required as this is not included in the shapefile...',
        'level'           :('string',50),
        'LL'              :('string',25),#should probably be separate LLX and LLY etc... fields with 'float' type...
        'LR'              :('string',25),
        'metadata'        :'no fieldtype required as this is not included in the shapefile...',
        'metadatadate'    :('string',25),
        'mode'            :('string',50),
        'nbands'          :'int',
        'nbits'           :'int',
        'nodata'          :'float',
        'orbit'           :('string',50),
        'orientation'     :('string',50),
        'ownerid'         :('string',50),
        'ownername'       :('string',50),
        'quicklook'       :('string',50),
        'resampling'      :('string',50),
        'rotation'        :'float',
        'rows'            :'int',
        'satellite'       :('string',50),
        'sceneid'         :('string',50),
        'sensor'          :('string',50),
        'srs'             :'no fieldtype required as this is not included in the shapefile...',
        'sunazimuth'      :'float',
        'sunelevation'    :'float',
        'thumbnail'       :('string',50),
        'title'           :'no fieldtype required as this is not included in the shapefile...',
        'UL'              :('string',25),
        'UR'              :('string',25), 
        'useConstraints'  :'no fieldtype required as this is not included in the shapefile...',
        'viewangle'       :'float'
}
