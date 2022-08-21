"""This module containes funciton that provide interraction with the user ! """

from circuit import Circuit


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
        
            
def sub_menu() -> None:
    print("ADDING COMPONENT TO THE CIRCUIT")
    component_choice = input("1 -> POWERSOURCE \t 2 -> TRANSFORMER \n 3 -> ROTING MACHINE 4 -> LIAISON \t 5 -> CIRCUIT BREAKER")

main_menu()
