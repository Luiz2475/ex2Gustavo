print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
opcao = int(input('Insira a opção desejada: '))
while opcao not in [1, 2, 3]: 
   opcao = int(input('Insira a opção desejada: '))
estoque = {}
if opcao == 1:
   produto = str(input('Digite o nome do produto: '))
   estoque[produto] = int(input('Digite a quantidade: '))
   print('Produto adicionado')
   print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
   opcao = int(input('Insira a opção desejada: '))
   while opcao > 3: 
     opcao = int(input('Insira a opção desejada: '))
   if opcao == 1:
       produto = str(input('Digite o nome do produto: '))
       estoque[produto] = int(input('Digite a quantidade: '))
       print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
   opcao = int(input('Insira a opção desejada: '))
   while opcao > 3: 
     opcao = int(input('Insira a opção desejada: '))
   if opcao == 1:
       produto = str(input('Digite o nome do produto: '))
       estoque[produto] = int(input('Digite a quantidade: '))
   elif opcao == 2:
      atualizarProduto = input('Insira o nome do Produto: ')
      if atualizarProduto == produto:
         estoque[produto] = int(input('Insira nova quantidade: '))  
         print(f'A nova quantidade do produto é : {estoque[produto]}')
   elif opcao == 3: 
      saber = input("Produto desejado: ")
      print(estoque[saber])
   elif opcao == 2:
      atualizarProduto = input('Insira o nome do Produto: ')
      if atualizarProduto == produto:
         estoque[produto] = int(input('Insira nova quantidade: '))  
         print(f'A nova quantidade do produto é : {estoque[produto]}')
         print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
   opcao = int(input('Insira a opção desejada: '))
   while opcao > 3: 
     opcao = int(input('Insira a opção desejada: '))
   if opcao == 1:
       produto = str(input('Digite o nome do produto: '))
       estoque[produto] = int(input('Digite a quantidade: '))
   elif opcao == 2:
      atualizarProduto = input('Insira o nome do Produto: ')
      if atualizarProduto == produto:
         estoque[produto] = int(input('Insira nova quantidade: '))  
         print(f'A nova quantidade do produto é : {estoque[produto]}')
   elif opcao == 3: 
      saber = input("Produto desejado: ")
      print(estoque[saber])
   elif opcao == 3: 
      saber = input("Produto desejado: ")
      print(estoque[saber])
      print(' 1-Adicionar produtos \n 2-Atualizar a quantidade \n 3-Consultar quantidade')
   opcao = int(input('Insira a opção desejada: '))
   while opcao > 3: 
     opcao = int(input('Insira a opção desejada: '))
   if opcao == 1:
       produto = str(input('Digite o nome do produto: '))
       estoque[produto] = int(input('Digite a quantidade: '))
   elif opcao == 2:
      atualizarProduto = input('Insira o nome do Produto: ')
      if atualizarProduto == produto:
         estoque[produto] = int(input('Insira nova quantidade: '))  
         print(f'A nova quantidade do produto é : {estoque[produto]}')
   elif opcao == 3: 
      saber = input("Produto desejado: ")
      print(estoque[saber])
elif opcao == 2:
   print("Estoque vazio")
elif opcao == 3:
   print("Estoque vazio")
