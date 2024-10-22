""" PCADATUROAV """
#coding: utf-8
#Program:   pcadaturoav
#Obejtivo:  Rotinas de atualização das abas
#Data:      14/Julho/2021
#Input:     Digitação para CRUD da agenda
#Process:   Depende da opção Consulta, Inclui, Altera, Exclui
#OutPut:    Banco atualizado, pesquisa feita
#================================================================

import sys
import PySimpleGUI as sg
from ccaddb0 import Db

#========================== ROTINAS AVULSAS E COMUNS ==================
def pxmontaconsulta(odtoprm):

    """ [Monta a Consulta dos Profissionais]
    """

    lsdata = []
    #--- obtém todos registros do Cadastro ---
    lsdata = pxobterdados(odtoprm)
    odtoprm.data = lsdata

    #--- Formata o registro para a Consulta ---
    if len(odtoprm.data) == 0:
        sg.popup('Consulta Cadastro de Profissionais Vazio')

    else:
        #--- Recebe os registros formatados para a consulta ---
        odtoprm.datafrmt =pxfrmtdados(odtoprm)

#_____________________________________________________________________
def pxmntdados(odtoprm):

    """[summary]

    Returns:
        [type]: [description]
    """

    lsmed = []
    #window = odtoprm.window
    wssql = 'SELECT nm_med FROM Tcadmed0 ORDER BY nm_med'

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        sg.popup_error('Erro Medico não Cadastrado no banco de dados')
    else:
        for row in rows:
            #for col in range(0, len(row)):
            for col in row:
                lsmed.append(row[col])

    return lsmed

# __________________________________________
def pxobterdados(odtoprm):

    """[Prepara o Sql, para trazer todos
        registros os dados da Base de dados]
    Returns:
        [list]: [lista com os profissionais cadastrados]
    """

    wsql = '{} \n'.format('SELECT med.nm_med, nu_crm, ')    # 0, 1
    wsql = wsql + '{} \n'.format('loc.nm_local, end.nm_end, \
        end.nu_end, end.de_compl, ')    # 2, 3, 4, 5,
    wsql = wsql + '{} \n'.format('end.nm_cidade, end.nm_bairro, \
        end.nm_estado, ')               # 6, 7, 8,
    wsql = wsql + '{} \n'.format('end.nu_tel1, end.nu_tel2, \
        end.nu_tel3, end.de_obs, ')     # 9, 10, 11, 12(obs)
    wsql = wsql + '{}, \n'.format('agen.de_ag0, agen.de_ag1,\
        agen.de_ag2 ')                  # 13, 14, 15,
    wsql = wsql + '{}, \n'.format('agen.de_ag3, agen.de_ag4, \
        agen.de_ag5 ')                  # 16, 17, 18,
    wsql = wsql + '{}, \n'.format('agen.de_ag6, agen.de_ag7, \
        agen.de_ag8 ')                  # 19, 20, 21,
    wsql = wsql + '{}, \n'.format('agen.de_ag9, agen.de_ag10, \
        agen.de_ag11 ')                 # 22, 23, 24,
    wsql = wsql + '{}, \n'.format('agen.de_ag12, agen.de_ag13, \
        agen.de_ag14 ')                 # 25, 26, 27,
    wsql = wsql + '{} \n'.format('conv.nm_conv, cont.de_email1, \
        cont.de_email2, ')              # 28, 29, 30,
    wsql = wsql + '{} \n'.format('cont.nu_cel1, cont.nu_cel2, \
        cont.nu_cel3, cont.de_obs,' )   # 31, 32, 33, 34
    wsql = wsql + '{} \n'.format('med.id_med,')                            # 35
    wsql = wsql + '{} \n'.format('end.id_med, end.id_local, end.id_end,' ) # 36, 37, 38
    wsql = wsql + '{} \n'.format('agen.id_med, agen.id_end,' )             # 39, 40
    wsql = wsql + '{} \n'.format('cont.id_med, cont.id_cont,')             # 41, 42
    wsql = wsql + '{} \n'.format('cont.id_conv, end.nu_cep,')              # 43, 44
    wsql = wsql + '{} \n'.format('agen.id_agen')                           # 45
    wsql = wsql + '{} \n'.format('FROM ')
    wsql = wsql + '{} \n'.format(' TCADMED0 med ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDEND0  end  ON (med.id_med   = end.id_med)')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADLOC0     loc  ON (end.id_local = loc.id_local)')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDAGEN0 agen ON (med.id_med   = agen.id_med)')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDCONT0 cont ON (med.id_med   = cont.id_med)')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADCONV0    conv ON (cont.id_conv = conv.id_conv)')
    wsql = wsql + '{} \n'.format('ORDER BY nm_med')
    print('wsql Consulta: \n{}'.format(wsql))

    oDb = Db(odtoprm.pathdb, wsql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        sg.popup_ok('Cadastro Vazio')

    return rows

# __________________________________________
def pxobteratuliz(odtoprm):

    """[Prepara o Sql, para trazer um Registro Atualizado]

    Returns:
        [list]: [lista com o profissionail cadastrado]
    """

    wsql = '{} \n'.format('SELECT med.nm_med, nu_crm, ')        # 0, 1
    wsql = wsql + '{} \n'.format('loc.nm_local, end.nm_end, \
        end.nu_end, end.de_compl,  ')                           # 2, 3, 4, 5,
    wsql = wsql + '{} \n'.format('end.nm_cidade, end.nm_bairro, \
        end.nm_estado, ')                                       # 6, 7, 8,
    wsql = wsql + '{} \n'.format('end.nu_tel1, end.nu_tel2, \
        end.nu_tel3, end.de_obs, ')                            # 9, 10, 11, 12(obs)
    wsql = wsql + '{}, \n'.format('agen.de_ag0, agen.de_ag1, agen.de_ag2 ')     # 13, 14, 15,
    wsql = wsql + '{}, \n'.format('agen.de_ag3, agen.de_ag4, agen.de_ag5 ')     # 16, 17, 18,
    wsql = wsql + '{}, \n'.format('agen.de_ag6, agen.de_ag7, agen.de_ag8 ')     # 19, 20, 21,
    wsql = wsql + '{}, \n'.format('agen.de_ag9, agen.de_ag10, agen.de_ag11 ')   # 22, 23, 24,
    wsql = wsql + '{}, \n'.format('agen.de_ag12, agen.de_ag13, agen.de_ag14 ')  # 25, 26, 27,
    wsql = wsql + '{} \n'.format('conv.nm_conv, cont.de_email1,\
        cont.de_email2, ')      # 28, 29, 30,
    wsql = wsql + '{} \n'.format('cont.nu_cel1, cont.nu_cel2, cont.nu_cel3, \
        cont.de_obs,' )         # 31, 32, 33, 34
    wsql = wsql + '{} \n'.format('med.id_med,')                             # 35
    wsql = wsql + '{} \n'.format('end.id_med, end.id_local, end.id_end,' )  # 36,37, 38
    wsql = wsql + '{} \n'.format('agen.id_med, agen.id_end,' )              # 39, 40
    wsql = wsql + '{} \n'.format('cont.id_med, cont.id_cont, cont.id_conv, \
        end.nu_cep, agen.id_agen ')    # 41, 42, 43, 44(cep)
    wsql = wsql + '{} \n'.format('FROM ')
    wsql = wsql + '{} \n'.format(' TCADMED0 med ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDEND0  end  ON (med.id_med   = end.id_med) ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADLOC0     loc  ON (end.id_local = loc.id_local) ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDAGEN0 agen ON (end.id_end   = agen.id_end) ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADMEDCONT0 cont ON (med.id_med   = cont.id_med) ')
    wsql = wsql + '{} \n'.format('  LEFT JOIN TCADCONV0    conv ON (cont.id_conv = conv.id_conv) ')

    if odtoprm.datasel[35] is None:
        pass
    elif odtoprm.datasel[35] > 0:
        wsql = wsql + '{} {}  \n'.format(' WHERE med.id_med = ', odtoprm.datasel[35])

    if odtoprm.datasel[38] is None:
        pass
    elif odtoprm.datasel[38] > 0:
        wsql = wsql + '{} {} \n'.format('    AND end.id_end = ', odtoprm.datasel[38])

    if odtoprm.datasel[42] is None:
        pass
    elif odtoprm.datasel[42] > 0:
        wsql = wsql + '{} {} \n'.format('    AND cont.id_cont = ', odtoprm.datasel[42])

    if odtoprm.datasel[43] is None:
        pass
    elif odtoprm.datasel[43] > 0:
        wsql = wsql + '{} {}  \n'.format(' WHERE conv.id_conv = ', odtoprm.datasel[43])

    wsql = wsql + '{} \n'.format('ORDER BY nm_med')
    print('wsql:\n{}'.format(wsql))

    oDb = Db(odtoprm.patharq, wsql, ',', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        sg.popup_ok('Obter pxobteratuliz - Não Encontrou')

    odtoprm.data = rows

#____________________________________
def pxfrmtdados(odtoprm):

    """[Recebe a base de dados e Formata para
         serem mostrados na consula para  seleção]
    Returns:
        [list]: [lista formatada para exibição]
    """

    lsaux = []
    lsdados = []
    valret = ''
    tabcol = [0, 2, 3, 4, 5, 9, 13, 28, 31]
    #['Nome', 'Local', 'Endereço', 'Nº', 'Comp', 'Tel1', 'Agenda', 'Conv', 'Cel1']

    rows = odtoprm.data

    for row in rows:
        for ind in range(0, len(tabcol)):
            col = tabcol[ind]
            if (row[col] is None) or (row[col] is False):
                valret = '  '
            else:
                valret = row[col]

            #--- col =13, Formatando a agenda para exibição na consulta ---
            #== Se mexer na tabcol, tem que alterar a col ---
            if col == 13:
                valret = pxmntage(row)

            lsaux.append(valret) #Agenda

        #--- Grava a linha da consulta em lsdadoss
        lsdados.append(list(lsaux))
        lsaux.clear()

    return lsdados

#___________________________________________
def pxmntage(row):

    """ [Recebe o registro que contem a agenda e formata]
    Returns:
        [str]: [Retorna uma string no formato, dª, M T,]
    """

    tbdsem = ['2ª', 'M', 'T', '3ª', 'M', 'T', '4ª', 'M', 'T', '5ª', 'M', 'T', '6ª', 'M', 'T']
    lsdsem = []
    col1 = 0
    col2 = 0
    wage = ''

    for col in range(13, 28, 3):
        col1 = col + 1
        col2 = col + 2
        #--- Testa o dia da semana se None, não existe a Agenda ---
        if wage == 'Sem Agendamento':
            pass # 'ler proximo'
        #
        elif (row[13] is None or row[13] is False) and \
            (row[16] is None or row[16] is False) and \
            (row[19] is None or row[19] is False) and \
            (row[22] is None or row[22] is False) and \
            (row[25] is None or row[25] is False):
            wage = 'Sem Agendamento'
        else:
            #--- Monta o Agenda ---
            #--- Dia --------------
            if row[col] == True:
                wage = wage + tbdsem[col - 13] + ' '
                #--- Manhã (M)-----------------
                if row[col1] == True:
                    wage = wage +tbdsem[col1 - 13] + ' '
                else:
                    wage = wage +  '* '
                #--- Tarde (M)-----------------
                if row[col2] == True:
                    wage = wage + tbdsem[col2 - 13] + ', '
                else:
                    wage = wage + '*, '

    lsdsem.append(wage)

    return wage

#_____________________________________________________________________
def pxmnlocal(odtoprm):

    """[summary]

    Returns:
        [type]: [description]
    """

    lsloc = []
    dcloc = {}
    #dcloc[str(pkey)] = valor

    wssql = 'SELECT id_local, nm_local FROM TCADLOC0 ORDER BY nm_local'

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        sg.popup_error('Não tem LOCAL Cadastrado')
    else:
        for row in rows:
            lsloc.append(row[1])
            dcloc[row[1]] = row[0]

        return [lsloc, dcloc]

#_____________________________________________________________________
def pxmntconvenio(odtoprm):

    """[summary]

    Returns:
        [type]: [description]
    """

    lscnv = []
    dccnv = {}
    #dcdic[str(pkey)] = valor

    wssql = 'SELECT id_conv, nm_conv FROM TCADCONV0 ORDER BY nm_conv'

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        pass
        #sg.popup_ok('Sem Convenio Cadastrado')
    else:
        for row in rows:
            lscnv.append(row[1])
            dccnv[row[1]] = row[0]

        return [lscnv, dccnv]

#_____________________________________________________________________
def pxobtercrm(pmed, window, odtoprm):

    """ [obter o crm do medico]
    Args:
            pmed ([text]): [nome do medico]
            wsql ([text]): [Sql para obter o numero do crm]
            Db   ([Class]): [Inicialização, db_nome, db_sql, db_tabela, db_value
                              db_tabela, db_value, passe vazio]
    Returns:
        nu_crm [text]: [numero do crm do medico]
    """

    wssql = 'SELECT id_med, nu_crm FROM Tcadmed0 WHERE LOWER(nm_med) = ' +  \
     'LOWER(' + chr(34) + pmed + chr(34) +')'

    print('wssql - {}'.format(wssql))

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        rows = ''
        #sg.popup_ok('Erro Medico não Cadastrado no DB')   #teste

    return rows

#_______________________________________________________________________
def pxcrtende(odtoprm):

    """ {Critica de Endereço ]
    Args:
        odtoprmv ([Class]): [Parametros para validar o Endereço]
    Returns:
        True/False [Bolean]: [Se Existe o Endereço / Se NÃO Existe]
    """

    #--- Verifica se existe o endereço ---
    wtab = 'TCADMEDEND0'
    wsql = '{}'.format('SELECT Count(*) ')
    wsql = wsql + ' FROM {} '.format(wtab)
    wsql = wsql + 'WHERE "{}" = "{}" '.format('id_med', odtoprm.dcids['id_med'])
    wsql = wsql + '  AND "{}" = "{}" '.format('id_end', odtoprm.dcids['id_end'])
    wsql = wsql + '  AND "{}" = "{}" '.format('nm_end', odtoprm.values['ende'])
    wsql = wsql + '  AND "{}" = "{}" '.format('nu_end', odtoprm.values['nume'])
    wsql = wsql + '  AND "{}" = "{}" '.format('de_compl', odtoprm.values['comp'])
    print('wsql Valida Endereço do Profissional - {}'.format(wsql))

    #lsarqdb = odtoprm.pathdb
    oDb = Db( odtoprm.pathdb, wsql, '','')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    wsret = 'OK'
    wqtos = int(rows[0][0])
    if wqtos > 0:
        wsmsg = 'Já CADASTRADO, este Endereço, Número/complemento'
        sg.popup_error(wsmsg)
        wsret =  'ERRO'

    return wsret

#_____________________________________________________________________
def pxobteridloc(odtoprm):

    """ [obter o id do local]
    Args:
        Db ([Class]): [Inicialização, db_nome, db_sql, db_tabela, db_value
                        db_tabela, db_value, passe vazio]
    Returns:
        id_loc [num]: [numero do crm do id do local]
    """
    wsret = 'ERRO'
    wssql = "SELECT id_local FROM TCADLOC0 WHERE LOWER(nm_local) = " +  \
        "LOWER(" + chr(34) + odtoprm.values['-local-'] + chr(34) + ")"

    print('wssql - {}'.format(wssql))

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 0:
        wsret = 9999
        #sg.popup_error('ERRO ' +  odtoprm.values['-local']  + ' não Cadastrado no DB')   #teste
    else:
        odtoprm.idloc = rows[0][0]
        wsret = 'OK'

    return wsret

#___________________________________________________
def pxvalidaagenda(odtoprm):

    """ [Valida se ja existe agenda para medicox endereço
    Args:
            odtoprm ([class]): [classe com os dados do sistema]
            wsql    ([text]): [Sql para validar medico/enderço]
            Db      ([Class]): [Inicialização, db_nome, db_sql, db_tabela, db_value
                              db_tabela, db_value, passe vazio]
    Returns:
        rows [text]: [0 - Não Existe, 1- Ja existe a agenda]
    """

    wssql = 'SELECT count(*) FROM {} \n'.format('TCADMEDAGEN0')
    wssql = wssql + '{} {} = {}'.format('WHERE', 'id_med', odtoprm.dcids['id_med'])
    wssql = wssql + '{} {} = {}'.format('  AND', 'id_end', odtoprm.dcids['id_end'])

    oDb = Db(odtoprm.pathdb, wssql, '', '')
    oDb.db_conecta()
    rows = oDb.db_consulta()
    oDb.db_desconecta()

    if rows == 1:
        rows = ''
        #sg.popup_ok('Erro Agenda Já Cadastrado')   #teste

    return rows

#________________________________________________
# def pxmntagenda(dias):
#     dias = [']']

#     tabtf = [False, True]
#     wsql = ''
#     for col in range(0, len(dias)):
#        .
#         if col == len(dias) - 1:
#             wcpo = '{} = {}'.format(coluna, tabtf[int(dias[col])])
#         else:
#             wcpo = '{} = {}, '.format(coluna, tabtf[int(dias[col])])

#         wsql = wsql + wcpo

#     tam = len(wsql) - 2
#     print('wsql = {}'.format(wsql))
#     a=1


# try:
#     process_data()
# except Exception as exc:
#     raise DataProcessingFailedError(str(exc))
# try:
#     value = collection[key]
# except KeyError:
#     return key_not_found(key)
# else:
#     return handle_value(value)

# sg.popup('Attention!')
# sg.popup_ok('Default popup')
# sg.popup_yes_no('Popup with Yes and No buttons')
# sg.popup_cancel('Popup with cancel button')
# sg.popup_ok_cancel('Popup with OK and cancel buttons')
# sg.popup_error('popup with red error button')
# sg.popup_auto_close('Popup window that closes au
