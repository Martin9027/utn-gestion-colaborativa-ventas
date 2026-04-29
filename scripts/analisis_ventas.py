# Se cargan manualmente cantidades y precios de ventas simuladas
cantidad_mouse1 = 10
precio_mouse1 = 8000

cantidad_teclado1 = 5
precio_teclado1 = 15000

cantidad_mouse2 = 8
precio_mouse2 = 8000

cantidad_monitor1 = 2
precio_monitor1 = 70000

cantidad_teclado2 = 6
precio_teclado2 = 15000

# Se calcula el dinero producido por cada venta individual
venta1 = cantidad_mouse1 * precio_mouse1
venta2 = cantidad_teclado1 * precio_teclado1
venta3 = cantidad_mouse2 * precio_mouse2
venta4 = cantidad_monitor1 * precio_monitor1
venta5 = cantidad_teclado2 * precio_teclado2

# Se suman todas las ventas para obtener la recaudacion total
ventas_totales = venta1 + venta2 + venta3 + venta4 + venta5

# Se agrupan las cantidades para identificar cual producto tuvo mayor salida
mouse_total = cantidad_mouse1 + cantidad_mouse2
teclado_total = cantidad_teclado1 + cantidad_teclado2
monitor_total = cantidad_monitor1

print("Ventas totales:", ventas_totales)

# Mediante condicionales se compara que producto vendio mas unidades
if mouse_total > teclado_total and mouse_total > monitor_total:
    print("Producto mas vendido: Mouse")
elif teclado_total > mouse_total and teclado_total > monitor_total:
    print("Producto mas vendido: Teclado")
else:
    print("Producto mas vendido: Monitor")
