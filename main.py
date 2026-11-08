from conciertos import Concierto, Usuario, EntradaGrada, EntradaPista, EntradaVIP 

c1 = Concierto("David Bisbal", "Sevilla", 50.0, 100, True)
c2 = Concierto("Maluma", "Madrid", 60.0, 120, True)
c3 = Concierto("Alejandro Sanz", "Valencia", 45.0, 80, True)
conciertos = [c1, c2, c3]


u1 = Usuario("Antonio", 46)
u2 = Usuario("Milan", 19)
u3 = Usuario("Frida", 50)
usuarios = [u1, u2, u3]


u1.comprar_entrada(c1, "pista")
u1.comprar_entrada(c3, "vip")
u2.comprar_entrada(c2, "grada")
u2.comprar_entrada(c3, "pista")
u3.comprar_entrada(c1, "vip")
u3.comprar_entrada(c3, "pista")


u1.valorar(c1, 8)
u2.valorar(c2, 9)
u3.valorar(c3, 10)


total_entradas = 0
total_pista = 0
total_grada = 0
total_vip = 0
recaudacion_total = 0
mas_vendidas = None
max_entradas = 0
menos_vendidas = None
min_entradas = 100

for concierto in conciertos:
    vendidas = 0
    for entrada in concierto.entradas_vendidas:
        vendidas += 1
        texto = str(entrada)
        if "pista" in texto:
            total_pista += 1
        elif "grada" in texto:
            total_grada += 1
        elif "VIP" in texto:
            total_vip += 1

    total_entradas += vendidas
    recaudacion_total += concierto.calcular_recaudacion()

    if mas_vendidas is None or vendidas > max_entradas:
        mas_vendidas = concierto
        max_entradas = vendidas
        
    if menos_vendidas is None or vendidas < min_entradas:
        menos_vendidas = concierto
        min_entradas = vendidas


if total_entradas > 0:
    precio_medio = recaudacion_total / total_entradas
else:
    precio_medio = 0.0

print(f"Entradas vendidas en total: {total_entradas}")
print(f"Pista: {total_pista} | Grada: {total_grada} | VIP: {total_vip}")
print(f"Recaudación total: {recaudacion_total} €")
print(f"Precio medio de las entradas: {precio_medio} €")
print(f"Más entradas vendidas: {mas_vendidas} ({max_entradas})")
print(f"Menos entradas vendidas: {menos_vendidas} ({min_entradas})")
