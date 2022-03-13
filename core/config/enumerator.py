
from urllib.parse import urlparse
from core.config.base import Config

class EnumeratationConfig(Config):

    def __init__(self) -> None:
        self.__recursive          = False
        self.__timeout            = 30
        self.__sources            = None
        Config.__init__(self)

    
    def SetTarget(self, target):
        if target.startswith('http'):
            target = urlparse(target).hostname

        Config.SetTarget(self, target)
    
    def SetTimeout(self, timeout):
        self.__timeout = timeout

    def GetTimeout(self):
        return self.__timeout

    def enableRecursive(self):
        self.__recursive = True

    def isRecursiveEnabled(self):
        return self.__recursive

    def SetSources(self, sources):
        self.__sources = sources

    def GetSources(self):
        return self.__sources


class List3rConfig(EnumeratationConfig):

    def __init__(self) -> None:
        EnumeratationConfig.__init__(self)


class FinderConfig(EnumeratationConfig):

    def __init__(self) -> None:
        self.__apis                 = None
        self.__maxEnumerationTime   = 10
        EnumeratationConfig.__init__(self)

    def SetAPIs(self, apis: dict):
        self.__apis = apis

    def GetAPIs(self):
        return self.__apis

    def SetMaxEnumerationTime(self, maxEnumerationTime):
        self.__maxEnumerationTime = maxEnumerationTime

    def GetMaxEnumerationTime(self):
        return self.__maxEnumerationTime


class ReverseIPConfig(EnumeratationConfig):
    
    def __init__(self) -> None:
        EnumeratationConfig.__init__(self)


class EnumeratorConfig(EnumeratationConfig):

    def __init__(self) -> None:
        self.__list3r     = None
        self.__finder     = None
        self.__reverseIP  = None 
        EnumeratationConfig.__init__(self)

    def SetList3rConfig(self, list3r: List3rConfig):
        self.__list3r = list3r

    def GetList3rConfig(self):
        return self.__list3r

    def SetFinderConfig(self, finder: FinderConfig):
        self.__finder = finder

    def GetFinderConfig(self):
        return self.__finder

    def SetReverseIPConfig(self, reverseIP: ReverseIPConfig):
        self.__reverseIP = reverseIP

    def GetReverseIPConfig(self):
        return self.__reverseIP


    