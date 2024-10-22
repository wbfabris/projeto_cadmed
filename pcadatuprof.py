""" [PCADATUPROF]   """

# coding: utf-8
# Program:   pcadatuprof
# Obejtivo:  Rotinas de atualização das abas profissional(medico)
# Data:      14/Julho/2021
# Input:     Digitação para CRUD da agenda
# Process:   Depende da opção Consulta, Inclui, Altera, Exclui
# OutPut:    Banco atualizado, pesquisa feita
# ================================================================

import PySimpleGUI as sg
import pcadutil as rp
from ccaddb0 import Db


# ====================+===== PROFISSIONAL ========================
# ___________________________________________
def pxprofmain(odtoprm):
    """[Contola as ativades do Profissional]"""

    if odtoprm.dctab["-prof-"] == "INC":
        odtoprm.window["profexc"].update(visible=False)

    elif odtoprm.dctab["-prof-"] == "ALT":
        odtoprm.window["profexc"].update(visible=False)

    if odtoprm.event == "salvar":
        if odtoprm.dctab["-prof-"] == "INC":
            pxprofinc(odtoprm)

        elif odtoprm.dctab["-prof-"] == "ALT":
            pxprofalt(odtoprm)

    elif odtoprm.event == "profexc":
        # pxprofexc(odtoprm)
        pass

    elif odtoprm.event == "limpar":
        # odtoprm.limpa_prof()
        pass


# ___________________________________________
def pxprofinc(odtoprm):
    """[Incluir o Profissional]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:

    Returns:
        nu_crm [text]: [numero do crm do medico]
    """
    # _______________________________________

    odtoprm.window["proftexc"].Update(disabled=True)

    # --- Testa se o profisional foi cadastrado ---'
    if odtoprm.values["nome"] == "":
        sg.popup_ok("Informe o nome do Profissional")
        return

    valoretorno = ""
    wtab = "Tcadmed0"
    wsql = "INSERT INTO {}({}, {}) ".format(wtab, "nm_med", "nu_crm")
    wsql = wsql + 'VALUES("{}", "{}")'.format(
        odtoprm.values["nome"], odtoprm.values["crm"]
    )

    print(f"prof inc existe {wsql}")

    odb = Db(odtoprm.pathdb, wsql, "", "")
    odb.db_conecta()
    valoretorno = odb.db_executa()
    if valoretorno is None:
        wsql = "SELECT {} FROM {} WHERE {} = {}".format(
            "id_med",
            wtab,
            "nm_med",
            chr(34) + odtoprm.values["nome"] + chr(34),
        )
        odb.db_sql = wsql
        rows = odb.db_consulta()
        odb.db_comitt()
        odb.db_desconecta()
        #
        # --- Atualiza o odtoprm ----
        odtoprm.dcids["id_med"] = rows[0][0]
        odtoprm.dctab["-prof-"] = "ALT"
        odtoprm.campo = odtoprm.values["nome"]
        rp.pxatunometela(odtoprm)
        rp.pxobteroper(odtoprm)
        odtoprm.window["profexc"].Update(disabled=False)
        odtoprm.window["profexc"].Update
        sg.popup_ok("Solicitação Efetuada")


# ___________________________________________
def pxprofalt(odtoprm):
    """[Alterar o Profissional]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
        Alterar o registro
    Returns:
        nu_crm [text]: [numero do crm do medico]
    """
    # --- chr(34)=" e chr(39)='
    # ------------------------------------------------
    valoretorno = ""
    wtab = "TCADMED0"

    wsql = "UPDATE {} ".format(wtab)
    wsql = (
        wsql
        + " SET nm_med = "
        + chr(34)
        + odtoprm.values["nome"]
        + chr(34)
        + ",\n"
    )
    wsql = (
        wsql
        + "     nu_crm = "
        + chr(34)
        + odtoprm.values["crm"]
        + chr(34)
        + "\n"
    )
    wsql = wsql + " {} = {}".format(
        "WHERE id_med ", odtoprm.data[odtoprm.row][35]
    )

    print("upd med == {}".format(wsql))

    odb = Db(odtoprm.pathdb, wsql, "", "")
    odb.db_conecta()
    valoretorno = odb.db_executa()

    if valoretorno is None:
        odb.db_comitt()
        odb.db_desconecta()
        # --- Atualiza o odtoprm ----
        odtoprm.campo = odtoprm.values["nome"]
        rp.pxatunometela(odtoprm)
        rp.pxobteroper(odtoprm)
        odtoprm.window["profexc"].Update(disabled=False)
        odtoprm.window.Refresh()
        sg.popup_ok("Solicitação Efetuada")


# __________________________________
def pxprofexc(odtoprm):
    """[Excluir o Profissional]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
        Alterar o registro
    Returns:
        nu_crm [text]: [numero do crm do medico]
    """
    # --- chr(34)=" e chr(39)='
    # ------------------------------------------------
    valoretorno = ""
    wtab = "TCADMED0"
    # valoretorno = rp.mbox('Exclusão', 'Confirma a Exclusão de ' + odtoprm.values['nome'] + '?', 4)
    valoretorno = sg.popup_ok_cancel(
        "Exclusão,\
     Confirma a Exclusão de {"
        + odtoprm.values["nome"]
        + "}?"
    )
    if valoretorno == "OK":

        wsql = "DELETE FROM {} ".format(wtab)
        wsql += " {} = {}".format("WHERE id_med ", odtoprm.dcids["id_med"])

        print("==> del medico {} {}".format(odtoprm.dcids["id_med"], wsql))

        odb = Db(odtoprm.pathdb, wsql, "", "")
        odb.db_conecta()
        valoretorno = odb.db_executa()
        if valoretorno is None:
            # --- Atualiza o odtoprm ----
            odb.db_comitt()
            odb.db_desconecta()
            odtoprm.limpa_prof()
            odtoprm.limpa_endereco()
            odtoprm.limpa_agenda()
            odtoprm.limpa_contato()
            odtoprm.campo = ""
            rp.pxatunometela(odtoprm)
            sg.popup_ok("Solicitação Efetuada")

    else:
        sg.popup_ok("Exclusão do Profissional, Cancelada pelo Usuário")
        # rp.mbox('Exclusão', 'Cancelada pelo Usuário', 4)
