def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1e3,  
        "Gram": 1,
        "Centigram": 1e-2,
        "Milligram": 1e-3,
        "Microgram": 1e-6,
        "Nanogram": 1e-9,
        "Pound": 453.592,
        "Ounce": 28.3495,
        "Ton": 1e6,
        "Quintal": 1e5,
    }

    value_in_grams = value * conversion_factors[from_unit]
    result = value_in_grams / conversion_factors[to_unit]
    return result
