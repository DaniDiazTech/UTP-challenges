def AutoPartes(ventas: list):
    return dict(zip(range(len(ventas)), ventas))

def consultaRegistro(ventas, idProducto):
    f = False
    for item in ventas.values():
        if item[0] == idProducto:
            print(f"Producto consultado : {item[0]}  Descripción  {item[1]}  #Parte  {item[2]}  Cantidad vendida  {item[3]}  Stock  {item[4]}  Comprador {item[5]}  Documento  {item[6]}  Fecha Venta  {item[7]}")
            f = True
    if f is False:
        print("No hay registro de venta de ese producto")




t1 = ([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')], 2010)

t2 = ([
 (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
 (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
 (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
 (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')], 2001)

t3 = ([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')], 9852)


print(consultaRegistro(AutoPartes(t1[0]), t1[1]))
print(consultaRegistro(AutoPartes(t2[0]), t2[1]))
c3 = consultaRegistro(AutoPartes(t3[0]), t3[1])
print(c3 == "Producto consultado : 9852  Descripción  Culata  #Parte  XC9875  Cantidad vendida  2  Stock  165  Comprador Luis Molero  Documento  3455846  Fecha Venta  14/06/2020\nProducto consultado : 9852  Descripción  Culata  #Parte  XC9875  Cantidad vendida  2  Stock  165  Comprador Jose Mejia  Documento  1355846  Fecha Venta  14/06/2020")
