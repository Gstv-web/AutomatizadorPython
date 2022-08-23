from report_converter import ReportConverterInterface
from report import Report
from openpyxl import load_workbook


class AtmosferaConverter(ReportConverterInterface):

    def convert_report(self, report:Report):
        self.cast_sent_report(report.sent_file)
        self.cast_received_report(report.received_file)
        self.writer.set_styles()
        self.writer.remove_blacklist_numbers()
        self.writer.remove_blank_messages()
        self.writer.save()

    def cast_sent_report(self, sent_file_name):
        workbook = load_workbook("./Entrada/Atmosfera/Enviados/Relatório Daniel - Centro  29_07.xlsx") 
        worksheet = workbook['RELATÓRIO']
        value = []
        for col in worksheet.iter_rows(min_row=1, min_col=1):
            for cell in col:
                if None in cell.value:
                    pass
                else:
                    value.append(cell.value)
                    print(cell.value)


    def cast_received_report(self, received_file_name):
        pass