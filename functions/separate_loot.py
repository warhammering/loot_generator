"""
This function separate all the loots into their own category
"""


# total_quality:            78%

# This function separates the found loot into specified categories.
def separate_loot(found_loot: dict, categories: list) -> dict:
    """Separates the loot into specified categories.

    Args:
        found_loot (dict): A dictionary with all the loot found.
        categories (list): A list of categories to separate the loot into.

    Returns:
        dict: A dictionary with the loot separated into the specified categories.
    """
    # Separate currencies from the other items
    currencies: dict = {
        k: v
        for k, v in found_loot.items()
        if k in ["Pennies", "Shillings", "Crowns"] and v
    }

    # Separate the loot
    separated_loot = {category: found_loot.get(category, []) for category in categories}

    # Get the remaining items
    remaining_items = {k: v for k, v in found_loot.items() if k not in categories}

    return currencies, separated_loot, remaining_items
