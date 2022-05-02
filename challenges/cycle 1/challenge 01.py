# CDT (Term deposit) application

def CDT(user, capital, time):
    """
    user, str: Alfanumeric id of the user
    capital, int: Amount of money introduced to the CDT
    time, int: Months
    """
    
    
    interest = 0.03 # Fixed interest rate
    lost_percentage = 0.02 # In case the user retired the money before two months

    interest_value = (capital * interest * time) / 12
    
    if time <= 2: # If the user retires the money before two months
        # Negative value
        interest_value = - (capital * lost_percentage)

    total_value = capital + interest_value


    # As required by the challenge. Spanish return
    return f"Para el usuario {user} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {time} meses es: {total_value}"

# Example
print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366', 650000, 2))
