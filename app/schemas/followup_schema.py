from pydantic import BaseModel
from typing import Optional, List
import datetime

class followupBase(BaseModel):
    id: Optional[int]

# on requete avec le nombre de jours/mois pour la durée voulu 
class followup(followupBase):
    months: Optional[int]
    days: Optional[int]

# pour le body pour l'ajout de nouvelle donnée d'imc par 
# l'utilisateur
class followup_imc(followupBase):
    id_user: int
    weight: int
    imc: int
    date: datetime.datetime
    day: Optional[int]
    month: Optional[int]
    year: Optional[int]
