""" pcadmanut """

# coding: utf-8
# Program:    pcadmanut
# Obejtivo:  Tela de Manutenção da agenda
# Data:       14/Julho/2021
# Input:     Digitação para CRUD da agenda
# Process:   Depende da opção Consulta, Inclui, Altera, Exclui
# OutPut:    Banco atualizado, pesquisa feita
# ================================================================#

import PySimpleGUI as sg
from Ccadcep import Obterend
import pcadutil as rp

# import pcadatu as patue
import pcadatuprof as patuprof  # rotinas do medico
import pcadatuende as patuende  # rotinas do endereço
import pcadatuagen as patuagen  # rotinas da agenda
import pcadatucont as patucont  # rotinas do contato
import pcadaturocm as paturocm  # rotinas comuns


# ___________________________________________________
def pxmainmnutinc(odtoprm):
    """[summary]"""

    print("PCADMANUT INC  - Recebi {}".format(odtoprm.data))

    # --- set the theme for the screen/window ---
    # sg.theme("GrayGrayGray")

    # --- Acessa DB e Monta lista de profissionais ---
    # odtoprm.data = rp.pxmntdados(odtoprm)

    # --- monta tabelas Locais e Convenio ---
    pxmontatabelas(odtoprm)

    # --- Monta tela de medico
    odtoprm.layout = pxtelacria(odtoprm)
    pxtelaprocessa(odtoprm)


# _____________________________
def pxmainmnutalt(odtoprm):
    """[summary]"""

    print("PCADMANUT ALT  - Recebi {}".format(odtoprm.data[odtoprm.row]))

    # --- monta tabelas Locais e Convenio ---
    pxmontatabelas(odtoprm)

    # ---
    odtoprm.vemcons = True
    layout = pxtelacria(odtoprm)
    odtoprm.layout = layout
    pxtelaprocessa(odtoprm)


# ____________________________________
def pxmontatabelas(odtoprm):
    """[summary]"""

    lsaux = []

    # --- Acessa DB e  Monta lista de Locais ---
    lsaux = paturocm.pxmnlocal(odtoprm)
    odtoprm.local = lsaux[0]
    odtoprm.dcloc = lsaux[1]

    # --- Acessa banco dados e Monta lista de Convenio  --
    lsaux = paturocm.pxmntconvenio(odtoprm)
    odtoprm.conv = lsaux[0]
    odtoprm.dccnv = lsaux[1]


# ____________________________________
def pxtelacria(odtoprm):
    """[summary]

    Returns:
        [type]: [description]
    """

    # --- define layout ---

    # left_col = [[sg.Frame('Médico', [[sg.Text('Médico:'), sg.Input(size=(20, 1),
    #     key='-INMED-'), sg.Button('Pesq.', key='-PSQ-')],
    #     [sg.Listbox(values=odtoprm.data, size=(34, 20), key='-LIST-', enable_events=True)]])]]

    # --- Nome ---
    layout_1 = [
        [
            sg.Text("Nome.......:", size=(10, 0)),
            sg.Input(size=(50, 0), key="nome"),
            sg.Input(
                size=(5, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="opmed",
                justification="center",
            ),
        ],
        [
            sg.Text("CRM........:", size=(10, 0)),
            sg.Input(size=(10, 0), key="crm"),
        ],
        [
            sg.Button("Salvar", key="salvar"),
            sg.Button("Excluir", key="profexc", visible=False),
            sg.Button("Limpar", key="limpar", visible=False),
            sg.Button("Voltar", key="profvoltar"),
        ],
    ]

    # --- Endereço ---
    layout_2 = [
        [
            sg.Input(
                size=(65, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="ussel",
                justification="center",
            ),
            sg.Input(
                size=(5, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="opend",
                justification="center",
            ),
        ],
        [
            sg.Text("Local......:", size=(10, 0)),
            sg.Combo(odtoprm.local, size=(10, 0), key="-local-"),
        ],
        [
            sg.Text("CEP........:", size=(10, 0)),
            sg.Input(size=(15, 0), key="cep", default_text=""),
            sg.Button("Pesq. Cep"),
        ],
        [
            sg.Text("Endereço...:", size=(10, 0)),
            sg.Input(size=(50, 0), key="ende", default_text=""),
        ],
        [
            sg.Text("Número.....:", size=(10, 0)),
            sg.Input(size=(6, 0), key="nume", default_text=""),
            sg.Text(
                "Complemento:",
                size=(10, 0),
            ),
            sg.Input(size=(6, 0), key="comp", default_text=""),
        ],
        [
            sg.Text("Cidade.....:", size=(10, 0)),
            sg.Input(size=(50, 0), key="cida", default_text=""),
        ],
        [
            sg.Text("Bairro.....:", size=(10, 0)),
            sg.Input(size=(50, 0), key="bair", default_text=""),
        ],
        [
            sg.Text("Estado.....:", size=(10, 0)),
            sg.Input(size=(3, 0), key="esta", default_text=""),
        ],
        [
            sg.Text("Telefone 1.:", size=(10, 0)),
            sg.Input(size=(50, 0), key="tel1", default_text=""),
        ],
        [
            sg.Text("Telefone 2.:", size=(10, 0)),
            sg.Input(size=(50, 0), key="tel2", default_text=""),
        ],
        [
            sg.Text("Telefone 3.:", size=(10, 0)),
            sg.Input(size=(50, 0), key="tel3", default_text=""),
        ],
        [
            sg.Text("Obs.......:", size=(10, 0)),
            sg.Input(size=(80, 0), key="obse", default_text=""),
        ],
        [
            sg.Button("Salvar", key="salvar"),
            sg.Button("Excluir", key="endeexc", visible=False),
            sg.Button("Limpar", key="limpar"),
            sg.Button("Voltar", key="endvoltar"),
        ],
    ]

    # --- Agenda ---
    layout_3 = [
        [
            sg.Input(
                size=(35, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="ussel1",
                justification="center",
            ),
            sg.Input(
                size=(5, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="opage",
                justification="center",
            ),
        ],
        [
            sg.Frame(
                "",
                [
                    [
                        sg.Text("Dia Semana", size=(10, 0)),
                        sg.Text("     Manhã", size=(7, 0)),
                        sg.Text("Tarde", size=(7, 0)),
                    ],
                    [
                        sg.CBox("Segunda", size=(10, 1), key="cb0"),
                        sg.CBox("M", key="cb1", default=False),
                        sg.CBox("T", key="cb2"),
                    ],
                    [
                        sg.CBox("Terça  ", size=(10, 1), key="cb3"),
                        sg.CBox("M", key="cb4", default=False),
                        sg.CBox("T", key="cb5"),
                    ],
                    [
                        sg.CBox("Quarta ", size=(10, 1), key="cb6"),
                        sg.CBox("M", key="cb7", default=False),
                        sg.CBox("T", key="cb8"),
                    ],
                    [
                        sg.CBox("Quinta ", size=(10, 1), key="cb9"),
                        sg.CBox("M", key="cb10", default=False),
                        sg.CBox("T", key="cb11"),
                    ],
                    [
                        sg.CBox("Sexta  ", size=(10, 1), key="cb12"),
                        sg.CBox("M", key="cb13", default=False),
                        sg.CBox("T", key="cb14"),
                    ],
                    [
                        sg.Button("Salvar", key="salvar"),
                        sg.Button("Excluir", key="agenexc", visible=False),
                        sg.Button("Limpar", key="limpar"),
                        sg.Button("Voltar", key="agevoltar"),
                    ],
                ],
            )
        ],
    ]

    # --- Contato ---
    layout_4 = [
        [
            sg.Input(
                size=(54, 0),
                background_color="white",
                text_color="blue",
                disabled=True,
                key="ussel2",
                justification="center",
            ),
            sg.Input(
                size=(5, 0),
                background_color="white",
                text_color="blue",
                disabled=False,
                key="opcon",
                justification="center",
            ),
        ],
        [
            sg.Text("Email1....:", size=(10, 0)),
            sg.Input(size=(40, 0), key="emai1"),
        ],
        [
            sg.Text("Email2....:", size=(10, 0)),
            sg.Input(size=(40, 0), key="emai2"),
        ],
        [
            sg.Text(
                "Convenio......:",
            ),
            sg.Combo(odtoprm.conv, key="-conv-"),
        ],
        [
            sg.Text("Celular1..:", size=(10, 0)),
            sg.Input(size=(20, 0), key="cel1", default_text=""),
        ],
        [
            sg.Text("Celular2..:", size=(10, 0)),
            sg.Input(size=(20, 0), key="cel2", default_text=""),
        ],
        [
            sg.Text("Celular3..:", size=(10, 0)),
            sg.Input(size=(20, 0), key="cel3", default_text=""),
        ],
        [
            sg.Text("Obs.......:", size=(10, 0)),
            sg.Input(size=(80, 0), key="obs", default_text=""),
        ],
        [
            sg.Button("Salvar", key="salvar"),
            sg.Button(
                "Excluir", key="contexc", disabled=True, visible=False
            ),  # wbf 20/10/24
            sg.Button("Limpar", key="limpar", visible=False),
            sg.Button("Voltar", key="convoltar"),
        ],
    ]

    tab_group = sg.TabGroup(
        [
            [
                sg.Tab("Profissional", layout_1, key="-prof-"),
                sg.Tab("Endereço", layout_2, key="-ende-"),
                sg.Tab("Agenda", layout_3, key="-agen-"),
                sg.Tab("Contatos", layout_4, key="-cont-"),
            ]
        ],
        enable_events=True,
    )

    right_col = [[tab_group]]

    layout = [[sg.Column(right_col, background_color="black")]]

    # layout = [[sg.Column(left_col, key='-LCOL-', background_color='black'),
    #          sg.Column(right_col, background_color='black')]]

    # layout = [[sg.Column(left_col, background_color='black'),
    #           sg.Column(right_col, background_color='black')]]

    return layout


# === Processa Tela =================
# ____________________________________
def pxtelaprocessa(odtoprm):
    """[summary]"""

    wsctrl = True

    # --- Cria a Tela ---
    window = sg.Window(
        "Agenda de Profissionais", odtoprm.layout, disable_close=True
    )  # finalize=True

    odtoprm.window = window

    # --- ler os event(key) e values(valores input)
    while wsctrl:

        # --- Ler a Windows e recebe Event e Values ---
        event, values = window.read()

        # --- Guarda os dados Lidos ---
        odtoprm.event = event
        odtoprm.values = values

        print("--- leu a tela, Guardou event e os valores----")
        print(" EVENTO: {} - ".format(event))
        print(" VALUES: {} - ".format(values))
        print("----------------------------------------------")

        rp.pxobteroper(odtoprm)

        # --- Vindo da consulta é alteração atualizar os campos na tela ---
        if odtoprm.vemcons:
            rp.pxmntddcons(odtoprm)
            rp.pxatunometela(odtoprm)
            odtoprm.vemcons = False

        else:
            # --- Testa o evento a processar ---
            if event in (sg.WIN_CLOSED, "Exit"):
                break

            if event == "Encerrar":
                window.close()

            if event == "-LIST-":
                pxproclist(values, window, odtoprm)

            elif event == "-PSQ-":
                pxprocpsq(values, window, odtoprm.data)

            elif event in (
                "profvoltar",
                "endvoltar",
                "agevoltar",
                "convoltar",
            ):
                wsctrl = False

            elif event == "Pesq. Cep":
                pxpesqcep(odtoprm)

            elif values[0] == "-prof-":
                patuprof.pxprofmain(odtoprm)

            elif values[0] == "-ende-":
                patuende.pxendemain(odtoprm)

            elif values[0] == "-agen-":
                patuagen.pxagenmain(odtoprm)

            elif values[0] == "-cont-":
                patucont.pxcontmain(odtoprm)

    window.close()


# _________________________________________________
def pxproclist(values, window, odtoprm):
    """[summary]"""

    wmed = values["-LIST-"][0]
    window["-INMED-"].update("")

    # --- Acessa DB e pega id, crm ---
    lsidcrm = paturocm.pxobtercrm(wmed, window, odtoprm)
    if lsidcrm == "Erro":
        pass  # aviso = 'existe o Nome, e não tem crm'

    else:
        # --- pega o idmed e crm do prof selecionado na list e atualiza o odtoprm  ---
        window["nome"].update(wmed)
        wcrm = lsidcrm[0][1]
        window["crm"].update(wcrm)
        odtoprm.idmed = lsidcrm[0][0]
        window["-LIST-"].Update(values=odtoprm.data)
        window["excluir"].Update(disabled=False)
        window["excluir"].v

    window["ussel"].update(wmed)
    window["ussel1"].update(wmed)
    window["ussel2"].update(wmed)
    window.Refresh()


# _________________________________________________
def pxprocpsq(values, window, data):
    """[summary]"""

    wpesq = values["-INMED-"]
    if wpesq == "*":
        window["-LIST-"].Update(values=data)
        window["-INMED-"].update("")
        window.Refresh()

    elif len(wpesq) > 2:
        pxlstpsq(wpesq, data, window)


# _________________________________________________
def pxlstpsq(search, names, window):
    """pxlstpsq [Pesquisa se o radical existe na lista
                 e remonta a lista]
    Args:
        search ([text]): [Radical de pesquisa]
        names ([List]): [List com os medicos]
        window ([class]): [Tela do programa]
    """
    i = 0
    lsmed = []
    wsmostra = True

    for name in names:

        if name[0 : len(search)].lower() in search.lower():
            lsmed.append(names[i])

        elif name[0 : len(search)].lower() > search.lower():
            window["-LIST-"].Update(values=lsmed)
            wsmostra = False
            window.Refresh()
            break

        i += 1

    if len(lsmed) == 0:
        wsmg = "Não existe NOME começando por: [" + search + "])"
        sg.popup(wsmg)
    else:
        if wsmostra:
            window["-LIST-"].Update(values=lsmed)
            wsmostra = False
            window.Refresh()


# _________________________________________________
def pxpesqcep(odtoprm):
    """[summary]"""

    cep = str(odtoprm.values["cep"])
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")
    odtoprm.values["cep"] = cep

    if len(odtoprm.values["cep"]) == 0:
        sg.popup("Cep não ionformado")

    elif len(odtoprm.values["cep"]) > 8:
        sg.popup("Tamanho do Cep > 8")

    else:
        ocep = Obterend(odtoprm.values["cep"])
        lsend = ocep.pxobterend()

        if lsend["logradouro"] == "Não há dados a serem exibidos":
            sg.popup("Não há dados a serem exibidos")
            odtoprm.window["ende"].update("")
            odtoprm.window["cida"].update("")
            odtoprm.window["bair"].update("")
            odtoprm.window["esta"].update("")
            odtoprm.window["cep"].update(lsend["cep"])

        else:
            odtoprm.window["ende"].update(lsend["logradouro"])
            odtoprm.window["cida"].update(lsend["localidade"])
            odtoprm.window["bair"].update(lsend["bairro"])
            odtoprm.window["esta"].update(lsend["uf"])
            odtoprm.window["cep"].update(lsend["cep"])

        odtoprm.window.Refresh()


# ______________________________________________
def pxatulista(odtoprm):
    """[summary]"""

    window = odtoprm.window
    lsdados = paturocm.pxmntdados(odtoprm)
    window["-LIST-"].Update(values=lsdados)


# pxmaimant()
