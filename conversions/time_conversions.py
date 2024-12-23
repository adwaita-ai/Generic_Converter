def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "Second": 1,
        "Millisecond": 1e-3,
        "Microsecond": 1e-6,
        "Nanosecond": 1e-9,
        "Minute": 60,
        "Hour": 3600,  
        "Day": 86400,  
        "Week": 604800,  
        "Month": 2628000,  
        "Year": 31536000,  
        "Decade": 315360000,  
        "Century": 3153600000,  
        "Millennium": 31536000000,  
    }

    value_in_seconds = value * conversion_factors[from_unit]
    result = value_in_seconds / conversion_factors[to_unit]
    return result
