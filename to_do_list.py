to_do_list = []

# Funzione per aggiungere attività
def add_activity(to_do_list):
    activity_to_add = input("Inserisci un'attività: ")
    to_do_list.append(activity_to_add)
    print(f"Attività '{activity_to_add}' aggiunta alla lista con successo!")

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
def delete_activity(to_do_list):
    if not to_do_list:
        print("La lista è vuota. Non ci sono attività da eliminare.")
        # se non ci sono attività da eliminare non esegue i passaggi sucessivi
        return
    
    while True:
        print("\nSottomenu Elimina attività:")
        print("\t1. Elimina un'attività specifica")
        print("\t2. Elimina l'ultima attività")
        print("\t3. Torna al Menu")

        choice = input("Cosa vuoi fare: ")

        if choice == "1":
            if not to_do_list:
                print("La lista è vuota. Non ci sono attività da eliminare.")
            else:
                activity_to_delete = input("Quale attività vuoi rimuovere? ")
                try:
                    to_do_list.remove(activity_to_delete)
                    print(f"Attività '{activity_to_delete}' eliminata con successo!")
                except ValueError:
                    print(f"L'attività '{activity_to_delete}' non è presente nella lista.")
        elif choice == "2":
            if not to_do_list:
                print("La lista è vuota. Non ci sono attività da eliminare.")
            else:
                removed_activity = to_do_list.pop()  # Rimuove l'ultima attività
                print(f"Attività '{removed_activity}' eliminata con successo!")
        elif choice == "3":
            print("Torno al menu principale.")
            break
        else:
            print("Scelta non valida. Ritorno al menu principale.")

# Dizionario che associa le opzioni del menu alle funzioni corrispondenti
menu_options = {
    1: add_activity,
    2: see_activity,
    3: delete_activity,
    4: exit
}

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

    if action in menu_options:
        # Esegue la funzione associata all'opzione
        menu_options[action](to_do_list)
    else:
        print("Scelta non valida. Riprova.")