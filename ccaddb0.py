"""[CCADDB0]"""
import ctypes
import sqlite3
from sqlite3 import Error

class Db:

    """[Classe que representa o banco de dados (database) da aplicação]
    """

    #_____________________________________________________________________
    def __init__(self, db_nome, db_sql, db_tabela, db_value):

        #___ Inicializa o banco de dados ___
        self.db_nome = db_nome      # Nome do Banco
        self.db_sql = db_sql        # Sql
        self.db_tabela = db_tabela  # Lista de reg a ser processado
        self.db_value = db_value    # qtde de campos (?,?,?)

    #_____________________________________________________________________
    def db_conecta(self):

        """[Conecta passando o nome do arquivo]
        """
        wmsg = ''

        try:
            self.conn = sqlite3.connect(self.db_nome)

        except Error as err:
            wmsg = 'Na coneção com Banco {} Erro {}'.format(self.db_nome, err)
            mbox('ERRO',wmsg, 1)

    #_____________________________________________________________________
    def db_cursor(self):

        """[Conecta recebendo o nome do arquivo]
        """
        cursor = []

        try:
            self.conn = sqlite3.connect(self.db_nome)
            cursor    = self.conn.cursor()
            return cursor

        except Error as err:
            wmsg = 'ERRO - Não criou o Cursor - conn {}Erro {}'.format(self.conn, err)
            mbox('ERRO',wmsg, 1)

    #_____________________________________________________________________
    def db_executa(self):

        """[summary]

        Returns:
            [type]: [Executa uma operação]
        """

        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(self.db_sql)
                self.conn.commit()
                return None

            except sqlite3.IntegrityError:
                wmsg = 'Registro já Cadastrado'
                mbox('AVISO',wmsg, 1)
                return 'Aviso'

            except sqlite3.OperationalError:
                wmsg = 'Nome de campo inválido (OperationalError)'
                mbox('ERRO', wmsg, 1)
                return 'Erro'

        except Error as err:
            wmsg ='Faça a conexão do banco antes executar uma ação. Erro {}'.format(err)
            mbox('ERRO', wmsg, 1)
            return 'Erro'

    #____________________________________________________________________
    def db_executa_muitos(self):


        """[Executa muitas operações]

        Returns:
            [str]: [None ou 'Erro']
        """
        wmsg = ''

        cursor = self.conn.cursor()

        try:

            records = cursor.execute(self.db_sql)
            records = list(records)
            cursor.executemany('INSERT INTO ' + self.db_tabela + \
                ' VALUES(' + self.db_value + ');', records)
            print('Foram inseridos', cursor.rowcount, 'registros na tabela:' +  \
                self.db_tabela)
            self.conn.commit()
            return None

        except sqlite3.IntegrityError:
            wmsg = 'Registro já Cadastrado {}'.format(self.db_sql)
            mbox('AVISO', wmsg, 1)
            return 'Erro'

        except sqlite3.OperationalError:
            wmsg = 'Nome de campo inválido (OperationalError)'
            mbox('ERRO', wmsg, 1)
            return 'Erro'

    #_____________________________________________________________________
    def db_consulta(self):

        """[Fa uma consulta e retorna o registros existente]

        Returns:
            [Tupla]: [Registros existentes]
        """

        try:
            cursor = self.conn.cursor()
            cursor.execute(self.db_sql)
			# o fetchall retorna o resultado do select
			# o retorno é uma lista
            rows = cursor.fetchall()
            return rows #cursor.fetchall())

        except AttributeError:
            wmsg = 'Sem coneção com banco'
            mbox('ERRO', wmsg, 1)
            return 'Erro'

    #_____________________________________________________________________
    def db_consultaum(self):

        """[ler uma tabela passada de um DB]

        Returns:
            [type]: [Consulta uma tabela e retorna o registros lidos]
        """

		#___ ler uma tabela passada de um DB ___

        try:
            cursor = self.conn.cursor()
            cursor.execute(self.db_sql)
			# o fetchall retorna o resultado do select
			# o retorno é uma lista
            rows = cursor.fetchone()
            if rows is None:
                row = 0
            else:
                row = int(rows[0]) #alterado 21/06/21

            return row   #cursor.fetchall())

        except AttributeError:
            wmsg = 'ERRO - Sem coneção com banco'
            mbox('ERRO', wmsg, 1)
            return 'Erro'

    #_____________________________________________________________________
    def db_executatrans(self):


        """[Executa uma operação numa Transação]

        Returns:
            [type]: [Executa uma operação, numa Transação]
        """
        wmsg = ''

        print('db_executatrans')

        #___Executa uma operação ___
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(self.db_sql)
                return None

            except sqlite3.IntegrityError:
                wmsg = 'ERRO - LOCAL já Cadastrado {} '.format(self.db_sql)
                mbox('ERRO', wmsg, 1)
                return 'ERRO'

            except sqlite3.OperationalError:
                wmsg = 'Erro {} (OperationalError)'.format(self.db_sql)
                mbox('ERRO', wmsg, 1)
                return 'ERRO'

        except AttributeError:
            wmsg = 'Faça a conexão do banco antes executar uma ação'
            mbox('ERRO', wmsg, 1)
            return 'ERRO'

    #_____________________________________________________________________
    def db_begin(self):

        """[summary]
        """

        cursor = self.conn.cursor()
        cursor.execute('begin')

    #_____________________________________________________________________
    def db_isolation(self):

        """[summary]
        """

        self.conn.isolation_level = None

    #_____________________________________________________________________
    def db_comitt(self):

        """[summary]
        """
        self.conn.commit()

    #_____________________________________________________________________
    def db_rollback(self):

        """[summary]
        """

        self.conn.rollback()

    #_____________________________________________________________________
    def db_desconecta(self):

        """[Desconecta do banco]
        """

        try:

            self.conn.close()

        except AttributeError:
            print('ERRO no close')

#_________________________________________________________________
def mbox(title, text, style):

    """[Desconecta do banco]
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

#__________________________________________________________________________
def values_in_col(cursor, table_name, print_out=True):

    """ Returns a dictionary with columns as keys
    and the number of not-null entries as associated values.
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()

    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0

    for col in col_dict:
        cursor.execute('SELECT ({0}) FROM {1} '
                  'WHERE {0} IS  NULL'.format(col, table_name))
        # In my case this approach resulted in a
        # better performance than using COUNT
        number_rows = len(cursor.fetchall())
        col_dict[col] = number_rows

    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))

    return col_dict
#__________________________________________________________________________
def listanomes():

    """[Desconecta do banco]
    """

    lista = ['carla', 'regina', 'suelen', 'veronica', 'cristiane']
    print('Nomes que constam na lista')

    for nome in lista:
        print('   Nome: {}'.format(nome))

#__________________________________________________________________________
# from   CPLOTDB0 import Db
# import PLOPRM00  as rp
# dcvalues = {}
# wserro = ""
