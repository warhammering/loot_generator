"""
Module with the functionality to get other trappings
"""
import random as r


# count_other_trappings         89%
# roll_for_items                72%
# other_items_found             77%
### total quality:              79.3%


# This function counts all instances of other trappings
def count_other_trappings(loot_dict: dict) -> int:
    """Counts all instances of other trappings in the loot found

    Args:
        loot_dict (dict): The loot found dictionary

    Returns:
        int: The number of times "Other Trapping" appears
    """
    # Initialize a variable to store the count of "Other Trapping"
    count: int = sum(
        # For each value in the loot dictionary values...
        value.count("Other Trapping")
        for value in loot_dict.values()
        if isinstance(value, list)
    )

    # Return the total count of "Other Trapping"
    return count


# This function return a list of the other trappings found
def roll_for_items(loot_dict: dict, items_dict: dict) -> list:
    """Create a list with the founded items

    Args:
        loot_dict (dict): The loot found dictionary
        items_dict (dict): The other_items dictionary

    Returns:
        list: A list with the picked
    """
    count = count_other_trappings(loot_dict)

    # If no item founds then return nothing
    if count < 1:
        return None
    # Initialize the list to hold the found items
    found_items: list = []

    # Define the categories
    categories = list(items_dict.keys())

    # For each instance of "Other Trapping"
    for _ in range(count):
        # Roll a die to select a category
        category = r.choice(categories)

        # Roll a 100-sided die to select an item within the category
        roll = r.randint(1, 100)

        # Find the item that correspond to the roll
        for item_range, item in items_dict[category].items():
            if roll in item_range:
                found_items.append(item)
                break

    return found_items


# This function returns the string of the founded items
def other_items_found(items: list) -> str:
    """Formatted string with the items found

    Args:
        items (list): A list of other trappings found

    Returns:
        str: The formatted string
    """
    # If items is None or empty, return None
    if not items:
        return None

    # If there is only 1 item
    if len(items) == 1:
        return f"The other trapping found is a {items[0]}"

    # If there are two items, return their names
    if len(items) == 2:
        return f"The other trappings found are a {items[0]} and a {items[1]}"

    # If there are more than two items, format the list with commas and 'and' in the last one
    items_str: str = ", ".join(f"{item}" for item in items[:-1])
    return f"The other trappings found are {items_str} and a {items[-1]}"
