# punto d

monto_compra = float(input("ingrese el monto de compra: $"))
es_vip = input("¿es cliente VIP? (true/false): ") == "true"
tiene_codigo_descuento = input("¿tiene código de descuento especial (true/false): ") == "true"
descuento = 0

if monto_compra > 100:
    descuento += 20
if es_vip:
    descuento += 10
if tiene_codigo_descuento:
    descuento += 5

descuento_total = (descuento / 100) * monto_compra
total_a_pagar = monto_compra - descuento_total

#mostrar resultado
print(f"descuento aplicado : (descuento)%")
print(f"total a pagar después del descuento: $(total_a_pagar:.2f)")
