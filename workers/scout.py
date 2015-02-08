import multiprocessing
from time import sleep
class Scout(multiprocessing.Process):
    def __init__(self, group, assignment, keywords, threshold, queue, start):
        super(Scout, self).__init__()
        
        self.group = group
        self.queue = queue
        self.start = start

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
        self.queue.put((self.group, self.messages))
        self.clear_messages()

    def search_file(self, filePath):
        with open(filePath, "r") as file:
            goodness = 0
            for line in file:
                for word in self.keywords:
                    goodness = goodness + line.count(word)
            self.send_message((self.get_index(), goodness > self.threshold))

            
    def get_index(self):
        return self.index + self.start

    def run(self, **args):
        self.traverse_assignment()
        
queue = multiprocessing.Queue()
scouts = []

scouts.append(Scout("Year 2038", ["../data/Year_2038_problem", "../data/Winterval"], ["Unix"], 0, queue, 0))
for scout in scouts:
    scout.run()

for scout in scouts:
    print queue.get()
