"""
Module for calculating gems and jewels value in the loot
"""
import random as r

# roll_10_dice                      95%
# roll_5_dice                       95%
# roll_3_dice                       95%
# roll_dice_for_gem_type            87%
# roll_dice_for_location            88%
# is_item_a_gem                     92%
# get_value                         83%
# calculate_total_value             86%
# convert_to_largest_currency       92%
### total_quality:                  97.4%


# Function to roll dices
def roll_10_dice(number_of_dice: int) -> int:
    """Create a number of d10 dices to be roll

    Args:
        number_of_dice (int): the number of 10-sided dice

    Returns:
        int: The total value rolled from the 10-sided dice
    """
    return sum(r.randint(1, 10) for _ in range(number_of_dice))


def roll_5_dice(number_of_dice: int) -> int:
    """Create a number of d10 dices to be roll

    Args:
        number_of_dice (int): the number of 5-sided dice

    Returns:
        int: The total value rolled from the 5-sided dice
    """
    return sum(r.randint(1, 5) for _ in range(number_of_dice))


def roll_3_dice(number_of_dice: int) -> int:
    """Create a number of d10 dices to be roll

    Args:
        number_of_dice (int): the number of 3-sided dice

    Returns:
        int: The total value rolled from the 3-sided dice
    """
    return sum(r.randint(1, 3) for _ in range(number_of_dice))


# This function calculates the value of a gem based on its type
def roll_dice_for_gem_type(gem_type: str) -> int:
    """Calculate the value of a gem based on its type"""
    # If the gem type is "Brass", calculate its value as 4 rolls of a 10-sided die.
    if gem_type == "Brass":
        return roll_10_dice(4)  # Value in pennies
    # If the gem type is "Silver", calculate its value as 2 rolls of a 10-sided die times 12.
    if gem_type == "Silver":
        return roll_10_dice(2) * 12  # Convert from shillings to pennies
    # If the gem type is "Gold", calculate its value as 1 roll of a 10-sided die times 240.
    # If the gem type is not recognized, return 0.
    return roll_10_dice(1) * 240 if gem_type == "Gold" else 0


# This function calculates the value of an item based on the location where it was found
def roll_dice_for_location(location: str) -> int:
    """Calculate the value of an item based on the location"""
    # If the location is either "Hovel", "Shrine", or "Craftsman's Corner",
    # The value is returned in pennies.
    if location in {
        "Hovel",
        "Shrine",
        "Craftsman's Corner",
        "Peasant",
        "Small Monster",
    }:
        return roll_10_dice(4)  # Value in pennies
    # If the location is either "House", "Chapel", or "Workshop",
    if location in {"House", "Chapel", "Workshop", "Citizen", "Large Monster"}:
        return roll_10_dice(2) * 12  # Convert from shillings to pennies
    # If the location is either "Estate", "Temple", or "Guildhall",
    # If the location is not recognized, return 0.
    if location in {"Estate", "Temple", "Guildhall", "Noble", "Legendary Monster"}:
        return roll_10_dice(1) * 240  # Convert from crowns to pennies
    return 0


# This function checks if a given item is a gem, based on a provided table of gems
def is_item_a_gem(item: str, table_of_gems: dict) -> bool:
    """Check if the item is a gem"""
    # Iterate over the gem types in the table_of_gems dictionary.
    # If the item is in the values for a gem type, return True.
    return any(item in gems.values() for gems in table_of_gems.values())


# This function calculates the value of an item based on its type and the location where it was found
def get_value(item: str, location: str, table_of_gems: dict) -> int:
    """
    Calculate the value of an item based on its type and the selected location.

    Args:
        item (str): The item whose value is to be calculated.
        selected_location (str): The location where the item was found.
        gems_table (dict): A dictionary that maps gem types to their values.

    Returns:
        int: The value of the item in pennies.
    """
    # If the item is not a gem, calculate its value based on the location.
    if not is_item_a_gem(item, table_of_gems):
        return roll_dice_for_location(location)
    # If the item is a gem, calculate its value based on its type.
    # Iterate over the gem types and their values in the table_of_gems dictionary.
    # If the item is in the values for a gem type, calculate its value.
    # If the item is not in the values for any gem type, return 0.
    return next(
        (
            roll_dice_for_gem_type(gem_type)
            for gem_type, value in table_of_gems.items()
            if item in value.values()
        ),
        0,
    )


# This function calculate the total value of all the items in the jewels_value list
def calculate_total_value(
    jewels_value_dict: dict, location: str, table_of_gems: dict
) -> int:
    """Calculate the total value of all items in a dictionary.

    Args:
        jewels_value_dict (dict): A dictionary that maps categories to lists of items.
        selected_location (str): The location where the items were found.
        gems_table (dict): A dictionary that maps gem types to their values.

    Returns:
        int: The total value of all items in the dictionary, in pennies.
    """
    # Initialize the total value
    total_value = 0

    # For each category in the dictionary
    for value in jewels_value_dict.values():
        # For each item in that category
        for item in value:
            # Add the value of the item to the total value
            total_value += get_value(item, location, table_of_gems)

    return total_value


# This function convert all the pennies into other kind of coins, trying to always get largest currency
def convert_to_largest_currency(value_in_pennies: int) -> int:
    """Takes in the total value of pennies and convert it to the highest currency

    Args:
        value_in_pennies (int): Value in pennies

    Returns:
        int: The value in pennies converted to the higher coins and separated by coin type
    """
    crowns, remaining_pennies = divmod(value_in_pennies, 240)
    shillings, pennies = divmod(remaining_pennies, 12)

    return crowns, shillings, pennies
