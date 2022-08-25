# buscar os relatórios pendentes de conversão (arquivo, webservice, ftp)
# identificar qual classe usar para ler o relatório
# converter o relatório no padrão de cada plataforma
import os.path
from report import Report
from iknow_converter import IknowConverter
from alcance_converter import AlcanceConverter
from ligdata_converter import LigdataConverter
from bewake_converter import BewakeConverter
from atmosfera_converter import AtmosferaConverter
from iknow_rcs_converter import IknowRCSConverter
from report_writer import ReportWriter

def find_next_pending_report():
    """
    Busca próximo relatório pendente
    :return: Report
    Mudar função futuramente para buscar relatório pelo webservice, dependendo da plataforma
    """

    ### IKNOW ###
    # sent_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Enviados", "enviados.csv")
    # received_file = os.path.join("Entrada", "iKnow", "Whatsapp", "Recebidos", "recebidos.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_IKNOW)
    
    ### ALCANCE ###
    # sent_file = os.path.join("Entrada", "Alcance", "relatorio.csv")
    # received_file = os.path.join("Entrada", "Alcance", "relatorio.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_ALCANCE)

    ### LIGDATA ###
    # sent_file = os.path.join("Entrada", "Ligdata", "relatorio_envioDanielgeral1.xlsx")
    # received_file = os.path.join("Entrada", "Ligdata", "relatorio_envioDanielgeral1.xlsx")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_LIGDATA)

    ### BEWAKE ###
    # sent_file = os.path.join("Entrada", "Bewake", "16.08 - Jeep.csv")
    # received_file = os.path.join("Entrada", "Bewake", "16.08 - Jeep.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_BEWAKE)
    
    ### ATMOSFERA ###
    # sent_file = os.path.join("Entrada", "Atmosfera", "Enviados", "Relatório Daniel - Centro  29_07.xlsx")
    # received_file = os.path.join("Entrada", "Atmosfera", "Recebidos", "Respostas Daniel - Centro 29_07.xlsx")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_ATMOSFERA)
    
    ### IKNOW RCS ###
    sent_file = os.path.join("Entrada", "iKnow", "RCS", "Enviados", "relatorio_mensagens_enviadas.csv")
    received_file = os.path.join("Entrada", "iKnow", "RCS", "Recebidos", "relatorio_mensagens_recebidas.csv")
    interaction_file = os.path.join("Entrada", "iKnow", "RCS", "Interacoes", "relatorio_iteracoes.csv")
    pending_report = Report(sent_file, received_file, interaction_file, Report.SUPPLIER_IKNOW)

    return pending_report


def update_report_file(pending_report: Report):
    # writer = ReportWriter("./Saida/iKnow/Whatsapp/finalizado.xlsx") # iKnow
    # writer = ReportWriter("./Saida/Alcance/finalizado.xlsx") # Alcance
    # writer = ReportWriter("./Saida/Ligdata/finalizado.xlsx") # Ligdata
    # writer = ReportWriter("./Saida/Bewake/finalizado.xlsx") # Bewake
    # writer = ReportWriter("./Saida/Atmosfera/finalizado.xlsx") # Atmosfera
    writer = ReportWriter("./Saida/iKnow/RCS/finalizado.xlsx") # iKnow RCS
    
    if pending_report.supplier == Report.SUPPLIER_IKNOW:
        # ic = IknowConverter(writer)
        # ic.convert_report(pending_report)

        # ac = AlcanceConverter(writer)
        # ac.convert_report(pending_report)

        # lc = LigdataConverter(writer)
        # lc.convert_report(pending_report)

        # bc = BewakeConverter(writer)
        # bc.convert_report(pending_report)

        # atc = AtmosferaConverter(writer)
        # atc.convert_report(pending_report)

        irc = IknowRCSConverter(writer)
        irc.convert_report(pending_report)


def main():
    pending_report = find_next_pending_report()
    update_report_file(pending_report)


if __name__ == "__main__":
    main()
