import math
from circuit import Circuit
from circuit_breaker import CircuitBreaker
from liaison import Liaison
from powser_source import PowerSource
from transformateur import Transformateur

c1 = Circuit(20000)


reseau_amont = PowerSource([20000, 'V'], [500 * math.pow(10, 6), 'VA'])
liaison = Liaison('cuivre', 50, 2000, 'htb')
circuit_breaker = CircuitBreaker()
# transfo = Transformateur([400, 'V'], 15, [1000, 'KVA'], 3600)
# transfo2 = Transformateur([403, 'V'], 15, [1000, 'KVA'], 3600)

c1.add_component(reseau_amont, True)
c1.add_component(liaison, True)
c1.add_component(circuit_breaker, True)

# print(c1.get_equivalent_impedance())
# print(c1.get_icc())

