from sms_report_converter import SMSReportConverterInterface
from sms_report import SMSReport
import csv
import xlrd


class TalkSMSConverter(SMSReportConverterInterface):

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
            for[campanha, telefone, mensagem, operadora, data, tarifa, status, arquivo] in _reader:
                if status != "Higienizado" and telefone not in self.sent_numbers:
                    self.sent_numbers.append(telefone)
                    self.writer.write_sent_message(self.fix_number(telefone), self.fix_date(data), status)


    def cast_received_report(self, received_file_name):
        book = xlrd.open_workbook(received_file_name)
        sheet = book.sheet_by_name("Detalhamento - SMS")
        phone = sheet.col_values(0)
        message = sheet.col_values(2)

        phones = []
        messages = []

        for p in phone:
            if p == "Terminal" or p == '':
                continue
            else:
                phones.append(p)
                
        for m in message:
            if m == "Terminal" or m == '':
                continue
            else:
                messages.append(m)

        for p, m in zip(phones, messages):
            self.writer.write_received_message(*[p, m])