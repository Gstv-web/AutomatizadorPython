from report_converter import ReportConverterInterface
from report import Report
import csv

class N8Converter(ReportConverterInterface):

    def convert_report(self, report: Report):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.interaction_file)
        self.writer.save()


    def cast_activation_report(self, activation_file_name):
        with open(activation_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            self.writer.create_activation_sheet()
            date = []
            phone = []
            duration = []
            status = []
            for row in _reader:

                if '' in row[0][:] and row[12] != 'Atendido':
                    pass
                else:
                    pre_date = row[0][:]
                    pre_phone = row[6][2:]
                    pre_duration = row[11]
                    pre_status = row[12]
                    date.append(pre_date)
                    phone.append(pre_phone)
                    duration.append(pre_duration)
                    status.append(pre_status)

            
            fields = [str(phone), str(date), str(duration), str(status)]
            
            for i in fields:
                self.writer.write_activation_message(fields[i])

                
                
    def cast_call_interaction_report(self, interaction_file_name):
        pass