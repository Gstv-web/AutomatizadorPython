from rcs_report_converter import RCSReportConverterInterface
from rcs_report import RCSReport
import csv

class IknowRCSConverter(RCSReportConverterInterface):

    def convert_rcs_report(self, report: RCSReport):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.cast_interaction_report(report.interaction_file)
        self.writer.set_styles()
        self.writer.remove_blacklist_numbers()
        self.writer.remove_blank_messages()
        self.write_csv(report.interaction_file)
        self.writer.save()

    
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
        with open(received_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            next(_reader)
            for [numero, data_recebimento, conteudo] in _reader:
                self.writer.write_received_message(self.fix_number(numero), conteudo)


    def cast_interaction_report(self, interaction_file_name):
        with open(interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=',')
            self.writer.create_interaction_sheet()
            for row in _reader:
                number = self.fix_number(row[0])
                self.writer.write_interaction_message([*[number],*row[1:]])
    

    def write_csv(self, interaction_file_name):
        f = open("teste_rcs.csv", "w", newline="")
        with open(interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=',')
            self.writer.create_interaction_sheet()
            for row in _reader:
                number = self.fix_number(row[0])
                writer = csv.writer(f)
                writer.writerow([number, *row[1:]])