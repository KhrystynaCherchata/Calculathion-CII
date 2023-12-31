from __future__ import annotations

from g1 import g1
from g3 import g3


def lng_carrier_d_values(dwt_value: float):
    if dwt_value >= 100000:
        d1 = 0.89
        d2 = 0.98
        d3 = 1.06
        d4 = 1.13
    else:
        d1 = 0.78
        d2 = 0.92
        d3 = 1.10
        d4 = 1.37
    return d1, d2, d3, d4


def gas_carrier_d_values(dwt_value: float):
    if dwt_value >= 65000:
        d1 = 0.81
        d2 = 0.91
        d3 = 1.12
        d4 = 1.44
    else:  # here everything dwt_value < 65000
        d1 = 0.85
        d2 = 0.95
        d3 = 1.06
        d4 = 1.25
    return d1, d2, d3, d4


d_values_fun = {"gas carrier": gas_carrier_d_values,
                "lng carrier": lng_carrier_d_values}

d_values = {"bulk carrier": {
    "d1": 0.86,
    "d2": 0.94,
    "d3": 1.06,
    "d4": 1.18
},
    "tanker": {
        "d1": 0.82,
        "d2": 0.93,
        "d3": 1.08,
        "d4": 1.28
    },
    "container ship": {
        "d1": 0.83,
        "d2": 0.94,
        "d3": 1.07,
        "d4": 1.19
    },
    "general cargo ship": {
        "d1": 0.83,
        "d2": 0.94,
        "d3": 1.06,
        "d4": 1.19
    },
    "refrigerated cargo carrier": {
        "d1": 0.78,
        "d2": 0.91,
        "d3": 1.07,
        "d4": 1.20
    },
    "combination carrier": {
        "d1": 0.87,
        "d2": 0.96,
        "d3": 1.06,
        "d4": 1.14
    },
    "ro-ro cargo ship (vc)": {
        "d1": 0.86,
        "d2": 0.94,
        "d3": 1.06,
        "d4": 1.16
    },
    "ro-ro cargo ship": {
        "d1": 0.66,
        "d2": 0.9,
        "d3": 1.11,
        "d4": 1.37
    },
    "ro-ro passenger ship": {
        "d1": 0.72,
        "d2": 0.90,
        "d3": 1.12,
        "d4": 1.41
    },
    "cruise passenger ship": {
        "d1": 0.87,
        "d2": 0.95,
        "d3": 1.06,
        "d4": 1.16
    }
}


def g4(ship_type: str, result_g3: float, result_g1: float, dwt: float | None):
    if ship_type in d_values_fun:
        d1, d2, d3, d4 = d_values_fun.get(ship_type.lower())(dwt)
    else:
        d1, d2, d3, d4 = list(d_values.get(ship_type.lower()).values())
    print(f"{d1=} {result_g3=} {result_g1=}")
    print(f"d1 {result_g3 * d1}")
    print(f"d2 {result_g3 * d2}")
    print(f"d3 {result_g3 * d3}")
    print(f"d4 {result_g3 * d4}")
    a = result_g3 * d1
    b = result_g3 * d2
    c = result_g3 * d3
    d = result_g3 * d4
    if result_g1 < a:
        return "A"
    elif result_g1 < b:
        return "B"
    elif result_g1 < c:
        return "C"
    elif result_g1 < d:
        return "D"
    else:
        return "E"


#1. *lng_carrier_d_values and gas_carrier_d_values Functions:*
# - These functions take a dwt_value (deadweight tonnage) as input.
# - Based on the dwt_value, they calculate and return four values
# (d1, d2, d3, d4) specific to LNG carriers and gas carriers.
# 2. *d_values_fun Dictionary:*
# - Associates ship types ("gas carrier" or "lng carrier")
# with their respective functions (gas_carrier_d_values or lng_carrier_d_values).
# 3. *d_values Dictionary:*
# - Defines dictionaries for various ship types (e.g., "bulk carrier," "tanker," etc.).
# - Each ship type dictionary contains values (d1, d2, d3, d4) associated with G1 and G3 parameters.
# 4. *g4 Function:*
# - Takes parameters ship_type, result_g3, result_g1, and dwt.
# - Determines d1, d2, d3, d4 based on the ship type using the dictionaries.
# - Calculates values a, b, c, and d based on result_g3 and the calculated d values.
# - Compares result_g1 with these calculated values and returns a classification ("A," "B," "C," "D," or "E").
# The script seems to be part of a larger system for assessing ships,
# considering deadweight tonnage, G1, and G3 parameters to classify them into categories.
# If you have specific questions or if there's something specific you'd like to understand or modify, feel free to ask!