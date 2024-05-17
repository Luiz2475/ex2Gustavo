print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
opcao = int(input('Insira a opção desejada: '))
while opcao > 3: 
   opcao = int(input('Insira a opção desejada: '))
estoque = {}
if opcao == 1:
   produto = str(input('Digite o nome do produto: '))
   estoque[produto] = int(input('Digite a quantidade: '))
   print(estoque)
   print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
   opcao = 0
   opcao = int(input('Insira a opção desejada: '))
   while opcao > 3: 
    opcao = input('Insira a opção desejada: ')
    if opcao == 1:
       produto = str(input('Digite o nome do produto: '))
       estoque[produto] = int(input('Digite a quantidade: '))
    elif opcao == 2:
       print("a")
       atualizarProduto = int(input('Insira o nome do Produto: '))
       if atualizarProduto == produto:
          estoque[produto] = int(input('Insira nova quantidade: '))  
          print(estoque)
elif opcao == 2:
   print("Estoque vazio")
elif opcao == 3:
   print("Estoque vazio")
