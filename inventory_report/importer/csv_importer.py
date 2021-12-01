from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split(".")[-1]
        if file_extension != "csv":
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
                data = []
                for row in reader:
                    data.append(row)
                return data
