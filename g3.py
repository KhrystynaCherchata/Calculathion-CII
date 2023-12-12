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


#Certainly! Let's break down the logic of the provided Python code:
    # 1. *Dictionary Definition:* python
# The code defines a dictionary named YEAR_Z,
# where keys are years (as strings) and values
# are corresponding numeric values.
    # 2. *Function Definition:
    # def g3(year: str, result_g2: float):
# The function g3 is defined with two
# parameters: year (a string representing the year) and result_g2 (a float).
    # 3. *Year Check:*
# It checks if the input year, converted to an integer, is less than 2027.
    # 4. *Get Z Value:*
    # python
    # z = YEAR_Z.get(str(year))
# It retrieves the corresponding value for the
# given year from the YEAR_Z dictionary. The get method is used to avoid potential KeyError.
    # 5. *Calculation and Exception Handling:
# Inside the try block, it calculates result_g3
# using the formula (result_g2 * (100 - z)) / 100.
# If there's a TypeError (e.g., if z is not a numeric value),
# it catches the exception and prints an error message.
    # 6. *Else Clause for Years >= 2027:If the input year is greater than or
# equal to 2027, the function returns None.
# To summarize, the function takes a year and a float,
# looks up a corresponding adjustment value (z) from the YEAR_Z dictionary,
# and calculates a new result (result_g3). If there's an issue with the type of z,
# it prints an error message. If the year is 2027 or later, the function returns None.