def aantal_dagen(inputFile):
    with open(inputFile, "r", encoding="utf-8") as bestand:
        regels = bestand.readlines()

    return max(0, len(regels) - 1)


def auto_bereken(inputFile, outputFile):
    with open(inputFile, "r", encoding="utf-8") as invoerbestand:
        regels = invoerbestand.readlines()[1:]

    with open(outputFile, "w", encoding="utf-8") as uitvoerbestand:
        for regel in regels:
            if not regel.strip():
                continue

            datum, personen, setpoint, buiten, neerslag = regel.split()

            personen = int(personen)
            setpoint = float(setpoint)
            buiten = float(buiten)
            neerslag = float(neerslag)

            verschil = setpoint - buiten

            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = min(personen + 1, 4)
            bewatering = neerslag < 3

            uitvoerbestand.write(
                f"{datum};{cv};{ventilatie};{bewatering}\n"
            )


def overwrite_settings(outputFile):
    datum = input("Voor welke datum? (DD-MM-JJJJ): ")
    systeem = input(
        "Kies systeem (1=CV-ketel, 2=ventilatie, 3=bewatering): "
    )

    if systeem not in ("1", "2", "3"):
        print("Ongeldig systeem gekozen.")
        return -3

    waarde = input("Welke nieuwe waarde? ")

    try:
        if systeem == "1":
            nieuwe_waarde = int(waarde)
            if not 0 <= nieuwe_waarde <= 100:
                raise ValueError

        elif systeem == "2":
            nieuwe_waarde = int(waarde)
            if not 0 <= nieuwe_waarde <= 4:
                raise ValueError

        else:
            if waarde not in ("0", "1"):
                raise ValueError
            nieuwe_waarde = waarde == "1"

    except ValueError:
        print("Ongeldige waarde ingevoerd.")
        return -3

    with open(outputFile, "r", encoding="utf-8") as bestand:
        regels = bestand.readlines()

    gevonden = False

    for i in range(len(regels)):
        onderdelen = regels[i].strip().split(";")

        if onderdelen[0] == datum:
            onderdelen[int(systeem)] = str(nieuwe_waarde)
            regels[i] = ";".join(onderdelen) + "\n"
            gevonden = True
            break

    if not gevonden:
        print("Datum niet gevonden.")
        return -1

    with open(outputFile, "w", encoding="utf-8") as bestand:
        bestand.writelines(regels)

    print("Waarde succesvol aangepast.")
    return 0


def smart_app_controller():
    inputFile = "weerdata.txt"
    outputFile = "actuatoren.txt"

    while True:
        print("\n--- Smart App Controller ---")
        print("1. Hoeveel dagen zijn aanwezig?")
        print("2. Bereken alle actuatoren")
        print("3. Overschrijf een actuatorwaarde")
        print("4. Terug naar hoofdmenu")

        keuze = input("Maak je keuze: ")

        try:
            if keuze == "1":
                print("Aantal dagen:", aantal_dagen(inputFile))

            elif keuze == "2":
                auto_bereken(inputFile, outputFile)
                print("Actuatorbestand succesvol aangemaakt.")

            elif keuze == "3":
                resultaat = overwrite_settings(outputFile)
                if resultaat == -1:
                    print("Kies een datum uit het uitvoerbestand.")
                elif resultaat == -3:
                    print("Pas je invoer aan en probeer opnieuw.")

            elif keuze == "4":
                break

            else:
                print("Ongeldige menuoptie.")

        except (OSError, ValueError) as fout:
            print("Er is een fout opgetreden:", fout)


if __name__ == "__main__":
    smart_app_controller()
