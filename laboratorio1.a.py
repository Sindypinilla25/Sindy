#punto a

dias_asignados = int(input("ingrese los dias asignados a la tarea: "))
dias_retraso = int(input("ingrese los dias de retraso: "))

if dias_asignados > 0:
    porcentage_retraso = (dias_retraso/dias_asignados) * 100
    print("retraso: ", dias_retraso,"dias")
    print("porcentaje de retraso: ", round(porcentage_retraso, 2), "%")
else:
    print("Error: Los dias asignados deben ser mayores a 0.")
