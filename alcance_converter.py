from report_converter import ReportConverterInterface
from report import Report

class AlcanceConverter(ReportConverterInterface):

    def convert_report(self, report: Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.set_styles()
        self.writer.remove_blacklist_numbers()
        self.writer.remove_blank_messages()
        self.writer.save()


    def cast_sent_report(self, sent_file_name):
        _file = open(sent_file_name, 'r')
        next(_file)
        for line in _file:
            [contato, dt_envio, resp] = line.split(";")
            self.writer.write_sent_message(contato, "Enviado", self.fix_date(dt_envio))


    def cast_received_report(self, received_file_name):
        _file = open(received_file_name, 'r')
        next(_file)
        for line in _file:
            [contato, dt_envio, resp] = line.split(";")
            self.writer.write_received_message(contato, resp)