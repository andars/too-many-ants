from os import listdir
from multiprocessing import Queue

empty = None
from workers.scout import Scout

class ScoutController():
    def __init__(self):
        self.scouts = []
        self.scout_message_queue = Queue()

    def execute(self, terms):
        assignments = self.get_document_list("data/")
        print(assignments)
        for assignment in assignments:
            self.scouts.append(Scout("", assignment[0], terms, 0, self.scout_message_queue, assignment[1])) 

        for scout in self.scouts:
            scout.run()

        for scout in self.scouts:
            print(self.scout_message_queue.get())

    def read_scout_messages(self):
        scout_messages = {}
        for scout in self.scouts:
            scout_message = self.scout_message_queue.get()
            

        return scout_messages


    def get_document_list(self, documentPath):
        documents = listdir(documentPath)
        num_docs = len(documents)
        scout_loads = [(documents[i:i+3],i) for i in range(0,len(documents),3)]
        return scout_loads

search_scout_controller = ScoutController()

scout_loads = search_scout_controller.get_document_list("data/")

print(scout_loads)

search_scout_controller.execute("Wowoverymuch")

