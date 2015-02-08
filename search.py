from os import listdir
from multiprocessing import Queue

empty = None

class WorkerController():
    def __init__(self):
        self.workers = []
        self.worker_message_queue = Queue()

    def read_worker_messages(self):
        worker_messages = {}
        for worker in self.workers:
            worker_message = self.worker_message_queue.get()
            

        return worker_messages


    def get_document_list(self, documentPath):
        documents = listdir(documentPath)
        num_docs = len(documents)
        worker_loads = [documents[i:i+3] for i in range(0,len(documents),3)]
        return worker_loads

search_worker_controller = WorkerController()

worker_loads = search_worker_controller.get_document_list("data/")

print(worker_loads)

