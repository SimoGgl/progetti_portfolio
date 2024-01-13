to_do_list = ["cane"]

# Funzione per aggiungere attività
def add_activity(activity, to_do_list):
    to_do_list.append(activity)
    input(f"Attività {activity} aggiunta alla lista con successo!")

# Funzione visualizzare le attività
def see_activity():
    print(f" Ecco l'elenco delle tue attività:\n'{to_do_list}'\n")

# Funzione per elimiare l'attività
def delet_activity(activity, to_do_list):
    try:
        to_do_list.remove(activity)
        print(f"L'attività '{activity}' è stata rimossa con successo")
    except ValueError:
        print(f"L'attività '{activity}' non è presente nella lista")


# Funzione principale
on = True

while on:
    action = input("Menu:\
                   \n\t1. Aggiungi attività\
                   \n\t2. Visualizza attività\
                   \n\t3. Elimina attività\
                   \n\t4. Esci\n\n"
                   "cosa vuoi fare: ")
    
    # Converto in intero per la selezione
    action = int(action) 

    if action == 1:
        activity_to_add = input("Inserisci un'attività: ") 
        add_activity(activity_to_add, to_do_list)

    elif action == 2:
        see_activity()

    elif action == 3:
        activity_to_delet = input("Quale attività vuoi rimuovere?\n")
        delet_activity(activity_to_delet, to_do_list)

    elif action == 4:
        on = False