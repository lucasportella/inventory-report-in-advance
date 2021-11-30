import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = []
            for row in reader:
                data.append(row)
            print(data)
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)


print(Inventory.import_data("inventory_report/data/inventory.csv", "completo"))
