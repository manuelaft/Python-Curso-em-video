# ex105

'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas                                                                                                                                                 
    - A maior nota                                                                                                                                                                
        - A menor nota                                                                                                                                                              
            - A média da turma                                                                                                                                                      
                - A situação (opcional)'''

def notas(*num,sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    media=(f'{sum(num)/len(num):.2f}')
    dicionario={'Total':len(num),'Maior nota':max(num),'Menor nota':min(num),'Média':media}
    print('--'*50)
    if sit:
        if float(media)<=4.0:
            dicionario['Situação']='RUIM'
        elif float(media)>=4.1 and float(media)<=6.0:
            dicionario['Situação']='RAZOÁVEL'
        elif float(media)>=6.1 and float(media)<=8.0:
            dicionario['Situação']='BOA'
        else:
            dicionario['Situação']='EXCELENTE'
        
    return dicionario


# Programa Principal
lista=[]
while True:
    respostas=float(input('Digite a nota (999 para parar): '))
    if respostas!=999:
        lista.append(respostas)
    else:
        break

resposta=notas(*lista,sit=True)
print(resposta)

# print(help(notas))
