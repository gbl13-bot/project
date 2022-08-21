import math as M
import enum
from component import Component

class Tension (enum.Enum):
    low = 6000
    middle = 20000
    high = 150000

class ReseauAmont(Component):
    def __init__(self, supply_voltage, scc):
        Component.__init__(self, supply_voltage)
        self.scc = {"valeur": scc[0], "unite" : scc[1]}
    
    def get_impedance(self):
        self.impendance = M.pow(self.tension['valeur'], 2) / self.scc['valeur']
        return self.impendance

    def get_resistance(self):
        if self.tension['valeur'] == int(Tension.low.value):
            self.resistance = self.get_impedance() * 0.3
        elif self.tension['valeur'] == int(Tension.middle.value):
            self.resistance = self.get_impedance() * 0.2
        elif self.tension['valeur'] == int(Tension.high.value):
            self.resistance = self.get_impedance() * 0.1
        return self.resistance
            
    def get_reactance(self):
        self.reactance = self.get_impedance()* 0.980
        return self.reactance
