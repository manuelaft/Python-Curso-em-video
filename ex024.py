# ex024

'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"'''

cidade=str(input('Em que cidade você nasceu? ')).strip()
c=cidade.capitalize()
print('Santo' in c)

# Sempre que você for ler uma string (input), coloque o strip, por via das dúvidas
