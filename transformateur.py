import math as M
from component import Component
import enum

class Tension (enum.Enum):
    low = 6
    middle = 20
    high = 150

class Transformateur(Component):
    def __init__(self, supply_voltage, ucc, sn, perte_joule):
        Component.__init__(self, supply_voltage)
        self.ucc = ucc
        self.perte_joule = perte_joule
        self.sn = {"valeur" :sn[0], "unite" :sn[1]}

    
    def intensite_nominal(self):
        return self.sn['valeur'] / (self.tension['valeur'] * M.sqrt(3))

    def get_impedance(self):
        return (self.ucc / 100) * (M.pow(self.tension['valeur'], 2) / self.sn['valeur'])
    
    def get_resistance(self):
        print()
        if self.tension['valeur'] == int(Tension.low.value):
            self.resistance = self.get_impedance() * 0.3
        elif self.tension['valeur'] == int(Tension.middle.value):
            self.resistance = self.get_impedance() * 0.2
        elif self.perte_joule != 0:
            self.resistance = self.perte_joule / (3* self.intensite_nominal())
        else:
            self.resistance = self.get_impedance() * 0.1
        return self.resistance

    def get_reactance(self):
        return self.get_impedance()
