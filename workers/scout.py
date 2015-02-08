class Scout():
    def __init__(self, group, target):
        self.group = group
        self.target = target

    def searchFile(self, filePath):
        fileHandler = open(filePath, "r")
        fileData = fileHandler.read()
        fileHandler.close()