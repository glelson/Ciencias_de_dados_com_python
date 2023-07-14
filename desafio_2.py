def menu ():
    menu = '''
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [lc] lista contas
    [nc] nova lista
    [nu] novo usuario
    [q] Sair
    ==>'''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Operação falou o valor informado é inválido.")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
            print("operação falou! você não tem saldo suficiente.")

    elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite.")
        
    elif excedeu_saques:
            print("operação falhou! numero maximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    else:
            print("operação falou! valor invalido")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n__________________________\n")
    if extrato:
        print(extrato)
    else:    
        print("Não tem movimentação da conta")
    print(f"\nsaldo atual {saldo:.2f}")
    print("\n__________________________\n")     

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")

    nome = input("Informe o nome completo: ")
    data_nacimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nacimento, "cpf": cpf, "endereco": endereco})

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o cpf do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n___conta criada com sucesso!___")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}
    print("\n ### Usuario nao encontrado ###\n")

def filtrar_usuario(cpf, usuario):
    for valor in usuario.items():
        if valor == cpf:
            return True
    return None

def lista_contas(contas):
     for conta in contas:
        linha = f"""\
          agencia:\t{conta["agencia"]}
          c/c:\t\t{conta['numero_conta']}
          Tilular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
usuario = []
contas = []
LIMETE_SAQUES = 3
AGENCIA = '0001'


while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMETE_SAQUES,
        )
      

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuario)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuario)

        if conta:
            contas.append(conta)

    elif opcao == "q":
        break
    
    elif opcao == "lc":
        lista_contas(contas)

    else:
        print("opeção errada.")


