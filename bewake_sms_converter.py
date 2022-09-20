from sms_report_converter import SMSReportConverterInterface
from sms_report import SMSReport
import csv


class BewakeSMSConverter(SMSReportConverterInterface):

    def convert_sms_report(self, report: SMSReport):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.insert_sent_header()
        self.writer.insert_received_header()
        self.writer.set_styles()
        self.writer.save()

    def cast_sent_report(self, sent_file_name):
        with open(sent_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=";")
            next(_reader)
            for[codigo, entrada_em, programado_em, enviado_em, nome, celular, tipo, status, servico, operadora, whatsapp, campanha, resposta, duracao] in _reader:
                if status == "SUCESSO" and celular not in self.sent_numbers:
                    self.sent_numbers.append(celular)
                    # self.writer.remove_blacklist_numbers()
                    self.writer.write_sent_message(self.fix_number(celular), self.fix_date(enviado_em), self.fix_status(status))
            
    def cast_received_report(self, received_file_name):
        with open(received_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=";")
            next(_reader)
            for[codigo, entrada_em, programado_em, enviado_em, nome, celular, tipo, status, servico, operadora, whatsapp, campanha, resposta, duracao] in _reader:
                if status == "RECEBIDO SUCESSO":
                    self.writer.write_received_message(self.fix_number(celular), resposta)