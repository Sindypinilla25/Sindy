#solicitar valores al usuario
consumo_anual = float(input("ingrese el consumo anual de energia (KWh): "))
eficiencia = float(input("ingrese la eficiencia del panel ("%"): ")) / 100 #convertir a decimal
area_panel = float(input("ingrese la seperficie promedio de un panel (m^2): "))
radiacion_solar = float(input("ingrese la radiacion solar promedio (KWh/m^2/dia): "))
import math
#calcular la potencia diaria generada por un dia
potencia_diaria_panel = (area_panel)*(radiacion_solar)*(eficiencia)
print(f"/npotencia diaria generada por un panel: (potencia_diaraia_panel:2f)KWh")

#calcular la potencia anual generada por un panel 
potencia_diaria_panel = (area_panel)*(365)
print(f"potencia anual generada por un panel: (potencia_anual_panel:2f)kwh")

#determinar cuantos paneles son necesarios
panales_necesarios = math.ceil(consumo_anual/potencia_diaria_panel) 
print(f"cantidad de paneles necesarios: (potencia_anual_panel:2f)kwh")

#calcular el área total necesaria
area_panel = (panales_necesarios)*(area_panel)
print(f"área total necesaria para instalar los paneles: (área_total:2f)m^2")
