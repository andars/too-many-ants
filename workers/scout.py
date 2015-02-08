class Scout(multiprocessing.Process):
    def __init__(self, group, assignment, keywords, threshold, queue):
        super(Scout, self).__init__()
        
        self.group = group
        self.queue = queue

        self.index = 0
        self.assignment = assignment
        self.keywords = keywords
        self.messages = []
        self.threshold = threshold
    
    def send_message(self, message):
        self.messages.append(message) 
    
    def clear_messages(self):
        self.messages = []

    def traverse_assignment(self):
        for target_document in self.assignment:
            self.search_file(target_document)    
            self.index += 1

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

    def run(self, **args):
        self.queue.put(self.messages)
        