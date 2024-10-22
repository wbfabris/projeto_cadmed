""" [PCADUTIL]  """

# coding: utf-8
# Program:   pcadutil
# Obejtivo:  Funções comum ao sistema
# Data:      Novembro/2020
# Input:     Rotinas Generics
# Process:   recebe dados da tela
# OutPut:    retonar um vetor com as informacoes
# ================================================================

import time
import os
import sys
import datetime
import webbrowser
import traceback
import ctypes  # An included library with Python install.
import tkinter
import PySimpleGUI as sg


# _____________________________________________________________________
def pxobtarqdb():
    """[Obtem o endereço do Banco de Dados]

    Returns:
        [list]: [path, arquivo, path\arq]
    """

    lcpath = os.getcwd() + "\\"
    lcpath = lcpath = os.getcwd() + "\\"
    lcarqd = "DCAD0000.db"
    lcarqv = lcpath + lcarqd
    plobtarq = [lcpath, lcarqd, lcarqv]
    return plobtarq


# _____________________________________________________________________
def pxobteroper(odtoprm):
    """[Atualiza a operação INC, ALT, EXC nas telas]
    Args:
        odtoprm ([type]): [description]
    """
    try:
        print("dctab - {}".format(odtoprm.dctab))
        window = odtoprm.window
        window["opmed"].update(odtoprm.dctab["-prof-"])
        window["opend"].update(odtoprm.dctab["-ende-"])
        window["opage"].update(odtoprm.dctab["-agen-"])
        window["opcon"].update(odtoprm.dctab["-cont-"])
        window.Refresh()

    except OSError as err:
        print("OPER - OS error: {0}".format(err))
        sg.PopupError("OPER - OS error: {0}".format(err))

    except:
        print("OPER - Unexpected error:", sys.exc_info()[0])
        sg.PopupError("OPER - OS error: {0}".format(sys.exc_info()[0]))


# _______________________________________________
def pxatunometela(odtoprm):
    """[Atualiza o nome nas telas]"""
    try:
        window = odtoprm.window
        window["ussel"].update(odtoprm.campo)
        window["ussel1"].update(odtoprm.campo)
        window["ussel2"].update(odtoprm.campo)
        window.Refresh()
        print("Nome nas abas {}".format(odtoprm.campo))

    except OSError as err:
        print("OS error: {0}".format(err))
        sg.PopupError("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sg.PopupError("OS error: {0}".format(sys.exc_info()[0]))
        raise


# ______________________________________________
def pxconfirma(wsmsg):
    """[summary]

    Returns:
        [type]: [description]
    """

    layout = [
        [sg.Text("{}?".format(wsmsg))],
        [sg.Button("Sim"), sg.Button("Não")],
    ]

    window = sg.Window("Confirma", layout)

    try:
        while True:  # Event Loop
            event, values = window.read(close=True)
            print(event, values)

            if event in (None, "Não"):
                break
            if event == "Sim":
                return True

        window.close()

    except Exception as e:
        tb = traceback.format_exc()
        # sg.Print(f'An error happened.  Here is the info:', e, tb)
        sg.popup_error("ERRO!", e, tb)


# ________________________________________________
def pxmntddcons(odtoprm):
    """[Monta os dados na Tela]"""

    window = odtoprm.window
    lsregsel = odtoprm.datasel

    if len(lsregsel) == 0 or lsregsel[35] is None:
        odtoprm.dctab["-prof-"] = "INC"
    else:
        odtoprm.dctab["-prof-"] = "ALT"
        window["profexc"].Update(disabled=False)  # wbf
        window["nome"].update(lsregsel[0])
        window["crm"].update(lsregsel[1])

    if lsregsel[38] is None:
        odtoprm.dctab["-ende-"] = "INC"
    else:
        odtoprm.dctab["-ende-"] = "ALT"
        window["endeexc"].Update(disabled=False)
        window["ussel"].update(lsregsel[0])
        window["-local-"].update(lsregsel[2])
        window["ende"].update(lsregsel[3])
        window["nume"].update(lsregsel[4])
        window["comp"].update(lsregsel[5])
        window["cida"].update(lsregsel[6])
        window["bair"].update(lsregsel[7])
        window["esta"].update(lsregsel[8])
        window["cep"].update(lsregsel[44])
        window["obse"].update(lsregsel[12])
        window.Refresh()

    if lsregsel[40] is None:
        odtoprm.dctab["-agen-"] = "INC"
    else:
        odtoprm.dctab["-agen-"] = "ALT"
        window["agenexc"].Update(disabled=False)
        window["ussel1"].update(lsregsel[0])
        pxmontaagenda(odtoprm)

    if lsregsel[43] is None:
        odtoprm.dctab["-cont-"] = "INC"
    else:
        odtoprm.dctab["-cont-"] = "ALT"
        window["contexc"].Update(disabled=False)
        window["ussel2"].update(lsregsel[0])
        window["emai1"].update(lsregsel[29])
        window["emai2"].update(lsregsel[30])
        window["-conv-"].update(lsregsel[28])
        window["cel1"].update(lsregsel[31])
        window["cel2"].update(lsregsel[32])
        window["cel3"].update(lsregsel[33])
        window["obs"].update(lsregsel[34])
        window.Refresh()


# _______________________________________________
def pxmontaagenda(odtoprm):
    """[summary]"""

    tabtf = [False, True]

    for col in range(13, 28):

        coluna = "{}{}".format("cb", col - 13)
        odtoprm.window[coluna].update(tabtf[odtoprm.datasel[col]])

    odtoprm.window.Refresh()


# _______________________________________________
def pxagecritica(odtoprm):
    """[summary]

    Returns:
        [type]: [description]
    """

    tabdia = ["segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    cold = 0
    # col1 = 0
    # col2 = 0
    # coluna1 = ''
    # coluna2 = ''
    # coluna3 = ''
    wret = True

    for col in range(0, 15, 3):

        col1 = col
        col2 = col1 + 1
        col3 = col1 + 2

        coluna1 = "{}{}".format("cb", col1)
        coluna2 = "{}{}".format("cb", col2)
        coluna3 = "{}{}".format("cb", col3)

        if odtoprm.values[coluna1] is True and (
            odtoprm.values[coluna2] is False
            and odtoprm.values[coluna3] is False
        ):
            sg.popup_ok(
                "Informe se o atendimento é de Manhã ou a \
                Tarde para {}".format(
                    (tabdia[cold])
                )
            )
            wret = False
            break

        elif (odtoprm.values[coluna1] is False) and (
            odtoprm.values[coluna2] is True or odtoprm.values[coluna3] is True
        ):
            wmsg = "Ative o dia da semana {}".format(tabdia[cold])
            sg.popup_ok(wmsg)
            wret = False
            break

        cold += 1
    return wret


# _______________________________________________
def pxagemontasql(odtoprm):
    """[summary]"""
    campo = ""
    valor = ""
    dcfv = {"False": 0, "True": 1}

    for col in range(0, 15):
        wcb = "{}{}".format("cb", col)
        wag = "{}{}".format("de_ag", col)

        if col < 14:
            campo += "{}, ".format(wag)
            valor += "{}, ".format(dcfv[str(odtoprm.values[wcb])])
        else:
            campo += "{} ".format(wag)
            valor += "{}".format(dcfv[str(odtoprm.values[wcb])])

    return [campo, valor]


# ___________________________________________________
def pxagemntsqlalt(odtoprm):
    """[Monta sql para replace ]

    Returns:
        [Strin]: [SQL de alteração montado]
    """

    campo = ""
    dcfv = {"False": 0, "True": 1}

    wsql = "{} \n".format("UPDATE TCADMEDAGEN0 ")
    wsql += " SET "  # {} = {}, \n'.format('id_med', odtoprm.dcids['id_med'])
    #  wsql += '     {} = {}, \n'.format('id_end', odtoprm.dcids['id_end'])

    for col in range(0, 15):
        wcb = "{}{}".format("cb", col)
        wag = "{}{}".format("de_ag", col)

        if col < 14:
            campo += "     {} = {}, \n".format(
                wag, (dcfv[str(odtoprm.values[wcb])])
            )
        else:
            campo += "     {} = {} \n".format(
                wag, (dcfv[str(odtoprm.values[wcb])])
            )

    wsql += campo
    wsql += "{} {} = {} \n".format("WHERE", "id_med", odtoprm.dcids["id_med"])
    wsql += "{} {} = {} \n".format("  AND", "id_end", odtoprm.dcids["id_end"])
    print("Agenda Alteração -\n {}".format(wsql))

    return wsql


# ___________________________________________________
def mbox(title, text, style):
    """[summary]
    Returns:
        [obj]: [Envia uma tela de sim ou não]
    """

    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    ##Ex. Mbox('Your title', 'Your text', 1)
    ## Observe que os estilos são os seguintes:
    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No
    ##  6 : Cancel | Try Again | Continue


# _________________________________________________________________
def pxobtarqmov():
    """pxobtarqmov [Obtém o path da aplicação]
    Returns:
        [list]: [com path, Arq, path+arq, aba]"""
    #
    lcpath = os.getcwd() + "\\"
    lcarq = "Extrato Mensal.xlsx"
    lcarqv = lcpath + lcarq
    lsabas = "Rascunho"
    plobtarq = [lcpath, lcarq, lcarqv, lsabas]
    return plobtarq


# _____________________________________________
def pxxopenarq(plcarq):
    """pxxopenarq [Abre o arquivo passado]
    Args:
        plcarq ([texto]): [recbe path+arquivo]
    """
    webbrowser.open(plcarq)


# ____________________________________________
def pxobtarqrelat(pwsnrel):
    """pxobtarqrelat [recebe parte do nome do relatorio]
    Args:
        pwsnrel ([list]): [com path+diretorio, arq, path+dir+arq]
    """

    lcpath = os.getcwd() + "\\Relatorio\\"
    lcarq = "RelMov" + pwsnrel + ".htm"
    lcarqv = lcpath + lcarq
    plobtarq = [lcpath, lcarq, lcarqv]
    return plobtarq


# ___________________________________________
def pxxcriakey():
    """pxxcriakey [obtem data e hora, formata]
    Returns:
       [list]: [com data formatada e aaaammddhhmmss]
    """

    lstret = []
    lsdata = datetime.datetime.now()
    lsdatafrmt = lsdata.strftime("%d/%m/%y %H:%M:%S")
    lsdataKey = (
        lsdatafrmt[6:8]
        + lsdatafrmt[3:5]
        + lsdatafrmt[0:2]
        + lsdatafrmt[9:11]
        + lsdatafrmt[12:14]
        + lsdatafrmt[15:17]
        + lsdatafrmt[18:20]
    )
    lstret = [lsdatafrmt, lsdataKey]
    return lstret


# ___________________________________________
def pxtrocaptovirg(wstexto):
    """pxtrocaptovirg [Troca o ponto por virgula]
    Args:
        wstexto ([text]): [recebe um texto 9999.99]
    Returns:
        [text]: [retorna o texto 9999,99]"""

    money = ""
    count = 0
    if ("." in wstexto) is False:
        wstexto = wstexto + ".00"

    value = str(wstexto).split(".")
    value[0] = value[0].strip()

    for digit in value[0][::-1]:
        #
        if digit == "-":
            continue
        elif count == 3:
            money = money + "." + digit
            count = 1
        else:
            money += digit
            count += 1

    if len(value[1]) == 0:
        value[1] = "00"
    elif len(value[1]) == 1:
        value[1] = value[1] + "0"

    # --- Verifica se é negativo e coloca o sinal negativo ---
    if digit == "-":
        money = money + "-"
    #
    money = money[::-1] + "," + value[1]
    # print('valor recebido {}, valor editado {}'.format(wstexto, money))
    return money


# ___________________________________________
def pxxobtermes(pwsdata):
    """[Recebe uma texto, com data,e obtem o mês]
    Returns:
        [text]: [retorna o mês por extenso]
    """
    #
    meses = (
        "mes",
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    )
    #
    wsdata = str(pwsdata)
    if wsdata[0:4].isnumeric:
        mes = int(wsdata[5:7])
    else:
        mes = int(wsdata[3:5])

    mesext = meses[mes]
    #
    return mesext


# ___ Calcula o tempo gasto _________________
def pxxduracao(lchrinicio):
    """[recebe a hora incio, obtem a hora atual e faz a diferença]
    Returns:
        [text]: [com a duração calculada e editada]
    """
    #
    lchrfim = time.perf_counter()
    lcdur = lchrfim - lchrinicio
    lcdur = str(lcdur)
    print("Duração da Função {} ".format(lcdur))
    return lcdur
    #
