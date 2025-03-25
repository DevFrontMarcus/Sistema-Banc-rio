from banco import Banco
import os

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal do sistema bancário."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'SISTEMA BANCÁRIO':^50}")
    print("="*50)
    print("\n[1] - Criar Nova Conta")
    print("[2] - Acessar Conta Existente")
    print("[3] - Listar Contas")
    print("[0] - Sair")
    print("="*50)
    return input("\nEscolha uma opção: ")

def menu_conta(numero_conta, nome_cliente):
    """Exibe o menu de operações de uma conta."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'CONTA ' + numero_conta:^50}")
    print(f"{'Cliente: ' + nome_cliente:^50}")
    print("="*50)
    print("\n[1] - Consultar Saldo")
    print("[2] - Depositar")
    print("[3] - Sacar")
    print("[4] - Transferir")
    print("[5] - Extrato")
    print("[0] - Voltar ao Menu Principal")
    print("="*50)
    return input("\nEscolha uma operação: ")

def exibir_extrato(extrato):
    """Exibe o extrato formatado."""
    limpar_tela()
    print("\n" + "="*80)
    print(f"{'EXTRATO DE MOVIMENTAÇÕES':^80}")
    print("="*80)
    print(f"{'Data e Hora':<20} | {'Tipo':<30} | {'Valor':>10} | {'Saldo':>10}")
    print("-"*80)
    
    for transacao in extrato:
        print(f"{transacao['data']:<20} | {transacao['tipo']:<30} | " 
              f"R$ {transacao['valor']:>7.2f} | R$ {transacao['saldo']:>7.2f}")
    
    print("="*80)
    input("\nPressione Enter para voltar...")

def criar_conta(banco):
    """Interface para criar uma nova conta."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'CRIAR NOVA CONTA':^50}")
    print("="*50 + "\n")
    
    nome = input("Nome completo: ")
    
    while True:
        try:
            saldo_inicial = float(input("Saldo inicial (R$): "))
            if saldo_inicial < 0:
                print("O saldo inicial não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um valor numérico válido.")
    
    senha = input("Crie uma senha: ")
    
    try:
        numero_conta = banco.criar_conta(nome, senha, saldo_inicial)
        print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")
        input("\nPressione Enter para continuar...")
        return True
    except Exception as e:
        print(f"\nErro ao criar conta: {e}")
        input("\nPressione Enter para continuar...")
        return False

def acessar_conta(banco):
    """Interface para acessar uma conta existente."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'ACESSAR CONTA':^50}")
    print("="*50 + "\n")
    
    numero_conta = input("Número da conta: ")
    
    try:
        conta = banco.buscar_conta(numero_conta)
        operar_conta(banco, numero_conta, conta.nome)
        return True
    except ValueError as e:
        print(f"\nErro: {e}")
        input("\nPressione Enter para continuar...")
        return False

def listar_contas(banco):
    """Interface para listar todas as contas."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'LISTA DE CONTAS':^50}")
    print("="*50 + "\n")
    
    contas = banco.listar_contas()
    
    if not contas:
        print("Não há contas cadastradas.")
    else:
        print(f"{'Número':<10} | {'Cliente'}")
        print("-"*50)
        for numero, nome in contas:
            print(f"{numero:<10} | {nome}")
    
    input("\nPressione Enter para continuar...")

def consultar_saldo(banco, numero_conta):
    """Interface para consultar o saldo de uma conta."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'CONSULTA DE SALDO':^50}")
    print("="*50 + "\n")
    
    senha = input("Digite sua senha: ")
    
    try:
        saldo = banco.consultar_saldo(numero_conta, senha)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    except ValueError as e:
        print(f"\nErro: {e}")
    
    input("\nPressione Enter para continuar...")

def realizar_deposito(banco, numero_conta):
    """Interface para realizar um depósito."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'DEPÓSITO':^50}")
    print("="*50 + "\n")
    
    try:
        valor = float(input("Valor a depositar (R$): "))
        banco.depositar(numero_conta, valor)
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError as e:
        print(f"\nErro: {e}")
    
    input("\nPressione Enter para continuar...")

def realizar_saque(banco, numero_conta):
    """Interface para realizar um saque."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'SAQUE':^50}")
    print("="*50 + "\n")
    
    try:
        valor = float(input("Valor a sacar (R$): "))
        senha = input("Digite sua senha: ")
        
        banco.sacar(numero_conta, valor, senha)
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError as e:
        print(f"\nErro: {e}")
    
    input("\nPressione Enter para continuar...")

def realizar_transferencia(banco, numero_conta):
    """Interface para realizar uma transferência."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'TRANSFERÊNCIA':^50}")
    print("="*50 + "\n")
    
    try:
        conta_destino = input("Número da conta de destino: ")
        valor = float(input("Valor a transferir (R$): "))
        senha = input("Digite sua senha: ")
        
        banco.transferir(numero_conta, conta_destino, valor, senha)
        print(f"\nTransferência de R$ {valor:.2f} realizada com sucesso!")
    except ValueError as e:
        print(f"\nErro: {e}")
    
    input("\nPressione Enter para continuar...")

def ver_extrato(banco, numero_conta):
    """Interface para ver o extrato de uma conta."""
    limpar_tela()
    print("\n" + "="*50)
    print(f"{'EXTRATO':^50}")
    print("="*50 + "\n")
    
    senha = input("Digite sua senha: ")
    
    try:
        extrato = banco.obter_extrato(numero_conta, senha)
        exibir_extrato(extrato)
    except ValueError as e:
        print(f"\nErro: {e}")
        input("\nPressione Enter para continuar...")

def operar_conta(banco, numero_conta, nome_cliente):
    """Gerencia as operações em uma conta específica."""
    while True:
        opcao = menu_conta(numero_conta, nome_cliente)
        
        if opcao == "1":
            consultar_saldo(banco, numero_conta)
        elif opcao == "2":
            realizar_deposito(banco, numero_conta)
        elif opcao == "3":
            realizar_saque(banco, numero_conta)
        elif opcao == "4":
            realizar_transferencia(banco, numero_conta)
        elif opcao == "5":
            ver_extrato(banco, numero_conta)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

def main():
    """Função principal do sistema bancário."""
    banco = Banco("Banco Python")
    
    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            criar_conta(banco)
        elif opcao == "2":
            acessar_conta(banco)
        elif opcao == "3":
            listar_contas(banco)
        elif opcao == "0":
            print("\nObrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main() 