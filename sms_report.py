
class SMSReport:

    SUPPLIER_BEWAKE = "bewake"

    def __init__(self, sent_file, received_file, supplier):
        self._supplier = supplier
        self.sent_file = sent_file
        self.received_file = received_file

    @property
    def supplier(self):
        return self._supplier