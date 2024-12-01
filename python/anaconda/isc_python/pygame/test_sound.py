import pygame
import numpy as np

# Initialiser pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2048)

def generer_son(frequence, duree, volume=0.5, sample_rate=44100):
    """
    Génère un tableau numpy représentant une onde sinusoïdale.
    Args:
        frequence (float): fréquence en Hz
        duree (float): durée en secondes
        volume (float): amplitude du son (0.0 à 1.0)
        sample_rate (int): fréquence d'échantillonnage en Hz
    Returns:
        pygame.mixer.Sound : Son généré
    """
    t = np.linspace(0, duree, int(sample_rate * duree), False)  # Tableau de temps
    # ~ onde = np.sin(2 * np.pi * frequence * t)  # Générer une onde sinusoïdale
    onde = np.sign(np.sin(2 * np.pi * frequence * t))  # Onde carrée
    # ~ onde = 2 * (t * frequence % 1) - 1  # Dent de scie
    # ~ onde = np.random.uniform(-1, 1, t.shape)  # Bruit blanc
    onde = (onde * volume * 32767).astype(np.int16)  # Normaliser pour -32768 à 32767
    buffer = np.zeros(len(onde) * 2, dtype=np.int16)  # Ajouter un canal si nécessaire (mono)
    buffer[0::2] = onde  # Canal gauche
    buffer[1::2] = onde  # Canal droit
    sound = pygame.mixer.Sound(buffer)
    return sound

# Générer quelques sons
son1 = generer_son(440, 1.0)  # La 440 Hz, 1 seconde
son2 = generer_son(880, 0.5)  # La octavié, 0.5 seconde

# Boucle principale pour jouer les sons
continuer = True
pygame.init()
ecran = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Synthèse sonore avec pygame")

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                son1.play()  # Jouer le son 1
            elif event.key == pygame.K_s:
                son2.play()  # Jouer le son 2

pygame.quit()


'''
Changement de forme d'onde : Remplace np.sin() par d'autres formes d'onde comme un carré, une dent de scie ou du bruit blanc :
onde = np.sign(np.sin(2 * np.pi * frequence * t))  # Onde carrée
onde = 2 * (t * frequence % 1) - 1  # Dent de scie
onde = np.random.uniform(-1, 1, t.shape)  # Bruit blanc


Enchaînement des sons : Combine plusieurs sons pour créer des effets ou des mélodies.

Polyphonie : Charge plusieurs sons avec pygame.mixer.Sound et jouez-les en parallèle.
'''

'''
Explications :

    numpy pour générer une forme d'onde :
        np.sin() génère une sinusoïde à la fréquence spécifiée.
        Les amplitudes sont normalisées dans la plage des valeurs audio pour pygame.mixer (int16 entre -32768 et 32767).

    pygame.mixer.Sound à partir d'un tableau mémoire :
        Le tableau est converti en un buffer compatible avec pygame.mixer.Sound.

    Mixer : pygame.mixer joue le son en utilisant les réglages initiaux (fréquence d'échantillonnage, taille des échantillons, etc.).
'''
