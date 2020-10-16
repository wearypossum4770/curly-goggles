from enum import Enum


class Conversions:
    def ounces_to_gallons(self, fluid_ounces=None, gallon=None, us_measurements=True):
        if us_measurements:
            return 128

    # TEA_SPOON =1
    # TABLE_SPOON=2
    # FLUID_OUNCE = 3
    # CUP=4
    # PINT=5
    # QUART =6
    # GALLON = 7


class WeightConversions(Enum):
    DRY_OUNCE = 1
    POUND = 2


class SizeConversions(Enum):
    INCH = 1
    FOOT = 2
    YARD = 3
    MILE = 4


liquid_conversions = [
    ["from unit", "from value", "convert to", "to value"]["gal", 1, "oz", 128],
    [
        "oz",
        1,
        "oz",
    ],
]
