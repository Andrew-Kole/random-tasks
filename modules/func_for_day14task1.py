ice_temperature = 0
gas_temperature = 100


def water_statement(water_temperature_local):
    if water_temperature_local <= 0:
        return "solid"
    elif 0 < water_temperature_local < 100:
        return "liquid"
    else:
        return "gas"


def water_statement_with_parametrs(water_temperature_local):
    if water_temperature_local <= ice_temperature:
        return "solid"
    elif ice_temperature < water_temperature_local < gas_temperature:
        return "liquid"
    else:
        return "gas"