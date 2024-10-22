# PCADMENU
""" [PCADMENU] """
# coding: utf-8
# Program:    pcadmenu
# Obejtivo:  Tela de Escolha da opção
# Data:       14/Julho/2021
# Input:     Digitação para CRUD da agenda
# Process:   Depende da opção Consulta, Inclui, Altera, Exclui
# OutPut:    Banco atualizado, pesquisa feita

import PySimpleGUI as sg
from ccaddtoprm import Dtoprm
import pcadcons as con
import pcadmanut as alt
import pcadutil as rp


# ____________________________________
def pxmenumain():
    """[summary]"""

    # --- Cria o layout da tela ---
    layout = pxtelacria()

    # --- Cria o layout da tela ---a
    pxtelaprocessa(layout)


# ____________________________________
def pxtelacria():
    """[summary]

    Returns:
        [type]: [description]
    """

    # --- Cria o Frame_Layout ---
    layout_frame = [
        [sg.Text("Selecione uma Opção")],
        [
            sg.Radio(
                "           Consultar",
                "RADIO1",
                size=(200, 1),
                key="CON",
                default=False,
                enable_events=True,
            )
        ],
        [
            sg.Radio(
                "           Cadastrar",
                "RADIO1",
                size=(200, 1),
                key="INC",
                default=False,
                enable_events=True,
            )
        ],
        [
            sg.Radio(
                "           Alterar  ",
                "RADIO1",
                size=(200, 1),
                key="ALT",
                default=False,
                enable_events=True,
            )
        ],
        [
            sg.Radio(
                "           Finalizar",
                "RADIO1",
                # size=(10, 1),
                # size=(200, 1),
                key="FIM",
                default=False,
                enable_events=True,
            )
        ],
    ]

    # --- Cria o Layout ---
    layout = [[sg.Frame("Menu do Sistema", layout_frame, title_color="blue")]]

    return layout


# ____________________________________
def pxtelaprocessa(layout):
    """[summary]"""

    # --- Cria a Tela ----
    window = sg.Window(
        "Menu de Opções",
        layout,
        disable_close=True,
        size=(210, 210),
        finalize=True,
    )

    # --- Loop até Selecionar uma Linha e ir para o programa de Atualização ---
    wscrtl = True
    while wscrtl:
        event, values = window.read()

        print(" MENU - event: {}, values: {}".format(event, values))

        if event in (sg.WIN_CLOSED, "Quit"):
            sg.popup_auto_close("Saindo e Obrigado")
            break

        if values["CON"]:
            pxconsulta()

        elif values["INC"]:
            pxmanutinc()

        elif values["ALT"]:
            pxmanutalt()

        elif values["FIM"]:
            wscrtl = False

        window["CON"].Update(False)
        window["INC"].Update(False)
        window["ALT"].Update(False)
        window["FIM"].Update(False)

    window.close()


# _____________________________________________
def pxconsulta():
    """[summary]"""

    # --- obter path do Banco de Dados ---
    lsarqdb = rp.pxobtarqdb()
    odtoprm = Dtoprm(lsarqdb[2], lsarqdb[2])
    odtoprm.opcmenu = "INC"

    con.pxmaincon(odtoprm)


# _____________________________________________
def pxmanutinc():
    """[summary]"""
    lsaux = []

    # --- obter path do Banco de Dados ---
    lsarqdb = rp.pxobtarqdb()
    odtoprm = Dtoprm(lsarqdb[2], lsarqdb[2])
    odtoprm.opcmenu = "INC"

    for idx in range(0, 46):
        lsaux.append("")

    odtoprm.data = list(lsaux)
    odtoprm.data[35] = 0
    print("odtoprm:{}".format(odtoprm))

    alt.pxmainmnutinc(odtoprm)


# _______________________________________________
def pxmanutalt():
    """[summary]"""

    lsarqdb = rp.pxobtarqdb()
    odtoprm = Dtoprm(lsarqdb[0], lsarqdb[2])
    odtoprm.opcmenu = "ALT"

    # --- Loop até Selecionar fim na tela de consulta ---
    while odtoprm.wctralt:

        # --- Obtém os registros formatados para a consulta ---
        con.pxmaincon(odtoprm)

        # --- Voltou da Consulta --
        if odtoprm.wctralt:
            # --- Obtem as operações para cada ABA --
            pxmntoperoper(odtoprm)
            # --- Passa o Registro Selecionado para Alteração/Exclusão ---
            # --- Chama o programa de Alteração ---
            alt.pxmainmnutalt(odtoprm)


# ________________________________________________
def pxmntoperoper(odtoprm):
    """[summary]
    Returns:
        [type]: [description]
    """

    # dctab = {'-prof-': 'INC', '-ende-': 'INC', '-agen-': 'INC', '-cont-': 'INC'}

    if odtoprm.row == 0 or odtoprm.row is None:
        pass
    else:
        # --- prof -------------------
        if odtoprm.datasel[35] is None:
            odtoprm.dctab["-prof-"] = "INC"
        else:
            odtoprm.dctab["-prof-"] = "ALT"

        # --- ende  -------------------
        if odtoprm.datasel[38] is None:
            odtoprm.dctab["-ende-"] = "INC"
        else:
            odtoprm.dctab["-ende-"] = "ALT"

        # --- agen --------------------
        if odtoprm.datasel[40] is None:
            odtoprm.dctab["-agen-"] = "INC"
        else:
            odtoprm.dctab["-agen-"] = "ALT"

        # --- cont -------------------
        if odtoprm.datasel[43] is None:
            odtoprm.dctab["-cont-"] = "INC"
        else:
            odtoprm.dctab["-cont-"] = "ALT"


print("Iniciando projeto CadMed")
pxmenumain()
