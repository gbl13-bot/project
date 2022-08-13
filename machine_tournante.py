import math as M
import enum
from component import Component

class Tension (enum.Enum):
    low = 6
    middle = 20
    high = 150

class MachineTounante(Component):

    def __init__(self, resistance, impedance, reactance, tension_alimentation, sn, x):
        Component.__init__(self, resistance, impedance, reactance, tension_alimentation)
        self.icc = 0
        self.x = x
        self.sn = {"valeur" :sn[0], "unite" :sn[1]}
    
    def get_impedance(self):
        return (self.x / 100) * (M.pow(self.tension['valeur'], 2) / self.sn['valeur'])
    
    def get_reactance(self):
        self.reactance = self.get_impedance()
        return self.reactance

    def get_resistance(self):
        if self.tension['valeur'] == int(Tension.low.value):
            self.resistance = self.get_impedance() * 0.3
        elif self.tension['valeur'] == int(Tension.middle.value):
            self.resistance = self.get_impedance() * 0.2
        else:
            self.resistance = self.get_impedance() * 0.1
        return self.resistance