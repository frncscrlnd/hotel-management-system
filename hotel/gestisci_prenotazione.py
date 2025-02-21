import datetime

Camera = []
Cliente = []
Prenotazione = []

def registra_nuove_prenotazioni(nome, numero_camera, data_check_in, data_check_out):
    nuova_prenotazione = {"nome": nome, "numero_camera" : numero_camera, "data_check_in" : data_check_in, "data_check_out" : data_check_out}
    Prenotazione.append(nuova_prenotazione)

registra_nuove_prenotazioni("Carlo", 32, datetime.date(2025, 1, 20), datetime.date(2025, 1, 30))
registra_nuove_prenotazioni("Franco", 19, datetime.date(2025, 7, 15), datetime.date(2025, 7, 20))