class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto 

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f"Entrada general para {self.concierto.artista} - {self.get_precio_total()} €"


class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f"Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €"


class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        return self.concierto.precio_base * 1.10 
    
    def __str__(self):
        return f"Entrada de pista para {self.concierto.artista} - {self.get_precio_total()} €"
    

class EntradaVIP(Entrada): 
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    def get_precio_total(self):
        if self.incluye_consumicion:      
            return self.concierto.precio_base * 1.20  
        return self.concierto.precio_base * 1.15 

    def __str__(self):
        return f"Entrada VIP para {self.concierto.artista} - {self.get_precio_total()} €" 


class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = []
        self.activo = activo 

    def calcular_recaudacion(self):
        total = 0.0
        for entrada in self.entradas_vendidas:
            total += entrada.get_precio_total()
        return total

    def calcular_precio_medio(self):
        contador = 0
        for entrada in self.entradas_vendidas:
            contador += 1

        if contador == 0:
            return 0.0
        return self.calcular_recaudacion() / contador

    def entradas_disponibles(self):
        vendidas = 0
        for entrada in self.entradas_vendidas:
            vendidas += 1
        return vendidas < self.aforo_maximo

    def __str__(self):
        return f"Concierto de {self.artista} en {self.ciudad}"


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    def comprar_entrada(self, concierto, tipo_entrada):
        if not concierto.activo:
            raise Exception(f"El concierto de {concierto.artista} no está activo")
        
        if concierto in self.conciertos_asistidos:
            raise Exception(f"{self.nombre} ya ha asistido al concierto de {concierto.artista}")
        
        if not concierto.entradas_disponibles():
            raise Exception(f"No quedan entradas para el concierto de {concierto.artista}")

        if tipo_entrada.lower() == "general":
            entrada = Entrada(concierto)
        elif tipo_entrada.lower() == "grada":
            entrada = EntradaGrada(concierto, "1A")
        elif tipo_entrada.lower() == "pista":
            entrada = EntradaPista(concierto, True)
        elif tipo_entrada.lower() == "vip":
            entrada = EntradaVIP(concierto, True)
        else:
            raise Exception("El tipo de entrada no es válido")

        concierto.entradas_vendidas.append(entrada)
        self.entradas_compradas.append(entrada)
        self.conciertos_asistidos.add(concierto)

    def valorar(self, concierto, valoracion):
        if concierto not in self.conciertos_asistidos:
            raise Exception(f"{self.nombre} no ha asistido al concierto de {concierto.artista}")

        if valoracion < 0 or valoracion > 10:
            raise Exception("La valoración debe estar entre 0 y 10")
        
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        asistidos = 0
        for concierto in self.conciertos_asistidos:
            asistidos += 1
        return f"{self.nombre} (ha asistido a {asistidos} conciertos)"