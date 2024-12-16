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

# Fetch salle 101
salle_101 = session.query(Salle).filter_by(nom='Salle 101').first()
print('Lu :', salle_101.id, salle_101.nom)

# attribuer la salle 101 a tous les eleves
eleves = session.query(Eleve).all()
for eleve in eleves:
    eleve.salle = salle_101

# Fetch salle 101
eleve = session.query(Eleve).filter_by(salle=salle_101).all()
for eleve in eleves:
    print(eleve.prenom)


# Valider les changements
session.commit()
