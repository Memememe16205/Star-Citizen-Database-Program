def main():

    name = input("Hello, what is your name: ")
    print("")
    print("Hello, " + name + ".")
    main_menu()
    
def main_menu():
    
    while True:
        print("---------------------")
        print("Main Menu:")
        print("1. Crusader C2 Hercules Starlifter")
        print("4. Exit Program")
        print("---------------------")
        
        shipPick = input("Which ship would you like to view information on? (Enter corresponding number): ")

        if(shipPick == "1"):
            C2_build()
        elif(shipPick == "2"):
            Connie_An_Build()
        elif(shipPick == "3"):
            O400i_build()
        elif(shipPick == "4"):
            exit_program()
        else:
            print("Invalid Option")
            main_menu()

def C2_build():
    
    print("1. Stock Build: The stock components that come with the ship.")
    print("2. Upgraded Build: This build is upgraded to the best components.")
    print("3. Discription: This is the discription of the ship, as well as basic information.")
    build = input("Which would you like to view? (Enter corresponding number): ")

    if(build == "1"):
        Hercules_C2_stock()
        main_menu()
    
    elif(build == "2"):
        Hercules_C2_upgraded()
        locations = input("Would you like to view the locations to buy the upgraded parts from? (Yes/No): ")
        
        if(locations == "Yes"):
            Hercules_C2_parts_locations()
            main_menu()
        
        elif(locations =="No"):
            print("Okay, returning to main menu")
            main_menu()

        else:
            print("Invalid Option, returning to main menu")
            main_menu()

    elif(build == "3"):
        Hercules_C2_def()
        main_menu()
        
    else:
        print("That is not a valid build.")
        C2_build()

def Connie_An_Build():
    
    build = input("Which parts list would you like to view? (Stock, Upgraded): ")

    if(build == "Stock"):
        Connie_An_stock()
        main_menu()
    
    elif(build == "Upgraded"):
        Connie_An_upgraded()
        locations = input("Would you like to view the locations to buy the upgraded parts from? (Yes/No): ")
        
        if(locations == "Yes"):
            Connie_An_parts_locations()
            main_menu()
        
        elif(locations =="No"):
            print("Okay, returning to main menu")
            main_menu()

        else:
            print("Invalid Option, returning to main menu")
            main_menu()
        
    else:
        print("That is not a valid build.")
        Connie_An_Build()

def O400i_build():
    
    build = input("Which parts list would you like to view? (Stock, Upgraded): ")

    if(build == "Stock"):
        O400i_stock()
        main_menu()
    
    elif(build == "Upgraded"):
        O400i_upgraded()
        locations = input("Would you like to view the locations to buy the upgraded parts from? (Yes/No): ")
        
        if(locations == "Yes"):
            O400i_parts_locations()
            main_menu()
        
        elif(locations =="No"):
            print("Okay, returning to main menu")
            main_menu()

        else:
            print("Invalid Option, returning to main menu")
            main_menu()
        
    else:
        print("That is not a valid build.")
        O400i_build()

def Hercules_C2_def():
    print("")
    print("-------------------------------------------------------------------------------------")
    print("The C2 Hercules Starlifter is a civilian heavy transport manufactured by Crusader Industries.")
    print("Utilizing the patented Hercules military-grade spaceframe and expanding cargo capacity,")
    print("while sacrificing barely any firepower, the C2 has taken the private sector by storm. It has")
    print("become the industry standard for racing teams, ship dealers and manufacturers, construction")
    print("orgs, mining corporations, and even large-scale touring entertainment outfits.")
    print("")
    print("Size: Large (S5)")
    print("Role: Transport")
    print("Crew: 1-2")
    print("Cargo Capacity: 696 SCU")
    print("Pledge Price: $400 ($370)")
    print("In-Game Price: 4,925,500 aUEC")
    print("Max Speed: 963 m/s")
    print("-------------------------------------------------------------------------------------")
    print("")
    
def Hercules_C2_stock():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 2x Size 4 M6A Laser Cannons, 1120 dps")
    print("Turret Weapons: 2x Size 4 M6A Laser Cannons per Turret, 1120 dps, 2 Turrets")
    print("Missiles: None")
    print("")
    print("Shields: 2x Size 3 Strongholds (Grade C Industrial Shields), 100,000 hp each")
    print("Coolers: 2x Size 3 ThermalCore (Grade C Industrial Coolers), 16,000k c/s each")
    print("Power Plant: 1x Size 3 Ginzel (Grade C Industrial Plant), 50,000 pwr/s")
    print("Quantum Drive: 1x Size 3 Kama (Grade C Industrial Drive), 59,589 km/s")
    print("-------------------------------------------------------------------------------------")
    print("")

def Hercules_C2_upgraded():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 2x Size 4 AD4B Ballistic Gatling Guns, 2733 dps")
    print("Turret Weapons: 2x Size 4 AD4B Ballistic Gatling Guns per Turret, 2733 dps, 2 Turrets")
    print("Missiles: None")
    print("")
    print("Shields: 2x Size 3 7CA 'Nargun' (Grade A Civilian Shields), 115,000 hp each")
    print("Coolers: 2x Size 3 Chill-Max (Grade A Industrial Coolers), 17,600k c/s each")
    print("Power Plant: 1x Size 3 Durango (Grade A Industrial Plant), 55,000 pwr/s")
    print("Quantum Drive: 1x Size 3 TS-2 (Grade A Military Drive), 208,561 km/s")
    print("")
    print("Total Price: 1,551,130 aUEC")
    print("-------------------------------------------------------------------------------------")
    print("")

def Hercules_C2_parts_locations():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("2x 7CA 'Nargun' (202,200 aUEC), and 1x TS-2 (93,700 aUEC): Cousin Crows, Orison (295,900 aUEC)")
    print("2x Chill-Max (574,500 aUEC), and 1x Durango (430,350 aUEC): Dumper's Depot, Area18 (1,004,850 aUEC)")
    print("6x AD4B (250,380 aUEC): CenterMass, Area18 (250,380 aUEC)")
    print("-------------------------------------------------------------------------------------")
    print("")

def Connie_An_stock():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 4x Size 4 CF-447 Rhino Laser Repeaters, 1572 dps")
    print("Turret Weapons: 2x Size 2 CF-227 Badger Laser Repeaters per Turret, 615 dps, 2 Turrets")
    print("Missiles: 24x Size 2 StrikeForce II Crosssection (2,058 dmg each), 28x Size 1 Marksman I Infared (1,140 dmg each)")
    print("")
    print("Shields: 1x Size 3 5CA 'Akura' (Grade C Civilian Shield), 100,000 hp")
    print("Coolers: 2x Size 2 Frost-Star EX (Grade C Civilian Coolers), 4,280k c/s each")
    print("Power Plants: 2x Size 2 DayBreak (Grade C Civilian Plants), 5,938 pwr/s each")
    print("Quantum Drive: 1x Size 2 Bolon (Grade C Civilian Drive), 74,486 km/s")
    print("-------------------------------------------------------------------------------------")
    print("")

def Connie_An_upgraded():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 4x Size 4 AD4B Ballistic Gatling Guns, 5,464 dps")
    print("Turret Weapons: 2x Size 2 Scorpion GT-215 Ballistic Gatling Guns per Turret, 2,582 dps, 2 Turrets")
    print("Missiles: 24x Size 2 Rattler II Crosssection (4,070 dmg each), 28x Size 1 Arrow I Infared (2,333 dmg each)")
    print("")
    print("Shields: 1x Size 3 7CA 'Nargun' (Grade A Civilian Shield), 115,000 hp")
    print("Coolers: 2x Size 2 Snowpack (Grade A Industrial Coolers), 8,800k c/s each")
    print("Power Plants: 2x Size 2 Genoa (Grade A Industrial Plants), 13,750 pwr/s each")
    print("Quantum Drive: 1x Size 2 XL-1 (Grade A Military Drive), 260,701 km/s")
    print("")
    print("Total Price: 865,752 aUEC")
    print("-------------------------------------------------------------------------------------")
    print("")

def Connie_An_parts_locations():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("1x 7CA 'Nargun' (101,100 aUEC), 4x Scorpion GT-215 (31,400 aUEC), and 1x XL-1 (94,900 aUEC): Cousin Crows, Orison (227,400 aUEC)")
    print("4x AD4B (166,920 aUEC): Crusader Showroom, Orison (166,920 aUEC)")
    print("2x Snowpack (165,800 aUEC), and 2x Genoa (301,200 aUEC): Omega Pro, New Babbage (467,000 aUEC)")
    print("28x Arrow I (2,464 aUEC): Ship Weapons Shop, HUR L3 (2,464 aUEC)")
    print("24x Rattler II, (2,184 aUEC): Ship Weapons Shop, HUR L4 (2,184 aUEC)")
    print("-------------------------------------------------------------------------------------")
    print("")
    
def O400i_stock():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 2x Size 3 CF-337 Panther Laser Repeaters, 492 dps")
    print("Turret Weapons: 2x Size 3 CF-337 Panther Laser Repeaters per Turret, 722 dps, 2 Turrets")
    print("Missiles: 16x Size 2 StrikeForce II Crosssection (2,058 dmg each), 16x Size 1 Marksman I Infrared (1,140 dmg each)")
    print("")
    print("Shields: 1x Size 3 Guard (Grade C Civilian Shield), 100,000 hp")
    print("Coolers: 3x Size 2 Snowfall (Grade B Industrial Coolers), 8,400k c/s")
    print("Power Plants: 3x Size 2 Sedulity (Grade B Industrial Plants), 13,125 pwr/s each")
    print("Quantum Drive: 1x Size 2 Torrent (Grade C Civilian Drive), 132,833 km/s")
    print("-------------------------------------------------------------------------------------")
    print("")

def O400i_upgraded():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("Pilot Weapons: 2x Size 3 Mantis GT-220 Ballistic Gatling Guns, 1,600 dps")
    print("Turret Weapons: 2x Size 3 Mantis GT-220 Ballistic Gatling Guns per Turret, 1,600 dps, 2 Turrets")
    print("Missiles: 16x Size 2 Rattler II Infrared (4,070 dmg each), 16x Size 1 Arrow I Infrared (2,333 dmg each)")
    print("")
    print("Shield: 1x Size 3 7CA 'Nargun' (Grade A Civilian Shield), 115,000 hp")
    print("Coolers: 3x Size 2 Snowpack (Grade A Industrial Coolers), 8,800k c/s each")
    print("Power Plants: 3x Size 2 Genoa (Grade A Industrial Plants), 13,750 pwr/s each")
    print("Quantum Drive: 1x Size 2 XL-1 (Grade A Military Drive), 260,701 km/s")
    print("")
    print("Total Price: 980,220 aUEC")
    print("-------------------------------------------------------------------------------------")
    print("")

def O400i_parts_locations():
    
    print("")
    print("-------------------------------------------------------------------------------------")
    print("1x 7CA 'Nargun' (101,100 aUEC), 1x XL-1 (94,900 aUEC), and 6x Mantis GT-220 (81,000 aUEC): Cousin Crows, Orison (277,000 aUEC)")
    print("2x Chill-Max (574,500 aUEC) and 1x Durango (430,350 aUEC): Dumper's Depot, Area18 (1,004,850 aUEC)")
    print("3x Snowpack (248,700 aUEC), and 16x Rattler II (1,312 aUEC): Dumper's Depot, Area18 (250,012 aUEC)")
    print("3x Genoa (451,800 aUEC): Platinum Bay, Everus Harbor (451,800 aUEC)")
    print("16x Arrow I (1,408 aUEC): Dumper's Depot (1,408 aUEC)")
    print("-------------------------------------------------------------------------------------")
    print("")

def exit_program():
    print("Goodbye")
    exit()
    

    
main()
                    
            
    
