"""
Function to determine armor flaws
"""
import random

# This function rolls a dice and returns a flaw based on the dice roll
def roll_dice_and_get_flaw() -> str:
    """
    Roll a dice and get a flaw based on the roll.

    Returns:
        str: The flaw description.
    """
    # Roll a dice and assign the result to table_dice
    table_dice: int = random.randint(1, 100)

    # Define the flaws and their corresponding dice ranges
    flaws = [
        (range(1, 2), "No Flaw"),
        (range(2, 16), "Bulky - Increase the armour’s Encumbrance by +1."),
        (
            range(16, 31),
            "Partial - The armour does not cover the entire location. An even number to hit, or a Critical Hit, ignores its APs.",
        ),
        (
            range(31, 51),
            "Shoddy - A Critical Hit to this location destroys the armour, which provides no APs against the attack.",
        ),
        (
            range(51, 66),
            "Ugly - The armour’s design attracts negative attention, imposing a penalty of -10 to related Fellowship Tests.",
        ),
        (
            range(66, 71),
            "Broken - The Armor is already broken or breaks on the next use.",
        ),
        (
            range(71, 81),
            "Unreliable - The armour does not provide full cover and gains the Partial Flaw. Penalties for wearing armour are doubled.",
        ),
        (
            range(81, 91),
            "Weakpoints - The armour is damaged or badly designed. If a weapon with the Impale Quality scores a Critical, the armour’s APs are ignored.",
        ),
        (range(91, 96), "Corrupted - The armour has the Corruption (Minor) Trait"),
        (range(96, 101), "Roll Twice"),
    ]

    # Check the rolled dice against the flaw ranges.
    return next(
        (
            flaw_description
            for flaw_range, flaw_description in flaws
            if table_dice in flaw_range
        ),
        "No flaw found",
    )


# This function rolls for a flaw that is not in the given list and not "Roll Twice"
def roll_for_flaw(flaw_list: list) -> str:
    """
    Roll for a flaw that is not in the given list and not "Roll Twice".

    Args:
        flaw_list (list): A list of existing flaws.

    Returns:
        str: The flaw description.
    """
    # Continuously roll for a new flaw
    while True:
        # Roll a dice and get a flaw
        flaw = roll_dice_and_get_flaw()

        # If the rolled flaw is not in the given list and is not "Roll Twice"
        # then return the flaw.
        # If the flaw is in the list or is "Roll Twice", the loop continues and a new flaw is rolled
        if flaw not in flaw_list and flaw != "Roll Twice":
            return flaw


# This function generates flaws for a piece of armour
def armour_flaw(allow_roll_twice: bool = True, flaw_list: list = None) -> str:
    """
    Get the flaws for a piece of armour.

    Args:
        allow_roll_twice (bool, optional): Whether "Roll Twice" is allowed. Defaults to True.
        flaw_list (list, optional): A list of existing flaws. Defaults to None.

    Returns:
        str: The flaw descriptions, separated by newline characters.
    """
    # If no list of flaws is provided, initialize an empty list
    if flaw_list is None:
        flaw_list = []

    # Continuously generate flaws
    while True:
        # Roll a dice and get a flaw
        flaw = roll_dice_and_get_flaw()

        # If the rolled flaw is already in the list, continue the loop to generate a new flaw
        if flaw in flaw_list:
            continue

        # If the rolled flaw is "No Flaw", return a no flaw message
        if flaw == "No Flaw":
            return "Sigmar smiles upon you. This armor has no flaw"

        # If the rolled flaw is "Roll Twice", and "Roll Twice" is allowed,
        # roll for a new flaw and add it to the list, then continue the loop to generate a new flaw
        if flaw == "Roll Twice" and allow_roll_twice:
            flaw_list.append(roll_for_flaw(flaw_list))
            continue

        # If the rolled flaw is not in the list and is not "Roll Twice", add it to the list
        flaw_list.append(flaw)

        # If the rolled flaw is not "Roll Twice", break the loop and stop generating new flaws
        if flaw != "Roll Twice":
            break

    # Return the list of flaws as a string, each flaw separated by a newline
    return "\n".join(flaw_list) if flaw_list else ""


# Check if the armor dont fit
fitting_dice: int = random.randint(1, 4)

# show message that the armor dont fit plus flaws
print(
    f"The armor does not fit properly and it needs to be refitted and it has the flaw: \n{armour_flaw()}"
    # otherwise return the flaws
    if fitting_dice == 1
    else f"The armor has the flaw: \n{armour_flaw()}"
)
