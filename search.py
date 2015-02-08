from os import listdir

empty = None

class WorkerController():
	def __init__(self):
		self.workers = []

	def read_worker_messages(self):
		worker_messages = {}
		for worker in self.workers:
			if worker_messages[worker.group] is empty:
				worker_messages[worker.group] = []
			worker_messages[worker.group].append(worker.messages)
			worker.clear_essage

		return worker_messages


	def get_document_list(self, documentPath):
		documents = listdir(documentPath)
		num_docs = len(documents)
		worker_loads = [documents[i:i+3] for i in range(0,len(documents),3)]
		return worker_loads

search_worker_controller = WorkerController()

worker_loads = search_worker_controller.get_document_list("data/")

print(worker_loads)

