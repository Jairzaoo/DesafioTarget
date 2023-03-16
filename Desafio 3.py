import json


with open('fat.json', 'r') as arquivo_json:
    faturamento_diario = json.load(arquivo_json)


faturamento_diario = {dia: valor for dia, valor in faturamento_diario.items() if valor > 0}


menor_faturamento = min(faturamento_diario.values())
maior_faturamento = max(faturamento_diario.values())


media_mensal = sum(faturamento_diario.values()) / len(faturamento_diario)


dias_acima_da_media = len([f for f in faturamento_diario.values() if f > media_mensal])


print(f'Menor faturamento diário: R${menor_faturamento:.2f}')
print(f'Maior faturamento diário: R${maior_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')