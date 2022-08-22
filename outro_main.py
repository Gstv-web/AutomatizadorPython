# buscar os relatórios pendentes de conversão (arquivo, webservice, ftp)
# identificar qual classe usar para ler o relatório
# converter o relatório no padrão iknow
import os.path
import pandas as pd
from report import Report
from iknow_converter import IknowConverter
from alcance_converter import AlcanceConverter
from ligdata_converter import LigdataConverter
from bewake_converter import BewakeConverter
from report_writer import ReportWriter


def find_next_pending_report():
    """
    Busca próximo relatório pendente
    :return: Report
    Mudar função futuramente para buscar relatório pelo webservice, dependendo da plataforma
    """
    # sent_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Enviados", "enviados.csv")
    # received_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Recebidos", "recebidos.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_IKNOW)
    
    # sent_file = os.path.join("Entrada", "Alcance", "relatorio.csv")
    # received_file = os.path.join("Entrada", "Alcance", "relatorio.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_LIGDATA)
    
    sent_file = os.path.join("Entrada", "Bewake", "16.08 - Jeep.csv")
    received_file = os.path.join("Entrada", "Bewake", "16.08 - Jeep.csv")
    pending_report = Report(sent_file, received_file, Report.SUPPLIER_BEWAKE)
    return pending_report


def update_report_file(pending_report: Report):
    # writer = ReportWriter("./Saida/iKnow/Whatsapp/finalizado.xlsx") # iKnow
    # writer = ReportWriter("./Saida/Alcance/finalizado.xlsx") # Alcance
    # writer = ReportWriter("./Saida/Ligdata/finalizado.xlsx") # Ligdata
    writer = ReportWriter("./Saida/Bewake/finalizado.xlsx") # Bewake
    
    if pending_report.supplier == Report.SUPPLIER_BEWAKE:
        # ic = IknowConverter(writer)
        # ic.convert_report(pending_report)

        # ac = AlcanceConverter(writer)
        # ac.convert_report(pending_report)

        # lc = LigdataConverter(writer)
        # lc.convert_report(pending_report)

        bc = BewakeConverter(writer)
        bc.convert_report(pending_report)

def main():
    pending_report = find_next_pending_report()
    update_report_file(pending_report)


if __name__ == "__main__":
    main()
