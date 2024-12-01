import datetime as dt
atual=dt.datetime.today().year
maior=0
menor=0
for c in range(1,8):
    ano=int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual-ano>18:
            maior+=atual-ano>18
    else:
        menor+=1 # esse 1 está aqui por que é como se a cada número menor que temos, fosse adicionado 
                 # mais um a variável de valor zero. E eles são somados/juntados pelo +=, dando o resultado
                 # do total de números menores que 18 no final
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))

# ínicio da Análise de dados !