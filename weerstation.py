def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(
        temp_celcius, windsnelheid, luchtvochtigheid
    )

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel < 10:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    temperaturen = []

    for dag in range(1, 8):
        try:
            invoer = input(
                f"Wat is op dag {dag} de temperatuur [C]: "
            )
            if invoer == "":
                break
            temperatuur = float(invoer)

            invoer = input(
                f"Wat is op dag {dag} de windsnelheid [m/s]: "
            )
            if invoer == "":
                break
            wind = float(invoer)

            invoer = input(
                f"Wat is op dag {dag} de vochtigheid [%]: "
            )
            if invoer == "":
                break
            vochtigheid = int(invoer)

            if not 0 <= vochtigheid <= 100:
                print("Vochtigheid moet tussen 0 en 100 liggen.")
                continue
            if wind < 0:
                print("Windsnelheid mag niet negatief zijn.")
                continue

        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw voor deze dag.")
            continue

        temperaturen.append(temperatuur)

        print(
            f"Het is {temperatuur:.1f}C "
            f"({Fahrenheit(temperatuur):.1f}F)"
        )
        print(weerrapport(temperatuur, wind, vochtigheid))
        print(
            f"Gem. temp tot nu toe is "
            f"{sum(temperaturen) / len(temperaturen):.1f}"
        )
        print("=" * 38)

    print("Weerstation beëindigd.")


if __name__ == "__main__":
    weerstation()
