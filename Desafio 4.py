faturamento_estados = [
    ('SP', 67836.43),
    ('RJ', 36678.66),
    ('MG', 29229.88),
    ('ES', 27165.48),
    ('Outros', 19849.53)
]


faturamento_total = sum(faturamento for estado, faturamento in faturamento_estados)


for estado, faturamento in faturamento_estados:
    percentual = faturamento / faturamento_total * 100
    print(f'{estado}: {percentual:.2f}%')