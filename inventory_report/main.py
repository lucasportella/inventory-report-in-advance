import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    parsers = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }

    path = sys.argv[1]
    report_type = sys.argv[2]
    file_extension = path.split(".")[-1]
    importer = InventoryRefactor(parsers[file_extension])
    print(importer.import_data(path, report_type), end='')
