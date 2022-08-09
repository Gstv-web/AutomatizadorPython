# buscar os relatórios pendentes de conversão (arquivo, webservice, ftp)
# identificar qual classe usar para ler o relatório
# converter o relatório no padrão iknow
import os.path
import pandas as pd
from report import Report
from iknow_converter import IknowConverter
from report_writer import ReportWriter


def find_next_pending_report():
    """
    Busca próximo relatório pendente
    :return: Report
    """
    sent_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Enviados", "enviados.csv")
    received_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Recebidos", "recebidos.csv")
    pending_report = Report(sent_file, received_file, Report.SUPPLIER_IKNOW)
    return pending_report


def update_report_file(pending_report: Report):
    writer = pd.ExcelWriter("./Saida/iKnow/Whatsapp/finalizado.xlsx")
    # writer = ReportWriter("Teste")
    
    if pending_report.supplier == Report.SUPPLIER_IKNOW:
        ic = IknowConverter(writer)
        ic.convert_report(pending_report)


def main():
    pending_report = find_next_pending_report()
    update_report_file(pending_report)


if __name__ == "__main__":
    main()
