class Scout():
    def __init__(self, group, assignment):
        self.group = group
        self.index = 0
        self.assignment = assignment
        
    def search_file(self, filePath):
        fileHandler = open(filePath, "r")
        fileData = fileHandler.read()
        fileHandler.close()

    def get_index(self):
        return self.index

    def get_assignment(self):
        return self.assignment
