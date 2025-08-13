agenda = {}
while True:
    print('1 - Adicionar novo contato')
    print('2 - Pesquisar contato')
    print('3 - Alterar contato')
    print('4 - Excluir contato')
    print('5 - Listar contatos')
    print('S - Sair')
    opcao = input('Digite a opção desejada: ').lower()
    if opcao == '1':
        nome = input('Digite o nome do contato: ').lower()
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print('Contato salvo com sucesso!')

    elif opcao == '2':
        pesquisa = input('Digite o nome do contato: ').lower()
        if pesquisa in agenda:
            print(f'{pesquisa}: {agenda[pesquisa]}')
        else:
            print('Digite uma entrada válida.')

    elif opcao == '3':
        alteracao = input('Digite o nome do contato a ser alterado: ').lower()
        if alteracao in agenda:
            agenda[alteracao] = input('Digite o novo telefone do contato: ')
            print(f'Contato alterado com sucesso! O novo telefone é: {alteracao}: {agenda[alteracao]}')
        else:
            print('Digite um contato válido.')

    elif opcao == '4':
            contato_deletar = input('Digite o nome do contato que deseja excluir: ').lower()
            if contato_deletar in agenda:
                del agenda[contato_deletar]
                print('Contato deletado com sucesso!')
            else:
                print('Digite um contato válido.')

    elif opcao == '5':
        print(agenda)

    elif opcao == 's':
        print(f'Você optou por sair. ')
        break