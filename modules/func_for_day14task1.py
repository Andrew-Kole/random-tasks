def water_statement(water_temperature_local):
    if water_temperature_local <= 0:
        return "solid"
    elif 0 < water_temperature_local < 100:
        return "liquid"
    else:
        return "gas"