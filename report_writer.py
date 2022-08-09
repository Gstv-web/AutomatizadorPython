from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Side


class ReportWriter:

    SENT_SHEET_NAME = "RELATÓRIO"
    RECEIVED_SHEET_NAME = "RESPOSTAS"

    def __init__(self, file_name):
        self.workbook = None
        self.file_name = None
        self.sent_sheet = None
        self.received_sheet = None
        self.file_name = file_name
        self.init_writer()

    def init_writer(self):
        self.workbook = Workbook()
        self.sent_sheet = self.workbook.active
        self.sent_sheet.title = ReportWriter.SENT_SHEET_NAME
        #self.sent_sheet = self.workbook.create_sheet(ReportWriter.SENT_SHEET_NAME)
        self.received_sheet = self.workbook.create_sheet(ReportWriter.RECEIVED_SHEET_NAME)
        self.set_styles()

    def set_sent_styles(self):
        self.sent_sheet.column_dimensions['A'].width = 17
        self.sent_sheet.column_dimensions['B'].width = 14
        self.sent_sheet.column_dimensions['C'].width = 14

    def set_received_styles(self):
        self.received_sheet.column_dimensions['A'].width = 17
        self.received_sheet.column_dimensions['B'].width = 300

    def set_styles(self):
        self.set_received_styles()
        self.set_sent_styles()

    def write_sent_message(self, number, status, sent_date):
        self.sent_sheet.append([number, status, sent_date])

    def write_received_message(self, number, received_text):
        self.received_sheet.append([number, received_text])

    def insert_sent_header(self):
        self.sent_sheet.insert_rows(0)
        self.sent_sheet['A1'] = 'TELEFONE'
        self.sent_sheet['B1'] = 'DATA'
        self.sent_sheet['C1'] = 'STATUS'

    # def insert_received_header(self):  
    #     self.received_sheet.insert_rows(0)
    #     self.received_sheet['A1'] = 'TELEFONE'
    #     self.received_sheet['B1'] = 'MENSAGEM'

    def save(self):
        self.workbook.save(self.file_name)