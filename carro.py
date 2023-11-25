class Carro:
    marca=("") 
    tipo=("")
    modelo=("")
    Combustible=("")
    Precio="0"
    Garantia="0"
    Fecha_I=("")
    Color=("")
    Asientos=0
valor=0
Toyota=Carro()
Toyota.marca="Toyota"
Toyota.tipo="Camioneta"
Toyota.modelo="Tacoma"
Toyota.Combustible="Gasolina"
Toyota.Precio="$28,500"
Toyota.Garantia="5 años"
Toyota.Fecha_I="11-enero-2023"
Toyota.Color="Rojo"
Toyota.Asientos=4
for atributo, valor in vars(Toyota).items():
    print(f"{atributo}: {valor}")
print("-----------------------------------")
Mercedez=Carro()
Mercedez=Toyota
Mercedez.marca="Mercedes-Benz"
Mercedez.tipo="Sedan"
Mercedez.modelo="Clase C"
Mercedez.Combustible="Hibrido"
Mercedez.Precio="$48,500"

for atributo1, valor1 in vars(Mercedez).items():
    print(f"{atributo1}: {valor1}")