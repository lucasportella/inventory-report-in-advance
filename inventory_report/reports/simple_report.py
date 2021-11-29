from datetime import datetime


class SimpleReport:
    def __init__(self, data):
        self.data = data
        self.oldest_manuf_date = data[0]["data_de_fabricacao"]
        self.closest_exp_date = data[0]["data_de_validade"]
        self.biggest_stock = data[0]["nome_da_empresa"]

    def generate(self):
        return f'''
Data de fabricação mais antiga:{self.oldest_manuf_date}
Data de validade mais próxima:{self.closest_exp_date}
Empresa com maior quantidade de produtos estocados:{self.biggest_stock}
        '''

test_data = [
  {
    id: 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]

my_report = SimpleReport(test_data)
print(my_report.generate())
