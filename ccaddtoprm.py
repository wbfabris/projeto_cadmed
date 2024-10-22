""" Dtoprm [DTO de Parametros]
Returns:
    [list]: [DTO parametros usados para gravar registro]
"""

# Coding: utf-8
# from PySimpleGUI.PySimpleGUI import SELECT_MODE_BROWSE, set_global_icon


class Dtoprm:
    """[Classe de parametros das telas]"""

    def __init__(
        self,
        patharq=[],
        pathdb=[],
        layout="",
        window="",
        event=[],
        values=[],
        data=[],
        datafrmt=[],
        datasel=[],
        row=0,
        local=[],
        conv=[],
        vemcons=False,
        dctab={
            "-prof-": "INC",
            "-ende-": "INC",
            "-agen-": "INC",
            "-cont-": "INC",
        },
        dcloc={"local": 0},
        dccnv={"conve": 0},
        dcuscnv={},
        dcusloc={},
        dcids={
            "id_med": 0,
            "id_local": 0,
            "id_end": 0,
            "id_age": 0,
            "id_cont": 0,
            "id_conv": 0,
        },
        idpsq="",
        wctralt=True,
        opcmenu="",
        inmed="-INMED-",
        psq="-PSQ-",
        lst="-LIST-",
        campo="",
    ):

        # _______________________________________________________________________________
        # --- Path, DB ---
        self.patharq = patharq
        self.pathdb = pathdb
        # ______________________________________________________________________________
        # --- Controle ---
        self.window = window
        self.event = event
        self.values = values
        self.layout = layout
        self.data = data  # reg. selecionados
        self.datafrmt = (
            datafrmt  # reg. formatados para a consluta dos selecionados
        )
        self.datasel = datasel  # reg. selecionado dos selecionados
        self.row = row  # número da linha selecionada
        self.local = local
        self.conv = conv
        self.vemcons = vemcons
        self.layout = layout
        self.dctab = dctab
        self.dcloc = dcloc
        self.dccnv = dccnv
        self.dcusloc = dcusloc
        self.dcuscnv = dcuscnv
        self.dcids = dcids
        self.idpsq = idpsq
        self.wctralt = wctralt
        self.opcmenu = opcmenu
        self.campo = campo

    # ______________________________________________________________________________
    # --- Profissional ---
    def limpa_prof(self):
        """[limpa tela da Profissional]"""

        self.window["nome"].update("")
        self.window["crm"].update("")
        self.dctab["-prof-"] = "INC"
        self.window["profexc"].update(visible=False)
        self.window["opmed"].update(self.dctab["-prof-"])
        self.window.Refresh()

    # _____________________________________________________________________________
    # --- Endereço ---
    def limpa_endereco(self):
        """[limpa tela da Endereço]"""
        self.window["-local-"].update("")
        self.window["cep"].update("")
        self.window["ende"].update("")
        self.window["nume"].update("")
        self.window["comp"].update("")
        self.window["cida"].update("")
        self.window["bair"].update("")
        self.window["esta"].update("")
        self.window["tel1"].update("")
        self.window["tel2"].update("")
        self.window["tel3"].update("")
        self.window["obse"].update("")
        self.dctab["-ende-"] = "INC"
        self.window["opend"].update(self.dctab["-ende-"])
        self.window.Refresh()

    # ______________________________________________________________________________
    # --- Agenda ---
    def limpa_agenda(self):
        """[limpa tela da agenda]"""
        for col in range(0, 15):
            wcpo = "{}{}".format("cb", col)
            self.window[wcpo].update("")

        self.dctab["-agen-"] = "INC"
        self.window["opage"].update(self.dctab["-agen-"])
        self.window.Refresh()

    # ______________________________________________________________________________
    # --- Contato ---
    def limpa_contato(self):
        """[Limpa a tela de contato]"""
        self.window["emai1"].update("")
        self.window["emai2"].update("")
        self.window["-conv-"].update("")
        self.window["cel1"].update("")
        self.window["cel2"].update("")
        self.window["cel3"].update("")
        self.window["obs"].update("")
        self.dctab["-cont-"] = "INC"
        self.window["opcon"].update(self.dctab["-cont-"])
        self.window.Refresh()

    # ______________________________________________________________________________
    def pxobterids(self):
        """[obter o id solicitado]"""
        lsaux = []
        ret = []

        if self.idpsq == "id_med":
            ret = list(lsaux[self.dcids["id_imed"]])

        elif self.idpsq == "id_local":
            ret = list(lsaux[self.dcids["id_local"]])

        elif self.idpsq == "id_end":
            ret = list(lsaux[self.dcids["id_end"]])

        elif self.idpsq == "id_age":
            ret = list(lsaux[self.dcids["id_age"]])

        elif self.idpsq == "id_cont":
            ret = list(lsaux[self.dcids["id_cont"]])

        elif self.idpsq == "id_conv":
            ret = list(lsaux[self.dcids["id_conv"]])

        elif self.idpsq == "medloc":
            idmed = self.dcids["id_imed"]
            idcto = self.dcids["id_local"]
            lsaux.append(idmed)
            lsaux.append(idcto)
            ret = list(lsaux)

        elif self.idpsq == "medcnv":
            idmed = self.dcids["id_imed"]
            idcto = self.dcids["id_conv"]
            lsaux.append(idmed)
            lsaux.append(idcto)
            ret = list(lsaux)

        return ret


# ______________________________________________________________________________
# odtoprm = Dtoprm()
# odtoprm.limpa_prof()
# odtoprm.limpa_endereco()
# odtoprm.limpa_agenda()
# odtoprm.limpa_contato()
# q=12
