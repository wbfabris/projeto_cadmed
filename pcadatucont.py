""" [PCADATUCONT]  """

# coding: utf-8
# Program:   pcadatucont.py
# Obejtivo:  Atualizar os dados de contatos
# Data:      29/Agosto/2021
# Input:     Recebe os dados da tela e atualizar o DB
# Process:   recebe dados da tela
# OutPut:    DB atualizado
# ================================================================

import sys
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText, Window, popup
from ccaddb0 import Db


# ========================= CONTATO ========================
# ___________________________________________
def pxcontmain(odtoprm):
    """[Contola as ativades da Contato]"""
    if odtoprm.event == "salvar4":
        if odtoprm.dctab.get("-cont-", "*") == "INC":
            pxcontinc(odtoprm)

        elif odtoprm.dctab.get("-cont-", "*") == "ALT":
            pxcontalt(odtoprm)

    elif odtoprm.event == "contexc":
        pxcontexc(odtoprm)

    elif odtoprm.event == "limpar5":
        odtoprm.limpa_contato()


# ________________________________________
def pxcontinc(odtoprm):
    """[Incluir o Contato]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
        Critica de validação
        Inclusão no Banco de Dados
    Returns:
        DB [text]: [endereço Atualizado]
    """

    pxverconvenio(odtoprm)

    # --- Testa se o Profisional foi cadastrado ---'
    if odtoprm.dcids["id_med"] == 0:
        sg.popup_ok("Cadastre o Profissional primeiro")

    else:
        # --- Inclui Contato ---
        wtab = "TCADMEDCONT0"
        wsql = "{} {}({}, {}, \n".format(
            "INSERT INTO", "TCADMEDCONT0", "id_med", "id_conv"
        )
        wsql += "{}, {}, {}, \n".format("de_email1", "de_email2", "nu_cel1")
        wsql += "{}, {}, {}) \n".format("nu_cel2", "nu_cel3", "de_obs")
        wsql += "{} \n".format("VALUES ")
        wsql += '("{}", "{}", \n'.format(
            odtoprm.dcids["id_med"], odtoprm.dcids["id_conv"]
        )
        wsql += '"{}", "{}", "{}", \n'.format(
            odtoprm.values["emai1"],
            odtoprm.values["emai2"],
            odtoprm.values["cel1"],
        )
        wsql += '"{}", "{}", "{}")'.format(
            odtoprm.values["cel2"],
            odtoprm.values["cel3"],
            odtoprm.values["obs"],
        )
        print("====> wsql Contatos {}".format(wsql))

        odb = Db(odtoprm.pathdb, wsql, "", "")
        odb.db_conecta()
        valoretorno = odb.db_executa()

        if valoretorno is None:
            wsql = "SELECT {} FROM {} \n".format("id_cont", wtab)
            wsql += "WHERE {} = {}".format("id_med", odtoprm.dcids["id_med"])
            print("====> wsql cont id {}".format(wsql))

            odb.db_sql = wsql
            rows = odb.db_consulta()
            odb.db_comitt()
            odb.db_desconecta()

            # --- Atualiza o odtoprm ----
            odtoprm.dcids["id_cont"] = rows[0][0]
            odtoprm.dctab["-cont-"] = "ALT"
            odtoprm.window["opcon"].update(odtoprm.dctab["-cont-"])
            odtoprm.window["contexc"].Update(disabled=False)
            odtoprm.window["contexc"].Update(v=True)
            odtoprm.window.Refresh()
            sg.popup_ok("Solicitação Efetuada")


# ________________________________________
def pxcontalt(odtoprm):
    """[Alterar o Endereço]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
     + chr(34)
    Returns:
        DB [text]: [endereço Atualizado]
    """
    pxverconvenio(odtoprm)

    # --- Altera Endereço ---
    wtab = "TCADMEDCONT0"
    wsql = "{} {} \n".format("UPDATE", wtab)
    wsql += " {} \n".format("SET")
    wsql += ' {} = "{}",\n'.format("id_conv", odtoprm.dcids["id_conv"])
    wsql += ' {} = "{}",\n'.format("de_email1", odtoprm.values["emai1"])
    wsql += ' {} = "{}",\n'.format("de_email2", odtoprm.values["emai2"])
    wsql += ' {} = "{}",\n'.format("nu_cel1", odtoprm.values["cel1"])
    wsql += ' {} = "{}",\n'.format("nu_cel2", odtoprm.values["cel2"])
    wsql += ' {} = "{}",\n'.format("nu_cel3", odtoprm.values["cel3"])
    wsql += ' {} = "{}" \n'.format("de_obs", odtoprm.values["obs"])
    wsql += 'WHERE {} = "{}" \n'.format("id_med", odtoprm.dcids["id_med"])
    wsql += '  AND {} = "{}" \n'.format("id_cont", odtoprm.dcids["id_cont"])
    print("====> wsql {}".format(wsql))

    odb = Db(odtoprm.pathdb, wsql, "", "")
    odb.db_conecta()
    rows = odb.db_executa()
    odb.db_comitt()
    odb.db_desconecta()

    if rows is None:
        # --- Atualiza o odtoprm ----
        odtoprm.dctab["-cont-"] == "ALT"
        odtoprm.window["opcon"].update(odtoprm.dctab["-cont-"])
        odtoprm.window["contexc"].Update(disabled=False)
        odtoprm.window.Refresh()
        sg.popup_ok("Solicitação Efetuada")


# ________________________________________
def pxcontexc(odtoprm):
    """[Exclui o Endereço]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
       Excluir o Endereço
    Returns:
        DB [text]: [endereço Excluido]
    """

    wtab = "TCADMEDCONT0"
    wsql = "{} {} \n".format("DELETE FROM", wtab)
    wsql += 'WHERE {} = "{}"\n'.format("id_med", odtoprm.dcids["id_med"])
    wsql += '  AND {} = "{}"'.format("id_cont", odtoprm.dcids["id_cont"])
    print("====> wsql {}".format(wsql))

    odb = Db(odtoprm.pathdb, wsql, "", "")
    odb.db_conecta()
    valoretorno = odb.db_executa()
    odb.db_comitt()
    odb.db_desconecta()

    if valoretorno is None:
        # --- Atualiza o odtoprm ----
        odtoprm.dctab["-cont-"] == "INC"
        odtoprm.window["opcon"].update("INC")
        odtoprm.window["contexc"].Update(disabled=True)
        odtoprm.limpa_contato()
        sg.popup_ok("Solicitação Efetuada")


# _________________________________________
def pxverconvenio(odtoprm):
    """[summary]"""

    if odtoprm.values["-conv-"] == "":
        a = 1
    elif odtoprm.dcids["id_conv"] == odtoprm.dccnv[odtoprm.values["-conv-"]]:
        a = 1
    else:
        print("==>> convenio foi alterado")
        odtoprm.dcids["id_conv"] = odtoprm.dccnv[odtoprm.values["-conv-"]]
