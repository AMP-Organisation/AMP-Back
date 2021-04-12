from pydantic import BaseModel
from typing import Optional, List

# rappel
# le schema correspond au format des données qu'on reçoit
# en requete sur l'api

class medicine(BaseModel):
    id: Optional[int]


# a specific schema for patch a disease
class medicinePatch(disease):
    name: Optional[str]
    name: Optional[str]
    dose: Optional[int]
    dose_max: Optional[int]
    # description: Optional[str]
    # is_vaccine: Optional[bool]
    # is_treatment: Optional[bool]
    # danger_level: Optional[int]


class baseMedicine(medicine):
    name: str
    dose: int
    dose_max: int

