def cliente(info):
    nombre = info["nombre"]
    edad = info["edad"]
    pir = info["primer_ingreso"]

    d = 0.05
    cost = 'N/A'
    attr = 'N/A'
    apto = True

    if edad > 18:
        cost = 20000
        attr = 'X-Treme'
        if pir:
            cost -= cost * d
    elif 15 <= edad <= 18:
        cost = 5000
        attr = 'Carros chocones'
        if pir:
            d = 0.07
            cost -= cost * d
    elif 7 <= edad <= 15:
        cost = 10000
        attr = 'Sillas voladoras'
        if pir:
            cost -= cost * d
    else:
        apto = False

    return {'nombre': nombre, 'edad': edad, 'atraccion': attr,'apto': apto, 'primer_ingreso': pir, 'total_boleta': cost}

t1 = {'id_cliente': 4, 'nombre': 'Tatiana Ruiz', 'edad': 8, 'primer_ingreso': True}
r1 = cliente(t1)
print(r1)