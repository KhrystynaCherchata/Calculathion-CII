from g1 import g1
from g2 import g2
from g3 import g3
from g4 import g4


def run(co2_emission, distance, ship_type, year, gt=None, dwt=None):
    result_g1 = g1(co2_emission=co2_emission, distance=distance, dwt=dwt, gt=gt)
    result_g2 = g2(ship_type=ship_type, dwt=dwt, gt=gt)
    result_g3 = g3(year=year, result_g2=result_g2)
    if result_g3 and result_g1 and result_g2:
        result_g4 = g4(ship_type=ship_type, result_g3=result_g3, result_g1=result_g1, dwt=dwt)
        return result_g4
    else:
        print("Check Values")


if __name__ == "__main__":
    co2_emission = 16257.877
    distance = 69219
    ship_type = "Bulk carrier"
    year = 2024
    dwt = 69800
    print(run(co2_emission, distance, ship_type, year, dwt=dwt))

#- g1 and g2 are called with parameters co2_emission, distance, dwt, and gt.
# - g3 is called with parameters year and the result of g2.
# - If results from g1, g2, and g3 exist, then g4 is
# called with parameters ship_type, results from g3 and g1,
# and dwt. The result from g4 is returned from the function.