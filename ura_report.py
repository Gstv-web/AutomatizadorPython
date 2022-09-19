
class URAReport:

    SUPPLIER_N8 = "N8"
    SUPPLIER_TALK = "Talk"
    SUPPLIER_TALKIP = "Talkip"

    def __init__(self, activation_file, call_interaction_file, supplier):
        self._supplier = supplier
        self.activation_file = activation_file
        self.call_interaction_file = call_interaction_file
    

    @property
    def supplier(self):
        return self._supplier