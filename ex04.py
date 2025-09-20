produto = input('Digite o nome do produto: ')
preço_unitario = float(input('Digite o preço unitário: '))
quantidade = int(input('Digite a quantidade comprada: '))

preço_total = preço_unitario * quantidade

desconto = float(input('Digite a porcetagem de desconto do produto: '))
preço_com_desconto = preço_total -(preço_total * desconto)/100

parcelas = int(input('digite  em quantas parcelas quer realizar essa compra?: '))
valor_parcelas = preço_com_desconto / parcelas
print('Valor final da compra:')
print('produto:', produto)
print('preço total sem desconto: R$', preço_total)
print('preço com desconto: R$', preço_com_desconto)
print('Quantidade de parcelas:', parcelas)
print('Valor de das parcelas: R$', valor_parcelas)

