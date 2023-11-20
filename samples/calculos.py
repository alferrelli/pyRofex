cost = {
    'shares' :{
        'comision': 0.33,
        'ddm': 0.0802,
        'iva':21
        },
    'bonds' : {
        'comision': 0.49,
        'ddm': 0.01
     }
}

days_of_year = 365



def calculate_cost(amount_buy, amount_sell, instrument_type):

    
    if instrument_type == 'share':
        comision_b = round(amount_buy*cost['instrument_type']['comision'],4)
        ddm_b = round(amount_buy*cost['instrument_type']['ddm'],4)
        iva_comision_b = round(comision_b*cost['instrument_type']['iva'],4)    
        iva_ddm_b = round(cost['instrument_type']['iva'],2)

        comision_s = round(amount_sell*cost['instrument_type']['comision'],4)
        ddm_s = round(amount_sell*cost['instrument_type']['ddm'],4)
        iva_comision_s = round(comision_s*cost['instrument_type']['iva'],4)    
        iva_ddm_s = round(cost['instrument_type']['iva'],2)
    else:
        iva_comision = 0
        iva_ddm = 0

# Calculo las comision intradiarias, iva y ddm se cobra por las dos operaciones
    if comision_b > comision_s:
        comision = comision_b
        iva_comision = iva_comision_b
    else:
        comision = comision_s
        iva_comision = iva_comision_s
    
    ddm =  ddm_b + ddm_s
    iva_ddm = iva_comision_b + iva_ddm_s

    return (comision,ddm,iva_comision,iva_ddm)


def calculate_caucion(tb,risk_free_rate):
    pass

def calculate_tna(buy, sell,days):
    days_in_years = days*(1/days_of_year)
    tna = round(((sell-buy)/(buy*days_in_years))*100,3)
    return (tna-1.015) # menos la comision
