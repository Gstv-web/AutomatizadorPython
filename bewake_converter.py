from report_converter import ReportConverterInterface
from report import Report
import csv

class BewakeConverter(ReportConverterInterface):

    def convert_wpp_report(self, report: Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.set_styles()
        self.writer.remove_blacklist_numbers()
        self.writer.remove_blank_messages()
        self.writer.save()


    def cast_sent_report(self, sent_file_name):
        with open(sent_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            next(_reader)
            for [codigo, entrada_em, programado_em, enviado_em, numero, celular, tipo, status, servico, operadora, whatsapp, campanha, resposta, duracao] in _reader:
                if "NUMERO INVALIDO" in status:
                    continue
                if celular not in self.sent_numbers:
                    self.sent_numbers.append(celular)
                    self.writer.remove_blacklist_numbers()
                    self.writer.write_sent_message(self.fix_number(celular), self.fix_status(status), self.fix_date(entrada_em))


    def cast_received_report(self, received_file_name):
        with open(received_file_name) as csvfile:
                _reader = csv.reader(csvfile, delimiter=';')
                next(_reader)
                for [codigo, entrada_em, programado_em, enviado_em, numero, celular, tipo, status, servico, operadora, whatsapp, campanha, resposta, duracao] in _reader:
                    new_resp = resposta.encode('unicode_escape').decode('utf-8')
                    resposta = new_resp
                    if resposta == "":
                        pass
                    else:
                        self.writer.write_received_message(numero, resposta)


    def convert_rcs_report(self, sent_file_name, received_file_name, interaction_file_name):
        pass

    def convert_ura_report(self, activation_file_name, call_interaction_file_name):
        pass