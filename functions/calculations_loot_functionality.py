"""
This module calculate all other loot that is not a gem or jewel
"""
from .calculations_gems_functionality import roll_10_dice, roll_5_dice, roll_3_dice

# calculate_art_value           88%
# calculate_non_art_value       88%
# calculate_item_value          81%
### total quality:              85.7%


# This function calculates the value of art items based on the location
def calculate_art_value(location: str) -> int:
    """Calculate the value of an art item based on the location."""
    # If the location is either "Hovel", "Shrine", or "Craftsman's Corner",
    if location in {
        "Hovel",
        "Shrine",
        "Craftsman's Corner",
        "Peasant",
        "Small Monster",
    }:
        return roll_10_dice(5)  # Value in pennies
    # If the location is either "House", "Chapel", or "Workshop",
    if location in {"House", "Chapel", "Workshop", "Citizen", "Large Monster"}:
        return roll_10_dice(5) * 12  # Convert from shillings to pennies
    # If the location is either "Estate", "Temple", or "Guildhall",
    if location in {"Estate", "Temple", "Guildhall", "Noble", "Legendary Monster"}:
        return roll_5_dice(1) * 240  # Convert from crowns to pennies
    # If the location is not recognized, set the item value to 0
    return 0


# This function calculates the value of non-art items based on the location
def calculate_non_art_value(location: str) -> int:
    """Calculate the value of a non-art item based on the location."""
    # If the location is either "Hovel", "Shrine", or "Craftsman's Corner",
    if location in {
        "Hovel",
        "Shrine",
        "Craftsman's Corner",
        "Peasant",
        "Small Monster",
    }:
        return roll_10_dice(1)  # Value in pennies
    # If the location is either "House", "Chapel", or "Workshop",
    if location in {"House", "Chapel", "Workshop", "Citizen", "Large Monster"}:
        return roll_10_dice(1) * 12  # Convert from shillings to pennies
    # If the location is either "Estate", "Temple", or "Guildhall",
    if location in {"Estate", "Temple", "Guildhall", "Noble", "Legendary Monster"}:
        return roll_3_dice(1) * 240  # Convert from crowns to pennies
    # If the location is not recognized, set the item value to 0
    return 0


# This function calculates the total value of a list of items based on the location and item type
def calculate_item_value(items: list, location: str, item_type: str) -> int:
    """Calculate the total value of a list of items based on the location and item type."""

    # Initialize the total value to 0
    total_value = 0

    # For each item in the items list
    for item in items:
        # If the item is "Other Trapping", skip it and continue with the next item
        if item == "Other Trapping":
            continue

        # If the type of the item is "Art", calculate its value based on the location using the calculate_art_value function
        if item_type == "Art":
            item_value = calculate_art_value(location)
        # If the type of the item is not "Art", calculate its value based on the location using the calculate_non_art_value function
        else:
            item_value = calculate_non_art_value(location)

        # Add the value of the item to the total value
        total_value += item_value

    # Return the total value of all items in the list
    return total_value
