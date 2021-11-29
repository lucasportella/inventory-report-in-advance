from datetime import datetime


class SimpleReport:
    current_date = datetime.now()

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
        for stock in data:
            stock_age = datetime.strptime(
                stock["data_de_validade"], "%Y-%m-%d"
            ) - datetime.strptime(stock["data_de_fabricacao"], "%Y-%m-%d")
            stock["stock_age"] = stock_age.days
        data.sort(key=lambda a: a["stock_age"], reverse=True)
        return data[0]["nome_da_empresa"]

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
