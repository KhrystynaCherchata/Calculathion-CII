from __future__ import annotations


def g1(co2_emission: float, distance: float, dwt: float | None = None, gt: float | None = None) -> float | None:
    grams_per_ton_km = None
    if dwt:
        grams_per_ton_km = (co2_emission / (dwt * distance)) * 1000000
    if gt:
        grams_per_ton_km = (co2_emission / (gt * distance)) * 1000000
    print(f"CO2 emissions per tonne-kilometre: {grams_per_ton_km:.2f} г")
    return round(grams_per_ton_km, 2) if grams_per_ton_km else grams_per_ton_km





#This g1 function is designed to calculate the CO2 emissions per
# ton-kilometer based on the given parameters. Let's break down the logic step by step:
# 1. Parameters such as co2_emission (emission volume), distance (distance traveled),
# dwt (dead-weight tonnage of the vessel), and gt (gross tonnage of the vessel) are accepted.
# 2. A variable named grams_per_ton_km is created and initialized to None.
# 3. It checks whether the dwt parameter is provided.
# If so, it calculates the emissions per ton-kilometer using the formula: co2_emission / (dwt * distance) * 1000000.
# The result is stored in the grams_per_ton_km variable.
# 4. If the gt parameter is provided, a similar calculation is performed using the vessel's weight in gross tons.
# 5. A message is printed on the screen with the calculated emissions value:
# "CO2 emissions per tonne-kilometre: {grams_per_ton_km:.2f} g".
# 6. The function returns the rounded value of grams_per_ton_km to two decimal places if it exists,
# or None if the corresponding vessel weight (dwt or gt) was not provided.
# In summary, this function allows for the calculation of CO2 emissions per ton-kilometer,
# taking into account the vessel's weight in deadweight tons (dwt) or gross tons (gt).