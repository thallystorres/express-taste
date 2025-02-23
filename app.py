import platform 
import subprocess
import time

restaurantes = []

def voltar_menu():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def limpar_tela():
    nome_sistema = platform.system()
    if nome_sistema == 'Windows':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def mudar_status_restaurante():
    listar_restaurantes()
    try:
        ativado = int(input("Digite qual restaurante você quer mudar o status: ")) - 1
        if restaurantes[ativado]['atividade'] == True:
            restaurantes[ativado]['atividade'] = False
            print("Restaurante desativado")
        else:
            restaurantes[ativado]['atividade'] = True
            limpar_tela()
            print("Restaurante ativado")
    except:
        input("Valor inválido, digite uma tecla para tentar novamente")
        mudar_status_restaurante()
    voltar_menu()

def cadastrar_restaurantes():
    restaurante = {'atividade' : False}
    limpar_tela()
    print('Cadastro de novos restaurantes\n')
    restaurante['nome'] = str(input('Digite o nome do restaurante: ')).capitalize()
    restaurante['categoria'] = str(input('Digite a categoria do restaurante: ')).capitalize()
    restaurantes.append(restaurante)
    print(f'O restaurante {restaurante['nome']} foi cadastrado com sucesso\n')
    voltar_menu()

def listar_restaurantes():
    limpar_tela()
    resultado = [f'{index + 1}: {restaurante['nome']} | {restaurante['categoria']} | {'Ativo' if restaurante['atividade'] == True else 'Inativo'}' for index, restaurante in enumerate(restaurantes)]
    print(f"Lista de restaurantes:\n\n{'\n'.join(resultado)}")
    
def finalizar_app():
    print("Finalizando app...")
    time.sleep(1)
    limpar_tela()


def opcao_invalida():
    print("Opção inválida.\n")
    voltar_menu()

def opcoes():
    opcao_escolhida = int(input('Escolha uma das opções: '))
    match opcao_escolhida:
        case 1:
            cadastrar_restaurantes()
        case 2:
            listar_restaurantes()
            voltar_menu()
        case 3:
            mudar_status_restaurante()
        case 4:
            finalizar_app()


def exibir_inicio():
    print("""
    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗  ████████╗░█████╗░░██████╗████████╗███████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║╚█████╗░░░░██║░░░█████╗░░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║██████╔╝░░░██║░░░███████╗
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝\n""")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Mudar status de restaurante')
    print('4. Sair\n')
    

def main():
    limpar_tela()
    exibir_inicio()
    opcoes()

if __name__ == '__main__':
    main()