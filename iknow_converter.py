from report_converter import ReportConverterInterface
from report import Report
from rcs_report import RCSReport
import csv

class IknowConverter(ReportConverterInterface):

    def convert_wpp_report(self, report: Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.set_styles()
        # self.writer.remove_55_from_numbers()
        # self.writer.edit_date()
        # self.writer.edit_status()
        # self.writer.remove_duplicates()
        self.writer.remove_blacklist_numbers()
        self.writer.remove_blank_messages()
        self.writer.save()

    # def convert_rcs_report(self, report: RCSReport):
    #     self.cast_sent_report(report.sent_file)
    #     self.cast_rcs_received_report(report.received_file)
    #     self.cast_interaction_report(report.interaction_file)
    #     self.writer.set_styles()
    #     self.writer.remove_blacklist_numbers()
    #     self.writer.remove_blank_messages()
    #     self.writer.save()    

    def cast_sent_report(self, sent_file_name):
        _file = open(sent_file_name, 'r')
        next(_file)
        for line in _file:
            [numero, status, data_envio, data_recebimento, data_leitura] = line.split(";")
            if numero not in self.sent_numbers:
                self.sent_numbers.append(numero)
                self.writer.remove_blacklist_numbers()
                self.writer.write_sent_message(numero, "Enviado", self.fix_date(data_envio))
        

    def cast_received_report(self, received_file_name):
        _file = open(received_file_name, 'r', encoding='utf-8')
        # next(_file) # Preciso verificar essa linha, que apaga 
        for line in _file:
            [telefone, mensagem] = line.split(";")
            self.writer.write_received_message(telefone, mensagem)
