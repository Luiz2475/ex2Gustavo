
print(' 1-Traduzir palavra \n 2-Adicionar palavra \n 3-Sair')
opcao = int(input('Insira a opção desejada: '))
while opcao > 3: 
   opcao = int(input('Insira a opção desejada: '))
palavras = {
            'dog' :  "cachorro",
            'Hello' :  "Ola",
            'cat' : "gato"
            }

if opcao == 1:
    palavra = str(input('Digite a palavra: '))
    print(f'A tradução é: {palavras[palavra]}')
    while opcao < 3:
     print(' 1-Traduzir palavra \n 2-Adicionar palavra \n 3-Sair')
     opcao = int(input('Insira a opção desejada: '))
     if opcao == 1:
       palavra = str(input('Digite a palavra: '))
       print(f'A tradução é: {palavras[palavra]}')
     elif opcao == 2:
       novaPalavra= str(input('Digite a palavra: '))
       palavras[novaPalavra] = str(input('Digite a tradução: '))
       print('Palavra adicionada!')
     else:
       quit
elif opcao == 2:
    novaPalavra= str(input('Digite a palavra: '))
    palavras[novaPalavra] = str(input('Digite a tradução: '))
    print('Palavra adicionada!')
    while opcao < 3:
     print(' 1-Traduzir palavra \n 2-Adicionar palavra \n 3-Sair')
     opcao = int(input('Insira a opção desejada: '))
     if opcao == 1:
       palavra = str(input('Digite a palavra: '))
       print(f'A tradução é: {palavras[palavra]}')
     else:
       quit
elif opcao == 3:
    quit
print('ola')