def parse(feet, inches):
    feet = float(feet)
    inches = float(inches)
    return feet, inches
def convert(feet, inches):
    result = feet * 0.3048 + inches * 0.254
    return result
