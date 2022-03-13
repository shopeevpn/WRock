
from core.config.base import OutputConfig


class Report:
    def __init__(self, config: OutputConfig) -> None:
        self.config = config
        self.fileName = self.config.GetFileName()
        self.report = self._get_report()

    def write(self, data):
        self.report.write(data)

    def _get_report(self):
        pass

    def save(self):
        self.report.save()

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace_back):
        self.save()

class Output:

    def __init__(self, fileName) -> None:
        self.fileName = fileName
        self.file = open(self.fileName, 'w+')

    def write(self, data, newline = True) -> None:
        pass

    def save(self):
        self.file.write(self.data)
        self.file.close()

    def repeated_data(self, data) -> bool:
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace_back):
        self.save()

        
class TxtOutput(Output):

    def __init__(self, fileName):
        self.data = str()
        Output.__init__(self, fileName)

    def write(self, data, newline = True):
        self.data += data
        if newline : self.data += "\n"

    def repeated_data(self, data):
        return (data in open(self.fileName, 'r').read() or data in self.data)


