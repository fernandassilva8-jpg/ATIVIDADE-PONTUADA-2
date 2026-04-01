import os 

os.system ("cls")

# ===========================
# HOSPITAL VIDA PLENA - SISTEMA DE AGENDAMENTO DE EXAMES 
# DESENVOLVEDOR: Fernanda santos da silva 

# Declaração dos vetores (listas) com os dados dos exames
# Estrutura: [Código, Nome do Exame, Preço]
# Inicialização dos "Vetores" (Listas) com os dados dos exames
# Seguindo a sugestão da atividade
codigos_disponiveis = [1, 2, 3, 4, 5, 6, 7]
nomes_exames = [
    "Hemograma Completo", 
    "Raio-X", 
    "Ultrassonografia", 
    "Eletrocardiograma", 
    "Tomografia", 
    "Ressonância Magnética", 
    "Exame de Glicose"
]
precos_exames = [50.00, 120.00, 200.00, 150.00, 450.00, 850.00, 35.00]

# Vetores para armazenar as escolhas do usuário
escolhidos_codigos = []
escolhidos_nomes = []
subtotal = 0.0

print("="*60)
print("          BEM-VINDO AO HOSPITAL VIDA PLENA")
print("="*60)

# Estrutura de repetição para o agendamento
continuar_agendando = True

while continuar_agendando:
    # Exibição da lista de exames
    print("\nLISTA DE EXAMES DISPONÍVEIS:")
    print(f"{'CÓD':<5} | {'NOME DO EXAME':<25} | {'PREÇO'}")
    print("-" * 50)
    
    # Laço para percorrer os vetores e exibir os dados
    for i in range(len(codigos_disponiveis)):
        print(f"{codigos_disponiveis[i]:<5} | {nomes_exames[i]:<25} | R$ {precos_exames[i]:.2f}")
    
    print("-" * 50)
    print("Digite '0' para encerrar o agendamento e ir para o pagamento.")

    # Entrada do usuário
    codigo_input = input("\nInforme o código do exame desejado: ")

    # Validação se a entrada é um número
    if codigo_input.isdigit():
        codigo_digitado = int(codigo_input)

        # Condicional para encerrar
        if codigo_digitado == 0:
            if len(escolhidos_codigos) == 0:
                print("\nNenhum exame foi selecionado ainda.")
                continue
            else:
                continuar_agendando = False
        
        # Verificação se o código existe nos vetores (validação)
        elif codigo_digitado in codigos_disponiveis:
            # Encontrar o índice do exame no vetor
            indice = codigos_disponiveis.index(codigo_digitado)
            
            # Adicionar aos vetores de agendamento e acumular valor
            escolhidos_codigos.append(codigos_disponiveis[indice])
            escolhidos_nomes.append(nomes_exames[indice])
            subtotal += precos_exames[indice]
            
            print(f" {nomes_exames[indice]} adicionado com sucesso!")
            
            # Pergunta se deseja adicionar mais um
            pergunta = input("Deseja agendar outro exame? (S/N): ").upper()
            if pergunta == "N":
                continuar_agendando = False
        else:
            print("\n CÓDIGO INVÁLIDO! Por favor, tente novamente.")
    else:
        print("\n ERRO: Digite apenas números válidos.")

# --- PROCESSAMENTO DO PAGAMENTO ---
print("\n" + "="*60)
print("              RESUMO DO AGENDAMENTO")
print("="*60)
print(f"Subtotal: R$ {subtotal:.2f}")

print("\nFORMAS DE PAGAMENTO:")
print("1 - Convênio (15% de desconto)")
print("2 - Particular (Sem desconto)")
print("3 - Cartão de Crédito (8% de acréscimo)")

forma_valida = False
ajuste = 0.0
descricao_pagamento = ""

# Laço para garantir escolha de pagamento válida
while not forma_valida:
    opcao_pgto = input("\nSelecione a forma de pagamento (1, 2 ou 3): ")

    if opcao_pgto == "1":
        descricao_pagamento = "Convênio"
        ajuste = -(subtotal * 0.15) # Cálculo do desconto
        forma_valida = True
    elif opcao_pgto == "2":
        descricao_pagamento = "Particular"
        ajuste = 0.0
        forma_valida = True
    elif opcao_pgto == "3":
        descricao_pagamento = "Cartão de Crédito"
        ajuste = subtotal * 0.08    # Cálculo do acréscimo
        forma_valida = True
    else:
        print(" Opção de pagamento inválida! Escolha 1, 2 ou 3.")

# Cálculo do valor final
valor_final = subtotal + ajuste

# --- EXIBIÇÃO DOS RESULTADOS FINAIS ---
print("\n" + "*"*60)
print("              COMPROVANTE FINAL")
print("*"*60)
print(f"Exames agendados: {escolhidos_nomes}")
print(f"Códigos: {escolhidos_codigos}")
print(f"Subtotal bruto: R$ {subtotal:.2f}")
print(f"Forma de Pagamento: {descricao_pagamento}")
print(f"Valor do desconto/acréscimo: R$ {ajuste:.2f}")
print("-" * 60)
print(f"VALOR TOTAL A PAGAR: R$ {valor_final:.2f}")
print("*" * 60)
print("O Hospital Vida Plena agradece a confiança!")