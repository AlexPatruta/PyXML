import xml.etree.ElementTree as ET
import datetime

class PyXML:
    """
    """

    def __init__(self, filePath = None):
        self.logs = {str(datetime.date.today()): str(datetime.datetime.now().time())}
        self.filePath = filePath

    def ParseTree(self, filePath = None):
        """
        """
        self.logs.update({"INFO": "Executing ParseTree()" + str(datetime.date.today())})
        if filePath:
            self.logs.update({"INFO": "Filepath OK"})
            try:
                self.logs.update({"INFO": "Trying to parse XML tree"})
                return ET.parse(filePath)
            except ex:
                self.logs.update({"EXCEPTION": str(ex)})
        else:
            self.logs.update({"ERROR": "Make sure the filepath is valid"})
    
    def UpdateLog(self, key, value):
        """
            Updates the log dictionary using the "update" method.
        """
        if key and value:
            self.logs.update({key: value})
        else:
            self.logs.update({"ERROR": "Invalid key or value."})

    def GetLog(self):
        """
            Returns the log dictionary
        """
        return self.logs
