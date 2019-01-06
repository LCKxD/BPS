import socket
import threading
from queue import Queue



server = input("Enter a ip or website: ")
print("")
print("Scaning ports 1-25 on " + server)

print("________________________________________")

target= server

print_lock = threading.Lock()

def pscan (port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((target,port))
		with print_lock:
			print("Port " + str(port) + " is open")

		con.close()

	except:
		pass

def threader():
	while True:
		worker = q.get()
		pscan(worker)
		q.task_done()

q= Queue()

for x in range(30):
	 t = threading.Thread(target = threader)
	 t.daemon = True
	 t.start()


for worker in range(1,1000):
	q.put(worker)

q.join()
