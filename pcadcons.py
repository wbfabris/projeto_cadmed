""" [pcadcons]   """

# coding: utf-8
# Program:    pcadcons
# Obejtivo:  Tela de consulta dos medicos
# Data:       14/Julho/2021
# Input:     DB de Medicos e lista todos
# Process:   lista todos.
# OutPut:    Se clica em alguma linha, retorna o nome do medico.

import PySimpleGUI as sg
import pcadaturocm as paturocm  # rotinas avulsas


# __________________________________________
def pxmaincon(odtoprm):
    """pxmaincon [Controle do  Programa]
    Returns:
        [list]: [lista completa e o registro se selecionado
    """

    paturocm.pxmontaconsulta(odtoprm)

    # --- Cria a tela e Envia ---
    odtoprm.layout = pxtelacria(odtoprm)
    # odtoprm.layout = layout

    # --- Gerencia a tela  de consulta ---
    pxproctela(odtoprm)
    # odtoprm = pxproctela(odtoprm)"


# __________________________________________
def pxtelacria(odtoprm):
    """pxtelacria [Recebe a lista Formatada para a Consulta,
                   e cria a tela de consulta]
    Returns:
        [ ]: [layout - o desneho da tela]
    """

    # --- Cabeçalho ----
    headings = [
        "Nome",
        "Local",
        "Endereço",
        "Nº",
        "Comp",
        "Tel1",
        "Agenda",
        "Conv",
        "Cel1",
    ]

    # --- Tamanho dos Campos do Cabeçalho ----
    data_cols_width = [20, 9, 20, 5, 5, 15, 34, 15, 15]

    # --- Layout da Tela ----
    layout = [
        [
            sg.Table(
                values=odtoprm.datafrmt,
                headings=headings,
                auto_size_columns=False,
                max_col_width=120,
                # header_text_color='withe',
                # header_background_color='blue',
                text_color="black",
                background_color="white",
                alternating_row_color="#e5ebd6",  # FFFFCC',   #'papaya whip',
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                col_widths=data_cols_width,
                vertical_scroll_only=False,
                num_rows=30,
                justification="left",  # 41
                enable_events=True,
                key="_filestable",
            )
        ],
        [sg.Button("Voltar", key="voltar")],
    ]

    return layout


# __________________________________________
def pxproctela(odtoprm):
    """pxproctela  [Recebe o layout da Tela e a DTO com os dados necessários ao sistema
                 e envia a tela, e aguarda interação do usuário]
    Args:
     layout ([Layout]): [Layout da tela de Consulta]
     odtoprm ([List]): [DTO com todos os campos necessários ao sistema]
    Returns:
      [list]: [odtoprm, e o número da linha seleciona]
    """

    # --- Cria a Tela ----
    window = sg.Window(
        "Relação dos medicos",
        odtoprm.layout,
        location=(0, 0),
        disable_close=True,
        finalize=True,
    )

    # window.maximize()
    odtoprm.window = window

    # --- Loop até Selecionar uma Linha voltar para o programa de Menu ----
    wsctrl = True
    while wsctrl:
        event, values = window.read()

        print("Evento: {}, Valores: {}".format(event, values))

        if event in (sg.WIN_CLOSED, "Quit"):
            break

        if event in ("voltar", "Quit"):
            odtoprm.wctralt = False
            wsctrl = False

        if event in ("Encerrar", "Quit"):
            odtoprm.wctralt = False
            wsctrl = False

        if event == "_filestable":
            if odtoprm.opcmenu == "ALT":
                row = values["_filestable"]
                row = row[0]
                odtoprm.row = row
                odtoprm.datasel = odtoprm.data[row]
                pxmontaid(odtoprm)
                odtoprm.campo = odtoprm.data[row][0]

                print("Linha    Selecionada: {}".format(row))
                print("Registro Selecionado: {}".format(odtoprm.datasel))
                print("Ids  Reg Selecionado: {}".format(odtoprm.dcids))
                wsctrl = False

    #
    window.close()


def pxmontaid(odtoprm):
    """[Preenche os ids das tabelas]"""

    # --- id do medico ---
    if odtoprm.datasel[35] is None:
        odtoprm.dcids["med"] = 0
    elif odtoprm.datasel[35] > 0:
        odtoprm.dcids["id_med"] = odtoprm.datasel[35]

    # --- id do Local ---
    if odtoprm.datasel[37] is None:
        odtoprm.dcids["id_local"] = 0
    elif odtoprm.datasel[37] > 0:
        odtoprm.dcids["id_local"] = odtoprm.datasel[37]

    # --- id do Endereço ---
    if odtoprm.datasel[38] is None:
        odtoprm.dcids["id_end"] = 0
    elif odtoprm.datasel[38] > 0:
        odtoprm.dcids["id_end"] = odtoprm.datasel[38]

    # --- id da Agenda ---
    # --- utiliza o id_med e id_end ---
    if odtoprm.datasel[45] is None:
        odtoprm.dcids["id_agen"] = 0
    elif odtoprm.datasel[45] > 0:
        odtoprm.dcids["id_agen"] = odtoprm.datasel[45]

    # --- id do Contato ---
    if odtoprm.datasel[42] is None:
        odtoprm.dcids["id_cont"] = 0
    elif odtoprm.datasel[43] > 0:
        odtoprm.dcids["id_cont"] = odtoprm.datasel[42]

    # --- id do Convenio ---
    if odtoprm.datasel[43] is None:
        odtoprm.dcids["id_conv"] = 0
    elif odtoprm.datasel[43] > 0:
        odtoprm.dcids["id_conv"] = odtoprm.datasel[43]
