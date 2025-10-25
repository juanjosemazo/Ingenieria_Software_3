from graphviz import Digraph

# Crear el diagrama de flujo para el mapa de valor visual
dot = Digraph(comment="Mapa de Valor Visual - Proyecto Agrícola")
dot.attr(rankdir="LR", size="8")

# Nodos principales
dot.node("A", "Productor Agrícola\n(Registra productos)")
dot.node("B", "Plataforma Digital\n(Conexión directa)")
dot.node("C", "Consumidor Final\n(Compra productos)")

# Flujo de actividades
dot.node("D", "Recibe pago justo")
dot.node("E", "Transacción segura")
dot.node("F", "Precio más justo")

# Conexiones
dot.edges(["AB", "BC"])
dot.edge("A", "D", label="Valor entregado")
dot.edge("B", "E", label="Proceso clave")
dot.edge("C", "F", label="Beneficio")

# Guardar y renderizar
file_path = "c:\Users\Lenovo\Desktop\Prueba_programacion\mapa_valor_visual"
dot.render(file_path, format="png", cleanup=True)
file_path + ".png"
#Comentario