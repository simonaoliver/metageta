'''
Metadata driver for ESRI GRIDs
==============================
@see:Format specification
    U{http://home.gdal.org/projects/aigrid/aigrid_format.html}
'''
#list of file name regular expressions
format_regex=[r'hdr\.adf$']

#import base dataset modules
import __default__

# import other modules (use "_"  prefix to import privately)
import sys, os

class Dataset(__default__.Dataset): 
    '''Subclass of __default__.Dataset class so we get a load of metadata populated automatically'''
    def __init__(self,f):
        '''Read Metadata for a ESRI GRID dataset and reset the filename from <path>\hdr.adf to <path>'''
        __default__.Dataset.__init__(self, f) #autopopulate basic metadata
        dir=os.path.dirname(f)
        self.metadata['filepath']=dir
        self.metadata['filename']=os.path.basename(dir)
        if self.metadata['compressiontype']=='Unknown':self.metadata['compressiontype']='RLE'