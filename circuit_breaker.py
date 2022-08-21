
from component import Component


class CircuitBreaker(Component):

    def __init__(self) -> None:
        self.reactance: float = 0.15
        self.is_default_point: bool = True
