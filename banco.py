import json
import os
from conta import Conta

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = {}
        self.arquivo_dados = "dados_banco.json"
        self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega dados das contas do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    
                    for num_conta, conta_dados in dados.items():
                        conta = Conta(
                            nome=conta_dados["nome"],
                            numero=num_conta,
                            saldo_inicial=conta_dados["saldo"],
                            senha=conta_dados["senha"]
                        )
                        conta.extrato = conta_dados["extrato"]
                        self.contas[num_conta] = conta
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
                self.contas = {}
    
    def salvar_dados(self):
        """Salva os dados das contas em um arquivo JSON."""
        dados = {}
        for num_conta, conta in self.contas.items():
            dados[num_conta] = {
                "nome": conta.nome,
                "saldo": conta.saldo,
                "senha": conta.senha,
                "extrato": conta.extrato
            }
        
        try:
            with open(self.arquivo_dados, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
    
    def criar_conta(self, nome, senha, saldo_inicial=0):
        """Cria uma nova conta no banco."""
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        
        # Gera um número de conta único
        if self.contas:
            ultimo_num = max(int(num) for num in self.contas.keys())
            num_conta = str(ultimo_num + 1).zfill(5)
        else:
            num_conta = "00001"
        
        # Verifica se o número de conta já existe
        if num_conta in self.contas:
            raise ValueError("Número de conta já existe")
        
        conta = Conta(nome, num_conta, saldo_inicial, senha)
        self.contas[num_conta] = conta
        self.salvar_dados()
        return num_conta
    
    def buscar_conta(self, numero_conta):
        """Busca uma conta pelo número."""
        if numero_conta not in self.contas:
            raise ValueError("Conta não encontrada")
        
        return self.contas[numero_conta]
    
    def listar_contas(self):
        """Retorna uma lista de todas as contas."""
        return [(num, conta.nome) for num, conta in self.contas.items()]
    
    def depositar(self, numero_conta, valor):
        """Deposita um valor em uma conta."""
        conta = self.buscar_conta(numero_conta)
        resultado = conta.depositar(valor)
        self.salvar_dados()
        return resultado
    
    def sacar(self, numero_conta, valor, senha):
        """Realiza um saque em uma conta."""
        conta = self.buscar_conta(numero_conta)
        resultado = conta.sacar(valor, senha)
        self.salvar_dados()
        return resultado
    
    def transferir(self, num_origem, num_destino, valor, senha):
        """Transfere um valor entre contas."""
        conta_origem = self.buscar_conta(num_origem)
        conta_destino = self.buscar_conta(num_destino)
        
        resultado = conta_origem.transferir(conta_destino, valor, senha)
        self.salvar_dados()
        return resultado
    
    def consultar_saldo(self, numero_conta, senha):
        """Consulta o saldo de uma conta."""
        conta = self.buscar_conta(numero_conta)
        return conta.obter_saldo(senha)
    
    def obter_extrato(self, numero_conta, senha):
        """Obtém o extrato de uma conta."""
        conta = self.buscar_conta(numero_conta)
        return conta.obter_extrato(senha) 