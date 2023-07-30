"""
Getting the loot from the tables module
"""
import random as r
from collections import defaultdict
from data.data_tables import (
    building_loot_table,
    mob_loot_table,
    domestics_table,
    art_table,
    clothing_table,
    gems_table,
    jewelry_table,
)


# get_item_from_table               88%
# get_items_from_table              96%
# get_jewelry_item                  91%
# roll_dice                         99%
# determine_gem_type                94%
# find_specific_gem                 99%
# find_gems_and_jewelry             80%
# calculate_item_amount             99%
# determine_loot                    73%
# get_loot                          79%
# select_location                   90%
### total quality:                  90.8%

# Gets an item from the table
def get_item_from_table(table: dict) -> str:
    """Selects a random item from the The table

    Returns:
        str: The selected item
    """
    roll = r.randint(1, 100)
    return next(
        (item for (start, end), item in table.items() if start <= roll <= end),
        "Unknown Item",
    )


# This function rolls for items that require other tables
def get_items_from_table(number_of_items: int, table: dict) -> list:
    """Selects a specified number of items from the provided table

    Args:
        number_of_items (int): The number of items to select.add()
        table (list): The table to select items from

    Returns:
        list: _description_
    """

    # Return a list with the items from current table
    return [get_item_from_table(table) for _ in range(number_of_items)]


# This function rolls for gems and jewels
def get_jewelry_item(table: dict) -> str:
    """Returns an item from a jewelry table based on a dice roll.

    Args:
        table (dict): A dictionary with ranges as keys and items as values.

    Returns:
        str: The item that matches the dice roll.
    """
    roll: int = r.randint(1, 100)
    return next((item for rng, item in table.items() if roll in rng), "Unknown Item")


# This function rolls a dice with a given number of sides and returns the result.
def roll_dice(sides: int) -> int:
    """Roll a dice with a given number of sides.

    Args:
        sides (int): The number of sides on the dice.

    Returns:
        int: The result of the dice roll.
    """
    # Use the random library's randint function to simulate a dice roll.
    return r.randint(1, sides)


# This function determines the type of gem based on the result of a dice roll.
def determine_gem_type(roll: int) -> str:
    """Determine the type of gem based on a dice roll.

    Args:
        roll (int): The result of a dice roll.

    Returns:
        str: The type of gem.
    """
    # Use an if-else condition to map dice roll results to gem types.
    if roll == 1:
        return "Brass"
    return "Silver" if roll == 2 else "Gold"


# This function finds a specific gem in the gem table based on the gem type.
def find_specific_gem(gem_type: str) -> str:
    """Find a specific gem in a given gem table.

    Args:
        gem_type (str): The type of gem.

    Returns:
        str: The specific gem found.
    """
    # Use the gem type to look up the gem table and find a specific gem.
    return gems_table[gem_type][roll_dice(10)]


# This function determines whether to find a gem or a jewelry item and which specific item to find.
def find_gems_and_jewelry(quantity: int) -> dict:
    """Rolls dice to determine whether to find a gem or jewelry, and which type to find.

    Args:
        quantity (int): The number of items to find.

    Returns:
        dict: A dictionary where the key is the specific gem found and the value is
              the quantity. If no gem is found, returns an empty dictionary.
    """
    # Initialize a default dictionary to keep track of loot.
    loot = defaultdict(int)

    # Perform the search for the specified quantity.
    for _ in range(quantity):
        # Roll a 1d10 dice
        roll = roll_dice(10)
        # If the roll is less than or equal to 5, find a gem.
        if roll <= 5:
            # Determine gem type
            gem_type = determine_gem_type(roll_dice(3))
            # Find specific gem
            specific_gem = find_specific_gem(gem_type)
            # Increase the count of the specific gem in the loot.
            loot[specific_gem] += 1
        else:
            # Otherwise, find a jewelry item.
            # Get jewelry item
            jewelry_item = get_jewelry_item(jewelry_table)
            # Increase the count of the jewelry item in the loot.
            loot[jewelry_item] += 1
    # Convert the loot from a default dictionary to a regular dictionary before returning.
    return dict(loot)


# This function calculates the amount of an item to be looted based on a provided range.
def calculate_item_amount(rng: tuple) -> int:
    """Calculate the amount of an item to be looted based on a range.

    Args:
        rng (tuple): The range of possible amounts.

    Returns:
        int: The calculated amount.
    """
    # Use the random library's randint function to calculate the item amount.
    return r.randint(*rng)


# This function determines the loot based on the item type.
def determine_loot(
    item: str, amount: int, domestic_dict: dict, art_dict: dict, clothing_dict: dict
) -> dict:
    """Determine the loot based on the item type.

    Args:
        item (str): The type of item.
        amount (int): The amount of the item.
        domestic_dict (dict): The domestics table.
        art_dict (dict): The art table.
        clothing_dict (dict): The clothing table.

    Returns:
        dict: The calculated loot.
    """
    # Check the item type and get the items from the corresponding table or directly return the amount for non-table items
    if item == "Domestics":
        # If the item is 'Domestics', get the items from the domestics table.
        return {item: get_items_from_table(amount, domestic_dict)}  # Domestics table
    if item == "Art":
        # If the item is 'Art', get the items from the art table.
        return {item: get_items_from_table(amount, art_dict)}  # Art table
    if item == "Cloth":
        # If the item is 'Cloth', get the items from the clothing table.
        return {item: get_items_from_table(amount, clothing_dict)}  # Clothing
    if item != "Gems":
        # If the item is not 'Gems', return the item amount directly.
        return {item: amount}  # Pennies, Shillings and Gold

    # If the item is 'Gems', find gems and jewelry and return them.
    gems_or_jewelry_lot = find_gems_and_jewelry(amount)
    loot = []
    for gem_or_jewelry, quantity in gems_or_jewelry_lot.items():
        loot.extend([gem_or_jewelry] * quantity)
    return {item: loot}


# This function returns loot from a location based on the loot table and dice rolls.
def get_loot(location: str) -> dict:
    # sourcery skip: dict-assign-update-to-union
    """Return loot from a location based on the loot table and dice rolls

    Args:
        location (str): The location of the loot

    Returns:
        dict: A dictionary with all the loot found in the location
    """
    # An empty dictionary that will be returning all the loot found
    loot: dict = {"Gems": []}

    for item, (percentage, rng) in building_loot_table[location].items():
        # Roll the dice
        dice_roll: int = roll_dice(100)
        # Check if the dice roll is within the loot probability
        if dice_roll <= percentage:
            # if it is, calculate the item amount
            item_amount: int = calculate_item_amount(rng)
            # Determine the loot based on the item type
            item_loot = determine_loot(
                item, item_amount, domestics_table, art_table, clothing_table
            )
            loot.update(item_loot)
    return loot


# This function returns loot from a location based on the loot table and dice rolls.
def get_mob_loot(location: str) -> dict:
    # sourcery skip: dict-assign-update-to-union
    """Return loot from a location based on the loot table and dice rolls

    Args:
        location (str): The location of the loot

    Returns:
        dict: A dictionary with all the loot found in the location
    """
    # An empty dictionary that will be returning all the loot found
    loot: dict = {"Gems": []}

    for item, (percentage, rng) in mob_loot_table[location].items():
        # Roll the dice
        dice_roll: int = roll_dice(100)
        # Check if the dice roll is within the loot probability
        if dice_roll <= percentage:
            # if it is, calculate the item amount
            item_amount: int = calculate_item_amount(rng)
            # Determine the loot based on the item type
            item_loot = determine_loot(
                item, item_amount, domestics_table, art_table, clothing_table
            )
            loot.update(item_loot)
    return loot


# This function prompt for what type of location is being looted
def select_location() -> str:
    """This function select what type of building is being looted and return it from the list

    Returns:
        str: The location that will be looted
    """
    # Prompt the user to select a location
    locations: list = list(building_loot_table.keys())
    print("Select a location:")
    # Loops trough all locations
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    selected: int = int(input("Location: ")) - 1
    return locations[selected]


def select_mob() -> str:
    """This function select what type of building is being looted and return it from the list

    Returns:
        str: The location that will be looted
    """
    # Prompt the user to select a location
    locations: list = list(mob_loot_table.keys())
    print("Select a location:")
    # Loops trough all locations
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    selected: int = int(input("Location: ")) - 1
    return locations[selected]
