import json

# Dados fictícios em formato JSON
faturamento_diario = """
[1000, 2000, 0, 1500, 3000, 0, 0, 500, 1000, 2000, 1000, 1500, 0, 0]
"""

# Carregar os dados
dados = json.loads(faturamento_diario)

# Filtrar dias com faturamento
dias_validos = [dia for dia in dados if dia > 0]

# Calcular menor, maior e média
menor = min(dias_validos)
maior = max(dias_validos)
media = sum(dias_validos) / len(dias_validos)

# Dias acima da média
dias_acima_da_media = sum(1 for dia in dias_validos if dia > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_da_media}")
