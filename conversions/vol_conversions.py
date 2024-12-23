def convert_vol(value, from_unit, to_unit):
    conversion_factors = {
        "Cubic meter": 1, 
        "Cubic kilometer": 1e9,
        "Cubic centimeter": 1e-6,
        "Cubic millimeter": 1e-9,
        "Litre": 1e-3,
        "Kilolitre": 1,
        "Millilitre": 1e-6,
        "Barrel": 0.158987294928,  
        "Gallon": 0.00378541,      
        "Quart": 0.000946353,      
        "Pint": 0.000473176,       
        "Cubic mile": 4.16818183e12,
        "Cubic inch": 1.63871e-5
    }

    value_in_cubic_meters = value * conversion_factors[from_unit]
    result = value_in_cubic_meters / conversion_factors[to_unit]
    return result