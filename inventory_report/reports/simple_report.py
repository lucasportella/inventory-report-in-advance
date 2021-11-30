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
