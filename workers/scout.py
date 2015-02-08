class Scout(multiprocessing.Process):
    def __init__(self, group, assignment, keywords, threshold):
        self.group = group
        self.index = 0
        self.assignment = assignment
        self.keywords = keywords
        self.messages = []
        self.threshold = threshold
    
    def send_message(self, message):
        self.messages.append(message) 
    
    def clear_messages(self):
        self.messages = []

    def run(self, **args):
        for target in assignment:
            self.search_file(target)    
            self.index += 1
        pass
        
    def search_file(self, filePath):
        with open(filePath, "r") as file:
            for line in file:
                goodness = 0
                for word in keywords:
                    goodness += line.count(word)
                if goodness > threshold:
                    self.send_message("is_good")

            
    def get_index(self):
        return self.index

    def get_assignment(self):
        return self.assignment
