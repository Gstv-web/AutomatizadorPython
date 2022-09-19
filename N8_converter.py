from ura_report_converter import URAReportConverterInterface
from ura_report import URAReport
import csv

class N8Converter(URAReportConverterInterface):

    def convert_ura_report(self, report: URAReport):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.call_interaction_file)
        # self.writer.sort_activation_data()
        self.writer.set_activation_styles()
        self.writer.set_call_interaction_styles()
        self.write_csv(report.call_interaction_file)
        self.writer.save()


    def cast_activation_report(self, activation_file_name):
        with open(activation_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            next(_reader)
            # self.writer.create_activation_sheet()
            # self.writer.insert_activation_header()

            atendidos = []
            fallido = []
            no_atendidos = []
            ocupado = []
            sin_llamar = []
            for row in _reader:
                
            
                if '' in row[0][:] and row[12] == 'Atendido':
                    number = self.fix_number(str(row[6]))
                    date = self.fix_date(str(row[0]))
                    duration = str(row[11])
                    status = str(row[12])
                    atendidos.append([number, date, duration, status])
                    #self.writer.write_activation_message(atendido)
                
                
                if '' in row[0][:] and row[12] == 'No Atendido':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    no_atendidos.append([number, date, duration, status])
                    #self.writer.write_activation_message(no_atendido)
                
                if '' in row[0][:] and row[12] == 'Ocupado':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    ocupado.append([number, date, duration, status])
                    # self.writer.write_activation_message([number, date, duration, status])
               
                if '' in row[0][:] and row[12] == 'Sin Llamar':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    sin_llamar.append([number, date, duration, status])
                    # self.writer.write_activation_message([number, date, duration, status])
                
                if '' in row[0][:] and row[12] == 'Fallido':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    duration = row[11]
                    status = row[12]
                    sin_llamar.append([number, date, duration, status])
                    # self.writer.write_activation_message([number, date, duration, status])

            for i in range(len(atendidos)):
                self.writer.write_activation_message(atendidos[i])

            for i in range(len(fallido)):
                self.writer.write_activation_message(fallido[i])

            for i in range(len(no_atendidos)):
                self.writer.write_activation_message(no_atendidos[i])

            for i in range(len(ocupado)):
                self.writer.write_activation_message(ocupado[i])

            for i in range(len(sin_llamar)):
                self.writer.write_activation_message(sin_llamar[i])

                
    def cast_call_interaction_report(self, call_interaction_file_name):
        with open(call_interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            # self.writer.create_call_interaction_sheet()
            fixed_values = []
            for i, row in enumerate(_reader):                 
                
                if i == 0:
                    number = row[6]
                    date = row[0]
                    self.writer.write_call_interaction_message([*[number], *[date], *row[30:]])
                if '' in row[0][:] and row[12] == 'Atendido' and row[30] != '':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])

                    self.writer.write_call_interaction_message([*[number], *[date], *row[30:]])
                
    def write_csv(self, call_interaction_file_name):
        f = open("teste.csv", "w", newline="")
        with open(call_interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=';')
            # self.writer.create_call_interaction_sheet()
            fixed_values = []
            for i, row in enumerate(_reader):                 
                
                if i == 0:
                    number = "telefone"
                    date = row[0]
                    writer = csv.writer(f)
                    writer.writerow([number, date, *row[30:]])
                if '' in row[0][:] and row[12] == 'Atendido' and row[30] != '':
                    number = self.fix_number(row[6])
                    date = self.fix_date(row[0])
                    writer = csv.writer(f)
                    writer.writerow([number, date, *row[30:]])
            
            f.close()
