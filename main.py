import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from weerstation import weerstation
from smart_app_controller import smart_app_controller


def huidig_weer():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.0907&longitude=5.1214"
        "&current=temperature_2m"
    )

    try:
        with urlopen(url, timeout=5) as antwoord:
            gegevens = json.loads(antwoord.read().decode("utf-8"))

        temperatuur = gegevens["current"]["temperature_2m"]
        print(f"De huidige temperatuur in Utrecht is {temperatuur} °C.")

    except (URLError, HTTPError, TimeoutError, ValueError, KeyError) as fout:
        print("Het actuele weer kon niet worden opgehaald:", fout)


def main():
    while True:
        print("\n===== SMART APP STORE =====")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Actueel weer in Utrecht")
        print("4. Afsluiten")

        keuze = input("Maak je keuze: ")

        try:
            if keuze == "1":
                weerstation()
            elif keuze == "2":
                smart_app_controller()
            elif keuze == "3":
                huidig_weer()
            elif keuze == "4":
                print("Tot ziens!")
                break
            else:
                print("Ongeldige keuze. Kies 1, 2, 3 of 4.")

        except (OSError, ValueError) as fout:
            print("Er ging iets mis:", fout)


if __name__ == "__main__":
    main()

