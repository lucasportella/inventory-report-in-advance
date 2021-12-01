from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split('.')[-1]
        if file_extension != 'json':
            raise ValueError('Arquivo inválido')
        else:
            with open(path) as file:
                return json.load(file)
