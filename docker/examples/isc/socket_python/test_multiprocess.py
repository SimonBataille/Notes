from multiprocessing import Queue, Process
import time

def emetteur(queue):
    """
    Envoie des messages dans la file d'attente.
    """
    for i in range(5):
        message = f'Message {i}'
        print('J\'envoie :', message)
        queue.put(message)
        time.sleep(1)
    queue.put('FIN')  # Signale au récepteur que l'émission est terminée

def recepteur(queue):
    """
    Reçoit et affiche les messages de la file d'attente.
    """
    while True:
        message = queue.get()
        print('Je reçois :', message)
        if message == 'FIN':  # Quitte la boucle à la réception de 'FIN'
            break

if __name__ == '__main__':
    # Créer la file de messages
    msg_queue = Queue()

    # Démarrer les processus
    proc_emetteur = Process(target=emetteur, args=(msg_queue,))
    proc_recepteur = Process(target=recepteur, args=(msg_queue,))

    proc_emetteur.start()
    proc_recepteur.start()

    # Attendre la fin des processus
    proc_emetteur.join()
    proc_recepteur.join()

    print('Fin du test')
