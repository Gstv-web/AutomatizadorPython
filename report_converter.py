from abc import ABC, abstractmethod
from report_writer import ReportWriter


class ReportConverterInterface(ABC):

    def __init__(self, writer: ReportWriter):
        self.writer = writer
        
    @abstractmethod
    def convert_report(self, sent_file_name, received_file_name):
        pass
