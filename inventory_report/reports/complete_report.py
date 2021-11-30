from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
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
    def get_products_quantity(cls, data):
        companies_products = cls.generate_products_object(data)
        for product in data:
            companies_products[product["nome_da_empresa"]] += 1
        result = "Produtos estocados por empresa: \n"
        # objetos em python aceitam iteração, chave é o product, valor é o
        # companies_products[product]
        for product in companies_products:
            result += f"- {product}: {companies_products[product]}\n"
        return result

    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)
        products_quantity = cls.get_products_quantity(data)
        complete_report = f"{simple_report}\n{products_quantity}"
        return complete_report
