from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Définir la base déclarative
Base = declarative_base()

# Définir la classe Eleve
class Eleve(Base):
    __tablename__ = 'eleves'  # Nom de la table

    id = Column(Integer, primary_key=True)  # Colonne pour l'ID
    prenom = Column(String, nullable=False)  # Colonne pour le prénom
    age = Column(Integer, nullable=False)  # Colonne pour l'âge
    salle_id = Column(Integer, ForeignKey('salles.id'), nullable=True)  # Clé étrangère vers 'salles.id'

    salle = relationship('Salle', back_populates='eleves')  # Relation avec la classe Salle

# Définir la classe Salle
class Salle(Base):
    __tablename__ = 'salles'  # Nom de la table

    id = Column(Integer, primary_key=True)  # Colonne pour l'ID
    nom = Column(String, nullable=False)  # Colonne pour le nom

    eleves = relationship('Eleve', back_populates='salle')  # Relation avec la classe Eleve

# Informations de connexion à la base de données
username = 'myuser'
password = 'mypassword'
host = 'localhost'
port = 5432
database = 'mydatabase'

# URL de connexion à PostgreSQL
DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Créer le moteur de base de données
engine = create_engine(DATABASE_URL)

# Créer les tables dans la base de données
Base.metadata.create_all(engine)

# Créer une session
Session = sessionmaker(bind=engine)
session = Session()

# Ajouter des salles
salle1 = Salle(nom='Salle 101')
salle2 = Salle(nom='Salle 102')
session.add_all([salle1, salle2])

# Valider les changements
session.commit()

# Ajouter des élèves avec une salle associée
session.add(Eleve(prenom='John', age=35, salle=salle1))
session.add(Eleve(prenom='Bill', age=45, salle=salle1))
session.add(Eleve(prenom='Keith', age=55, salle=salle2))

# Valider les changements
session.commit()
