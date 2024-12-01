import pygame
from pygame import *

import random
import numpy as np


LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

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
    onde = (onde * volume * 32767).astype(np.int16)  # Normaliser pour -32768 à 32767
    buffer = np.zeros(len(onde) * 2, dtype=np.int16)  # Ajouter un canal si nécessaire (mono)
    buffer[0::2] = onde  # Canal gauche
    buffer[1::2] = onde  # Canal droit
    sound = pygame.mixer.Sound(buffer)
    return sound

# Générer quelques sons
son1 = generer_son(440, 0.5)  # La 440 Hz, 1 seconde
son2 = generer_son(880, 0.5)  # La octavié, 0.5 seconde

# class vaisseau
class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_key):
        dx, dy = 0, 0  # Initialiser les déplacements

        if pressed_key[K_UP]:
            dy = -5
        if pressed_key[K_DOWN]:
            dy = 5
        if pressed_key[K_LEFT]:
            dx = -5
        if pressed_key[K_RIGHT]:
            dx = 5

        # Appliquer les déplacements
        self.rect = self.rect.move(dx, dy)

        # Gérer les limites de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN

        # Créer un missile lorsqu'on appuie sur la barre espace
        if pressed_key[K_SPACE]:
            if len(le_missile.sprites()) < 1:	
                missile = Missile(self.rect.center)
                tous_sprites.add(missile)
                le_missile.add(missile)
                    

# class missile
class Missile(pygame.sprite.Sprite):
    def __init__(self, center_missile):
        super(Missile, self).__init__()
        self.surf = pygame.Surface((25, 12))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=center_missile)
        son1.play()

    def update(self):
        # Déplacer le missile à droite
        self.rect.move_ip(15, 0)

        # Supprimer le missile si il sort de l'écran
        if self.rect.left > LARGEUR_ECRAN:
            self.kill()
      
            
# class ennemi
class Ennemi(pygame.sprite.Sprite):
    def __init__(self):
        super(Ennemi, self).__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 0, 0))
        # Les ennemis apparaissent à droite de l'écran à une hauteur aléatoire
        self.rect = self.surf.get_rect(
            center=(
                LARGEUR_ECRAN + 50,
                random.randint(0, HAUTEUR_ECRAN)
                )
        )
        # Chaque ennemi a une vitesse aléatoire (en pixel)
        self.speed = random.randint(5, 20)

    def update(self):
        # Déplacer l'ennemi vers la gauche
        self.rect.move_ip(-self.speed, 0)

        # Supprimer l'ennemi si il sort de l'écran
        if self.rect.right < 0:
            self.kill()


# class explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_vaisseau):
        super(Explosion, self).__init__()
        self.surf = pygame.Surface((75, 50))
        # explosion pendant 10 cycles
        self.compteur = 10
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=center_vaisseau)
        son2.play()
        
    def update(self):
        self.compteur = self.compteur - 1
        if self.compteur == 0:
            self.kill()


# class étoiles
class Etoile(pygame.sprite.Sprite):
    def __init__(self):
        super(Etoile, self).__init__()
        self.surf = pygame.Surface((15, 5))
        self.surf.fill((255, 255, 0))
        # Les Etoiles apparaissent à droite de l'écran à une hauteur aléatoire
        self.rect = self.surf.get_rect(
            center=(
                LARGEUR_ECRAN + 20,
                random.randint(0, HAUTEUR_ECRAN)
                )
        )
        # Chaque Etoile a une vitesse aléatoire (en pixel)
        self.speed = random.randint(5, 20)

    def update(self):
        # Déplacer l'Etoile vers la gauche
        self.rect.move_ip(-self.speed, 0)

        # Supprimer l'Etoile si il sort de l'écran
        if self.rect.right < 0:
            self.kill()
            

# Classe score
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self._scoreCourant = 0
        self._setText()
        
    def _setText(self):
        self.surf = police_score.render('Socre : ' + str(self._scoreCourant), False, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(LARGEUR_ECRAN/2, 15))
    
    def update(self):
        self._setText()
        
    def incremente(self, valeur):
        self._scoreCourant = self._scoreCourant + valeur

# init library
pygame.init()

# title
pygame.display.set_caption("The shoot'em up 1.0")

# surface principale
ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])

# police
pygame.font.init()
police_score = pygame.font.SysFont('Comic Sans Ms', 30)

# mixer
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2048)

# clock
clock = pygame.time.Clock()

# Ajouter les ennemis et les Etoiles
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 500)

ADD_STAR = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_STAR, 100)

# Sprite Group
tous_sprites = pygame.sprite.Group()
le_missile = pygame.sprite.Group()
les_ennemis = pygame.sprite.Group()
les_explosions = pygame.sprite.Group()
les_etoiles = pygame.sprite.Group()

# create vaisseau
vaisseau = Vaisseau()
tous_sprites.add(vaisseau)
score = Score()
tous_sprites.add(score)

# main loop
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == ADD_ENEMY:
            nouvel_ennemi = Ennemi()
            les_ennemis.add(nouvel_ennemi)
            tous_sprites.add(nouvel_ennemi)
        elif event.type == ADD_STAR:
            nouvelle_etoile = Etoile()
            les_etoiles.add(nouvelle_etoile)
            tous_sprites.add(nouvelle_etoile)
        

    # screen
    ecran.fill((0, 0, 0))
    
    # Détection des collisions
    if pygame.sprite.spritecollideany(vaisseau, les_ennemis):
        vaisseau.kill()
        explosion = Explosion(vaisseau.rect.center)
        les_explosions.add(explosion)
        tous_sprites.add(explosion)
        continuer = False
    
    for missile in le_missile:
        liste_ennemis_touches = pygame.sprite.spritecollide(missile, les_ennemis, True)
        if len(liste_ennemis_touches) > 0:
            missile.kill()
            score.incremente(len(liste_ennemis_touches))
        for ennemi in liste_ennemis_touches:
            explosion = Explosion(ennemi.rect.center)
            les_explosions.add(explosion)
            tous_sprites.add(explosion)

    # pressed key (déplacé en dehors de la boucle des événements)
    touche_appuyee = pygame.key.get_pressed()

    # Mise à jour du vaisseau avec l'argument touche_appuyee
    vaisseau.update(touche_appuyee)
    
    # Mise à jour du groupe du missile
    le_missile.update()
    
    # Mise à jour du groupe des ennemis
    les_ennemis.update()
    
    # Mise à jour du groupe des explosions
    les_explosions.update()
    
    # Mise à jour du groupe des etoiles
    les_etoiles.update()
    
    # Mise à jour du groupe du score    
    score.update()

    # Blit tous_sprite
    for mon_sprite in tous_sprites:
        ecran.blit(mon_sprite.surf, mon_sprite.rect)

    # update display
    pygame.display.flip()

    # slow down loop
    clock.tick(30)

pygame.time.delay(3000)
pygame.quit()
