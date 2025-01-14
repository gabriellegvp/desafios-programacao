def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

# Entrada do usuário
texto = input("Digite a string que deseja inverter: ")
print("String invertida:", inverter_string(texto))
