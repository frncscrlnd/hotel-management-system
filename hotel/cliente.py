class Cliente: 
    def __init__ (self, nome_cliente, cognome_cliente, cod_fis):
        self.nome_cliente = nome_cliente
        self.cognome_cliente = cognome_cliente
        self.cod_fis = cod_fis
    
    def __str__ (self):
        return f"Nome cliente: {self.nome_cliente}, cognome cliente: {self.cognome_cliente}, codice fiscale del cliente: {self.cod_fis}"
    