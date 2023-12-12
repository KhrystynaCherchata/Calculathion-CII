from __future__ import annotations


def bulk_carrier(dwt_value: float):
    if dwt_value >= 279000:
        # capacity = dtw_value
        a = 4745
        c = 0.622
    else:  # dwt_value < 279000
        a = 4745
        c = 0.622
    return a, c


def gas_carrier(dwt_value: float):
    if dwt_value >= 65000:
        # capacity = dtw_value
        a = 144050000000
        c = 2.071
    else:  # here everything dwt_value < 65000
        a = 8104
        c = 0.639
    return a, c


def tanker(dwt_value: float):
    a = 5247
    c = 0.610
    return a, c


def container_ship(dwt_value: float):
    a = 1984
    c = 0.489
    return a, c


def general_cargo_ship(dwt_value: float):
    if dwt_value >= 20000:
        a = 31948
        c = 0.792
    else:  # here everything dwt_value < 20000
        a = 588
        c = 0.3885
    return a, c


def refrigerated_cargo_carrier(dwt_value: float):
    a = 4600
    c = 0.557
    return a, c


def combination_carrier(dwt_value: float):
    a = 40853
    c = 0.812
    return a, c


def lng_carrier(dwt_value: float):
    if 100000 <= dwt_value:
        a = 9.827
        c = 0
    elif 65000 <= dwt_value < 100000:
        a = 144790000000000
        c = 2.673
    else:  # dwt_value < 65000
        a = 144790000000000
        c = 2.673
    return a, c


def ro_ro_cargo_ship(dwt_value: float):
    a = 10952
    c = 0.637
    return a, c


def ro_ro_cargo_ship_vc(gt_value: float):
    a = 5739
    c = 0.631
    return a, c


def ro_ro_passenger_ship(gt_value: float):
    a = 7540
    c = 0.587
    return a, c


def cruise_passenger_ship(gt_value: float):
    a = 930
    c = 0.383
    return a, c


SHIP_TYPE_DWT = {"bulk carrier": bulk_carrier, "gas carrier": gas_carrier,
                 "tanker": tanker, "container ship": container_ship,
                 "general cargo ship": general_cargo_ship,
                 "refrigerated cargo carrier": refrigerated_cargo_carrier,
                 "combination carrier": combination_carrier,
                 "lng carrier": lng_carrier,
                 "ro-ro cargo ship": ro_ro_cargo_ship}

SHIP_TYPE_GT = {"cruise passenger ship": cruise_passenger_ship,
                "ro-ro passenger ship": ro_ro_passenger_ship,
                "ro-ro cargo ship (vc)": ro_ro_cargo_ship_vc}


def g2(ship_type: str, dwt: float | None = None, gt: float | None = None):
    if dwt:
        fun = SHIP_TYPE_DWT.get(ship_type.lower())
        a, c = fun(dwt)  # if fun else None, None
    else:
        fun = SHIP_TYPE_GT.get(ship_type.lower())
        a, c = fun(gt)  # if fun else None, None
    capacity = dwt if dwt else gt
    if a and c:
        result_g2 = a * (capacity ** (-c))
        return round(result_g2, 3)
    return None


#Let's break down the logic of the code in more detail:
# 1. *Individual Ship Type Functions:*
    # - Each ship type has a dedicated function (e.g., bulk_carrier, gas_carrier) that calculates two parameters,
    # a and c,
    # based on the provided dead-weight tonnage (dwt_value).
    # - The values of a and c depend on specific conditions, such as the magnitude of dwt_value for each ship type.
# 2. *Main Calculation Function - g2:*
    # - This function takes three parameters: ship_type (a string representing the type of ship),
    # dwt (dead-weight tonnage), and gt (gross tonnage).
    # - It determines whether dwt or gt is provided and selects the appropriate
    # ship type function accordingly from the dictionaries SHIP_TYPE_DWT or SHIP_TYPE_GT.
    # - Calls the selected function to obtain values for a and c.
    # - Calculates the capacity (capacity) based on the provided parameter (dwt or gt).
    # - Computes the result of the formula a * (capacity ** (-c)) and rounds it to three decimal places.
    # - Returns the calculated result.
# 3. *Ship Type Dictionaries:*
    # - SHIP_TYPE_DWT contains mappings from ship types to
    # functions that calculate parameters based on dead-weight tonnage.
    # - SHIP_TYPE_GT contains mappings from ship types to
    # functions that calculate parameters based on gross tonnage.
 # 4. *Conditional Statements in Ship Type Functions:*
    # - The ship type functions often have conditional statements
    # to determine the values of a and c based on the magnitude of dwt_value.
# 5. *Special Cases in lng_carrier Function:*
    # - The lng_carrier function has specific ranges for dwt_value
    # and handles cases where the value is above 100,000, between 65,000 and 100,000, or below 65,000.
# 6. *Result Handling:*
    # - If a and c are obtained successfully,
    # the g2 function calculates and returns the result. If not, it returns None.
    # Overall, this code provides a modular and extensible
    # structure for calculating a performance parameter (g2)
    # for various types of ships based on either dead-weight tonnage
    # or gross tonnage. It uses functions and dictionaries to organize
    # and manage the ship type-specific logic.