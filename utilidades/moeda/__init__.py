def metade(num=0,format=False):
    return float(num)/2 if format==False else moeda(metade(num))

def dobro(num=0,format=False):
    return num*2 if format==False else moeda(dobro(num))

def aumentar(num=0,taxa=0,format=False):
    aumento=(taxa/100)*num
    return num+aumento if format==False else moeda(aumentar(num+aumento))

def diminuir(num=0,desconto=0,format=False):
    d=(desconto/100)*num
    return num-d if format==False else moeda(diminuir(num-d))

def moeda(num=0):
    num_format=(f'R${num:.2f}'.replace('.',','))
    return num_format

def resumo(num=0,taxa=0,desconto=0):
    if desconto<=9:
        tamanho='\t\t'
    else:
        tamanho='\t'
    print('--'*17)
    print(f'{'  RESUMO DO VALOR':^30}')
    print('--'*17)
    print(f'{'Preço analisado:'}\t{moeda(num)}')
    print(f'{'Dobro do preço:'}\t\t{dobro(num,format=True)}')
    print(f'{'Metade do preço:'}\t{metade(num,format=True)}')
    print(f'{f'{taxa}% de aumento:'}\t\t{aumentar(num,taxa,format=True)}')
    print(f'{f'{desconto}% de desconto:'}{tamanho}{diminuir(num,desconto,format=True)}')
    print('--'*17)
    print(tamanho)
    