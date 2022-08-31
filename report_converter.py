from abc import ABC, abstractmethod
from report_writer import ReportWriter


class ReportConverterInterface(ABC):

    def __init__(self, writer: ReportWriter):
        self.sent_numbers = []
        self.writer = writer
        
    @abstractmethod
    def convert_wpp_report(self, sent_file_name, received_file_name):
        pass

    @abstractmethod
    def convert_rcs_report(self, sent_file_name, received_file_name, interaction_file_name):
        pass

    @abstractmethod
    def convert_ura_report(self, activation_file_name, call_interaction_file_name):
        pass
    
    def fix_date(self, date): # Alcance usa o formato aaaa-mm-dd - Verificar
        date = date.split(" ")
        date[0] = date[0].replace('"', '')
        if "-" in date[0]:
            pre_date = date[0].split("-")
            if len(pre_date[0]) == 4:
                pre_date.reverse()
                bar = "/".join(pre_date)
                new_date = bar
                
                return new_date
        else:        
            return date[0]

    def fix_status(self, status):
        new_status = "Enviado"
        if status == "SUCESSO" or status == "RECEBIDO SUCESSO" or status == "Yes":
            status = new_status
        return status

    def fix_number(self, number):
        number = number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+", "")    
        if '55' in number:
            number = number[2:]
        return number