"""
Module for all tables to execute
"""

# Loot Table by Place
building_loot_table: dict = {
    # brass
    "Hovel": {
        "Pennies": (20, (2, 20)),
        "Shillings": (10, (1, 5)),
        "Crowns": (0, (1, 1)),
        "Domestics": (10, (1, 3)),
        "Gems": (0, (0, 0)),
        "Art": (0, (0, 0)),
        "Cloth": (10, (1, 1)),
    },
    "Shrine": {
        "Pennies": (25, (4, 40)),
        "Shillings": (15, (1, 5)),
        "Crowns": (0, (1, 1)),
        "Domestics": (0, (0, 0)),
        "Gems": (5, (1, 1)),
        "Art": (5, (1, 1)),
        "Cloth": (5, (1, 1)),
    },
    "Craftsman's Corner": {
        "Pennies": (35, (6, 60)),
        "Shillings": (20, (1, 5)),
        "Crowns": (1, (1, 1)),
        "Domestics": (10, (1, 3)),
        "Gems": (1, (1, 1)),
        "Art": (1, (1, 1)),
        "Cloth": (10, (1, 1)),
    },
    # silver
    "House": {
        "Pennies": (50, (6, 60)),
        "Shillings": (25, (1, 5)),
        "Crowns": (5, (1, 3)),
        "Domestics": (25, (1, 5)),
        "Gems": (2, (1, 3)),
        "Art": (10, (1, 2)),
        "Cloth": (25, (1, 3)),
    },
    "Chapel": {
        "Pennies": (50, (6, 60)),
        "Shillings": (35, (2, 20)),
        "Crowns": (5, (1, 3)),
        "Domestics": (10, (1, 5)),
        "Gems": (10, (1, 3)),
        "Art": (10, (1, 5)),
        "Cloth": (10, (1, 5)),
    },
    "Workshop": {
        "Pennies": (50, (8, 80)),
        "Shillings": (50, (3, 30)),
        "Crowns": (5, (1, 3)),
        "Domestics": (20, (1, 5)),
        "Gems": (5, (1, 3)),
        "Art": (10, (1, 3)),
        "Cloth": (20, (1, 3)),
    },
    # gold
    "Estate": {
        "Pennies": (100, (10, 200)),
        "Shillings": (75, (5, 50)),
        "Crowns": (20, (1, 10)),
        "Domestics": (50, (2, 10)),
        "Gems": (20, (1, 10)),
        "Art": (50, (1, 10)),
        "Cloth": (50, (2, 10)),
    },
    "Temple": {
        "Pennies": (100, (10, 100)),
        "Shillings": (85, (4, 40)),
        "Crowns": (25, (1, 10)),
        "Domestics": (25, (1, 10)),
        "Gems": (25, (1, 5)),
        "Art": (25, (1, 5)),
        "Cloth": (20, (1, 10)),
    },
    "Guildhall": {
        "Pennies": (100, (10, 100)),
        "Shillings": (90, (5, 50)),
        "Crowns": (25, (1, 10)),
        "Domestics": (35, (1, 5)),
        "Gems": (10, (1, 3)),
        "Art": (50, (1, 10)),
        "Cloth": (50, (1, 5)),
    },
}

# Loot table by creature
mob_loot_table: dict = {
    # human
    "Peasant": {
        "Pennies": (20, (1, 10)),
        "Shillings": (5, (1, 2)),
        "Crowns": (0, (0, 0)),
        "Domestics": (0, (0, 0)),
        "Gems": (0, (0, 0)),
        "Art": (0, (0, 0)),
        "Cloth": (1, (1, 1)),
    },
    "Citizen": {
        "Pennies": (50, (1, 20)),
        "Shillings": (20, (1, 5)),
        "Crowns": (2, (1, 1)),
        "Domestics": (0, (0, 0)),
        "Gems": (1, (1, 1)),
        "Art": (0, (1, 1)),
        "Cloth": (5, (1, 1)),
    },
    "Noble": {
        "Pennies": (0, (0, 0)),
        "Shillings": (50, (1, 10)),
        "Crowns": (25, (1, 5)),
        "Domestics": (10, (1, 3)),
        "Gems": (25, (1, 2)),
        "Art": (5, (1, 1)),
        "Cloth": (20, (1, 2)),
    },
    # creature
    "Small Monster": {
        "Pennies": (20, (1, 10)),
        "Shillings": (10, (1, 5)),
        "Crowns": (1, (1, 3)),
        "Domestics": (0, (0, 0)),
        "Gems": (1, (1, 1)),
        "Art": (0, (0, 0)),
        "Cloth": (0, (0, 0)),
    },
    "Large Monster": {
        "Pennies": (50, (1, 100)),
        "Shillings": (25, (1, 20)),
        "Crowns": (10, (1, 5)),
        "Domestics": (5, (1, 5)),
        "Gems": (10, (1, 3)),
        "Art": (0, (0, 0)),
        "Cloth": (0, (0, 0)),
    },
    "Legendary Monster": {
        "Pennies": (100, (2, 200)),
        "Shillings": (50, (5, 50)),
        "Crowns": (25, (1, 10)),
        "Domestics": (5, (1, 5)),
        "Gems": (20, (1, 10)),
        "Art": (0, (0, 0)),
        "Cloth": (0, (0, 0)),
    },
}

# Domestic Table
domestics_table: dict = {
    (1, 10): "Candelabra & Candles",
    (11, 20): "Cups & Glasses",
    (21, 30): "Cutlery",
    (31, 40): "Goblets",
    (41, 50): "Lantern & Oil",
    (51, 60): "Pipe & Tobacco",
    (61, 70): "Plates & Bowls",
    (71, 80): "Teaware",
    (81, 90): "Wine & Spirits",
    (91, 100): "Other Trapping",
}

# Art Table
art_table: dict = {
    (1, 3): "Abacus",
    (4, 6): "Carved Dragon Egg",
    (7, 9): "Ceremonial Weapon",
    (10, 12): "Chalice",
    (13, 15): "Costume Mask",
    (16, 18): "Crown (false or real)",
    (19, 21): "Decorative Comb",
    (22, 24): "Doll",
    (25, 27): "Engraved Dice",
    (28, 30): "Figurine",
    (31, 33): "Flask",
    (34, 36): "Flute",
    (37, 39): "Framed Portrait",
    (40, 42): "Game Board & Pieces",
    (43, 45): "Harp (Toy)",
    (46, 48): "Idol",
    (49, 51): "Instrument",
    (52, 54): "Ivory Drinking Horn",
    (55, 57): "Jewelry Box",
    (58, 60): "Large Statue",
    (61, 63): "Letter Opener",
    (64, 66): "Mini Sarcophagus",
    (67, 69): "Music Box",
    (70, 72): "Orrery",
    (73, 75): "Painting",
    (76, 78): "Paperweight",
    (79, 81): "Pewter Mug",
    (82, 84): "Sceptre",
    (85, 87): "Small Mirror",
    (88, 90): "Statuette",
    (91, 93): "Vase",
    (94, 96): "War Mask",
    (97, 99): "Wood Carving",
    (100, 100): "Other Trapping",
}

# Clothing Table
clothing_table: dict = {
    (1, 3): "Animal Pelt",
    (4, 6): "Belt",
    (7, 9): "Blankets",
    (10, 12): "Boots & Shoes",
    (13, 15): "Cape",
    (16, 18): "Cloak",
    (19, 21): "Fine Clothes",
    (22, 24): "Practical Clothes",
    (25, 27): "Travel Clothes",
    (28, 30): "Coat",
    (31, 33): "Costume",
    (34, 36): "Courtly Garb",
    (37, 39): "Fine Drapes",
    (40, 42): "Embroidery",
    (43, 45): "Fur Coat",
    (46, 48): "Fur Stole",
    (49, 51): "Fine Gloves",
    (52, 54): "Practical Gloves",
    (55, 57): "Silk Handkerchief",
    (58, 60): "Fancy Hat",
    (61, 63): "Practical Hat",
    (64, 66): "Fine Linens",
    (67, 69): "Practical Linens",
    (70, 72): "Pouch",
    (73, 75): "Purse",
    (76, 78): "Robes",
    (79, 81): "Fine Rug",
    (82, 84): "Woven Rug",
    (85, 87): "Shawl",
    (88, 90): "Tapestry",
    (91, 93): "Uniform",
    (94, 96): "Walking Cane",
    (97, 99): "Wall Hanging",
    (100, 100): "Other Trapping",
}

# Gems Table
gems_table: dict = {
    "Brass": {
        1: "Amber",
        2: "Agate",
        3: "Hematite",
        4: "Lapis Lazuli",
        5: "Malachite",
        6: "Rhodocrosite",
        7: "Obsidian",
        8: "Quartz",
        9: "Tiger Eye",
        10: "Turquoise",
    },
    "Silver": {
        1: "Amethyst",
        2: "Aquamarine",
        3: "Bloodstone",
        4: "Citrine",
        5: "Jasper",
        6: "Moonstone",
        7: "Onyx",
        8: "Peridot",
        9: "Topaz",
        10: "Zircon",
    },
    "Gold": {
        1: "Beryl",
        2: "Diamond",
        3: "Emerald",
        4: "Garnet",
        5: "Jade",
        6: "Opal",
        7: "Pearl",
        8: "Ruby",
        9: "Sapphire",
        10: "Spinel",
    },
}

# Jewelry Table
jewelry_table: dict = {
    range(1, 6): "Amulet",
    range(6, 10): "Armlet",
    range(10, 15): "Bracelet",
    range(15, 19): "Brooch",
    range(19, 23): "Chain",
    range(23, 26): "Choker",
    range(26, 30): "Circlet",
    range(30, 34): "Cuff Links",
    range(34, 43): "Earrings",
    range(43, 47): "Hairpin",
    range(47, 51): "Hatpin",
    range(51, 56): "Locket",
    range(56, 61): "Medallion",
    range(61, 66): "Necklace",
    range(66, 70): "Pendant",
    range(70, 74): "Pocket Watch",
    range(74, 78): "Prayer Beads",
    range(78, 83): "Decorative Ring",
    range(83, 87): "Promise Ring",
    range(87, 91): "Wedding Ring",
    range(91, 96): "Signet Ring",
    range(96, 101): "Torc",
}

# Other Items
other_trappings: dict = {
    "Packs & Containers": {
        range(1, 11): "Backpack",
        range(11, 16): "Barrel",
        range(16, 21): "Cask",
        range(21, 31): "Flask",
        range(31, 36): "Jug",
        range(36, 41): "Pewter Stein",
        range(41, 51): "Pouch",
        range(51, 61): "Purse",
        range(61, 66): "Sack",
        range(66, 71): "Large Sack",
        range(71, 76): "Saddlebags",
        range(76, 86): "Sling Bag",
        range(86, 91): "Scroll Case",
        range(91, 101): "Waterskin",
    },
    "Food & Drink": {
        range(1, 11): "pint Ale",
        range(11, 16): "keg Ale",
        range(16, 21): "pint Bugman’s Ale",
        range(21, 26): "Food - groceries/day",
        range(26, 31): "Imperial Breakfast",
        range(31, 41): "Meal - Inn",
        range(41, 51): "Rations - 1 day",
        range(51, 61): "Rations - 1 week",
        range(61, 71): "Rumster Pie",
        range(71, 76): "Spirits - pint",
        range(76, 81): "Wine - bottle",
        range(81, 86): "Wine - quality (bottle)",
        range(86, 91): "Wine - rare (bottle)",
        range(91, 101): "Wine/Spirits - drink",
    },
    "Books & Documents": {
        range(1, 6): "Book - Apothecary",
        range(6, 11): "Book - Art",
        range(11, 16): "Book - Cryptography",
        range(16, 21): "Book - Engineer",
        range(21, 26): "Book - Illuminated",
        range(26, 31): "Book - Law",
        range(31, 51): "Book - Literature",
        range(51, 56): "Book - Magic",
        range(56, 61): "Book - Medicine",
        range(61, 76): "Book - Printed",
        range(76, 86): "Book - Religion",
        range(86, 91): "Legal Document",
        range(91, 96): "Map",
        range(96, 101): "Parchment (12)",
    },
    "Prosthetics/Disguises": {
        range(1, 11): "Costume",
        range(11, 21): "Disguise Kit",
        range(21, 31): "Eye Patch",
        range(31, 41): "Face Powder",
        range(41, 51): "False Eye",
        range(51, 61): "False Leg",
        range(61, 71): "Gilded Nose",
        range(71, 76): "Hook",
        range(76, 81): "Engineering Marvel",
        range(81, 86): "Mask - Costume",
        range(86, 91): "Mask - War",
        range(91, 101): "Wooden Teeth",
    },
    "Occupational Tools": {
        range(1, 3): "Abacus",
        range(3, 6): "Animal Trap",
        range(6, 8): "Boat Hook",
        range(8, 10): "Broom",
        range(10, 12): "Bucket",
        range(12, 14): "Chisel",
        range(14, 16): "Clothes Pegs (12)",
        range(16, 18): "Comb",
        range(18, 21): "Crowbar",
        range(21, 23): "Ear Pick",
        range(23, 25): "Eyeglasses",
        range(25, 27): "Fish Hooks (12)",
        range(27, 29): "Fishing Line (spool)",
        range(29, 31): "Fishing Rod",
        range(31, 33): "Floor Brush",
        range(33, 35): "Gavel",
        range(35, 37): "Hammer",
        range(37, 39): "Hand Mirror",
        range(39, 41): "Hoe",
        range(41, 45): "Key",
        range(45, 49): "Knife",
        range(49, 51): "Lock Picks",
        range(51, 53): "Magnifying Glass",
        range(53, 55): "Manacles",
        range(55, 57): "Monocle",
        range(57, 59): "Mop",
        range(59, 61): "Nails (12)",
        range(61, 63): "Navigational Charts",
        range(63, 65): "Paint Brush",
        range(65, 67): "Pestle & Mortar",
        range(67, 69): "Pick",
        range(69, 71): "Pole (3 yards)",
        range(71, 73): "Quill Pen",
        range(73, 75): "Rake",
        range(75, 77): "Reading Lens",
        range(77, 79): "Saw",
        range(79, 81): "Sickle",
        range(81, 83): "Snare - wire",
        range(83, 85): "Spade",
        range(85, 88): "Spike",
        range(88, 90): "Stamp, engraved",
        range(90, 92): "Tongs, steel",
        range(92, 95): "Telescope",
        range(95, 99): "Trade Tools",
        range(99, 101): "Tweezers",
    },
    "Herbs, Meds & Drugs": {
        range(1, 3): "Adder’s Root",
        range(3, 6): "Alfunas",
        range(6, 8): "Antitoxin Kit",
        range(8, 10): "Avermanni Blueleaf",
        range(10, 12): "Bandage",
        range(12, 14): "Black Lotus",
        range(14, 16): "Clean Rag (12 strips)",
        range(16, 18): "Crutch",
        range(18, 21): "Digestive Tonic",
        range(21, 23): "Earth Root",
        range(23, 25): "Faxtoryll",
        range(25, 27): "Field Medical Kit (12)",
        range(27, 29): "Gesundheit",
        range(29, 31): "Hawthorn",
        range(31, 33): "Healing Draught",
        range(33, 35): "Healing Poultice",
        range(35, 37): "Heartkill",
        range(37, 39): "Herbal Ointment",
        range(39, 41): "Juck",
        range(41, 43): "Lady’s Mantle",
        range(43, 45): "Lye Soap (1 bar)",
        range(45, 47): "Mad Cap Mushrooms",
        range(47, 49): "Mage-Leaf",
        range(49, 51): "Mandrake Root",
        range(51, 53): "Medical Tools",
        range(53, 55): "Medicinal Alcohol",
        range(55, 57): "Moonflower",
        range(57, 59): "Needle & Thread",
        range(59, 61): "Nerve Tonic",
        range(61, 63): "Nightshade",
        range(63, 65): "Oxleaf",
        range(65, 67): "Ranald’s Delight",
        range(67, 69): "Salwort",
        range(69, 71): "Sigmafoil",
        range(71, 73): "Spellwort",
        range(73, 75): "Spiderleaf",
        range(75, 77): "Spit",
        range(77, 79): "Tarrabeth",
        range(79, 81): "Valerian",
        range(81, 83): "Vanera",
        range(83, 85): "Vinegar",
        range(85, 87): "Vitality Draught",
        range(87, 89): "Weirdroot",
        range(89, 91): "Willow",
        range(91, 93): "Yarrow",
        range(93, 95): "Zitterwort",
    },
    "Clothing & Accessories": {
        range(1, 6): "Amulet or Trinket",
        range(6, 8): "Animal Pelt",
        range(8, 10): "Belt",
        range(10, 11): "Boots",
        range(11, 13): "Breeches",
        range(13, 15): "Cape",
        range(15, 17): "Cloak",
        range(17, 19): "Clothing - Fine",
        range(19, 21): "Clothing - Practical",
        range(21, 23): "Clothing - Travel",
        range(23, 25): "Coat",
        range(25, 27): "Courtly Garb",
        range(27, 29): "Fine Dress",
        range(29, 31): "Fur Coat",
        range(31, 33): "Fur Stole",
        range(33, 35): "Gloves - Fine",
        range(35, 37): "Gloves - Practical",
        range(37, 39): "Gloves - Fur",
        range(39, 41): "Handkerchief",
        range(41, 43): "Hat - Fancy",
        range(43, 45): "Hat - Practical",
        range(45, 47): "Hood",
        range(47, 49): "Jewellery",
        range(49, 51): "Mask (Costume/War)",
        range(51, 53): "Neckerchief",
        range(53, 55): "Perfume",
        range(55, 57): "Pins (6)",
        range(57, 59): "Religious Symbol",
        range(59, 61): "Riding Boots & Spurs",
        range(61, 63): "Robes",
        range(63, 65): "Scarf",
        range(65, 67): "Sceptre",
        range(67, 69): "Shawl",
        range(69, 71): "Shoes",
        range(71, 73): "Signet Ring",
        range(73, 75): "Tattoo",
        range(75, 77): "Uniform",
        range(77, 79): "Walking Cane",
        range(79, 81): "Wig",
    },
    "Miscellaneous Items": {
        range(1, 3): "Ball",
        range(3, 5): "Baton",
        range(5, 7): "Bedroll",
        range(7, 9): "Bell - small",
        range(9, 11): "Blanket",
        range(11, 13): "Bowl",
        range(13, 15): "Candle (12)",
        range(15, 17): "Canvas Tarp",
        range(17, 19): "Chain - 1 yard",
        range(19, 21): "Chalk",
        range(21, 23): "Charcoal Stick",
        range(23, 25): "Coach Horn",
        range(25, 27): "Cooking Pot",
        range(27, 29): "Cup",
        range(29, 31): "Cutlery - Plain",
        range(31, 33): "Cutlery - Jewelled (set)",
        range(33, 35): "Davrich Lamp",
        range(35, 37): "Deck of Cards",
        range(37, 39): "Dice",
        range(39, 41): "Doll",
        range(41, 43): "Grappling Hook",
        range(43, 45): "Kettle",
        range(45, 47): "Kindling/Firewood",
        range(47, 49): "Lamp Oil",
        range(49, 51): "Lantern",
        range(51, 53): "Lantern - Storm",
        range(53, 55): "Linens",
        range(55, 57): "Matches",
        range(57, 59): "Mattress, Feather",
        range(59, 61): "Mess Kit",
        range(61, 63): "Mouth Harp",
        range(63, 65): "Musical Instrument",
        range(65, 67): "Pan",
        range(67, 69): "Pipe and Tobacco",
        range(69, 71): "Placard",
        range(71, 73): "Plate",
        range(73, 75): "Pot Lamp",
        range(75, 77): "Rags",
        range(77, 79): "Rope - 10 yards",
        range(79, 81): "Rug",
        range(81, 83): "String, 10 yards",
        range(83, 85): "Tapestry",
        range(85, 87): "Tent",
        range(87, 89): "Tinderbox",
        range(89, 91): "Torch (12)",
        range(91, 94): "Whistle",
    },
}
