import enum
from component import Component

class ResistiviteValueCoursCircuitMax(enum.Enum):
    CUIVRE = 0.01851
    ALUMINIUM = 0.02941

class ResistiviteValueCoursCircuitMin(enum.Enum):
    CUIVRE = 0.023
    ALUMINIUM = 0.037

class ModeDePoseCable(enum.Enum):
    CABLE_TRIPHASE = 0.08
    CABLE_UNI_POLAIRE = 0.09
    CABLE_UNI_ESPACE = 0.15

class ModeDePoseBarre(enum.Enum):
    JEU_DE_BARRE = 0.15

class LineDeDistrib(enum.Enum):
    BAS = 0.3
    HAUTE_A = 0.3
    HAUTE_B = 0.4



class Liaison():

    def __init__(self, resistivite, section_des_conduc, longeur, reactance_mode=""):
        self.resistance = 0
        self.reactance = 0
        self.is_default_point = False
        self.section_des_conduc = section_des_conduc

        self.reactance_mode = reactance_mode
        self.longueur = longeur

        if (resistivite == 'cuivre'):
            self.resistivite = ResistiviteValueCoursCircuitMax.CUIVRE
        else:
            self.resistivite = ResistiviteValueCoursCircuitMax.ALUMINIUM

    def get_resistance(self):
        self.resistance = float(self.resistivite.value) * (self.longueur / self.section_des_conduc)
        return self.resistance

    def get_reactance(self):
        if self.reactance_mode:
            if self.reactance_mode == 'triphase':
                self.reactance = float(ModeDePoseCable.CABLE_TRIPHASE.value) * (self.longueur / 1000)
            elif self.reactance_mode == 'polaire':
                self.reactance = float(ModeDePoseCable.CABLE_UNI_POLAIRE.value) * (self.longueur / 1000)
            elif self.reactance_mode == 'espace':
                self.reactance = float(ModeDePoseCable.CABLE_UNI_ESPACE.value) * (self.longueur / 1000)
            elif self.reactance_mode == "bt":
                self.reactance = float(LineDeDistrib.BAS.value) * (self.longueur / 1000)
            elif self.reactance_mode == "hta":
                self.reactance = float(LineDeDistrib.HAUTE_A.value) * (self.longueur / 1000)
            else :
                self.reactance = float(LineDeDistrib.HAUTE_B.value) * (self.longueur / 1000)
        return self.reactance
