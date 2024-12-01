idades=[]
nome_homem=''
idade_homem=0
idade_mulher=[]
for c in range(1,5):
    print('―――――― {}ª PESSOA ――――――'.format(c))
    n=str(input('Nome: ')).strip()
    i=int(input('Idade: '))
    s=str(input('Sexo [M/F]: ')).strip().upper()
    idades+=[i]
    if s=='M' and i>idade_homem:
        idade_homem=i
        nome_homem=n

    if s=='F':
        if i<20:
            idade_mulher+=[i]

soma=int(sum(idades))
print('A média de idade do grupo é {:.1f} anos'.format(soma/4))
print(f'O homem mais velho tem {idade_homem} e se chama {nome_homem}.')
print('Ao todo são {} mulheres com menos de 20 anos'.format(len(idade_mulher)))

# versão corrigida do Guanabara, apenas idade e nome do homem mais velho (não consegui entender muito bem, por isso recorri ao ChatGPT):

if c==1 and s=='M': # primeiro passo é comparar a primeira iteração (isso tudo dentro do for)
    idade_homem=i   # e atribuir os valores dos acumuladores com as variáveis dentro do for
    nome_homem=n
if s=='M' and i>idade_homem: # OU SEJA, se a próxima idade, da próxima iteração for maior que o valor da última
    i=idade_homem # a nova idade do homem vai ser essa, isso vai se repetir até a última iteração, atualizando a idade e o nome
    nome_homem=n # Agora por exemplo, se a última iteração a idade for menor que as outras, não vai contabilizar já que (i>idade_homem)
                 # e idade_homem está o valor mais alto. Então vai aparecer os valores da maior iteração (pode ser terceira, segunda ou primeira)

# Correção último item, quantas mulheres menores de 20 anos

mulheres_menoresidades=0
if s=='F' and i<20: # Isso dentro do loop, ou seja vai se repetir a cada iteração
    mulheres_menoresidades+=1 # A cada iteração que tiver um F menor que 20, vai somar mais um, e por ai vai até o final e termos o valor total

''' TEORIA MUITO IMPORTANTE!!!

    Um dos erros mais comuns que eu encontrei até agora fazendo esse e outros exercícios foi que a iteração do loop atualizava a cada vez
e não contabilizava os valores anteriores. Exemplo:

for c in range (4):
    num=int(input(Digite um valor: ))

print(num)

Eu posso ter digitado 4, 6, 8 e 9 mas invés de considerar todos, considera-se apenas a última iteração, o 9. Para resolver isso, é por isso 
que criamos uma variável acumulativa/contadora fora do loop, para que elas possam ser atualizadas e acessadas dentro dele. Aqui está a
explicação do ChatGPT que me ajudou muito:'''

# Esse problema acontece porque, provavelmente, as variáveis do homem mais velho estão sendo atualizadas a cada loop, em vez de comparar 
# a idade de cada pessoa para ver se é maior que a idade atual do homem mais velho. Para corrigir isso, você precisa manter a idade 
# e o nome do homem mais velho fora do loop e, dentro do loop, atualizar esses valores apenas se a idade da pessoa atual for maior que a 
# idade atual do homem mais velho.

#    Explicação:
# Definimos nome_homem_mais_velho e idade_homem_mais_velho antes do loop para que possam ser acessados e atualizados em cada iteração.
# Dentro do for, verificamos se a pessoa é do sexo masculino (sexo.upper() == 'M') e se sua idade é maior que a idade do homem mais velho 
# registrada até agora. Se ambas as condições forem atendidas, atualizamos o nome e a idade do homem mais velho.
# Ao final do loop, mostramos o nome e a idade do homem mais velho.

'''
    Outro problema que eu enfrentei também foi porque meu if s=='M' estava fora do loop, portanto ele acontecia apenas uma vez,
apenas na última iteração e apenas com os dados dessa última. Ou seja não atualizava a variável contadora que eu criei fora do loop, antes
a cada novo dado inserido. Exemplo e explicação do ChatGPT:

O problema está na indentação do if. Ele precisa estar dentro do loop for para ser verificado a cada nova pessoa. 
No seu código, o if está fora do loop, então ele é executado apenas uma vez, depois que o for já terminou. '''

# Aqui está a correção com o if dentro do for:

# nome_homem = ''
# idade_homem = 0

# for c in range(1, 5):
#    print('―――――― {}ª PESSOA ――――――'.format(c))
#    n = str(input('Nome: '))
#    i = int(input('Idade: '))
#    s = str(input('Sexo [M/F]: '))

    # Verifica se a pessoa é do sexo masculino e se sua idade é maior que a do homem mais velho até agora
#    if s.upper() == 'M' and i > idade_homem:
#        idade_homem = i
#        nome_homem = n

# Exibe o resultado fora do loop
# print(f'O homem mais velho é {nome_homem}, com {idade_homem} anos.')

# Mudanças:
# Colocamos o if dentro do for, para que a verificação seja feita em cada iteração.
# A condição s.upper() == 'M' garante que o código funcione mesmo que o usuário digite "m" minúsculo.
# O print(f'O homem mais velho é {nome_homem}, com {idade_homem} anos.') fica fora do loop, sendo exibido apenas uma vez, após as verificações.
# Com isso, o programa deve armazenar corretamente o nome e a idade do homem mais velho entre as quatro pessoas.