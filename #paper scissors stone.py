#Carta/ Forbice/ Sasso
import random #Generate a random value from the sequence sequence
import os #Python OS module allows us to use the operating system dependent functionalities and to interact with the underlying operating system
import re #A regular expression (or RE) specifies a set of strings that matches it
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Roccia, Carta, Forbici ")
    sceltaUtente = input("Scegli la tua parola [R]occia, [C]arta, or [F]orbici: ")
    if not re.match("[FfRrCc]", sceltaUtente):
        print ("Scegli lettera: ")
        print ("[R]occia, [F]orbici o [C]arta.")
        continue

    # Scelta utente 
    print ("La tua scelta: " + sceltaUtente)
    choices = ['R', 'C', 'F']
    opponenetChoice = random.choice(choices)
    print ("Io scelgo: " + opponenetChoice)
    if opponenetChoice == str.upper(sceltaUtente):
        print ("PAREGGIO! ")
    #if opponenetChoice == str("R") and str.upper(sceltaUtente) == "P"
    elif opponenetChoice == 'R' and sceltaUtente.upper() == 'F':      
        print ("Le Forbici Battono la roccia, I win! ")
        continue
    elif opponenetChoice == 'F' and sceltaUtente.upper() == 'C':      
        print ("Le forbici battono carta! I win! ")
        continue
    elif opponenetChoice == 'C' and sceltaUtente.upper() == 'R':      
        print ("La carta batte la roccia, I win! ")
        continue
    else:       
        print ("You win!")