import os, sys

'''
Load configuration settings as needed. On first load, cache the results for
later reuse.
'''
class Config (object):
    cache = {}
    # Default config directory
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    #print('Config: estimated path:', dir_path)
    dir = os.path.join(dir_path, '..', 'config')

    @staticmethod
    def showCache():
        print('Config.cache: (key: value): {')
        for key in Config.cache:
            print('(%s : %s)' % (key, Config.cache[key]))
        print(')')

    @staticmethod
    def setDir(path):
        Config.dir = path
        Config._loadAll()

    @staticmethod
    def load(fpath):
        Config._loadOne(fpath)

    @staticmethod
    def get(key):
        try:
            value = Config.cache[key]
        except (TypeError, KeyError):
            value = None
        finally:
            return value

    @staticmethod
    def set(**kwargs):
        for key in kwargs:
            value = kwargs[key]
            Config.cache[key] = value

    @staticmethod
    def _loadAll():
        configFiles = Config._getConfigFiles()
        for fpath in configFiles:
            Config._loadOne(fpath)

    @staticmethod
    def _getConfigFiles():
        configFiles = []
        for fname in os.listdir(Config.dir):
            if fname[-4:] == '.cfg':
                configFiles.append(os.path.join(Config.dir, fname))
        return configFiles


    @staticmethod
    def _loadOne(fpath):
        with open(fpath, 'r') as configFile:
            for line in configFile:
                if '=' in line:
                    pair = line.split('=')
                    key = pair[0]
                    value = pair[1].split('\n')[0]
                    #print('Config: Config.cache[%s]=%s' % (key, value))
                    Config.cache[key] = value


Config._loadAll()
