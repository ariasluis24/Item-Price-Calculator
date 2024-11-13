from decimal import Decimal, ROUND_HALF_UP

IVA = Decimal(1.16)
IVA_Subtotal = Decimal(0.16)

def calcular_total(valores):
    return sum(Decimal(valor) for valor in valores)

'''
def distribuir_items(items, renglones):
    # // TODO Fail when there is 2 rows and 5 items, but the order should get one row with 4 items and the other row just 1 item.
    # // TODO Try to do the distribution manually.
    # Distribuye los items entre los renglones
    items_por_renglon = [items // renglones] * renglones
    sobrantes = items % renglones

    for i in range(sobrantes):
        items_por_renglon[i] += 1
    
    return items_por_renglon

'''

def distribuir_items_manual(renglones):
    my_list = []
    for i in range(renglones):
        items_por_renglon = int(input(f' Cuantos items tiene el renglon {i+1}?:  '))
        my_list.append(items_por_renglon)
    
    return my_list

def obtener_valores(items_por_renglon):
    valores = []
    for i, num_items in enumerate(items_por_renglon):
        print(f"\nRenglón {i+1} (con {num_items} item(s)):")
        if num_items == 1:
            valor = Decimal(input("  Ingresa el valor unitario del item: "))
        else:
            valor = Decimal(input(f"  Ingresa el valor unitario del item (se multiplicará por {num_items}): ")) * num_items
        valores.append(valor)
    return valores

'''
# def ajustar_precios(precio_deseado, valores):
    
#     total_inicial = calcular_total(valores)
    
#     ajuste_necesario = Decimal(precio_deseado) - total_inicial
    
#     # Proporción para ajustar cada ítem
#     proporciones = [Decimal(precio) / Decimal(total_inicial) for precio in valores]
    
#     precios_ajustados = []
#     exceso_a_redistribuir = 0  # Para manejar ajustes negativos

#     for i, precio in enumerate(valores):
#         ajuste = ajuste_necesario * proporciones[i]
#         nuevo_precio = Decimal(precio) + Decimal(ajuste) 

#         # Si el ajuste hace que el precio sea negativo, acumula el exceso
#         if nuevo_precio < 0:
#             exceso_a_redistribuir += abs(nuevo_precio)
#             precios_ajustados.append(0)
#         else:
#             precios_ajustados.append(nuevo_precio)
    
#     # Redistribuye el exceso a los ítems no negativos
#     for i, precio in enumerate(precios_ajustados):
#         if exceso_a_redistribuir > 0 and precio > 0:
#             # Asigna la menor cantidad entre el exceso y el precio disponible
#             redistribuir = min(exceso_a_redistribuir, precio)
#             precios_ajustados[i] += redistribuir
#             exceso_a_redistribuir -= redistribuir

#     return precios_ajustados

'''

def ajustar_precios(precio_deseado, valores):
    
    # Determinar si todos los valores son enteros
    todos_enteros = all(float(precio).is_integer() for precio in valores)
    
    # Calcular el total inicial
    total_inicial = sum(map(Decimal, valores))
    
    # Calcular el ajuste necesario
    ajuste_necesario = Decimal(precio_deseado) - total_inicial
    
    # Proporción para ajustar cada ítem
    proporciones = [Decimal(precio) / total_inicial for precio in valores]
    
    precios_ajustados = []
    exceso_a_redistribuir = Decimal(0)  # Para manejar ajustes negativos

    for i, precio in enumerate(valores):
        # Calcular el ajuste proporcional
        ajuste = ajuste_necesario * proporciones[i]
        nuevo_precio = Decimal(precio) + ajuste
        
        # Redondear a entero si todos los valores son enteros
        if todos_enteros:
            nuevo_precio = nuevo_precio.to_integral_value(ROUND_HALF_UP)
        
        # Si el ajuste hace que el precio sea negativo, acumula el exceso
        if nuevo_precio < 0:
            exceso_a_redistribuir += abs(nuevo_precio)
            precios_ajustados.append(Decimal(0))
        else:
            precios_ajustados.append(nuevo_precio)
    
    # Redistribuye el exceso a los ítems no negativos
    for i, precio in enumerate(precios_ajustados):
        if exceso_a_redistribuir > 0 and precio > 0:
            redistribuir = min(exceso_a_redistribuir, precio)
            precios_ajustados[i] += redistribuir
            exceso_a_redistribuir -= redistribuir

    return precios_ajustados

def ajustar_precios_con_IVA(precio_deseado, valores):
    
    total_inicial = calcular_total(valores)
    
    ajuste_necesario = (round((Decimal(precio_deseado) / Decimal(1.16)),2)) - (Decimal(total_inicial))
    
    # Proporción para ajustar cada ítem
    proporciones = [Decimal(precio) / Decimal(total_inicial) for precio in valores]
    
    precios_ajustados = []
    exceso_a_redistribuir = 0  # Para manejar ajustes negativos

    for i, precio in enumerate(valores):
        ajuste = ajuste_necesario * proporciones[i]
        nuevo_precio = Decimal(precio) + Decimal(ajuste) 

        # Si el ajuste hace que el precio sea negativo, acumula el exceso
        if nuevo_precio < 0:
            exceso_a_redistribuir += abs(nuevo_precio)
            precios_ajustados.append(0)
        else:
            precios_ajustados.append(nuevo_precio)
    
    # Redistribuye el exceso a los ítems no negativos
    for i, precio in enumerate(precios_ajustados):
        if exceso_a_redistribuir > 0 and precio > 0:
            # Asigna la menor cantidad entre el exceso y el precio disponible
            redistribuir = min(exceso_a_redistribuir, precio)
            precios_ajustados[i] += redistribuir
            exceso_a_redistribuir -= redistribuir

    return precios_ajustados
