"""
All the functions to format the loot 
"""

import random as r
from collections import Counter
from data.synonyms_and_stash import synonyms_for_buildings, synonyms_for_mobs


# select_building_synonym               95%
# select_stash_location                 100%
# build_currency_string                 71%
# join_strings                          90%
# build_item_string_from_dict           64%
# build_item_string_from_list           82%
# build_item_string                     95%
# format_value                          90%
# check_no_loot                         100%
# append_loot                           95%
# generate_loot_message                 83%
# format_loot                           69%
### total quality:                      84.5%


# This function selects a synonym for the type of building.
def select_building_synonym(building_type: str) -> str:
    """Selects a synonym for the type of building

    Args:
        building_type (str): The Name of the building type

    Returns:
        str: A synonym for that building
    """
    # The 'synonyms' dictionary contains synonyms for different building types.
    # If no synonym use place instead
    building_synonyms: list = synonyms_for_buildings.get(building_type, ["place"])

    # A random choice is made from the list of synonyms.
    return r.choice(building_synonyms)


# This function selects a synonym for the type of mob.
def select_mob_synonym(mob_type: str) -> str:
    """Selects a synonym for the type of mob

    Args:
        mob_type (str): The Name of the mob type

    Returns:
        str: A synonym for that mob
    """
    # The 'synonyms' dictionary contains synonyms for different mob types.
    # If no synonym use place instead
    mob_synonyms: list = synonyms_for_mobs.get(mob_type, ["corpse"])

    # A random choice is made from the list of synonyms.
    return r.choice(mob_synonyms)


# This function selects a random location for stashing money.
def select_stash_location(stashed_money_locations: list) -> str:
    """Selects a random location to stash money

    Args:
        stashed_money_locations (list): A list of the different places the money could be stashed

    Returns:
        str: The randomly selected location
    """
    # A random location is chosen from the list of stashed_money_locations.
    return r.choice(stashed_money_locations)


# This function creates a formatted string for the currencies.
def build_currency_string(currencies: dict) -> str:
    """This functions takes in a dictionary of currencies and creates a formatted string

    Args:
        currencies (dict): The dictionary of the currencies

    Returns:
        str: The formatted string for the currencies
    """
    # Initialize an empty list to hold currency strings.
    currency_list: list = []

    # Iterate over the currencies dictionary. If a currency has a non-zero amount,
    # create a string representing the amount of that currency and add it to currency_list.
    for item, amount in currencies.items():
        if isinstance(amount, list) and amount and int(amount[0]) != 0:
            currency_list.append(f"{amount[0]} {item}")
        elif isinstance(amount, int) and amount != 0:
            currency_list.append(f"{amount} {item}")

    # Check if the list is empty
    if not currency_list:
        return ""

    # Check if the list has only one item
    if len(currency_list) == 1:
        return currency_list[0]

    # If there's more than one item, join all items except the last with ', '
    # and join the last item with ' and '
    return f"{', '.join(currency_list[:-1])} and {currency_list[-1]}"


# This function joins a list of strings with commas and 'and' as appropriate.
def join_strings(strings: list) -> str:
    """Join a list of strings with commas and 'and' as appropriate.

    Args:
        strings (list): A list of strings.

    Returns:
        str: The list of strings joined with commas and 'and' as appropriate.
    """
    # If there's only one string, return it.
    if len(strings) == 1:
        return strings[0]

    # If there are multiple strings, join all but the last with ', ' and last join with ' and '
    return f"{', '.join(strings[:-1])} and {strings[-1]}"


# This function builds a string describing the items found in the loot when items is a dictionary.
def build_item_string_from_dict(items: dict) -> str:
    """Build a string describing the items found in the loot when items is a dictionary.

    Args:
        items (dict): A dictionary where the keys are item categories and the values are lists of items.

    Returns:
        str: A string describing the items.
    """
    # Initialize an empty list to hold item strings.
    item_strings = []

    # For each category and list of items in the items dictionary, count the number of each item using a Counter.
    # For each item and count, create a string describing the item and its count and append it to a list of strings for that category.
    # Join the list of strings for that category into a single string with appropriate formatting, and append it to the list of item strings.
    for category, category_items in items.items():
        if category_items:
            item_counts = Counter(category_items)
            item_strings_list = []
            for item, count in item_counts.items():
                item_string = f"{count} x {item}" if count > 1 else item
                item_strings_list.append(item_string)
            category_string = join_strings(item_strings_list)
            item_string = f"{category}: {category_string}"
            item_strings.append(item_string)

    # Join the list of item strings into a single string with newline characters between each item string, and return it.
    return "\n".join(item_strings)


# This function builds a string describing the items found in the loot when items is a list.
def build_item_string_from_list(items: list) -> str:
    """Build a string describing the items found in the loot when items is a list.

    Args:
        items (list): A list of items.

    Returns:
        str: A string describing the items.
    """
    # If there are no items, return an empty string.
    if not items:
        return ""

    # Count the number of each item using a Counter.
    # For each item and count, create a string describing the item and its count and append it to a list of strings.
    # Join the list of strings into a single string with appropriate formatting, and return it.
    item_counts = Counter(items)
    item_strings_list = [
        f"{count} x {item}" if count > 1 else item
        for item, count in item_counts.items()
    ]
    return join_strings(item_strings_list)


# This function builds a string describing the items found in the loot.
def build_item_string(items):
    """Builds a string describing the items found in the loot.

    Args:
        items (dict or list): The items to describe. Can be a dictionary where the keys are item categories and the values are lists of items, or a list of items.

    Returns:
        str: A string describing the items.
    """
    # If items is a dictionary, use build_item_string_from_dict to build the item string.
    if isinstance(items, dict):
        return build_item_string_from_dict(items)
    # If items is a list, use build_item_string_from_list to build the item string.
    if isinstance(items, list):
        return build_item_string_from_list(items)
    # If items is neither a dictionary nor a list, raise a TypeError.
    raise TypeError("Expected a dictionary or a list.")


# This function formats numeric values into a string representation of a currency.
def format_value(gold_crowns: int, silver_shillings: int, brass_pennies: int) -> str:
    """Convert numeric values into a string

    Args:
        crowns (int): _description_
        shillings (int): _description_
        pennies (int): _description_

    Returns:
        str: _description_
    """
    # The function formats the numbers into a string using f-string formatting.
    return f"{gold_crowns}GC, {silver_shillings}ss and {brass_pennies}bp"


# This function checks if there is any loot at all.
def check_no_loot(loot_components: list) -> bool:
    """Check if there's no loot at all.

    Args:
        loot_components (list): A list of strings representing different kinds of loot.

    Returns:
        bool: True if there's no loot, False otherwise.
    """
    # If all components are empty, the function returns True indicating there's no loot else False
    return not any(loot_components)


# This function appends a message to the loot list if the loot_component is not empty.
def append_loot(loot: list, loot_component: str, message: str):
    """Append a formatted message to the loot list if the loot_component is not empty.

    Args:
        loot (list): The list to append the message to.
        loot_component (str): The loot component to check.
        message (str): The message to append if the loot component is not empty.
    """
    # If loot_component is not empty, the message is appended to the loot list.
    if loot_component:
        loot.append(message)


# This function generates a formatted message and appends it to the loot list if the loot_component is not empty.
def generate_loot_message(
    loot: list,
    loot_component: str,
    message_template: str,
    loot_string_key: str,
    loot_strings: dict,
):
    """Generate a formatted message and append it to the loot list if the loot component is not empty.

    Args:
        loot (list): The list to append the message to.
        loot_component (str): The loot component to check.
        message_template (str): The message template to use for formatting the message.
        loot_string_key (str): The key to retrieve from the loot_strings dictionary.
        loot_strings (dict): A dictionary with additional strings needed to format the loot string.
    """
    # If loot_component is not empty, a message is generated using the provided message_template and values from the loot_strings dictionary.
    # The generated message is then appended to the loot list.
    if loot_component:
        loot_string = loot_strings[loot_string_key]
        message = message_template.format(
            stash_place=loot_strings["stash_place"],
            loot_component=loot_component,
            loot_string=loot_string,
        )
        loot.append(message)


# This function formats a string that describes the loot found in a location.
def format_loot(
    currency_string: str,
    gems_string: str,
    art_string: str,
    cloth_string: str,
    domestics_string: str,
    loot_strings: dict,
) -> str:
    """Formats a string that describes the loot found in the location.

    Args:
        currency_string (str): A string representing the currency loot.
        gems_string (str): A string representing the gems loot.
        art_string (str): A string representing the art loot.
        cloth_string (str): A string representing the cloth loot.
        domestics_string (str): A string representing the domestic items loot.
        loot_strings (dict): A dictionary with additional strings needed to format the loot string.

    Returns:
        str: A string that describes all the loot found in the location.
    """
    # Check if there's no loot at all
    if check_no_loot(
        [currency_string, gems_string, art_string, cloth_string, domestics_string]
    ):
        return f"You search through the {loot_strings['building_synonym']}, but find nothing"

    # If there is loot, the function starts building a list of strings to describe the loot.
    loot = [f"You search through the {loot_strings['building_synonym']}, and ..."]

    # Generate messages for different types of loot
    generate_loot_message(
        loot,
        currency_string,
        "{stash_place} you find {loot_component}.",
        "stash_place",
        loot_strings,
    )
    generate_loot_message(
        loot,
        gems_string,
        "Very well hidden you find gems and jewels, they are {loot_component} with an approximate worth of {loot_string}.",
        "worth_jewels_string",
        loot_strings,
    )
    generate_loot_message(
        loot,
        art_string,
        "You discovered the following nestled art: {loot_component} with an approximate worth of {loot_string}.",
        "worth_art_string",
        loot_strings,
    )
    generate_loot_message(
        loot,
        cloth_string,
        "You stumbled upon these textiles: {loot_component} with an approximate worth of {loot_string}.",
        "worth_cloth_string",
        loot_strings,
    )
    generate_loot_message(
        loot,
        domestics_string,
        "You uncovered the following domestics artifacts: {loot_component} with an approximate worth of {loot_string}.",
        "worth_domestics_string",
        loot_strings,
    )

    # Finally, the function joins all the strings in the loot list into a single string with '\n' as the separator,
    return "\n".join(loot)
