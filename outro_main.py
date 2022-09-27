# buscar os relatórios pendentes de conversão (arquivo, webservice, ftp)
# identificar qual classe usar para ler o relatório
# converter o relatório no padrão de cada plataforma
import os.path
from report import Report
from rcs_report import RCSReport
from ura_report import URAReport
from sms_report import SMSReport
from iknow_converter import IknowConverter
from iknow_rcs_converter import IknowRCSConverter
from alcance_converter import AlcanceConverter
from ligdata_converter import LigdataConverter
from bewake_converter import BewakeConverter
from atmosfera_converter import AtmosferaConverter
from N8_converter import N8Converter
from talkip_converter import TalkipConverter
from talk_ura_converter import TalkConverter
from report_writer import ReportWriter
from bewake_sms_converter import BewakeSMSConverter
from talk_sms_converter import TalkSMSConverter

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
    # sent_file = os.path.join("Entrada", "Bewake", "Whatsapp" "16.08 - Jeep.csv")
    # received_file = os.path.join("Entrada", "Bewake", "Whatsapp", "16.08 - Jeep.csv")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_BEWAKE)
    
    ### ATMOSFERA ###
    # sent_file = os.path.join("Entrada", "Atmosfera", "Enviados", "Relatório Daniel - Centro  29_07.xlsx")
    # received_file = os.path.join("Entrada", "Atmosfera", "Recebidos", "Respostas Daniel - Centro 29_07.xlsx")
    # pending_report = Report(sent_file, received_file, Report.SUPPLIER_ATMOSFERA)
    
    ### IKNOW RCS ###
    # sent_file = os.path.join("Entrada", "iKnow", "RCS", "Enviados", "relatorio_mensagens_enviadas.csv")
    # received_file = os.path.join("Entrada", "iKnow", "RCS", "Recebidos", "relatorio_mensagens_recebidas.csv")
    # interaction_file = os.path.join("Entrada", "iKnow", "RCS", "Interacoes", "relatorio_iteracoes.csv")
    # pending_report = RCSReport(sent_file, received_file, interaction_file, RCSReport.SUPPLIER_IKNOW)

    ### N8 (URA) ###
    # activation_file = os.path.join("Entrada", "N8", "URA_ANGRA_TF.csv")
    # call_interaction_file = os.path.join("Entrada", "N8", "URA_ANGRA_TF.csv")
    # pending_report = URAReport(activation_file, call_interaction_file, URAReport.SUPPLIER_N8)

    ### Talkip (URA) ###
    # activation_file = os.path.join("Entrada", "Talkip", "discagem", "relatorio_discagem_Trilha 2-Base Nicolau-Filtered2-20k-22-08-2022.csv")
    # call_interaction_file = os.path.join("Entrada", "Talkip", "Interacao", "relatorio_interacao_Trilha2-Base Nicolau-Filtered2-20k-22-08-2022.csv")
    # pending_report = URAReport(activation_file, call_interaction_file, URAReport.SUPPLIER_TALKIP)

    ### Talk (URA) ###
    # activation_file = os.path.join("Entrada", "Talk", "URA", "Talk - URA.xls")
    # call_interaction_file = os.path.join("Entrada", "Talk", "URA", "Talk - URA.xls")
    # pending_report = URAReport(activation_file, call_interaction_file, URAReport.SUPPLIER_TALK)

    ### Bewake (SMS) ###
    # sent_file = os.path.join("Entrada", "Bewake", "SMS", "SMS - Bewake.csv")
    # received_file = os.path.join("Entrada", "Bewake", "SMS", "SMS - Bewake.csv")
    # pending_report = SMSReport(sent_file, received_file, SMSReport.SUPPLIER_BEWAKE)

    ### Talk (SMS) ###
    sent_file = os.path.join("Entrada", "Talk", "SMS", "Enviados", "1955_Relatorio_Detalhado_19-09-2022_a_27-09-2022.csv")
    received_file = os.path.join("Entrada", "Talk", "SMS", "Recebidos", "Relatorio_Resposta_19_09_2022_a_27_09_2022.xls")
    pending_report = SMSReport(sent_file, received_file, SMSReport.SUPPLIER_TALK)

    return pending_report


def update_report_file(pending_report: SMSReport):
    # writer = ReportWriter("./Saida/iKnow/Whatsapp/finalizado.xlsx") # iKnow
    # writer = ReportWriter("./Saida/Alcance/finalizado.xlsx") # Alcance
    # writer = ReportWriter("./Saida/Ligdata/finalizado.xlsx") # Ligdata
    # writer = ReportWriter("./Saida/Bewake/Whatsapp/finalizado.xlsx") # Bewake
    # writer = ReportWriter("./Saida/Atmosfera/finalizado.xlsx") # Atmosfera
    # writer = ReportWriter("./Saida/iKnow/RCS/finalizado.xlsx") # iKnow RCS
    # writer = ReportWriter("./Saida/N8/finalizado.xlsx") # N8 (URA)
    # writer = ReportWriter("./Saida/Talkip/finalizado.xlsx") # Talkip (URA)
    # writer = ReportWriter("./Saida/Talk/URA/finalizado.xlsx") # Talk (URA)
    # writer = ReportWriter("./Saida/Bewake/SMS/finalizado.xlsx") # Bewake (SMS)
    writer = ReportWriter("./Saida/Talk/SMS/finalizado.xlsx") # Talk (SMS)

    if pending_report.supplier == SMSReport.SUPPLIER_TALK:
        # ic.convert_report(pending_report)
        # ic.convert_wpp_report(pending_report)

        # ac = AlcanceConverter(writer)
        # ac.convert_wpp_report(pending_report)

        # lc = LigdataConverter(writer)
        # lc.convert_report(pending_report)

        # bc = BewakeConverter(writer)
        # bc.convert_report(pending_report)

        # atc = AtmosferaConverter(writer)
        # atc.convert_report(pending_report)

        # irc = IknowRCSConverter(writer)
        # irc.convert_rcs_report(pending_report)
        
        # n8 = N8Converter(writer)
        # n8.convert_ura_report(pending_report)

        # tkp = TalkipConverter(writer)
        # tkp.convert_ura_report(pending_report)

        # tk = TalkConverter(writer)
        # tk.convert_ura_report(pending_report)

        # bsms = BewakeSMSConverter(writer)
        # bsms.convert_sms_report(pending_report)

        tksms = TalkSMSConverter(writer)
        tksms.convert_sms_report(pending_report)

def main():
    pending_report = find_next_pending_report()
    update_report_file(pending_report)


if __name__ == "__main__":
    main()
