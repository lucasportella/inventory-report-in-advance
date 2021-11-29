from datetime import datetime


class SimpleReport:
    current_date = datetime.now()

    def __init__(self, data):
        self.data = data
        self.oldest_manuf_date = data[0]["data_de_fabricacao"]
        self.closest_exp_date = data[0]["data_de_validade"]
        self.biggest_stock = data[0]["nome_da_empresa"]

    @classmethod
    def get_oldest_manuf_date(cls, data):
        manuf_dates = [
            date["data_de_fabricacao"]
            for date in data
            ]
        manuf_dates.sort()
        return manuf_dates[0]

    @classmethod
    def get_closest_exp_date(cls, data):
        exp_dates = [
            date["data_de_validade"]
            for date in data
            if datetime.strptime(date["data_de_validade"], '%Y-%m-%d') > cls.current_date]
        exp_dates.sort()
        return exp_dates[0]

    def generate(cls, data):
        return f'''
{cls.get_oldest_manuf_date(data)}
{cls.get_closest_exp_date(data)}
        '''

test_data = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]

my_report = SimpleReport(test_data)
print(my_report.generate(test_data))
