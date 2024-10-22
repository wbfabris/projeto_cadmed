
import viacep

d = viacep.ViaCEP('78048000')

data = d.getDadosCEP()

data

#{'cep': '78048-000', 'logradouro': 'Avenida Miguel Sutil', 'complemento': 'de 5686 a 6588 - lado par', 
# 'bairro': 'Alvorada', 'localidade': 'Cuiabá', 'uf': 'MT', 'unidade': '', 'ibge': '5103403', 'gia': ''}

