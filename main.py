def menu():
    print('--- Sistema di gestione ---');
    print('1. Registrare una nuova prenotazione');
    print('2. Visualizzare elenco prenotazioni attive');
    print('3. Annullare prenotazione');
    print('4. Calcolare numero di notti');
    print('5. Esci');

while True:
    menu();
    choise = int(input('Selezionare una scelta: '));

    if choise == 1:
        print('Registrazioe prenotazione');
    elif choise == 2:
        print('Visualizazzione elenco prenotazione');
    elif choise == 3:
        print('Annullamento prenotazione');
    elif choise == 4:
        print('Calcolare numero notti');
    elif choise == 5:
        print('grazie per aver utilizzato il nostro sistema, arrivederci!');
        break;