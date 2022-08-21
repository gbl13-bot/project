"""This module containes funciton that provide interraction with the user ! """

from circuit import Circuit
from circuit_breaker import CircuitBreaker
from liaison import Liaison
from powser_source import PowerSource
from roting_machine import MachineTounante
from transformateur import Transformateur


def main_menu() -> None:
    """The main menu function"""

    print("-" * 194)
    print("-" * 193)
    print("-" * 192)
    print("\t" * 22, "WELCOME TO CCC")
    print("-" * 192)
    print("-" * 193)
    print("-" * 194)

    print("\t" * 5 ,"CREATING A NEW CIRCUIT")
    circuit_name = input("Enter the name of the circuit: ")
    while True:
        while True:
            electric_voltage = input("Enter electrical voltage: ")
            try:
                electric_voltage = float(electric_voltage)
                circuit = Circuit(electric_voltage, circuit_name)
                break
            except ValueError:
                print("Please, enter a valid number")
        
            
def sub_menu(circuit: Circuit) -> None:
    print("ADDING COMPONENT TO THE CIRCUIT")
    while True:
        component_choice = input("1 -> POWERSOURCE \t 2 -> TRANSFORMER \n 3 -> ROTING MACHINE 4 -> LIAISON \t 5 -> CIRCUIT BREAKER")
        try:
            component_choice = int(component_choice)
            choose_component(component_choice, circuit)
        except ValueError:
            print("Please, enter a valid number")
            

def choose_component(choice: int, circuit: Circuit) -> None:
    scc = [input("Enter scc value: "), input("Choose the mesuring unit: ")]

    try:
        choice = int(choice)
        try:
            mesuring_unit = {"p" : ["VA", "KVA"]}
            scc = float(scc[0]) and scc[1] in mesuring_unit["p"][0]
        except ValueError:
            print("Enter a valid value !")

        if choice == 1:
            try:
                power_source1 = PowerSource(circuit.supply_voltage, scc)

            except ValueError:
                print("Please, enter a valid number")

        elif choice == 2:
            ucc = input("Enter ucc: ")
            sn = [input("Enter sn value: "), input("Choose the mesuring unit: ")] 
            try:
                ucc = float(ucc)
                sn = int(sn[0])
                transformer = Transformateur(circuit.supply_voltage, ucc, sn)
            except ValueError:
                print("Please, enter a valid number")

        elif choice == 3:
            sn = [input("Enter sn value: "), input("Choose the mesuring unit: ")] 
            x = input("Enter x: ")

            try:
                x = int(x)
                sn = int(sn[0])
                roting_machine = MachineTounante(circuit.supply_voltage, sn, x)
            except:
                print("Please, enter a valid number")

        elif choice == 4:
            resistivite = input("Enter resistivite: ")
            section_de_conduc = input("Enter conductor section cable value: ")
            length = input("Enter length: ")
            reactance_mode = input("Enter reactance mode [bt/hta/htb]: ")

            try:
                section_de_conduc = int(section_de_conduc)
                length = int(length)
                liaison = Liaison(resistivite, section_de_conduc, length, reactance_mode)
            except ValueError:
                print("Please, enter a valid number")
        else:
            circuit_breaker = CircuitBreaker()
    except ValueError:
        print("Please, enter a valid number")


            
    
main_menu()
