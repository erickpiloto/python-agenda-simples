import json
import pandas

AGENDA = {}

def carrega_bd():
    global BD
    try:
        bd = open('agenda.txt','r')
        BD = json.loads(bd.read())
        bd.close()
    except:
        print('NENHUM BANCO DE DADOS ENCONTRADO!')
        print()
        input('Tecle <ENTER> para iniciar uma NOVA AGENDA!')
        BD = {}
        print()

def salva_bd():
    bd = open('agenda.txt', 'w')
    bd_json = json.dumps(AGENDA)
    bd.write(bd_json)
    bd.close()

def mostra_agenda():
    print('=====================================')
    print('==   EXIBINDO TODOS OS CONTATOS    ==')
    print('=====================================')
    for i in AGENDA:
        print('Nome:',i)
        print('Fone:',AGENDA[i]['Fone'])
        print('Email:',AGENDA[i]['Email'])
        print('Cidade:',AGENDA[i]['Cidade'])
        print('---------------------------------')

def busca_contato(contato):
    print('=====================================')
    print('==        BUSCANDO CONTATO         ==')
    print('=====================================')
    print('Nome:', contato)
    print('Fone:', AGENDA[contato]['Fone'])
    print('Email:', AGENDA[contato]['Email'])
    print('Cidade:', AGENDA[contato]['Cidade'])
    print('---------------------------------')

def add_contato(nome, fone, email, cidade):
    AGENDA[nome] = {
        'Fone':fone,
        'Email':email,
        'Cidade':cidade
    }
    print('======================================')
    print('=== CONTATO ADICIONADO COM SUCESSO ===')
    print('======================================')

def edita_contato(nome, fone, email, cidade):
    AGENDA[nome] = {
        'Fone':fone,
        'Email':email,
        'Cidade':cidade
    }
    print('======================================')
    print('===  CONTATO EDITADO COM SUCESSO   ===')
    print('======================================')

def excluir_contato(nome):
    AGENDA.pop(nome)
    print('======================================')
    print('===  CONTATO EXCLUÍDO COM SUCESSO  ===')
    print('======================================')

def exporta_csv():
    try:
        bd = open('agenda.txt','r')
        conversao = pandas.read_json(bd)
        csv = conversao.to_csv()
        save = open('agenda.csv','w')
        save.write(csv)
        bd.close()
        save.close()
    except:
        print()
        print('Salve a agenda antes de exportar!!!!')
        print()
        input('Tecle <ENTER> para continuar...')
        print()

def menu():
    print('=====================================')
    print('==  AGENDA -  ESCOLHA UMA OPÇÃO:   ==')
    print('=====================================')
    print('1 - MOSTRA TODOS OS CONTATOS')
    print('2 - BUSCA POR CONTATO')
    print('3 - INCLUI UM CONTATO')
    print('4 - ALTERA UM CONTATO')
    print('5 - EXCLUI UM CONTATO')
    print('6 - SALVA AGENDA')
    print('7 - CARREGA AGENDA')
    print('8 - EXPORTA AGENDA (.csv)')
    print('0 - SAIR')
    print()
    opcao = input('Digite uma opção: ')
    print()
    if opcao == '1':
        mostra_agenda()
    elif opcao == '2':
        cont = input('Digite o nome que deseja consultar: ')
        try:
            busca_contato(cont)
        except:
            print()
            input('CONTATO NÃO ENCONTRADO!  -  Tecle <ENTER> para continuar...')
            print()
    elif opcao == '3':
        n1 = input('Digite o nome que deseja adicionar:')
        f1 = input('Digite o fone de {}:'.format(n1))
        e1 = input('Digite o email de {}:'.format(n1))
        c1 = input('Digite a cidade de {}:'.format(n1))
        add_contato(n1,f1,e1,c1)
    elif opcao == '4':
        n2 = input('Qual contato deseja alterar: ')
        f2 = input('Digite o fone de {}:'.format(n2))
        e2 = input('Digite o email de {}:'.format(n2))
        c2 = input('Digite a cidade de {}:'.format(n2))
        edita_contato(n2,f2,e2,c2)
    elif opcao == '5':
        n3 = input('Digite o contato que deseja excluir: ')
        try:
            excluir_contato(n3)
        except:
            print()
            input('ESTE CONTATO NÃO EXISTE!! - Tecle <ENTER> para continuar...')
            print()
    elif opcao == '6':
        print('Salvando Agenda...')
        salva_bd()
        print()
        input('AGENDA SALVA COM SUCESSO  -  Tecle <ENTER> para continuar...')
        print()
    elif opcao == '7':
        print('Carregando Agenda...')
        carrega_bd()
        print()
        input('AGENDA CARREGADA COM SUCESSO   -   Tecle <ENTER> para continuar...')
    elif opcao == '8':
        print('Exportando Agenda...')
        exporta_csv()
        print()
        input('AGENDA EXPORTADA COM SUCESSO   -   Tecle <ENTER> para continuar...')
    elif opcao == '0':
        print('Saindo do programa...')
        op = input('Gostaria de salvar as alterações feitas? [S]im ou [N]ão: ')
        if op == 'S' or op == 's':
            salva_bd()
            print('Salvando e saindo...')
            exit()
        else:
            print('Saindo...')
            exit()
    else:
        print()
        print('DIGITE UMA OPÇÃO VÁLIDA!!!')
        print()
        print()
        input('Tecle <ENTER> para continuar...')
        print()

def main():
    carrega_bd()
    global AGENDA
    AGENDA = BD
    while True:
        menu()

main()

1