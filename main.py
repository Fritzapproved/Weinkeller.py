import csv
import pandas as pd

weine = []

while True:
    winzer = input("Winzer: ").lower().strip()
    rebsorte = input("Rebsorte: ").lower().strip()
    jahrgang_input = input("Jahrgang: ")
    # Checken, ob Jahrgang ein Integer zwischen 1900 und 2050 ist
    while True:
        if jahrgang_input.isdigit():
            # Check if the integer is between 1 and 100
            if int(jahrgang_input) in range(1900, 2051):
                jahrgang = jahrgang_input
                break
            else:
                print("Jahrgang muss zwischen '1900' und '2050' liegen.")
                jahrgang_input = input("Jahrgang: ")
        else:
            jahrgang_input = input("Huh? Jahgang: ")

    # Anzahl abfragen
    anzahl_input = input("Anzahl: ")

    # Checken, ob Anzahl ein Integer ist
    while True:
        if anzahl_input.isdigit():
            # Check if the integer is between 1 and 100
            if int(anzahl_input) in range(1, 100):
                anzahl = anzahl_input
                break
            else:
                print("Anzahl muss zwischen '0' und '100' liegen.")
                anzahl_input = input("Anzahl: ")
        else:
            anzahl_input = input("Huh? Anzahl: ")


    neuer_wein = [winzer, rebsorte, jahrgang, anzahl]

    neuer_wein_check = (neuer_wein[0], neuer_wein[1], neuer_wein[2])

    weine.append(neuer_wein)
    print(weine)

    # Checken, ob neuer_wein schon in Liste enthalten ist - Pana-Style

    weinliste = pd.read_csv("Data/weinliste.csv")

    # Checken, ob neuer_wein schon in Liste enthalten ist
    with open('Data/weinliste.csv') as weinliste_csv:
        csv_reader = csv.reader(weinliste_csv, delimiter=',')
        line_count = -1
        gefunden = False
        for item in csv_reader:
            eintrag = (item[0], item[1], item[2])
            if eintrag == neuer_wein_check:
                print("Wein gefunden!")
                gefunden = True
                anzahl_alt = weinliste.iloc[line_count, 3]
                anzahl_neu = int(anzahl_alt) + int(anzahl)
                print("Neue Anzahl:", anzahl_neu)
                weinliste = weinliste.drop(weinliste.index[line_count])

                data_append = {
                    'winzer': [winzer],
                    'rebsorte': [rebsorte],
                    'jahrgang': [jahrgang],
                    'anzahl': [anzahl_neu]
                }
                # Make data frame of above data
                df = pd.DataFrame(data_append)

                weinliste.to_csv('Data/weinliste.csv', encoding='utf-8', index=False, sep=',')
                df.to_csv('Data/weinliste.csv', mode='a', encoding='utf-8', index=False, sep=',', header = False)

                line_count += 1
            else:
                line_count += 1

    if gefunden == False:
        data_new = {
            'winzer': [winzer],
            'rebsorte': [rebsorte],
            'jahrgang': [jahrgang],
            'anzahl': [anzahl]
        }
        df = pd.DataFrame(data_new)
        weinliste.to_csv('Data/weinliste.csv', encoding='utf-8', index=False, sep=',')
        df.to_csv('Data/weinliste.csv', mode='a', encoding='utf-8', index=False, sep=',', header=False)

    weinliste = pd.read_csv("Data/weinliste.csv")
    print(weinliste)
    #Weiteren Wein in die Liste aufnehmen?
    false = True
    while (True):
        weiter = input("Weiter? (j/n)")
        weiter = weiter.lower()
        if "j" in weiter:
            break
        elif "n" in weiter:
            false = False
            break
        else:
            print("Huh?")
    if false == False:
        break






