""" [PCADATU]   """
#coding: utf-8
#Program:   pcadatu
#Obejtivo:  Rotinas de atualização das abas
#Data:      14/Julho/2021
#Input:     Digitação para CRUD da agenda
#Process:   Depende da opção Consulta, Inclui, Altera, Exclui
#OutPut:    Banco atualizado, pesquisa feita
#================================================================

import sys
import PySimpleGUI as sg
#from PySimpleGUI.PySimpleGUI import InputText, Window, popup
from ccaddb0 import Db
import pcadaturocm as paturocm

#================================== ENDERECO ===========================
#___________________________________________
def pxendemain(odtoprm):

    """ [Contola as ativades da Endereço]
    """

    if odtoprm.event == 'salvar0':
        if odtoprm.dctab.get('-ende-', '*') == 'INC':
            pxendeinc(odtoprm)

        elif odtoprm.dctab.get('-ende-', '*') == 'ALT':
            pxendealt(odtoprm)

    elif odtoprm.event == 'excluir':
        pxendeexc(odtoprm)

    elif odtoprm.event == 'limpar1':
        odtoprm.limpa_endereco()

#________________________________________
def pxendeinc(odtoprm):

    """ [Incluir o Endereço]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
        Critica de validação
        Inclusão no Banco de Dados
    Returns:
        DB [text]: [endereço Atualizado]
    """

    wmsg = ''

    #--- Testa se o profisional foi cadastrado ---'
    if odtoprm.dcids['id_med'] == 0:
        sg.popup_ok('Cadastre o Profissional primeiro')

    #--- Testa se o local foi cadastrado ---'
    elif odtoprm.values['-local-'] == '':
        wmsg = 'Selecione um Local'
        sg.popup(wmsg)

    else:
        odtoprm.dcids['id_local'] =  odtoprm.dcloc.get(odtoprm.values['-local-'], '*')
        #--- Valida se o endereço existe ---
        if paturocm.pxcrtende(odtoprm) == "OK":
            if (odtoprm.dcids['id_med'] == 0 or  odtoprm.dcids['id_local'] == 0):
                sg.popup_error('Erro nos ids: Med: {}, Local:{} '.format(odtoprm.dcids['id_med'],
                odtoprm.dcids['id_local']))

            else:
                #--- Inclui Endereço -
                valoretorno = ''
                wtab = 'TCADMEDEND0'
                wsql = 'INSERT INTO {}\n ('.format(wtab)
                wsql = wsql + '{}, {}, {}, '.format('id_med', 'id_local', 'nm_end')
                wsql = wsql + '{}, {}, {}, '.format('nu_end', 'de_compl', 'nm_cidade')
                wsql = wsql + '{}, {}, {}, '.format('nm_bairro', 'nm_estado', 'nu_cep')
                wsql = wsql + '{}, {}, {}, {})\n'.format('nu_tel1', 'nu_tel2', 'nu_tel3', 'de_obs')
                wsql = wsql + '{} '.format('VALUES')
                wsql = wsql + '("{}", "{}", "{}", '.format(odtoprm.dcids['id_med'],
                 odtoprm.dcids['id_local'], odtoprm.values['ende'])
                wsql = wsql + '"{}", "{}", "{}", '.format(odtoprm.values['nume'],
                 odtoprm.values['comp'], odtoprm.values['cida'])
                wsql = wsql + '"{}", "{}", "{}", "{}", '.format(odtoprm.values['bair'],
                 odtoprm.values['esta'], odtoprm.values['cep'],
                odtoprm.values['tel1'])
                wsql = wsql + '"{}", "{}", "{}")'.format(odtoprm.values['tel2'],
                 odtoprm.values['tel3'], odtoprm.values['obse'])
                print('====> wsql INC {}'.format(wsql))

                odb = Db(odtoprm.pathdb, wsql, '', '')
                odb.db_conecta()
                valoretorno =  odb.db_executa()

                if valoretorno is None:
                    wsql = 'SELECT {} FROM {} WHERE {} = {}'. format('id_end', wtab, \
                    'nm_end', chr(34) + odtoprm.values['ende'] + chr(34))
                    wsql = wsql + '  AND "{}" = "{}"'. format('nu_end', odtoprm.values['nume'])
                    wsql = wsql + '  AND "{}" = "{}"'. format('de_compl', odtoprm.values['comp'])
                    print('====> wsql idend END {}'.format(wsql))

                    odb.db_sql = wsql
                    rows = odb.db_consulta()
                    odb.db_comitt()
                    odb.db_desconecta()

                    #--- Atualiza o odtoprm ----
                    odtoprm.dcids['id_end'] = rows[0][0]
                    odtoprm.dctab['-ende-'] =  'ALT'
                    odtoprm.window['opend'].update(odtoprm.dctab['-ende-'])
                    odtoprm.window['endeexc'].Update(disabled=False)
                    odtoprm.window.Refresh()
                    sg.popup_ok('Solicitação Efetuada')

#________________________________________
def pxendealt(odtoprm):

    """ [Alterar o Endereço]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
     + chr(34)
    Returns:
        DB [text]: [endereço Atualizado]
    """

    #--- Valida se o endereço existe ---
    if  paturocm.pxcrtende(odtoprm) == 'OK':

        #--- Altera Endereço ---
        wtab = 'TCADMEDEND0'
        wsql = '{} {} \n'.format('UPDATE', wtab)
        wsql = wsql + ' SET {} = "{}",\n'.format('nm_end', odtoprm.values['ende'])
        wsql = wsql + ' {} = "{}",\n'.format('nu_end', odtoprm.values['nume'])
        wsql = wsql + ' {} = "{}",\n'.format('de_compl', odtoprm.values['comp'])
        wsql = wsql + ' {} = "{}",\n'.format('nm_cidade', odtoprm.values['cida'])
        wsql = wsql + ' {} = "{}",\n'.format('nm_bairro', odtoprm.values['bair'])
        wsql = wsql + ' {} = "{}",\n'.format('nm_estado', odtoprm.values['esta'])
        wsql = wsql + ' {} = "{}",\n'.format('nu_cep', odtoprm.values['cep'])
        wsql = wsql + ' {} = "{}",\n'.format('nu_tel1', odtoprm.values['tel1'])
        wsql = wsql + ' {} = "{}",\n'.format('nu_tel2', odtoprm.values['tel2'])
        wsql = wsql + ' {} = "{}",\n'.format('nu_tel3', odtoprm.values['tel3'])
        wsql = wsql + ' {} = "{} "\n'.format('de_obs', odtoprm.values['obse'])
        wsql = wsql + ' WHERE {} = "{}"\n'.format('id_med', odtoprm.dcids['id_med'])
        wsql = wsql + '   AND {} = "{}"\n'.format('id_end', odtoprm.dcids['id_end'])
        wsql = wsql + '   AND {} = "{}"\n'.format('id_local', odtoprm.dcids['id_local'])
        print('====> wsql {}'.format(wsql))

        odb = Db(odtoprm.pathdb, wsql, '', '')
        odb.db_conecta()
        rows =  odb.db_executa()
        odb.db_comitt()
        odb.db_desconecta()
        if rows == 'OK':
            sys.exit()
        #

        #--- Atualiza o odtoprm ----
        odtoprm.dctab['-ende-'] =  'ALT'
        odtoprm.window['opend'].update(odtoprm.dctab['-ende-'])
        odtoprm.window['endeexc'].Update(disabled=False)
        odtoprm.window.Refresh()
        sg.popup_ok('Solicitação Efetuada')

#________________________________________
def pxendeexc(odtoprm):

    """ [Exclui o Endereço]
    Args:
        odtoprm ([class]): [com todos os dados da aplicaçao]
    Process:
       Excluir o Endereço
    Returns:
        DB [text]: [endereço Excluido]
    """

    wtab = 'TCADMEDEND0'
    wsql = '{} {} \n('.format('DELETE FROM', wtab)
    wsql = wsql + ' WHERE {} = "{}",\n'.format('id_med', odtoprm.dcids['id_med'])
    wsql = wsql + '   AND {} = "{}",\n'.format('id_end', odtoprm.dcids['id_end'])
    print('====> wsql {}'.format(wsql))

    odb = Db(odtoprm.pathdb, wsql, '', '')
    odb.db_conecta()
    valoretorno =  odb.db_executa()
    if valoretorno is None:
        odb.db_comitt()
        odb.db_desconecta()
        #--- Atualiza o odtoprm ----
        odtoprm.dctab['-ende-'] =  'INC'
        odtoprm.window['opend'].update('INC')
        odtoprm.window['excluir'].Update(disabled=True)
        odtoprm.limpa_endereco()
        sg.popup_ok('Solicitação Efetuada')
