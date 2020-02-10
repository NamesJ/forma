from . import Driver
from . import Log

import sys

class Finder (object):
    def __init__(self, **kwargs):
        self.driver = Driver()
        self._parseKwargs(**kwargs)

    def __repr__(self):
        return str(self.fid) + ': ' + str(type(self).__name__)

    @property
    def hdr(self):
        return str(self) + ': '

    def clog(self, func, prop=False):
        sProp = 'property ' if prop else ''
        message = '%s %s() %swas called.' % (self.hdr, func, sProp)
        Log.debug(message)

    def _parseKwargs(self, **kwargs):
        result = self._parseBy(**kwargs)
        if result != True:
            print('Finder: Error: No valid selector provided.')
            print('User provided the following kwargs:\n  ', kwargs)
            sys.exit(1)

        result = self._parseIndex(**kwargs)
        if result != True:
            if result == -1:
                print('Finder: type of \"index\" must be int.')
                sys.exit(1)

    def _parseBy(self, **kwargs):
        bys=['class_name','css','id','link','name','partial_link','tag','xpath']
        for by in bys:
            try:
                self.key = kwargs[by]
            except KeyError:
                continue
            else:
                if by == 'class_name':
                    self.by = 'class name'
                elif by == 'css':
                    self.by = 'css selector'
                elif by == 'partial_link':
                    self.by = 'partial link text'
                elif by == 'link':
                    self.by = 'link text'
                elif by == 'tag':
                    self.by = 'tag name'
                else:
                    self.by = by
                return True

    def _parseIndex(self, **kwargs):
        try:
            self.index = kwargs['index']
        except KeyError:
            self.index = 0
        finally:
            if type(self.index) is int:
                return True
            else:
                return -1

    @property
    def fid(self):
        return (self.by, self.key)

    def find(self):
        self.clog('find')
        if self.index is None:
            return self.driver.find_element(self.by, self.key)
        else:
            return self.driver.find_elements(self.by, self.key)[self.index]
