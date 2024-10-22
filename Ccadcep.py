# Class:     Cmedcep
# Obejtivo:  Acessa os correios e pega o cep
# Data:      Junho/2021
# Input:     Passa o cep
# Process:   Gera uma lista com enderço, Bairro, cidade, UF
# OutPut:    Retorna a lista
# ================================================================

import requests


class Obterend:
    """[recebe o cep e retorna o endereço]"""

    def __init__(self, pcep):
        """__init__ [Recebe o str com 8 digitos]
        Args:
            pcep ([str]): [numero do cep]
        """
        self.pcep = pcep

    # _________________________________________
    def pxobterend(self):
        """pxobterend [recebe o self.pcep e retorna um dicionario]
        Returns:
            [dict]: {"cep": "01001-000", "logradouro": "Praça da Sé",  "complemento": "lado ímpar",
        "unidade": "", "bairro": "Sé", "localidade": "São Paulo", "uf": "SP", "estado": "São Paulo",
        "regiao": "Sudeste", "ibge": "3550308", "gia": "1004", "ddd": "11", "siafi": "7107"}
        """

        dict_requisicao = {}

        if len(self.pcep) == 8:
            link = f"https://viacep.com.br/ws/{self.pcep}/json/"
            requisicao = requests.get(link)
            print(requisicao)

            if str(requisicao) == "<Response [200]>":
                if str(requisicao.json()) == str("{'erro': 'true'}"):
                    dict_requisicao = pxcriaarqjson(
                        self.pcep, "Não há dados a serem exibidos"
                    )

                else:
                    dict_requisicao = requisicao.json()

            else:
                print("Cep Invalido, {self.pcep}")
                dict_requisicao = pxcriaarqjson(self.pcep, "CEP invalido")

        else:
            print(f"Tamanho do Cep Inválido, {len(self.pcep)}")
            dict_requisicao = pxcriaarqjson(
                self.pcep, "Tamanho do Cep Inválido"
            )

        return dict(dict_requisicao)


def pxcriaarqjson(cep, ptexto):

    # Dicionário de dados com logradouro contendo "erro1"
    dados = {
        "cep": cep,
        "logradouro": ptexto,
        "complemento": "",
        "bairro": "",
        "localidade": "",
        "uf": "",
        "ibge": "",
        "gia": "",
        "ddd": "",
        "siafi": "",
    }

    # # Salvando o dicionário em um arquivo JSON
    # with open("endereco_com_erro.json", "w", encoding="utf-8") as arquivo_json:
    #     json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
    # print("Arquivo JSON criado com sucesso!")

    return dados


# ++++++++++++++++++++++++++++++++++++++++++

# lscep = [
#     "59020-310",
#     "59020310",
#     "37503130",
#     "20270005",
#     "20270000",
#     "28625000",
# ]

# for i in range(0, len(lscep)):

#     ocep = Obterend(lscep[i])
#     lsend = ocep.pxobterend()

#     print(
#         lsend["cep"],
#         lsend["logradouro"],
#         lsend["bairro"],
#         lsend["localidade"],
#         lsend["uf"],
#     )
