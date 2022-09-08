from ura_report_converter import URAReportConverterInterface
from ura_report import URAReport
import csv

class N8Converter(URAReportConverterInterface):

    def convert_ura_report(self, report: URAReport):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.call_interaction_file)
        self.writer.set_activation_styles()
        self.writer.save()


    def cast_activation_report(self, activation_file_name):
        with open(activation_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            next(_reader)
            # self.writer.create_activation_sheet()
            # self.writer.insert_activation_header()
            for row in _reader:
                
                atendido = []
                no_atendido = []
                ocupado = []
                sin_llamar =[]

                # if '' in row[0][:] and row[12] != 'Atendido':
                if '' in row[0][:] and row[12] == 'Atendido':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    # atendido.append([number, date, duration, status])
                    self.writer.write_activation_message([number, date, duration, status])
                
                
                if '' in row[0][:] and row[12] == 'No Atendido':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    # no_atendido.append([number, date, duration, status])
                    self.writer.write_activation_message([number, date, duration, status])
                
                if '' in row[0][:] and row[12] == 'Ocupado':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    #ocupado.append([number, date, duration, status])
                    self.writer.write_activation_message([number, date, duration, status])
               
                if '' in row[0][:] and row[12] == 'Sin Llamar':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    #sin_llamar.append([number, date, duration, status])
                    self.writer.write_activation_message([number, date, duration, status])
            
                
    def cast_call_interaction_report(self, call_interaction_file_name):
        with open(call_interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            # self.writer.create_call_interaction_sheet()
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
                    