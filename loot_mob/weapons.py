"""
Function to determine weapon flaws
"""
import random

# This function rolls a dice and returns a flaw based on the dice roll
def roll_dice_and_get_flaw():
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
        (range(2, 11), "Bulky - Increase the weapon’s Encumbrance by +1."),
        (
            range(11, 21),
            "Dangerous - The weapon is unwieldy or broken. Any failed test including a 9 on either die results in a Fumble.",
        ),
        (
            range(21, 31),
            "Imprecise - The weapon is poorly balanced or difficult to bring to bear, suffering a penalty of -1 SL when attacking.",
        ),
        (range(31, 41), "Shoddy - The weapon breaks when you roll a Fumble."),
        (
            range(41, 51),
            "Broken - The Weapon is already broken or breaks on the next use",
        ),
        (
            range(51, 61),
            "Slow - The weapon is heavy or difficult to use properly. The weapon always strikes last in a Round, and opponents gain +1 SL to any Test to defend against its attacks.",
        ),
        (
            range(61, 71),
            "Ugly - The weapon’s design attracts negative attention, imposing a -10 penalty to related Fellowship Tests.",
        ),
        (
            range(71, 81),
            "Undamaging - The weapon is badly designed or rusted. All APs are doubled against it. Further, the weapon does not inflict a minimum of 1 Wound.",
        ),
        (
            range(81, 91),
            "Unreliable - Due to its size or unbalanced design, the weapon receives -1 SL to failed Tests.",
        ),
        (range(91, 96), "Corrupted - The weapon has the Corruption (Minor) Trait"),
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
def roll_for_flaw(flaw_list):
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


# This function generates flaws for a weapon
def weapon_flaw(allow_roll_twice=True, flaw_list=None) -> str:
    """
    Get the flaws for a weapon.

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
            return "Ranald's blessings upon you. This weapon has no flaw"

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


# show message with the weapons flaws
print(f"This weapon has the flaw: \n{weapon_flaw()}")
