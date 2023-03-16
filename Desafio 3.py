import json


with open('dados.json', 'r') as file:
    faturamento = json.load(file)

dias_faturamento_acima_media = []
dias_acima_media = 0

media_mensal = sum(dia['valor'] for dia in faturamento if dia['valor'] != 0.0) / len([dia for dia in faturamento if dia['valor'] != 0.0])

menor_faturamento = faturamento[0]['valor']
maior_faturamento = faturamento[0]['valor']



for dia in faturamento:

    if dia['valor'] < menor_faturamento and dia['valor'] != 0.00:
        menor_faturamento = dia['valor']
        dia_menor_faturamento = dia['dia']
    
    if dia['valor'] > maior_faturamento:
        maior_faturamento = dia['valor']
        dia_maior_faturamento = dia['dia']
        
    if dia['valor'] > media_mensal:
        dias_acima_media += 1
        dias_faturamento_acima_media.append(dia['dia'])


print(f"Menor faturamento: R${menor_faturamento:.2f} (dia {dia_menor_faturamento})")
print(f"Maior faturamento: R${maior_faturamento:.2f} (dia {dia_maior_faturamento})")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
print(f"Dias com faturamento acima da média: {', '.join(str(dia) for dia in dias_faturamento_acima_media)}")
