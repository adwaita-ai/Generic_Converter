def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1, 
        "Kilometer": 1e3,
        "Decimeter": 0.1,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Fathom": 1.8288,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Inch": 0.0254,
        "Microinch": 2.54e-8, 
    }

    value_in_meters = value * conversion_factors[from_unit]
    result = value_in_meters / conversion_factors[to_unit]
    return result