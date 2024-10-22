import PySimpleGUI as sg

class Cadtabelas():

    """[recebe a Tabela cadastral]
    """

    def __init__(self, de_tab, nnm_tab):

        """[summary]
        """        


        """[Inicializa a tabela com o nome recebido]
        
        ARGS: 
        """        
        self.de_tab = de_tab
        self.nnm_tab = nnm_tab
    
    #____________________________________________
    def pxmain():
        wlay = wlayout()
        
    def wlayout():

        left_col = [[sg.Frame('Médico', [[sg.Text('Médico:'), sg.Input(size=(20, 1),
            key='-INMED-'), sg.Button('Pesq.', key='-PSQ-')],
            [sg.Listbox(values= , size=(34, 20), key='-LIST-', enable_events=True)]])]]

    #--- Nome ---
        layout_1 = [[sg.Text(sel.de_tab + 'Nome.......:', size=(10, 0)),
          sg.Input(size=(50, 0), key='nome'),
          sg.Input(size=(5, 0), background_color='white', text_color='blue',
          disabled=True, key='opmed', justification='center')],
        [sg.Text('CRM........:', size=(10, 0)),
          sg.Input(size=(10, 0), key='crm')],
        [sg.Button('Salvar', key='salvar'),
         sg.Button('Excluir', key='profexc', disabled=True),
         sg.Button('Limpar', key='limpar'),
         sg.Button('Voltar', key='profvoltar')]]


        #--- Layout --- 
        layout = [  
                [sg.Frame(layout=[
                [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)]],
                    title = ' Medico ', relief=sg.RELIEF_SUNKEN, tooltip='Nome do Medico', title_color='blue')]
        ]
        #

        self.windows = sg.Window("Cadastro de Medicos").layout(layout)
        a = 2

    def pxtelamain(self):

        #--- Display and interact with the Window using an Event Loop
        while True:         
            #--- Extrair os Dados da Janela ---
            self.event, self.values = self.janela.read()            

            #--- See if user wants to quit or janela was closed
            if  self.event in (sg.WIN_CLOSED, 'Encerrar'):    
                break
            
            # elif self.event == 'Limpar': 
            #     pxlimpar(self)
            
            # elif self.event == 'Pesq. Cep':
            #     # pxpesqcep(self)

            # elif self.event == 'Enviar':
            #     if pxcritica(self) == True:
            #         pxcincluir(self)

        # Finish up by removing from the screen
        self.janela.close()
    
otela = Cadtabelas()
retor = otela.pxtelamain()

        pass