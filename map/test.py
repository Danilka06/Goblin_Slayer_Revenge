"""
for room in level_map:
    for y in room:
        for x in y:
            x is cell
"""


level_map = [
    [  # room     # x
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],  # y
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", " ", " ", " ", " ", " ", " ", "r", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", " ", " ", " ", " ", " ", "r", " ", "p", " ", " ", " ", " ", " ", " ", " ", "d"],
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "g", " ", " ", "w"],
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ]
]