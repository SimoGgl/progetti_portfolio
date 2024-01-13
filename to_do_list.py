class ToDoListManager:
    def __init__(self):
        self.to_do_list = []

    # Funzione per aggiungere attività
    def add_activity(self):
        activity_to_add = input("Inserisci un'attività: ")
        self.to_do_list.append(activity_to_add)
        print(f"Attività '{activity_to_add}' aggiunta alla lista con successo!")

    # Funzione per visualizzare le attività
    def see_activity(self):
        if not self.to_do_list:
            print("La lista è vuota. Non ci sono attività.")
        else:
            print("Lista delle attività:")
            # itera su ogni elemento della lista to_do_list, assegnando a i l'indice (iniziando da 1) e a activity il valore corrispondente
            for i, activity in enumerate(self.to_do_list, start=1):
                # utilizzo le f-string per stampare gli elementi della lista con il loro indice
                print(f"{i}. {activity}")

    # Funzione per eliminare l'attività
    def delete_activity(self):
        # controllo sulla presenza di attività
        if not self.to_do_list:
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
                self._delete_specific_activity()
            elif choice == "2":
                self._delete_last_activity()
            elif choice == "3":
                print("Torno al menu principale.")
                break
            else:
                print("Scelta non valida. Riprova.")

    # Funzione per eliminare un'attività specifica
    def _delete_specific_activity(self):
        if not self.to_do_list:
            print("La lista è vuota. Non ci sono attività da eliminare.")
        else:
            activity_to_delete = input("Quale attività vuoi rimuovere? ")
            try:
                self.to_do_list.remove(activity_to_delete)
                print(f"Attività '{activity_to_delete}' eliminata con successo!")
            except ValueError:
                print(f"L'attività '{activity_to_delete}' non è presente nella lista.")

    # Funzione per eliminare l'ultima attività
    def _delete_last_activity(self):
        if not self.to_do_list:
            print("La lista è vuota. Non ci sono attività da eliminare.")
        else:
            removed_activity = self.to_do_list.pop()
            print(f"Attività '{removed_activity}' eliminata con successo!")

# Funzione principale
def main():
    to_do_manager = ToDoListManager()

    while True:
        print("\nMenu:")
        print("\t1. Aggiungi attività")
        print("\t2. Visualizza attività")
        print("\t3. Elimina attività")
        print("\t4. Esci")
    
        action = input("Cosa vuoi fare: ")

        try:
            action = int(action)
        except ValueError:
            print("Inserisci un numero valido.")
            continue

       # Dizionario che associa le opzioni del menu alle funzioni corrispondenti
        menu_options = {
            1: to_do_manager.add_activity,
            2: to_do_manager.see_activity,
            3: to_do_manager.delete_activity,
            4: exit
        }

        if action in menu_options:
            # Esegue la funzione associata all'opzione
            menu_options[action]()
        else:
            print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()
