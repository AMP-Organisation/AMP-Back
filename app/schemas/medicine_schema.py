from pydantic import BaseModel
from typing import Optional, List

# rappel
# le schema correspond au format des données qu'on reçoit
# en requete sur l'api

class medicine(BaseModel):
    id: Optional[int]


# a specific schema for patch a medicine
class medicinePatch(medicine):
    name: Optional[str]
    dose: Optional[int]
    dose_max: Optional[int]
    description: Optional[str]
    delay: Optional[int]
    # is_vaccine: Optional[bool]
    # is_treatment: Optional[bool]
    # danger_level: Optional[int]

class medicinePost(medicine):
    name: str
    description: Optional[str]
    dose: int
    dose_max: int
    list_type: List[int]
    delay: int
    # il y aura d'autre champs texte a mettre, ou au moins en optionnel

class baseMedicine(medicine):
    name: str
    dose: int
    dose_max: int

