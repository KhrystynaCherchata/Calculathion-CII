YEAR_Z = {"2023": 5,
          "2024": 7,
          "2025": 9,
          "2026": 11}


def g3(year: str, result_g2: float):
    if int(year) < 2027:
        z = YEAR_Z.get(str(year))
        try:
            result_g3 = result_g2 * (100 - z) / 100
            return result_g3
        except TypeError as err:
            print("z has incorrect value")
    else:
        return None
