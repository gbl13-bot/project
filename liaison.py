import enum
from component import Component

class LiaisonResistivite(enum.Enum):
    CUIVRE = 0.01851
    ALUMINIUM = 0.02941

class ModeDePoseCable(enum.Enum):
    CABLE_TRIPHASE = 0.13
    CABLE_UNI_POLAIRE = 0.09
    CABLE_UNI_ESPACE = 0.13

class ModeDePoseBarre(enum.Enum):
    CABLE_TRIPHASE = 0.08
    CABLE_UNI_POLAIRE = 0.09
    CABLE_UNI_ESPACE = 0.15

class LineDeDistrib(enum.Enum):
    BAS = 0.3
    HAUTE_A = 0.3
    HAUTE_B = 0.4

class Liaison():

    def __init__(self, resistance, resistivite, reactance, section_des_conduc, mode_de_pose, type_de_reseau, longeur):
        self.resistance = resistance
        self.reactance = reactance
        self.section_des_conduc = section_des_conduc
        self.mode_de_pose = {'valeur' : mode_de_pose[0], 'name': mode_de_pose[1]}
        self.type_de_reseau = {'valeur' : type_de_reseau[0], 'name': type_de_reseau[1]}
        self.longueur = longeur

        if (resistivite == 'cuivre'):
            self.resistivite = LiaisonResistivite.CUIVRE
        else:
            self.resistivite = LiaisonResistivite.ALUMINIUM

    def get_resistance(self):
        self.resistance = float(self.resistivite.value) * (self.longueur / self.section_des_conduc)
        return self.resistance

    def get_reactance(self):
        if self.mode_de_pose['valeur']:
            if self.mode_de_pose['name'] == 'triphase':
                self.reactance = float(ModeDePose.CABLE_TRIPHASE.value) * self.longueur
            elif self.mode_de_pose['name'] == 'polaire':
                self.reactance = float(ModeDePose.CABLE_UNI_POLAIRE.value) * self.longueur
            else:
                self.reactance = float(ModeDePose.CABLE_UNI_ESPACE.value) * self.longueur

        elif self.type_de_reseau['valeur']:
            print(self.type_de_reseau['name'])
            if self.type_de_reseau['name'] == "bt":
                self.reactance = float(LineDeDistrib.BAS.value) * (self.longueur / 1000)
            elif self.type_de_reseau['name'] == "hta":
                self.reactance = float(LineDeDistrib.HAUTE_A.value) * (self.longueur / 1000)
            elif self.type_de_reseau['name'] == "htb":
                self.reactance = float(LineDeDistrib.HAUTE_B.value) * (self.longueur / 1000)
        return self.reactance