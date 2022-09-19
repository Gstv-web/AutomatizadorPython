from ura_report_converter import URAReportConverterInterface
from ura_report import URAReport
import csv


class TalkipConverter(URAReportConverterInterface):

    def convert_ura_report(self, report: URAReport):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.call_interaction_file)
        self.writer.set_activation_styles()
        self.writer.set_call_interaction_styles()
        self.writer.save()

    
    def cast_activation_report(self, activation_file_name):
        with open(activation_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=',')

            atendidos = []
            caixa_postal = []
            nao_atendidos = []
            temp_indisp = []
            nao_existe = []

            for row in _reader:

                if row[3] == "Atendido":
                    number = self.fix_number(str(row[0]))
                    date = self.fix_date(str(row[2]))
                    duration = str(row[1])
                    status = str(row[3])
                    atendidos.append([number, date, duration, status])

                if row[3] == "Possivel caixa postal":
                    number = self.fix_number(str(row[0]))
                    date = self.fix_date(str(row[2]))
                    duration = str(row[1])
                    status = str(row[3])
                    caixa_postal.append([number, date, duration, status])
                
                if row[3] == "Nao Atendido":
                    number = self.fix_number(str(row[0]))
                    date = self.fix_date(str(row[2]))
                    duration = str(row[1])
                    status = str(row[3])
                    nao_atendidos.append([number, date, duration, status])

                if row[3] == "Temporariamente indisponivel":
                    number = self.fix_number(str(row[0]))
                    date = self.fix_date(str(row[2]))
                    duration = str(row[1])
                    status = str(row[3])
                    temp_indisp.append([number, date, duration, status])

                if row[3] == "Nao Existe":
                    number = self.fix_number(str(row[0]))
                    date = self.fix_date(str(row[2]))
                    duration = str(row[1])
                    status = str(row[3])
                    nao_existe.append([number, date, duration, status])

            for i in range(len(atendidos)):
                self.writer.write_activation_message(atendidos[i])

            for i in range(len(nao_atendidos)):
                self.writer.write_activation_message(nao_atendidos[i])

            for i in range(len(caixa_postal)):
                self.writer.write_activation_message(caixa_postal[i])

            for i in range(len(temp_indisp)):
                self.writer.write_activation_message(temp_indisp[i])

            for i in range(len(nao_existe)):
                self.writer.write_activation_message(nao_existe[i])

    def cast_call_interaction_report(self, call_interaction_file_name):
        with open(call_interaction_file_name) as csvfile:
            _reader = csv.reader(csvfile, delimiter=",")
            for row in _reader:
                number = self.fix_number(str(row[0]))
                date = self.fix_date(str(row[2]))
                self.writer.write_call_interaction_message([number, date, *row[3:]])
