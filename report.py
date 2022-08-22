
class Report:

    SUPPLIER_IKNOW = 'iknow'
    SUPPLIER_ALCANCE = 'alcance'
    SUPPLIER_BEWAKE = 'bewake'
    SUPPLIER_LIGDATA = 'ligdata'
    SUPPLIER_ATMOSFERA = 'atmosfera'

    def __init__(self, sent_file, received_file, supplier):
        self._supplier = supplier
        self.sent_file = sent_file
        self.received_file = received_file

    @property
    def supplier(self):
        return self._supplier