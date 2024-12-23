def convert_currency(value, from_unit, to_unit):
    conversion_factors = {
        "Dollar": 1.0,     
        "Euro": 1.1,           
        "Pound": 1.25,         
        "INR": 0.012,         
        "Dinar": 3.27,          
        "Yen": 0.0073,         
        "Dirham": 0.27,         
    }

    value_in_dollars = value / conversion_factors[from_unit]
    result = value_in_dollars * conversion_factors[to_unit]
    return result