import json

def load_ships():
    with open('ships.json') as file:
        data = json.load(file)
    return data['ships']

def main_menu():
    print("=== Starchives ===")
    print("1. Browse Ships by Manufacturer")
    print("2. Show All Ships")
    print("3. Exit")

def manufacturer_selection(ships):
    manufacturers = sorted(set(ship['manufacturer'] for ship in ships))
    print("\n=== Manufacturers ===")
    for index, manufacturer in enumerate(manufacturers, start=1):
        print(f"{index}. {manufacturer}")

    manufacturer_choice = input("Select a manufacturer (or 'q' to go back to the main menu): ")
    if manufacturer_choice == 'q':
        return None

    try:
        manufacturer_index = int(manufacturer_choice)
        if manufacturer_index < 1 or manufacturer_index > len(manufacturers):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid manufacturer number.")
        return manufacturer_selection(ships)

    selected_manufacturer = manufacturers[manufacturer_index - 1]
    filtered_ships = [ship for ship in ships if ship['manufacturer'] == selected_manufacturer]
    filtered_ships = sorted(filtered_ships, key=lambda ship: ship['ship_name'])
    show_ships(filtered_ships)

def show_ships(ships):
    print("\n=== Ships ===")
    for index, ship in enumerate(ships, start=1):
        print(f"{index}. {ship['ship_name']} - {ship['manufacturer']}")

    ship_choice = input("Select a ship number to view more details (or 'q' to go back to the main menu): ")
    if ship_choice == 'q':
        return None

    try:
        ship_index = int(ship_choice)
        if ship_index < 1 or ship_index > len(ships):
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid ship number.")
        return show_ships(ships)

    selected_ship = ships[ship_index - 1]
    print("\n=== Ship Details ===")
    print(f"Name: {selected_ship['ship_name']}")
    print(f"Manufacturer: {selected_ship['manufacturer']}")
    print(f"Role: {selected_ship['role']}")

def main():
    ships = load_ships()
    ships = sorted(ships, key=lambda ship: (ship['manufacturer'], ship['ship_name']))

    while True:
        main_menu()
        choice = input("Select an option: ")

        if choice == '1':
            manufacturer_selection(ships)
        elif choice == '2':
            show_ships(ships)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid menu number.")

if __name__ == '__main__':
    main()

