class Conta:
    def __init__(self, nome, numero, saldo_inicial=0, senha=None):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo_inicial
        self.senha = senha
        self.extrato = []
        self.registrar_transacao("Abertura de conta", saldo_inicial)
    
    def registrar_transacao(self, tipo, valor):
        """Registra uma transação no extrato da conta."""
        import datetime
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append({"data": data, "tipo": tipo, "valor": valor, "saldo": self.saldo})
    
    def verificar_senha(self, senha):
        """Verifica se a senha fornecida é válida."""
        return senha == self.senha
    
    def verificar_saldo(self, valor):
        """Verifica se há saldo suficiente para uma operação."""
        return self.saldo >= valor
    
    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        
        self.saldo += valor
        self.registrar_transacao("Depósito", valor)
        return True
    
    def sacar(self, valor, senha):
        """Realiza um saque da conta."""
        if not self.verificar_senha(senha):
            raise ValueError("Senha incorreta")
        
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        
        if not self.verificar_saldo(valor):
            raise ValueError("Saldo insuficiente para saque")
        
        self.saldo -= valor
        self.registrar_transacao("Saque", -valor)
        return True
    
    def transferir(self, conta_destino, valor, senha):
        """Transfere um valor para outra conta."""
        if not self.verificar_senha(senha):
            raise ValueError("Senha incorreta")
        
        if valor <= 0:
            raise ValueError("Valor de transferência deve ser positivo")
        
        if not self.verificar_saldo(valor):
            raise ValueError("Saldo insuficiente para transferência")
        
        self.saldo -= valor
        self.registrar_transacao(f"Transferência para conta {conta_destino.numero}", -valor)
        
        conta_destino.saldo += valor
        conta_destino.registrar_transacao(f"Transferência recebida da conta {self.numero}", valor)
        return True
    
    def obter_saldo(self, senha):
        """Retorna o saldo atual da conta."""
        if not self.verificar_senha(senha):
            raise ValueError("Senha incorreta")
        
        return self.saldo
    
    def obter_extrato(self, senha):
        """Retorna o extrato de transações da conta."""
        if not self.verificar_senha(senha):
            raise ValueError("Senha incorreta")
        
        return self.extrato 