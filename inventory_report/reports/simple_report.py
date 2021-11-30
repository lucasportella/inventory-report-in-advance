from datetime import datetime


class SimpleReport:
    current_date = datetime.now()

    @classmethod
    def generate_products_object(cls, data):
        # usar sort pq por algum motivo o primeiro for não começa
        #  o loop pela ordem dos objetos
        data.sort(key=lambda a: a["id"])
        companies = []
        for company in data:
            if company["nome_da_empresa"] not in companies:
                companies.append(company["nome_da_empresa"])
        companies_products = {}
        for company in companies:
            companies_products[company] = 0
        return companies_products

    @classmethod
    def get_oldest_manuf_date(cls, data):
        manuf_dates = [date["data_de_fabricacao"] for date in data]
        manuf_dates.sort()
        return manuf_dates[0]

    @classmethod
    def get_closest_exp_date(cls, data):
        exp_dates = [
            date["data_de_validade"]
            for date in data
            if datetime.strptime(date["data_de_validade"], "%Y-%m-%d")
            > cls.current_date
        ]
        exp_dates.sort()
        return exp_dates[0]

    @classmethod
    def get_biggest_stock_company(cls, data):
        companies_products = cls.generate_products_object(data)
        for product in data:
            companies_products[product["nome_da_empresa"]] += 1
        sorted_companies = sorted(
            companies_products.items(), key=lambda a: a[1], reverse=True
        )
        return sorted_companies[0][0]

        # stock age
        # for stock in data:
        #     stock_age = datetime.strptime(
        #         stock["data_de_validade"], "%Y-%m-%d"
        #     ) - datetime.strptime(stock["data_de_fabricacao"], "%Y-%m-%d")
        #     stock["stock_age"] = stock_age.days
        # data.sort(key=lambda a: a["stock_age"], reverse=True)
        # return data[0]["nome_da_empresa"]

    @classmethod
    def generate(cls, data):
        # avaliation return
        date1 = "Data de fabricação mais antiga: "
        date2 = "Data de validade mais próxima: "
        fab_date = f"{date1}{cls.get_oldest_manuf_date(data)}\n"
        val_date = f"{date2}{cls.get_closest_exp_date(data)}\n"
        company = "Empresa com maior quantidade de produtos "
        stock = f"estocados: {cls.get_biggest_stock_company(data)}\n"
        return f"{fab_date}{val_date}{company}{stock}"


# real aesthetic return
#         return f"""
# Data de fabricação mais antiga: {cls.get_oldest_manuf_date(data)}
# Data de validade mais próxima: {cls.get_closest_exp_date(data)}
# Empresa com maior quantidade de
# produtos estocados: {cls.get_biggest_stock_company(data)}
# """

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

print(SimpleReport.generate(test_data))