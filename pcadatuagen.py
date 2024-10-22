""" [PCADATUAGEN]   """
#coding: utf-8
#Program:   pcadatuagen
#Obejtivo:  Rotinas de atualização das abas
#Data:      14/Julho/2021
#Input:     Digitação para CRUD da agenda
#Process:   Depende da opção Consulta, Inclui, Altera, Exclui
#OutPut:    Banco atualizado, pesquisa feita
#================================================================

import sys
import PySimpleGUI as sg
import pcadutil as rp
from ccaddb0 import Db

#==================== AGENDA ===========================
#________________________________________________________
def pxagenmain(odtoprm):

    """ [Contola as ativades da Agenda]
    """

    if odtoprm.event == 'salvar2':
        if odtoprm.dctab.get('-agen-', '*') == 'INC':
            pxageninc(odtoprm)

        elif odtoprm.dctab.get('-ende-', '*') == 'ALT':
            pxagenalt(odtoprm)

    elif odtoprm.event == 'agenexc':
        pxagenexc(odtoprm)

    elif odtoprm.event == 'limpar3':
        odtoprm.limpa_agenda()

#__________________________________________
def pxageninc(odtoprm):

    """ [summary]
    """
    lscpos = []

    #--- Testa se o endereço foi cadastrado ---'
    if odtoprm.dcids['id_end'] == 0:
        sg.popup_ok('Cadastre o Endereço primeiro')

    #--- Critica --
    elif rp.pxagecritica(odtoprm):

        #--- retorno lscpos = [0-Campo, 1-Valores] ---
        lscpos = rp.pxagemontasql(odtoprm)

        #--- Inclui Agenda --
        wtab = 'TCADMEDAGEN0'
        wsql = 'INSERT INTO {}({}, {}, \n'.format(wtab, 'id_med', 'id_end')
        wsql += '{})\n'.format(lscpos[0])
        wsql += '{}{}, {}, '.format('VALUES(', odtoprm.dcids['id_med'], odtoprm.dcids['id_end'])
        wsql += '{}) \n'.format(lscpos[1])
        print('====> wsql INC Agenda - {}'.format(wsql))

        odb = Db(odtoprm.pathdb, wsql, '', '')
        odb.db_conecta()
        valoretorno =  odb.db_executa()
        if valoretorno == 'ERRO':
            sys.exit()

        odb.db_comitt()
        odb.db_desconecta()

        #--- Atualiza o odtoprm ----
        odtoprm.dctab['-agen-'] = 'ALT'
        odtoprm.window['opage'].update('ALT')
        odtoprm.window['agenexc'].Update(disabled=False)
        odtoprm.window.Refresh()
        sg.popup_ok('Solicitação Efetuada')

#__________________________________________
def pxagenalt(odtoprm):

    """ [Altera]
    """

    #--- Critica ---
    if rp.pxagecritica(odtoprm):
        wsql = rp.pxagemntsqlalt(odtoprm)

        odb = Db(odtoprm.pathdb, wsql, '', '')
        odb.db_conecta()
        valoretorno =  odb.db_executa()

        if valoretorno is None:
            odb.db_comitt()
            #odb.db_desconecta()

            #--- Atualiza o odtoprm ---
            #odtoprm.dctab['-agen-'] =  'ALT'
            #odtoprm.window['opage'].update('ALT')
            #odtoprm.window['agenexc'].Update(disabled=False)
            odtoprm.window.Refresh()
            sg.popup_ok('Solicitação Efetuada')

        odb.db_desconecta()
#__________________________________________
def pxagenexc(odtoprm):

    """ [É só clicar no botão limpar ]
    """
    wtab = 'TCADMEDAGEN0'
    wsql =  '{} {} \n'.format('DELETE FROM', wtab)
    wsql += ' WHERE {} = "{}"\n'.format('id_med', odtoprm.dcids['id_med'])
    wsql += '   AND {} = "{}"\n'.format('id_end', odtoprm.dcids['id_end'])
    wsql += '   AND {} = "{}"'.format('id_agen', odtoprm.dcids['id_age'])
    print('====> wsql {}'.format(wsql))

    odb = Db(odtoprm.pathdb, wsql, '', '')
    odb.db_conecta()
    valoretorno =  odb.db_executa()
    if valoretorno is None:
        odb.db_comitt()
        odb.db_desconecta()
        #--- Atualiza o odtoprm ----
        odtoprm.dctab['-agen-'] =  'INC'
        odtoprm.window['opage'].update('INC')
        odtoprm.window['agenexc'].Update(disabled=True)
        odtoprm.limpa_agenda()
        sg.popup_ok('Solicitação Efetuada')
