
from enum import Enum, auto
from core.request import Headers


class Config:
    def __init__(self) -> None:
        self.__target  = None
        self.__threads = 1
        self.__headers = None
        self.__verbose = False

    def SetTarget(self, target):
        self.__target = target

    def GetTarget(self):
        return self.__target
    
    def SetThreads(self, threads):
        self.__threads = threads

    def GetThreads(self):
        return self.__threads

    def SetHeaders(self, headers: Headers):
        self.__headers = headers

    def GetHeaders(self):
        return self.__headers

    def enableVerbose(self):
        self.__verbose = True

    def isVerboseEnabled(self):
        return self.__verbose

class Format(Enum):
    Text    = auto()

class OutputConfig:

    def __init__(self) -> None:
        self.__filename   = None
        self.__format     = None
        self.__enable     = False

    def SetFileName(self, fileName):
        self.__filename = fileName

    def GetFileName(self):
        return self.__filename

    def SetFormat(self, format):
        self.__format = format

    def GetFormat(self):
        return self.__format

    def isEnable(self):
        return self.__enable

    def enableOutput(self):
        self.__enable = True

    def disableOutput(self):
        self.__enable = False


class Mode(Enum):
    Both    = auto()
    Scan    = auto()
    Recon   = auto()
    Crawl   = auto()

class RockMode:

    def __init__(self) -> None:
        self.__mode = None

    def SetModeToBoth(self):
        self.__mode = Mode.Both

    def SetModeToScan(self):
        self.__mode = Mode.Scan

    def SetModeToRecon(self):
        self.__mode = Mode.Recon

    def SetModeToCrawl(self):
        self.__mode = Mode.Crawl

    def GetMode(self):
        return self.__mode



