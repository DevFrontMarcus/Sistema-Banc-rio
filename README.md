# Sistema Bancário em Python

Este é um sistema bancário simples, desenvolvido em Python, que permite gerenciar contas de clientes através de uma interface de terminal.

## Funcionalidades

- **Criação de contas**: Cadastro de novos clientes com nome, senha e saldo inicial.
- **Operações bancárias**:
  - Depósitos
  - Saques (com validação de senha e saldo)
  - Transferências entre contas
  - Consulta de saldo
  - Extrato de movimentações
- **Armazenamento de dados**: As informações são salvas em um arquivo JSON, simulando um banco de dados.
- **Segurança**: Todas as operações que envolvem movimentação de valores requerem validação de senha.

## Estrutura do Projeto

O projeto está organizado em três arquivos principais:

- **conta.py**: Contém a classe `Conta` que representa uma conta bancária individual.
- **banco.py**: Contém a classe `Banco` que gerencia as contas e as operações entre elas.
- **sistema_bancario.py**: Contém a interface de usuário e a lógica de interação com o sistema.

## Como Executar

Para executar o sistema, siga estes passos:

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Clone ou baixe este repositório.
3. No terminal, navegue até a pasta do projeto.
4. Execute o comando:

```bash
python sistema_bancario.py
```

## Funcionalidades Detalhadas

### Criação de Conta

- Nome completo do cliente
- Saldo inicial (opcional)
- Senha para operações

### Operações Disponíveis

1. **Consultar Saldo**: Exibe o saldo atual da conta (requer senha).
2. **Depositar**: Adiciona um valor ao saldo da conta.
3. **Sacar**: Retira um valor do saldo (requer senha e saldo suficiente).
4. **Transferir**: Transfere um valor para outra conta (requer senha, saldo suficiente e conta de destino válida).
5. **Extrato**: Exibe o histórico completo de movimentações da conta (requer senha).

## Armazenamento de Dados

Os dados das contas são armazenados no arquivo `dados_banco.json`, que é criado automaticamente na primeira execução. Este arquivo mantém as informações das contas mesmo após o programa ser encerrado.

## Tratamento de Erros

O sistema inclui tratamento para diversos erros, como:
- Tentativa de saque ou transferência com saldo insuficiente
- Senha incorreta
- Conta inexistente
- Valores inválidos (negativos ou não numéricos)

## Orientação a Objetos

O sistema foi desenvolvido seguindo os princípios de Programação Orientada a Objetos (POO), com classes bem definidas e encapsulamento de dados.

## Licença

Este projeto é livre para uso e modificação, desde que sejam mantidos os devidos créditos. 