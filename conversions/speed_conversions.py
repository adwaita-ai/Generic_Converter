def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": 1,              
        "m/hr": 1 / 3600,      
        "m/min": 1 / 60,        
        "km/s": 1000,           
        "km/hr": 1000 / 3600,   
        "km/min": 1000 / 60,    
        "cm/s": 0.01,           
        "cm/hr": 0.01 / 3600,   
        "cm/min": 0.01 / 60,    
        "mm/s": 0.001,          
        "mm/hr": 0.001 / 3600,  
        "mm/min": 0.001 / 60,   
        "mile": 1609.34,        
    }


    value_in_meters_per_second = value * conversion_factors[from_unit]
    result = value_in_meters_per_second / conversion_factors[to_unit]
    return result