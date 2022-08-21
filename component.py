class Component :
    ids: list[int] = []

    def __init__(self, supply_voltage):
        self.resistance: float = 0
        self.is_default_point: bool = False
        self.reactance: float = 0
        self.impedance: float = 0
        self.tension: dict = {"valeur": supply_voltage[0], "unite": supply_voltage[1]}
        self.id: int = self._set_id()

    def _set_id(self):
        self.id = 0
        if len(Component.ids):
            for _ in range(len(Component.ids)):
                    self.id += 1
        Component.ids.append(self.id)
        return self.id

    def get_id(self):
        return self.id
