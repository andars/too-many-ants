class Scout():
    def __init__(self, group, target):
        self.group = group
        self.target = target

    def getFileData(self, filePath):
        fileHandler = open(filePath, "r")
        fileData = fileHandler.read()
        fileHandler.close()
        return fileData