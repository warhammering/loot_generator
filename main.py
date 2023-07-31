from loot_building import main as loot_building
from loot_mob import main as loot_mob
from loot_mob import armor, weapons


def line_separator():
    print(
        "****************************************************************************"
    )


def main():
    print(
        "******************************************************************************"
    )
    print(
        "* Welcome to the loot generator based on skyperbole's Treasure and Artefacts *"
    )
    print(
        "******************************************************************************"
    )
    while True:
        print("\n****** What do you want to loot? ****** \n")
        print("a) loot a mob")
        print("b) loot a building")
        print("c) A weapon")
        print("d) An armor")
        print("write 'exit' to end")
        option = input("\n>")
        print(
            "\n************************************************************************************************"
        )

        if option.lower() == "a":
            print("loot a mob")
            loot_mob.loot_mob_main()
            formatting_separation()
        elif option.lower() == "b":
            print("loot a building")
            loot_building.loot_building_main()
            formatting_separation()
        elif option == "c":
            print("weapon with flaws")
            print("\n")
            weapons.generate_weapon_flaw()
            formatting_separation()
        elif option == "d":
            print("armor with flaws")
            print("\n")
            armor.generate_armor_flaw()
            formatting_separation()
        elif option.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def formatting_separation():
    print("\n")
    line_separator()
    line_separator()


if __name__ == "__main__":
    main()
