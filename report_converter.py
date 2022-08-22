from abc import ABC, abstractmethod
from report_writer import ReportWriter


class ReportConverterInterface(ABC):

    def __init__(self, writer: ReportWriter):
        self.sent_numbers = []
        self.writer = writer
        
    @abstractmethod
    def convert_report(self, sent_file_name, received_file_name):
        pass
    
    def fix_date(self, date): # Alcance usa o formato aaaa-mm-dd - Verificar
        date = date.split(" ")
        if '"' in date[0]:
            date[0] = date[0].replace('"', '')
        return date[0]

    def fix_status(self, status):
        new_status = "Enviado"
        if status == "SUCESSO" or status == "RECEBIDO SUCESSO":
            status = new_status
        return status

    def fix_number(self, number):
        number = str()
        if "(" ")" " " in number:
            number = number.replace("(", "").replace(")", "").replace(" ", "")
        if '55' in number and len(number) >= 12:
            number = number.lstrip('55')
        return number