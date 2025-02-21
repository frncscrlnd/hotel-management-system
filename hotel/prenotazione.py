class Prenotazione: 
    def __init__ (self, codice, data_check_in, data_check_out):
        self.codice = codice
        self.data_check_in = data_check_in
        self.data_check_out = data_check_out
    
    def __str__ (self):
        return f"Codice: {self.codice}, data_check_in: {self.data_check_in}, data_check_out: {self.data_check_out}"
        