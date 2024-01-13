to_do_list = ["cane"]

# Funzione per aggiungere attività
def add_activity(activity, to_do_list):
    to_do_list.append(activity)
    input(f"Attività '{activity}' aggiunta alla lista con successo!")

# Funzione per visualizzare le attività
def see_activity(to_do_list):
    if not to_do_list:
        print("La lista è vuota. Non ci sono attività.")
    else:
        print("Lista delle attività:")
        # itera su ogni elemento della lista to_do_list, assegnando a i l'indice (iniziando da 1) e a activity il valore corrispondente
        for i, activity in enumerate(to_do_list, start=1):
            # utilizzo le f-string per stampare gli elementi della lista con il loro indice
            print(f"{i}. {activity}")

# Funzione per elimiare l'attività
def delet_activity(activity, to_do_list):
    try:
        to_do_list.remove(activity)
        print(f"L'attività '{activity}' è stata rimossa con successo")
    except ValueError:
        print(f"L'attività '{activity}' non è presente nella lista")


on = True

# Funzione principale
while on:
    print("\nMenu:")
    print("\t1. Aggiungi attività")
    print("\t2. Visualizza attività")
    print("\t3. Elimina attività")
    print("\t4. Esci")
    
    action = input("Cosa vuoi fare: ") 

    # Converto in intero per la selezione
    try:
        action = int(action) 
    except ValueError:
        print("Inserisci un numero valido")
        continue

    if action == 1:
        activity_to_add = input("Inserisci un'attività: ") 
        add_activity(activity_to_add, to_do_list)

    elif action == 2:
        see_activity(to_do_list)

    elif action == 3:
        if not to_do_list:
            print("La lista è vuota. Non ci sono attività da eliminare.")
        else:
            activity_to_delet = input("Quale attività vuoi rimuovere? ")
            delet_activity(activity_to_delet, to_do_list)

    elif action == 4:
        on = False

    else:
        print("Scelta non valida. Riprova.")