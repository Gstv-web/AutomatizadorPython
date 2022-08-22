from report_converter import ReportConverterInterface
from report import Report


class LigdataConverter(ReportConverterInterface):

    def convert_report(self, report: Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.set_styles()
        self.writer.save()

    def cast_sent_report(self, sent_file_name):
        _file = open(sent_file_name, 'r')
        next(_file)
        for line in _file:
            [data, destinatarios, Status, Mensagem] = line.split(";")
            self.writer.write_sent_message(numero, status, self.fix_date(Data))

    def cast_received_report(self, received_file_name):
        pass