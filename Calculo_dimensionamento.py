# ==========================================================
# SISTEMA DE DIMENSIONAMENTO DE ENFERMAGEM
# ESCALA DE FUGULIN + PLANTÃO DE 12 HORAS
#
# Este sistema foi desenvolvido para auxiliar no cálculo de
# dimensionamento de enfermagem a partir da Escala de Fugulin.
#
# O sistema permite:
# 1. Configurar a quantidade de enfermeiros e técnicos do plantão.
# 2. Informar técnicos separados por setor/andar.
# 3. Cadastrar vários pacientes.
# 4. Calcular automaticamente o Fugulin de cada paciente.
# 5. Classificar o paciente por complexidade assistencial.
# 6. Calcular horas de enfermagem necessárias.
# 7. Comparar equipe real com equipe recomendada.
# 8. Gerar sugestão de escala balanceada por técnico/setor.
# 9. Considerar banho e curativo como carga extra.
#
# Regra específica definida:
# Se o paciente NÃO tiver banho no plantão, o sistema NÃO pergunta
# sobre curativo, pois o curativo não será considerado carga extra.
# ==========================================================


# Duração do plantão considerado no sistema
HORAS_PLANTAO = 12


# ==========================================================
# HORAS DE ENFERMAGEM POR CATEGORIA EM 24 HORAS
#
# Esses valores representam a quantidade de horas de
# enfermagem recomendadas por paciente em 24 horas.
#
# Como o sistema trabalha com plantão de 12 horas,
# o valor será dividido por 2 no momento do cálculo.
# ==========================================================

HORAS_24H = {
    "CM - Cuidados Mínimos": 4,
    "CIT - Cuidados Intermediários": 6,
    "CA - Cuidados Acamados / Alta Dependência": 10,
    "CSI - Cuidados Semi-Intensivos": 10,
    "CI - Cuidados Intensivos": 18
}


# ==========================================================
# PERCENTUAL RECOMENDADO DE ENFERMEIROS
#
# Cada categoria assistencial possui um percentual recomendado
# de enfermeiros.
#
# O restante do percentual é considerado para técnicos.
#
# Exemplo:
# 33% enfermeiros significa 67% técnicos.
# ==========================================================

PERCENTUAL_ENFERMEIRO = {
    "CM - Cuidados Mínimos": 0.33,
    "CIT - Cuidados Intermediários": 0.33,
    "CA - Cuidados Acamados / Alta Dependência": 0.36,
    "CSI - Cuidados Semi-Intensivos": 0.42,
    "CI - Cuidados Intensivos": 0.52
}


# ==========================================================
# ESCALA DE FUGULIN
#
# Cada item possui opções de 1 a 4 pontos.
#
# O usuário não precisa saber a pontuação de cabeça.
# Basta escolher a condição clínica do paciente e o sistema
# soma os pontos automaticamente.
# ==========================================================

ESCALA_FUGULIN = {
    "Estado mental": {
        1: "Orientação no tempo e espaço",
        2: "Períodos de desorientação no tempo e espaço",
        3: "Períodos de inconsciência",
        4: "Inconsciente"
    },
    "Oxigenação": {
        1: "Não depende de oxigênio",
        2: "Uso intermitente de máscara ou cateter de oxigênio",
        3: "Uso contínuo de máscara ou cateter de oxigênio",
        4: "Ventilação mecânica"
    },
    "Sinais vitais": {
        1: "Controle em intervalos de 8 horas",
        2: "Controle em intervalos de 6 horas",
        3: "Controle em intervalos de 4 horas",
        4: "Controle em intervalos menores que 2/2 horas"
    },
    "Motilidade": {
        1: "Movimenta todos os segmentos corpóreos",
        2: "Limitação de movimentos",
        3: "Movimentação passiva auxiliada pela enfermagem",
        4: "Movimentação passiva programada e realizada pela equipe de enfermagem"
    },
    "Deambulação": {
        1: "Ambulante",
        2: "Necessita de auxílio para deambular",
        3: "Locomoção através de cadeira de rodas",
        4: "Restrito ao leito"
    },
    "Alimentação": {
        1: "Auto suficiente",
        2: "Por boca com auxílio",
        3: "Através de SNG/SNE",
        4: "Através de cateter venoso central"
    },
    "Cuidado corporal": {
        1: "Auto suficiente",
        2: "Auxílio no banho no chuveiro e/ou higiene oral",
        3: "Banho no chuveiro, higiene oral realizada pela enfermagem",
        4: "Banho no leito, higiene oral realizada pela enfermagem"
    },
    "Eliminações": {
        1: "Auto suficiente",
        2: "Uso de vaso sanitário com auxílio",
        3: "Uso de comadre ou eliminações no leito",
        4: "Evacuação no leito e uso de SVD para controle de diurese"
    },
    "Terapêutica": {
        1: "IM ou VO",
        2: "Endovenosa intermitente",
        3: "Endovenosa contínua ou administrada através de SNG/SNE",
        4: "Uso de drogas vasoativas"
    },
    "Integridade cutânea-mucosa": {
        1: "Pele íntegra",
        2: "Solução de continuidade envolvendo epiderme, derme ou ambas",
        3: "Solução de continuidade envolvendo subcutâneo e músculo; incisão cirúrgica, ostomias ou drenos",
        4: "Solução de continuidade da pele com destruição da derme, epiderme e músculos"
    },
    "Curativo": {
        1: "Durante o banho",
        2: "Curativo realizado 1x/dia ou mais pela equipe de enfermagem",
        3: "Curativo realizado 2x/dia ou mais pela equipe de enfermagem",
        4: "Curativo realizado 3x/dia ou mais pela equipe de enfermagem"
    },
    "Tempo utilizado na realização de curativos": {
        1: "Sem curativo ou limpeza de ferida durante o banho",
        2: "Entre 5 e 15 minutos",
        3: "Entre 15 e 30 minutos",
        4: "Superior a 30 minutos"
    }
}


# ==========================================================
# FUNÇÃO: classificar_fugulin
#
# Recebe a pontuação total da Escala de Fugulin e retorna
# a categoria de complexidade assistencial do paciente.
# ==========================================================

def classificar_fugulin(total):
    if 12 <= total <= 17:
        return "CM - Cuidados Mínimos"
    elif 18 <= total <= 22:
        return "CIT - Cuidados Intermediários"
    elif 23 <= total <= 28:
        return "CA - Cuidados Acamados / Alta Dependência"
    elif 29 <= total <= 34:
        return "CSI - Cuidados Semi-Intensivos"
    else:
        return "CI - Cuidados Intensivos"


# ==========================================================
# FUNÇÃO: identificar_setor
#
# Identifica automaticamente o setor do paciente conforme
# o número do leito informado.
#
# Térreo: leitos 1 a 6
# 1º andar: leitos 101 a 117
# 2º andar: leitos 201 a 208
# ==========================================================

def identificar_setor(leito):
    leito_numero = int(leito)

    if 1 <= leito_numero <= 6:
        return "Térreo"
    elif 101 <= leito_numero <= 117:
        return "1º andar"
    elif 201 <= leito_numero <= 208:
        return "2º andar"
    else:
        return "Setor não identificado"


# ==========================================================
# FUNÇÃO: escolher_opcao
#
# Mostra as opções de cada item da Escala de Fugulin.
# A opção escolhida já corresponde à pontuação.
# ==========================================================

def escolher_opcao(item, opcoes):
    print("\n" + item.upper())

    for numero, descricao in opcoes.items():
        print(f"{numero} - {descricao} ({numero} ponto(s))")

    while True:
        try:
            escolha = int(input("Escolha a opção de 1 a 4: "))

            if escolha in opcoes:
                return escolha, opcoes[escolha]
            else:
                print("Opção inválida. Digite de 1 a 4.")

        except ValueError:
            print("Digite apenas números.")


# ==========================================================
# FUNÇÃO: calcular_fugulin_paciente
#
# Percorre todos os itens da Escala de Fugulin.
# Soma a pontuação escolhida pelo usuário.
# Classifica o paciente.
# Calcula as horas de enfermagem necessárias em 12 horas.
# ==========================================================

def calcular_fugulin_paciente():
    total = 0
    respostas = {}

    for item, opcoes in ESCALA_FUGULIN.items():
        pontuacao, descricao = escolher_opcao(item, opcoes)

        total = total + pontuacao

        respostas[item] = {
            "pontuacao": pontuacao,
            "descricao": descricao
        }

    categoria = classificar_fugulin(total)

    # As horas da tabela são para 24h.
    # Como o plantão é de 12h, divide por 2.
    horas_12h = HORAS_24H[categoria] / 2

    return total, categoria, horas_12h, respostas


# ==========================================================
# FUNÇÃO: arredondar_para_cima
#
# Arredonda para cima sem usar biblioteca.
# Isso é necessário porque não existe 0,4 profissional
# em uma escala real.
# ==========================================================

def arredondar_para_cima(valor):
    valor_inteiro = int(valor)

    if valor > valor_inteiro:
        return valor_inteiro + 1
    else:
        return valor_inteiro


# ==========================================================
# FUNÇÃO: calcular_carga_extra
#
# Calcula uma carga extra para ajudar na distribuição dos
# pacientes entre os técnicos.
#
# Regra definida:
# - Banho no plantão soma 5 pontos.
# - Curativo só soma mais 5 pontos se o paciente também
#   tiver banho no plantão.
# ==========================================================

def calcular_carga_extra(banho_turno, tem_curativo):
    carga_extra = 0

    if banho_turno == "sim":
        carga_extra = carga_extra + 5

        if tem_curativo == "sim":
            carga_extra = carga_extra + 5

    return carga_extra


# ==========================================================
# FUNÇÃO: distribuir_pacientes_por_setor
#
# Gera a sugestão de escala balanceada por setor.
# Distribui cada paciente para o técnico menos carregado
# dentro do mesmo setor.
# ==========================================================

def distribuir_pacientes_por_setor(pacientes, tecnicos_por_setor):
    escala_geral = {}

    for setor, quantidade_tecnicos in tecnicos_por_setor.items():
        escala_geral[setor] = []

        for i in range(quantidade_tecnicos):
            escala_geral[setor].append({
                "tecnico": f"Técnico {i + 1} - {setor}",
                "pacientes": [],
                "carga_total": 0,
                "carga_fugulin": 0,
                "total_banhos": 0,
                "total_curativos_com_banho": 0
            })

    pacientes_ordenados = sorted(
        pacientes,
        key=lambda p: p["carga_total"],
        reverse=True
    )

    for paciente in pacientes_ordenados:
        setor = paciente["setor"]

        if setor in escala_geral and len(escala_geral[setor]) > 0:
            tecnico_menos_carregado = min(
                escala_geral[setor],
                key=lambda t: t["carga_total"]
            )

            tecnico_menos_carregado["pacientes"].append(paciente)

            tecnico_menos_carregado["carga_total"] = (
                tecnico_menos_carregado["carga_total"]
                + paciente["carga_total"]
            )

            tecnico_menos_carregado["carga_fugulin"] = (
                tecnico_menos_carregado["carga_fugulin"]
                + paciente["pontuacao_fugulin"]
            )

            if paciente["banho_turno"] == "sim":
                tecnico_menos_carregado["total_banhos"] = (
                    tecnico_menos_carregado["total_banhos"] + 1
                )

            if paciente["banho_turno"] == "sim" and paciente["tem_curativo"] == "sim":
                tecnico_menos_carregado["total_curativos_com_banho"] = (
                    tecnico_menos_carregado["total_curativos_com_banho"] + 1
                )

        else:
            print(
                f"Atenção: paciente do leito {paciente['leito']} "
                f"não foi distribuído. Setor sem técnico cadastrado."
            )

    return escala_geral


# ==========================================================
# FUNÇÃO: configurar_equipe
#
# Permite informar a quantidade real de profissionais
# disponíveis no plantão.
# ==========================================================

def configurar_equipe():
    print("\nCONFIGURAÇÃO DA EQUIPE DO PLANTÃO")

    enfermeiros = int(input("Quantidade de enfermeiros no plantão: "))

    print("\nInforme a quantidade de técnicos por setor:")
    tecnicos_terreo = int(input("Técnicos no Térreo: "))
    tecnicos_primeiro = int(input("Técnicos no 1º andar: "))
    tecnicos_segundo = int(input("Técnicos no 2º andar: "))

    tecnicos_por_setor = {
        "Térreo": tecnicos_terreo,
        "1º andar": tecnicos_primeiro,
        "2º andar": tecnicos_segundo
    }

    tecnicos = tecnicos_terreo + tecnicos_primeiro + tecnicos_segundo

    return enfermeiros, tecnicos, tecnicos_por_setor


# ==========================================================
# FUNÇÃO: cadastrar_paciente
#
# Cadastra um paciente individualmente.
#
# Alteração feita:
# Se NÃO houver banho no plantão, o sistema não pergunta
# se há curativo, porque essa informação não será usada
# como carga extra na distribuição.
# ==========================================================

def cadastrar_paciente(pacientes):
    print("\nCADASTRO DE PACIENTE / FUGULIN")

    nome = input("Nome ou identificação do paciente: ")
    leito = input("Leito: ")

    setor = identificar_setor(leito)

    banho_turno = input("Paciente possui banho neste plantão? sim/não: ").lower()

    if banho_turno == "sim":
        tem_curativo = input("Paciente possui curativo junto ao banho? sim/não: ").lower()
    else:
        tem_curativo = "não"

    total, categoria, horas_12h, respostas = calcular_fugulin_paciente()

    carga_extra = calcular_carga_extra(banho_turno, tem_curativo)
    carga_total = total + carga_extra

    paciente = {
        "nome": nome,
        "leito": leito,
        "setor": setor,
        "pontuacao_fugulin": total,
        "categoria": categoria,
        "horas_12h": horas_12h,
        "banho_turno": banho_turno,
        "tem_curativo": tem_curativo,
        "carga_extra": carga_extra,
        "carga_total": carga_total,
        "respostas": respostas
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


# ==========================================================
# FUNÇÃO: cadastrar_varios_pacientes
#
# Permite cadastrar vários pacientes antes de voltar ao menu.
# ==========================================================

def cadastrar_varios_pacientes(pacientes):
    while True:
        quantidade = int(input("\nQuantos pacientes deseja cadastrar? "))

        for i in range(quantidade):
            print(f"\nCADASTRANDO PACIENTE {i + 1} DE {quantidade}")
            cadastrar_paciente(pacientes)

        continuar = input(
            "\nDeseja cadastrar mais algum paciente? sim/não: "
        ).lower()

        if continuar != "sim":
            print("\nRetornando ao menu principal...")
            break


# ==========================================================
# FUNÇÃO: mostrar_resultado_paciente
#
# Exibe os dados calculados de um paciente.
# ==========================================================

def mostrar_resultado_paciente(paciente):
    print("\n------------------------------------")
    print(f"Paciente: {paciente['nome']}")
    print(f"Leito: {paciente['leito']}")
    print(f"Setor: {paciente['setor']}")
    print(f"Pontuação Fugulin: {paciente['pontuacao_fugulin']}")
    print(f"Classificação: {paciente['categoria']}")
    print(f"Horas de enfermagem em 12h: {paciente['horas_12h']}h")
    print(f"Banho no plantão: {paciente['banho_turno']}")
    print(f"Curativo junto ao banho: {paciente['tem_curativo']}")
    print(f"Carga extra: {paciente['carga_extra']}")
    print(f"Carga total para distribuição: {paciente['carga_total']}")


# ==========================================================
# FUNÇÃO: consultar_paciente
#
# Permite consultar um paciente já cadastrado pelo nome
# ou pelo número do leito.
# ==========================================================

def consultar_paciente(pacientes):
    busca = input("\nDigite o nome ou leito do paciente: ")

    encontrado = False

    for paciente in pacientes:
        if paciente["nome"] == busca or paciente["leito"] == busca:
            mostrar_resultado_paciente(paciente)
            encontrado = True

    if encontrado == False:
        print("Paciente não encontrado.")


# ==========================================================
# FUNÇÃO: listar_pacientes
#
# Lista todos os pacientes cadastrados no sistema.
# ==========================================================

def listar_pacientes(pacientes):
    print("\nLISTA DE PACIENTES CADASTRADOS")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        for paciente in pacientes:
            print(
                f"Leito {paciente['leito']} | "
                f"{paciente['nome']} | "
                f"{paciente['setor']} | "
                f"{paciente['categoria']} | "
                f"Fugulin: {paciente['pontuacao_fugulin']} | "
                f"Banho: {paciente['banho_turno']} | "
                f"Curativo junto ao banho: {paciente['tem_curativo']}"
            )


# ==========================================================
# FUNÇÃO: consultar_dimensionamento
#
# Calcula e mostra o dimensionamento geral do plantão.
# ==========================================================

def consultar_dimensionamento(pacientes, enfermeiros, tecnicos):
    if len(pacientes) == 0:
        print("\nNenhum paciente cadastrado.")
        return

    total_horas_necessarias = 0

    for paciente in pacientes:
        total_horas_necessarias += paciente["horas_12h"]

    horas_enfermeiros_disponiveis = enfermeiros * HORAS_PLANTAO
    horas_tecnicos_disponiveis = tecnicos * HORAS_PLANTAO

    total_horas_disponiveis = (
        horas_enfermeiros_disponiveis
        + horas_tecnicos_disponiveis
    )

    total_profissionais = enfermeiros + tecnicos

    percentual_real_enfermeiro = enfermeiros / total_profissionais
    percentual_real_tecnico = tecnicos / total_profissionais

    horas_enfermeiro_necessarias = 0
    horas_tecnico_necessarias = 0

    for paciente in pacientes:
        percentual_enf = PERCENTUAL_ENFERMEIRO[paciente["categoria"]]
        percentual_tec = 1 - percentual_enf

        horas_enfermeiro_necessarias += paciente["horas_12h"] * percentual_enf
        horas_tecnico_necessarias += paciente["horas_12h"] * percentual_tec

    enfermeiros_necessarios = arredondar_para_cima(
        horas_enfermeiro_necessarias / HORAS_PLANTAO
    )

    tecnicos_necessarios = arredondar_para_cima(
        horas_tecnico_necessarias / HORAS_PLANTAO
    )

    print("\nDIMENSIONAMENTO GERAL DO PLANTÃO")
    print(f"Total de pacientes: {len(pacientes)}")
    print(f"Total de horas necessárias: {total_horas_necessarias:.2f}h")
    print(f"Total de horas disponíveis: {total_horas_disponiveis:.2f}h")

    print(f"\nHoras disponíveis de enfermeiros: {horas_enfermeiros_disponiveis:.2f}h")
    print(f"Horas disponíveis de técnicos: {horas_tecnicos_disponiveis:.2f}h")

    print(f"\nHoras necessárias de enfermeiros: {horas_enfermeiro_necessarias:.2f}h")
    print(f"Horas necessárias de técnicos: {horas_tecnico_necessarias:.2f}h")

    print(f"\nEnfermeiros necessários: {enfermeiros_necessarios}")
    print(f"Técnicos necessários: {tecnicos_necessarios}")

    print(f"\nPercentual real de enfermeiros: {percentual_real_enfermeiro * 100:.1f}%")
    print(f"Percentual real de técnicos: {percentual_real_tecnico * 100:.1f}%")

    if total_horas_disponiveis >= total_horas_necessarias:
        print("\nHoras totais disponíveis: SUFICIENTES")
    else:
        deficit = total_horas_necessarias - total_horas_disponiveis
        print("\nHoras totais disponíveis: INSUFICIENTES")
        print(f"Déficit total: {deficit:.2f}h")

    if enfermeiros >= enfermeiros_necessarios:
        print("Quantidade de enfermeiros: ADEQUADA")
    else:
        print("Quantidade de enfermeiros: ABAIXO DO RECOMENDADO")

    if tecnicos >= tecnicos_necessarios:
        print("Quantidade de técnicos: ADEQUADA")
    else:
        print("Quantidade de técnicos: ABAIXO DO RECOMENDADO")


# ==========================================================
# FUNÇÃO: consultar_escala_balanceada
#
# Mostra a sugestão de escala por técnico e por setor.
# ==========================================================

def consultar_escala_balanceada(pacientes, tecnicos_por_setor):
    if len(pacientes) == 0:
        print("\nNenhum paciente cadastrado.")
        return

    escala_por_setor = distribuir_pacientes_por_setor(
        pacientes,
        tecnicos_por_setor
    )

    print("\nSUGESTÃO DE ESCALA BALANCEADA POR SETOR")

    for setor, tecnicos_setor in escala_por_setor.items():
        print(f"\nSETOR: {setor}")
        print("------------------------------------")

        if len(tecnicos_setor) == 0:
            print("Nenhum técnico cadastrado neste setor.")

        for tecnico in tecnicos_setor:
            print(f"\n{tecnico['tecnico']}")
            print(f"Carga total: {tecnico['carga_total']} pontos")
            print(f"Carga Fugulin: {tecnico['carga_fugulin']} pontos")
            print(f"Total de banhos: {tecnico['total_banhos']}")
            print(f"Total de curativos com banho: {tecnico['total_curativos_com_banho']}")

            for paciente in tecnico["pacientes"]:
                print(
                    f"  - Leito {paciente['leito']} | "
                    f"{paciente['nome']} | "
                    f"{paciente['categoria']} | "
                    f"Fugulin: {paciente['pontuacao_fugulin']} | "
                    f"Banho: {paciente['banho_turno']} | "
                    f"Curativo junto ao banho: {paciente['tem_curativo']} | "
                    f"Carga total: {paciente['carga_total']}"
                )


# ==========================================================
# FUNÇÃO PRINCIPAL: main
#
# Controla o menu principal.
#
# Os dados dos pacientes ficam salvos na lista enquanto o
# programa estiver aberto.
# ==========================================================

def main():
    pacientes = []

    enfermeiros, tecnicos, tecnicos_por_setor = configurar_equipe()

    while True:
        print("\n====================================")
        print("MENU PRINCIPAL")
        print("====================================")
        print("1 - Cadastrar Fugulin / Paciente")
        print("2 - Consultar Fugulin por paciente")
        print("3 - Listar todos os pacientes cadastrados")
        print("4 - Consultar dimensionamento geral")
        print("5 - Consultar sugestão de escala por técnico/setor")
        print("6 - Alterar quantidade de profissionais")
        print("7 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_varios_pacientes(pacientes)

        elif opcao == "2":
            consultar_paciente(pacientes)

        elif opcao == "3":
            listar_pacientes(pacientes)

        elif opcao == "4":
            consultar_dimensionamento(pacientes, enfermeiros, tecnicos)

        elif opcao == "5":
            consultar_escala_balanceada(pacientes, tecnicos_por_setor)

        elif opcao == "6":
            enfermeiros, tecnicos, tecnicos_por_setor = configurar_equipe()
            print("\nQuantidade de profissionais atualizada com sucesso!")

        elif opcao == "7":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# ==========================================================
# INÍCIO DO PROGRAMA
# ==========================================================

main()
