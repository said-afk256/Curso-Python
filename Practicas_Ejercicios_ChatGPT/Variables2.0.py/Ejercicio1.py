# ==============================================================================
# MINIPROYECTO: GESTIÓN DE INVENTARIO Y CATEGORÍAS
# ==============================================================================

# 1. CREACIÓN DE DATOS FIJOS (Tuplas)
# Crea una tupla llamada 'categorias_fijas' que contenga: "Electrónica", "Línea Blanca", "Ferretería".
# Recuerda que usamos tuplas porque estas categorías no deben editarse por error.
categorias_fijas=tuple(["Electronica","Linea blanca","Ferreteria"])
print(f"Ejercicio 1: {categorias_fijas}")
print()

# 2. DESEMPAQUETADO
# Tienes el siguiente producto: producto_info = ("Laptop", "HP", 15000)
# Desempaqueta esa tupla en tres variables: nombre_prod, marca, precio.
producto_info=("Laptop","HP",15000)


nombre_producto,marca,precio=producto_info
print(f"Ejercicio2: {nombre_producto}")
print()

# 3. MANEJO DE CONJUNTOS (Sets)
# El sistema recibió etiquetas de búsqueda con duplicados: 
# etiquetas_sucias = ["oferta", "nuevo", "oferta", "pc", "nuevo"]
# Convierte esa lista a un conjunto llamado 'etiquetas_limpias' para eliminar los duplicados.
etiquetas_sucias = ["oferta", "nuevo", "oferta", "pc", "nuevo"]
etiquetas_limpias = set(etiquetas_sucias)

print(f"Ejercicio 3: {etiquetas_limpias}")
print()
# 4. OPERACIONES DE CONJUNTOS
# Tienes dos conjuntos de proveedores:
# proveedores_zona_a = {"Intel", "AMD", "Asus"}
# proveedores_zona_b = {"Intel", "AMD"}
# Comprueba si 'proveedores_zona_b' es un subconjunto de 'proveedores_zona_a' usando .issubset().

proveedores_zona_a = {"Intel", "AMD", "Asus"}
proveedores_zona_b = {"Intel", "AMD"}
verificacion_subset_proveedores=proveedores_zona_b.issubset(proveedores_zona_a)
print("Ejercicio 4: ")
if verificacion_subset_proveedores ==True:
    print("proveerdores_zona_b es un subconjunto de proveedores_zona_a")
else:
    print("Proveedores_zona_b no son un subconjuto de proveedores_zona_a")
print()

# ------------------------------------------------------------------------------
# EJERCICIO PARA TRABAJAR (Copia y completa):
# ------------------------------------------------------------------------------

# categorias_fijas = 
# producto_info = ("Laptop", "HP", 15000)
# (Desempaqueta aquí...)


# etiquetas_sucias = ["oferta", "nuevo", "oferta", "pc", "nuevo"]
# etiquetas_limpias = 

# proveedores_zona_a = {"Intel", "AMD", "Asus"}
# proveedores_zona_b = {"Intel", "AMD"}
# es_subconjunto = 

# ------------------------------------------------------------------------------
# MOSTRAR RESULTADOS (Usa f-strings):
# ------------------------------------------------------------------------------
print("--------------------------------------")
print()
# print(f"Categorías (Inmutables): {categorias_fijas}")
print(f"Categorías (Inmutables): {categorias_fijas}")

# print(f"Producto desempaquetado: {nombre_prod} de la marca {marca} cuesta ${precio}")
print(f"Producto desempaquetado: {nombre_producto} de la marca {marca} cuesta ${precio}")

# print(f"Etiquetas únicas: {etiquetas_limpias}")
print(f"Etiquetas únicas: {etiquetas_limpias}")

# print(f"¿La zona B es subconjunto de la A?: {es_subconjunto}")
print(f"¿La zona B es subconjunto de la A?: {verificacion_subset_proveedores}")
# ==============================================================================