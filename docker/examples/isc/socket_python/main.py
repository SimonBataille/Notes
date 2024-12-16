from multiprocessing import Queue, Process
import time
msg_queue = Queue()

def emetteur(queue):
    for i in range(5):
        message = f'Message {i}'
        print('J\'envoie :', message)
        queue.put(message)
        time.sleep(1)

def recepteur(queue):
    while True:
        message = queue.get()
        print('Je recois :', message)
        if message == 'Message 4':
            break

if __name__ == '__main__':
    proc_emetteur = Process(target=emetteur, args=(msg_queue,))
    proc_recepteur = Process(target=recepteur, args=(msg_queue,))

    proc_emetteur.start()
    proc_recepteur.start()

    proc_emetteur.join()
    proc_recepteur.join()

    print('End of test')
