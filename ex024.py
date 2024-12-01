cidade=str(input('Em que cidade você nasceu? ')).strip()
c=cidade.capitalize()
print('Santo' in c)

# Sempre que você for ler uma string (input), coloque o strip, por via das dúvidas

# ex025

nome=str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))

# Nesse caso, o capitalize (primeira letra da str maiúscula) não dá certo porque o que eu quero, o sobrenome, não é o primeiro nome
# Já o title converte as primeiras letras de todas as palavras em maiúsculo