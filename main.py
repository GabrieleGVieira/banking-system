import textwrap

from entities import CurrentAccount, Deposit, PrivateIndividual, Withdraw


class Main:
    def __init__(self):
        self.clients = []
        self.accounts = []

    def menu(self):
        menu = """\n
        ------ MENU ------
        Opções:
        1 - Depositar
        2 - Sacar
        3 - Visualizar Extrato
        4 - Criar Usuario
        5 - Criar Conta
        6 - Listar Contas
        7 - Sair
            """
        return input(textwrap.dedent(menu))

    def filter_client(self, cpf):
        client = [client for client in self.clients if client.cpf == cpf]
        if len(client) > 0:
            return client[0]
        else:
            return None

    def deposit(self):
        cpf = int(input("Informe o CPF do cliente: "))
        client = self.filter_client(cpf)

        if not client:
            print("\n -------- ERROR -------- \n")
            print("\nCliente não encontrado!")
            return
        print("\n -------- DEPÓSITOS -------- \n")
        value = int(input("Informe o valor deseja depositar: "))

        transaction = Deposit(value)
        client_account = client.accounts
        if not client_account:
            return
        client.transaction(client_account[0], transaction)

    def withdraw(self):
        cpf = int(input("Informe o CPF do cliente: "))
        client = self.filter_client(cpf)

        if not client:
            print("\n -------- ERROR -------- \n")
            print("\nCliente não encontrado!")
            return

        print("\n -------- SAQUES -------- \n")
        value = int(input("Informe o valor deseja sacar: "))

        transaction = Withdraw(value)
        client_account = client.accounts
        if not client_account:
            return
        client.transaction(client_account[0], transaction)

    def view_extract(self):
        cpf = int(input("Informe o CPF do cliente: "))
        client = self.filter_client(cpf)
        if not client:
            print("\n -------- ERROR -------- \n")
            print("\nCliente não encontrado!")
            return

        print("\n------ EXTRATO ----- \n")

        extract = client.accounts[0].historical.transaction
        if not extract:
            print("Não foram realizadas movimentações.")
            return
        else:
            for transaction in extract:
                print(f"\n{transaction['tipo']}:\n\tR$ {transaction['valor']:.2f}")

            print(f"\nSaldo:\n\tR$ {client.accounts[0].balance:.2f}")
            print("\n---------------------\n")

    def create_client(self):
        cpf = int(input("Digite o CPF do novo usuário: "))
        client = self.filter_client(cpf)

        if client:
            print("\n -------- ERROR -------- \n")
            print("Usuário já cadastrado.")
            return

        else:
            print("\n---- CADASTRO DE USUÁRIO ----- \n")

            name = input("Digite o Nome do novo usuário: ")
            birthday = input("Digite a Data de Nascimento do novo usuário: ")
            street = input("Digite o Endereço do novo usuário. Logadouro: ")
            nro = input("Numero: ")
            bairro = input("Bairro: ")
            city = input("Cidade: ")
            state = input("Estado: ")
            address = street + ", " + nro + ", " + bairro + ", " + city + "/" + state
            client = PrivateIndividual(address, name, cpf, birthday)
            self.clients.append(client)
            print("Usuário cadastrado com sucesso!")

    def create_account(self, account_number):
        cpf = int(input("Digite o CPF do novo usuário: "))
        client = self.filter_client(cpf)

        if not client:
            print("\n -------- ERROR -------- \n")
            print("\nCliente não encontrado!")
            return

        print("\n---- CRIAR DE CONTA ----- \n")

        account = CurrentAccount.new_account(client, account_number)
        self.accounts.append(account)
        client.accounts.append(account)

        print("\nConta criada com sucesso!\n")

    def list_accounts(self):
        print("\n------ LISTA DE CONTAS ----- \n")

        if len(self.accounts) <= 0:
            print("Não existem contas cadastradas.")
            return
        else:
            for account in self.accounts:
                print(account)
                print("\n---------------------\n")

    def run(self):
        while True:
            option = self.menu()

            if int(option) == 1:
                self.deposit()

            elif int(option) == 2:
                self.withdraw()

            elif int(option) == 3:
                self.view_extract()

            elif int(option) == 4:
                self.create_client()

            elif int(option) == 5:
                account_number = len(self.accounts) + 1
                self.create_account(account_number)

            elif int(option) == 6:
                self.list_accounts()

            elif int(option) == 7:
                print("Obrigado. Até breve.")
                break

            else:
                print("\n -------- ERROR -------- \n")
                print("Operação inválida.")
