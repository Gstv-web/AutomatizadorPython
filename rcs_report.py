
class RCSReport:

    SUPPLIER_IKNOW = 'iknow'
    
    def __init__(self, sent_file, received_file, interaction_file, supplier):
        self._supplier = supplier
        self.sent_file = sent_file
        self.received_file = received_file
        self.interaction_file = interaction_file
 

    @property
    def supplier(self):
        return self._supplier