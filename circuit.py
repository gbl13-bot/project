import math
from component import Component

class Circuit():

    def __init__(self, supply_voltage: float, name: str = "undefined"):
        self.tension = supply_voltage
        self.name = name
        self.is_icc_point = False
        self.component_list: list[Component] = []
        self.resistances_sum: float = 0 
        self.reactances_sum: float = 0 
        self.equivalent_impedance: float = 0
        self.icc: float = 0
        self.sub_circuits: list[Circuit] = []

# Adding new component
    def add_component(self, component, add=False, has_to_calcul_icc=False):
        self.component_list.append(component)
        if not component.is_default_point:
            self.reactances_sum += component.get_reactance()
            self.resistances_sum += component.get_resistance()
        self.calcul_equivalent_impedance()

        if add:
            self.add_sub_circuit()

    def add_components(self, components, add=False, has_to_calcul_icc=False):
        self.component_list = components
        for component in self.component_list:
            if not component.is_default_point:
                self.reactances_sum += component.get_reactance()
                self.resistances_sum += component.get_resistance()
        self.calcul_equivalent_impedance()

        if add:
            self.add_sub_circuit()
# Delete the component that has the id = `component_id`

    def delete_component(self, component_id: int):
        for component in self.component_list:
            if component.get_id() == component_id:
                self.component_list.remove(component)
            

    def get_component(self, component_id: int):
        for component in self.component_list:
            if component_id == component.get_id():
                return component

    def get_components(self):
        return self.component_list

    def add_sub_circuit(self):
        for component in self.component_list:
            if component.is_default_point or self.is_icc_point:
                self.sub_circuits.append(Circuit(self.tension))
                self.sub_circuits[-1].add_components(self.component_list)
                self.initialize_circuit()
                

    def calcul_equivalent_impedance(self) :
        self.equivalent_impedance = math.sqrt(math.pow(self.resistances_sum, 2) + math.pow(self.reactances_sum, 2))

    def calcul_icc(self):
       self.icc = self.tension / (math.sqrt(3) * self.get_equivalent_impedance())

    def get_icc(self):
        self.calcul_icc()
        return self.icc

    def get_equivalent_impedance(self):
        return self.equivalent_impedance

    def initialize_circuit(self):
        self.component_list = []
        self.reactances_sum = 0
        self.resistances_sum = 0
        self.equivalent_impedance = 0
