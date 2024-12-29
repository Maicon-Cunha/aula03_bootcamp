#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = 10
preco = 20

if quantidade < 0 or preco < 0: 
    print("Insira um valor positivo")
else:
    print(f"A quantidade é de {quantidade} unidades ao valor unitário de {preco} reais, totalizando {quantidade * preco} reais.")