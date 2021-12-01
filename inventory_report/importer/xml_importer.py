from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split(".")[-1]
        if file_extension != "xml":
            raise ValueError("Arquivo inválido")
        else:
            with open(path, "r", encoding="utf-8") as file:
                my_xml = file.read()
                data = xmltodict.parse(my_xml)
                data = [dict(entry) for entry in data["dataset"]["record"]]
                return data