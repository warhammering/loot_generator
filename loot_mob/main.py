"""
Main Module for loot_building
"""
import os
import sys


# get_loot_strings                  81%
# get_item_strings                  93%
# get_currency                      88%
# format_loot_string                94%
# formatting_loot                   85%
### total quality:                  88.2%


# Add the current directory to sys.path
sys.path.append(os.getcwd())

# Data Tables
from data.data_tables import (  # pylint: disable=wrong-import-position
    gems_table,
    other_trappings,
)

# Synonyms and stash for flavor text
from data.synonyms_and_stash import (  # pylint: disable=wrong-import-position
    location_to_stash_mob,
)

# Functionality for loot generation
from functions.loot_functions import (  # pylint: disable=wrong-import-position
    get_mob_loot,
    select_mob,
)

# Functionality for formatting the output
from functions.format_functions import (  # pylint: disable=wrong-import-position
    select_mob_synonym,
    select_stash_location,
    build_currency_string,
    build_item_string,
    format_loot,
    format_value,
)

# Functionality to calculate value from gems
from functions.calculations_gems_functionality import (  # pylint: disable=wrong-import-position
    calculate_total_value,
    convert_to_largest_currency,
)

# Functionality to calculate value from other items
from functions.calculations_loot_functionality import (  # pylint: disable=wrong-import-position
    calculate_item_value,
)

# Functionality to roll for other trappings
from functions.other_trappings_functionality import (  # pylint: disable=wrong-import-position
    roll_for_items,
    other_items_found,
)

# Functionality to separate loot
from functions.separate_loot import (  # pylint: disable=wrong-import-position
    separate_loot as loot_separation,
)


# This function generate the loot strings
def get_loot_strings(
    building_type: str, stashed_money_locations: list, loot_dicts: dict
) -> dict:
    """Generates the loot strings

    Args:
        building_type (str): The type of building.
        stashed_money_locations (list): List of places where money could be stashed.
        loot_dicts (dict): Dictionary containing different types of loot.

    Returns:
        dict: A dictionary containing strings for building synonym, stash place,
              and worth of jewels, domestics, art, and cloth.
    """
    # Initialize an empty dictionary to store the loot strings
    loot_strings: dict = {
        # Select a synonym for the building type
        "building_synonym": select_mob_synonym(building_type),
        # Select a stash location from the list of possible locations
        "stash_place": select_stash_location(stashed_money_locations),
        # Calculate the total value of gems
        "worth_jewels_string": format_value(
            *convert_to_largest_currency(
                calculate_total_value(
                    {"Gems": loot_dicts["Gems"]}, building_type, gems_table
                )
            )
        ),
        # Calculate the total value of domestics items
        "worth_domestics_string": format_value(
            *convert_to_largest_currency(
                calculate_item_value(
                    loot_dicts["Domestics"], building_type, "Domestics"
                )
            )
        ),
        # Calculate the total value of art items
        "worth_art_string": format_value(
            *convert_to_largest_currency(
                calculate_item_value(loot_dicts["Art"], building_type, "Art")
            )
        ),
        # Calculate the total value of the cloth items
        "worth_cloth_string": format_value(
            *convert_to_largest_currency(
                calculate_item_value(loot_dicts["Cloth"], building_type, "Cloth")
            )
        ),
    }

    # Return the dictionary containing the loot strings
    return loot_strings


# This function generate the item strings
def get_item_strings(separated_loot_dict: dict) -> dict:
    """Generates the item strings

    Args:
        separated_loot_dict (dict): Dictionary containing separated loot.

    Returns:
        dict: A dictionary containing strings for gems, art, cloth, and domestics.
    """

    # Initialize an empty dictionary to store the item strings
    item_strings: dict = {
        # Build a string describing the gems and store it in the dictionary
        "gems_string": build_item_string(separated_loot_dict["Gems"]),
        # Build a string describing the art items and store it in the dictionary
        "art_string": build_item_string(separated_loot_dict["Art"]),
        # Build a string describing the cloth items and store it in the dictionary
        "cloth_string": build_item_string(separated_loot_dict["Cloth"]),
        # Build a string describing the domestic items and store it in the dictionary
        "domestics_string": build_item_string(separated_loot_dict["Domestics"]),
    }

    # Return the dictionary containing the item strings
    return item_strings


# This function generate the currency string
def get_currency(separated_currency: dict) -> str:
    """Generates the currency string

    Args:
        separated_currency (dict): Dictionary containing separated currency.

    Returns:
        str: A string representing the currency.
    """

    # Separate the currency from the rest of the loot
    currency = {
        k: v
        for k, v in separated_currency.items()
        if k in ["Pennies", "Shillings", "Crowns"]
    }

    # Build the currency string
    currency_string: str = build_currency_string(currency)

    # Return the builded string
    return currency_string


# This function combine the different strings into one
def format_loot_string(
    currency_string: str, loot_strings: dict, item_strings: dict
) -> str:
    """Integrates all the strings into a formatted loot string

    Args:
        currency_string (str): String representing the currency.
        loot_strings (dict): Dictionary containing loot strings.
        item_strings (dict): Dictionary containing item strings.

    Returns:
        str: A string representing the formatted loot.
    """

    # The 'format_loot' function is called with the currency string, the item descriptions, and the loot descriptions.
    # The return value is a formatted string that integrates all these descriptions.
    return format_loot(
        currency_string,
        item_strings["gems_string"],
        item_strings["art_string"],
        item_strings["cloth_string"],
        item_strings["domestics_string"],
        loot_strings,
    )


# Main function of the module
def formatting_loot(
    found_loot: dict, building_type: str, stashed_money_locations: list
) -> str:
    """Converts the found loot into a descriptive string with added flavor text.

    Args:
        found_loot (dict): Dictionary containing the found loot.
        building_type (str): The type of building.
        stashed_money_locations (list): List of places where money could be stashed.

    Returns:
        str: A string representing the formatted loot.
    """

    # Define the loot categories
    categories = [
        "Gems",
        "Art",
        "Cloth",
        "Domestics",
        "Pennies",
        "Shillings",
        "Crowns",
    ]

    # Separate the loot
    _, loot, _ = loot_separation(found_loot, categories)

    # Get the loot strings
    loot_strings = get_loot_strings(building_type, stashed_money_locations, loot)

    # Get the item strings
    item_strings = get_item_strings(loot)

    # Get the currency string
    currency_string = get_currency(loot)

    # Format the loot string
    return format_loot_string(currency_string, loot_strings, item_strings)


def loot_mob_main():
    # Call the select_mob function to select a location
    selected_location: str = select_mob()

    # Get the loot for the selected location
    founded_loot: dict = get_mob_loot(selected_location)

    # Other loot found
    other_trappings_found: list = roll_for_items(founded_loot, other_trappings)

    # Define the loot categories
    loot_categories = [
        "Gems",
        "Art",
        "Cloth",
        "Domestics",
    ]

    # Separate the loot
    currencies, separated_loot, remaining_items = loot_separation(
        founded_loot, loot_categories
    )

    # Get the stash locations for the selected location
    stash_locations: list = location_to_stash_mob[selected_location]

    # Format and print the loot
    print(
        "\n****************************************************************************"
    )
    print(
        "****************************************************************************\n\n"
    )
    print(f"--- {formatting_loot(founded_loot, selected_location, stash_locations)}")

    if other_items_found(other_trappings_found) is not None:
        print(other_items_found(other_trappings_found))
