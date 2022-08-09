from report_converter import ReportConverterInterface
from report import Report
import pandas as pd

class IknowConverter(ReportConverterInterface):


    def convert_report(self, report: Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.save()

    def cast_sent_report(self, sent_file_name):
        sent_file = pd.read_csv(sent_file_name, sep=';')
        sent_file.rename(columns={'Número': 'NÚMERO', 'data de envio': 'DATA', 'status': 'STATUS'}, inplace=True)
        sent_file = sent_file[['NÚMERO', 'STATUS', 'DATA']]
        numero = str(sent_file['NÚMERO'])
        status = str(sent_file['STATUS'])
        data = str(sent_file['DATA'])
        self.writer.write_sent_message(numero, status, data)




    def cast_received_report(self, received_file_name):
        received_file = pd.read_csv(received_file_name, sep=';', names=['TELEFONE', 'MENSAGEM'])
        numero = str(received_file['TELEFONE'])
        mensagem = str(received_file['MENSAGEM'])
        self.writer.write_received_message(numero, mensagem)



