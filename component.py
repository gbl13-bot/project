class Component :

    def __init__(self, resistance, impedance, reactance, tension_alimentation):
        self.resistance = resistance
        self.reactance = reactance
        self.impedance = impedance
        self.tension = { "valeur": tension_alimentation[0], "unite": tension_alimentation[1]}
    