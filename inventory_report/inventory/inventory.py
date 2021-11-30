import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        file_format = path.split(".")[-1]
        parsers = {
            "csv": cls.csv_parser,
            "json": cls.json_parser,
            "xml": cls.xml_parser,
        }

        data = parsers[file_format](path)

        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def csv_parser(cls, path):
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = []
            for row in reader:
                data.append(row)
        return data

    @classmethod
    def json_parser(cls, path):
        with open(path) as file:
            data = json.load(file)
        return data

    @classmethod
    def xml_parser(cls, path):
        with open(path, "r", encoding="utf-8") as file:
            my_xml = file.read()
            data = xmltodict.parse(my_xml)
            data = [dict(entry) for entry in data["dataset"]["record"]]
            # tag root dataset, tags filhas record, xml parse retorna uma
            # serie de dicionarios ordenados, list comprehension para percorrer
            #  sobre os dicionarios pega só as tags dentro da tag record e joga
            #  dentro de uma classe dict, no fim temos uma lista de dicionarios
            #  tradicional
            return data
