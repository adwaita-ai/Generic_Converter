def convert_temp(value, from_unit, to_unit):
    conversion_formulas = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Celsius", "Newton"): lambda x: x * 33/100,


        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Fahrenheit", "Newton"): lambda x: (x - 32) * 11/60,
    

        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        ("Kelvin", "Newton"): lambda x: (x - 273.15) * 33/100,


        ("Newton", "Celsius"): lambda x: x * 100/33,
        ("Newton", "Fahrenheit"): lambda x: (x * 60/11) + 32,
        ("Newton", "Kelvin"): lambda x: (x * 100/33) + 273.15,
       
    }

    if (from_unit, to_unit) in conversion_formulas:
        result = conversion_formulas[(from_unit, to_unit)](value)
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

    return result