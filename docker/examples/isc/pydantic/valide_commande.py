from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date

class Produit(BaseModel):
    nom: str
    prix: float

class Commande(BaseModel):
    client: str
    produits: List[Produit] = Field(..., min_length=1)
    date_livraison: Optional[date]
    prix_total: float = Field(default=0.0)

    @field_validator('date_livraison')
    def check_date(value):
        if value and value < date.today():
            raise ValueError('La date de livraison doit etre dans le futur !')
        return value
    
    @field_validator('produits')
    def check_montant(produits):
        total = sum(produit.prix for produit in produits)
        if total > 1000:
            raise ValueError('Le total ne doit pas depasser 1000 euros !')
        return produits

try:
    commande = Commande(
        client='Bill',
        produits=[
            Produit(nom='Unite Centrale', prix=750),
            Produit(nom='Ecran', prix=300),
        ],
        date_livraison=date(2025, 1, 1)
    )
    print('Commande :', commande)
except ValueError as e:
    print('Erreur', e)
