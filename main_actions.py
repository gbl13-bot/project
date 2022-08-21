from circuit import Circuit


def main_menu() -> None:
    print("-" * 194)
    print("-" * 193)
    print("-" * 192)
    print("\t" * 22, "WELCOME TO CCC")
    print("-" * 192)
    print("-" * 193)
    print("-" * 194)

    print("\t" * 5 ,"Creating a new circuit")
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
        
            
def sub_menu():
    print("")
main_menu()


