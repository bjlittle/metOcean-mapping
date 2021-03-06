# Python module to hold the master references for MetOcean Metadata Translation prefixes

import StringIO
import re


class Prefixes(dict):
    __slots__ = []
    
    def __init__(self):
        #super(Prefixes, self).__init__()
        prefixd = {
        'rdfs'     : 'http://www.w3.org/2000/01/rdf-schema#',
        'rdf'      : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'skos'     : 'http://www.w3.org/2004/02/skos/core#',
        'xsd'      : 'http://www.w3.org/2001/XMLSchema#',
        'dc'       : 'http://purl.org/dc/terms/',
        'github'   : 'https://github.com/' ,
        'map'      : 'http://www.metarelate.net/metOcean/mapping/',
        'mr'       : 'http://www.metarelate.net/vocabulary/index.html#',
        'metoc'    : 'http://www.metarelate.net/metOcean/' ,
        'metocFormat' : 'http://www.metarelate.net/metOcean/format/' ,
        'metocMed' : 'http://www.metarelate.net/metOcean/mediator/' ,
        'moStCon'  : 'http://reference.metoffice.gov.uk/def/um/stash/concept/' ,
        'moStND'   : 'http://reference.metoffice.gov.uk/def/um/stash/new_dynamics/' ,
        'moStEG'   : 'http://reference.metoffice.gov.uk/def/um/stash/endgame/' ,
        'mofc'     : 'http://reference.metoffice.gov.uk/def/um/fieldcode/',
        'moumdpF3' : 'http://reference.metoffice.gov.uk/def/um/umdp/F3/',
        'moumdpC4' : 'http://reference.metoffice.gov.uk/def/um/umdp/c4/',
        'moumdpC4Pseud' : 'http://reference.metoffice.gov.uk/def/um/umdp/c4/pseudo/',
        'momet08'  : 'http://reference.metoffice.gov.uk/def/um/met08/',
        'cfsn'     : 'http://def.cfconventions.org/standard_names/' ,
        'cfm'      : 'http://def.cfconventions.org/datamodel/' ,
        'gribapi'  : 'http://def.ecmwf.int/api/grib/keys/',
        'openmathr1' : 'http://www.openmath.org/cd/relation1.xhtml#',
        'openmatha1' : 'http://www.openmath.org/cd/arith1.xhtml#',
        'meta'     : 'http://reference.metoffice.gov.uk/data/wmo/def/met#',
        'metamap'  : 'http://reference.metoffice.gov.uk/data/wmo/meta/mapping#',
        
        }
        self.update(prefixd)

    def __getattr__(self, key):
        return self[key]

    def value2key(self, value):
        for k, v in self.items():
           if v == value:
                return k 

    @property
    def sparql(self):
        ios = StringIO.StringIO()
        for key, value in sorted(self.items()):
            ios.write('PREFIX %s: <%s>\n' % (key, value))
        ios.write('\n')
        return ios.getvalue()

    @property
    def turtle(self):
        ios = StringIO.StringIO()
        for key, value in sorted(self.items()):
            ios.write('@prefix %s: <%s> .\n' % (key, value))
        ios.write('\n')
        return ios.getvalue()

    @property
    def rdf(self):
        ios = StringIO.StringIO()
        for key, value in sorted(self.items()):
            ios.write('xmlns:%s="%s"\n' % (key, value))
        ios.write('\n')
        return ios.getvalue()

    @property
    def irilist(self):
        return sorted(self.values())

    @property
    def datalist(self):
        return sorted([(x,y) for x,y in self.items() if not re.search('#$', y)])

    @property
    def prefixlist(self):
        return sorted(self.keys())


