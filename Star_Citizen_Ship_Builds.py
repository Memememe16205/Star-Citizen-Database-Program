class Ship:
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots

class Slot:
    def __init__(self, type, size):
        self.type = type
        self.size = size

class Part:
    def __init__(self, name, type, size, grade, price):
        self.name = name
        self.type = type
        self.size = size
        self.grade = grade
        self.price = price

def GetShips():
    allShips = []

    ship = Ship("A2", [])
    ship.slots.append(Slot("shield", 3))
    ship.slots.append(Slot("Shield", 3))
    ship.slots.append(Slot("weapon", 3))
    ship.slots.append(Slot("weapon", 2))
    ship.slots.append(Slot("qtdrive", 3))
    allShips.append(ship)

    ship = Ship("Mustang Alpha", [])
    ship.slots.append(Slot("shield", 1))
    ship.slots.append(Slot("shield", 1))
    ship.slots.append(Slot("weapon", 2))
    ship.slots.append(Slot("weapon", 2))
    ship.slots.append(Slot("weapon", 1))
    ship.slots.append(Slot("weapon", 1))
    ship.slots.append(Slot("qtdrive", 1))
    allShips.append(ship)

    return allShips

def GetShields():
    allShields = []

    allShields.append(Part("Akura", "shield", 1, "C", 123))
    allShields.append(Part("Not Akura", "shield", 1, "B", 456))
    allShields.append(Part("Something Else", "shield", 3, "C", 123))
    allShields.append(Part("UltraShield", "shield", 3, "A", 123))

    return allShields

def GetWeapons():
    allWeapons = []

    return allWeapons

def GetQtDrives():
    allQtDrives = []
    
    return allQtDrives

def GetParts():
    allParts = []

    allParts.append(Part("Akura", "shield", 1, "C", 123))
    allParts.append(Part("Not Akura", "shield", 1, "B", 456))
    allParts.append(Part("Something Else", "shield", 3, "C", 123))
    allParts.append(Part("UltraShield", "shield", 3, "A", 123))

    return allParts

def main():

    name = input("Hello, what is your name: ")
    print("")
    print("Hello, " + name + ".")
    main_menu()
    
def main_menu():
    
    while True:
        ships = GetShips()
        numberOfShips = ships.__len__()
        exitCommand = numberOfShips + 1

        print("---------------------")
        print("Main Menu:")
        for i in range(numberOfShips):
            print(f"{i+1}. {ships[i].name}")

        print(f"{exitCommand}. Exit Program")
        print("---------------------")
        
        shipInput = input("Which ship would you like to view information on? (Enter corresponding number): ")
        shipIndex = int(shipInput)-1

        if(shipIndex == exitCommand-1):
            exit_program()

        if(shipIndex not in range(0, numberOfShips-1)):
            print("Invalid Option")
            main_menu()

        Build(ships[shipIndex])
        
def Build(ship):
    numberOfSlots = ship.slots.__len__()

    print(f"The {ship.name} currently has the following slots:")
    for i in range(numberOfSlots):
        print(f"{i+1}. Slot: {ship.slots[i].type} Size: {ship.slots[i].size}")

    optionInput = input("Which would you like to view options for? (Enter corresponding number): ")
    optionIndex = int(optionInput)-1
    while optionIndex not in range(0, numberOfSlots-1):
        optionInput = input("Which would you like to view options for? (Enter corresponding number): ")
        optionIndex = int(optionInput)-1

    ViewSlotOptions(ship, ship.slots[optionIndex])

def ViewSlotOptions(ship, slot):
    parts = GetPartOptions(slot)

    print(f"The {ship.name} slot {slot.type} size {slot.size} can equip one of the following:")
    for part in parts:
        print(f"{part.name}: Size {part.size} Grade {part.grade} Price {part.price}")

    option = input("Press any key to continue, or 'm' to return to menu")

    if(option == "m"):
        main_menu()
    else:
        Build(ship)

def GetPartOptions(slot):
    return filter(lambda part: IsPartForSlot(part, slot), GetParts())

def IsPartForSlot(part, slot):
    if part.size != slot.size:
        return False
    
    if part.type != slot.type:
        return False
    
    return True

def exit_program():
    print("Goodbye")
    exit()
    


main()
                    
            
    
