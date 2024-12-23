def convert_num(value, from_unit, to_unit):
    conversion_factors = {
        "Binary(base 2)": 2,
        "Octal(base 8)": 8,
        "Decimal(base 10)": 10,
        "Hexadecimal(base 16)": 16,
    }
    
    from_base = conversion_factors[from_unit]
    decimal_value = int(value, from_base)
  
    to_base = conversion_factors[to_unit]
    if to_base == 2:  
        result = bin(decimal_value)[2:]  
    elif to_base == 8:  
        result = oct(decimal_value)[2:]  
    elif to_base == 10:
        result = str(decimal_value)
    elif to_base == 16:
        result = hex(decimal_value)[2:].upper() 
    else:
        raise ValueError("Unsupported base.")
    
    return result